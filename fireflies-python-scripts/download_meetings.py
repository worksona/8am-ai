#!/usr/bin/env python3
"""
8am AI Meetings Download Script

This script automates the download of meeting transcripts, summaries, and audio files
using the Fireflies MCP integration and the 8am-meetings-manifest.md file.
"""

import os
import re
import subprocess
import json
import requests
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MeetingDownloader:
    def __init__(self, manifest_path: str = "8am-meetings-manifest.md"):
        self.manifest_path = manifest_path
        self.base_dir = Path.home() / "Desktop" / "8-am-ai"
        self.base_dir.mkdir(exist_ok=True)
    
    def parse_manifest(self) -> List[Dict[str, str]]:
        """Parse the manifest file and return meetings with 'no' status."""
        meetings = []
        
        with open(self.manifest_path, 'r') as f:
            content = f.read()
        
        # Extract table rows
        lines = content.split('\n')
        in_table = False
        
        for line in lines:
            if line.startswith('| #'):
                in_table = True
                continue
            if line.startswith('|---'):
                continue
            if in_table and line.startswith('|') and line.strip() != '|':
                parts = [p.strip() for p in line.split('|')[1:-1]]  # Remove empty first/last
                if len(parts) >= 7:
                    meeting = {
                        'number': parts[0],
                        'status': parts[1],
                        'meeting_id': parts[2],
                        'title': parts[3],
                        'date': parts[4],
                        'duration': parts[5],
                        'folder_name': parts[6],
                        'notes': parts[7] if len(parts) > 7 else ''
                    }
                    if meeting['status'] == 'no':
                        meetings.append(meeting)
            elif in_table and not line.startswith('|'):
                break
        
        return meetings
    
    def run_claude_code(self, prompt: str) -> Optional[str]:
        """Run a command through Claude Code and return the result."""
        print(f"CLAUDE_REQUEST: {prompt}")
        print("CLAUDE_REQUEST_END")
        
        # Wait for user to provide the response
        print("Please provide the result from Claude Code (end with 'RESPONSE_END'):")
        response_lines = []
        while True:
            try:
                line = input()
                if line.strip() == "RESPONSE_END":
                    break
                response_lines.append(line)
            except EOFError:
                break
        
        return "\n".join(response_lines) if response_lines else None
    
    def get_meeting_summary(self, meeting_id: str) -> Optional[str]:
        """Get meeting summary using MCP Fireflies integration."""
        result = self.run_mcp_command("fireflies__get_summary", {
            "transcriptId": meeting_id,
            "filter": '["summary { overview }"]'
        })
        
        if result and 'summary' in result and 'overview' in result['summary']:
            return result['summary']['overview']
        return None
    
    def get_meeting_transcript(self, meeting_id: str) -> Optional[str]:
        """Get meeting transcript using MCP Fireflies integration."""
        result = self.run_mcp_command("fireflies__get_transcript", {
            "transcriptId": meeting_id,
            "filter": '["sentences { speaker_name text }"]'
        })
        
        if result and 'sentences' in result:
            # Format sentences as "Speaker: text" lines
            transcript_lines = []
            for sentence in result['sentences']:
                speaker = sentence.get('speaker_name', 'Unknown')
                text = sentence.get('text', '')
                transcript_lines.append(f"{speaker}: {text}")
            return '\n'.join(transcript_lines)
        return None
    
    def get_audio_url(self, meeting_id: str) -> Optional[str]:
        """Get audio URL for the meeting."""
        result = self.run_mcp_command("fireflies__get_transcript", {
            "transcriptId": meeting_id,
            "filter": '["audio_url"]'
        })
        
        if result and 'audio_url' in result:
            return result['audio_url']
        return None
    
    def download_audio(self, audio_url: str, output_path: Path) -> bool:
        """Download audio file from URL."""
        try:
            response = requests.get(audio_url, stream=True)
            response.raise_for_status()
            
            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            logger.info(f"Audio downloaded: {output_path}")
            return True
            
        except requests.RequestException as e:
            logger.error(f"Failed to download audio: {e}")
            return False
    
    def update_manifest_status(self, meeting_number: str, new_status: str, notes: str = ""):
        """Update the status of a meeting in the manifest file."""
        with open(self.manifest_path, 'r') as f:
            content = f.read()
        
        # Find and replace the status for the specific meeting
        pattern = f"\\| {meeting_number} \\| no \\|"
        replacement = f"| {meeting_number} | {new_status} |"
        
        if notes and new_status == "error":
            # Add error note
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if f"| {meeting_number} |" in line and "| no |" in line:
                    parts = line.split('|')
                    if len(parts) >= 8:
                        parts[2] = f" {new_status} "
                        if parts[-2].strip() == "-" or parts[-2].strip() == "":
                            parts[-2] = f" {notes} "
                        else:
                            parts[-2] = f" {parts[-2].strip()}, {notes} "
                        lines[i] = '|'.join(parts)
                    break
            content = '\n'.join(lines)
        else:
            content = re.sub(pattern, replacement, content)
        
        with open(self.manifest_path, 'w') as f:
            f.write(content)
    
    def download_meeting(self, meeting: Dict[str, str]) -> bool:
        """Download all files for a single meeting."""
        meeting_id = meeting['meeting_id']
        date = meeting['date']
        folder_name = meeting['folder_name']
        meeting_number = meeting['number']
        
        logger.info(f"Processing meeting {meeting_number}: {meeting['title']} ({date})")
        
        # Create folder
        folder_path = self.base_dir / folder_name
        folder_path.mkdir(exist_ok=True)
        
        # Update status to in_progress
        self.update_manifest_status(meeting_number, "in_progress")
        
        success = True
        error_notes = []
        
        try:
            # Download summary
            logger.info("Fetching summary...")
            summary = self.get_meeting_summary(meeting_id)
            if summary:
                with open(folder_path / "summary.txt", 'w') as f:
                    f.write(summary)
                logger.info("Summary saved")
            else:
                error_notes.append("summary failed")
                success = False
            
            # Download transcript
            logger.info("Fetching transcript...")
            transcript = self.get_meeting_transcript(meeting_id)
            if transcript:
                with open(folder_path / "transcript.txt", 'w') as f:
                    f.write(transcript)
                logger.info("Transcript saved")
            else:
                error_notes.append("transcript failed")
                success = False
            
            # Download audio
            logger.info("Fetching audio URL...")
            audio_url = self.get_audio_url(meeting_id)
            if audio_url:
                audio_success = self.download_audio(audio_url, folder_path / "audio.mp3")
                if not audio_success:
                    error_notes.append("audio download failed")
                    success = False
            else:
                error_notes.append("audio URL not found")
                success = False
            
            # Update status
            if success:
                self.update_manifest_status(meeting_number, "yes")
                logger.info(f"Meeting {meeting_number} completed successfully")
            else:
                error_msg = ", ".join(error_notes)
                self.update_manifest_status(meeting_number, "error", error_msg)
                logger.error(f"Meeting {meeting_number} completed with errors: {error_msg}")
            
            return success
            
        except Exception as e:
            logger.error(f"Unexpected error processing meeting {meeting_number}: {e}")
            self.update_manifest_status(meeting_number, "error", str(e))
            return False
    
    def download_all_pending(self) -> Tuple[int, int]:
        """Download all meetings with 'no' status."""
        meetings = self.parse_manifest()
        
        if not meetings:
            logger.info("No pending meetings found")
            return 0, 0
        
        logger.info(f"Found {len(meetings)} pending meetings")
        
        successful = 0
        failed = 0
        
        for meeting in meetings:
            if self.download_meeting(meeting):
                successful += 1
            else:
                failed += 1
        
        logger.info(f"Download complete: {successful} successful, {failed} failed")
        return successful, failed

def main():
    """Main function to run the download process."""
    downloader = MeetingDownloader()
    
    try:
        successful, failed = downloader.download_all_pending()
        print(f"\nDownload Summary:")
        print(f"Successful: {successful}")
        print(f"Failed: {failed}")
        print(f"Total processed: {successful + failed}")
        
    except KeyboardInterrupt:
        print("\nDownload interrupted by user")
    except Exception as e:
        print(f"Unexpected error: {e}")
        logger.error(f"Unexpected error in main: {e}")

if __name__ == "__main__":
    main()