#!/usr/bin/env python3
"""
Helper script for downloading meetings using Claude Code MCP integration

This script provides the MCP function calls you need to run in Claude Code
to download all your meetings automatically.
"""

import re
import requests
import json
from pathlib import Path

def parse_manifest(manifest_path: str = "8am-meetings-manifest.md"):
    """Parse the manifest file and return meetings with 'no' status."""
    meetings = []
    
    with open(manifest_path, 'r') as f:
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
            parts = [p.strip() for p in line.split('|')[1:-1]]
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

def generate_claude_commands():
    """Generate the exact MCP function calls for Claude Code."""
    meetings = parse_manifest()[:10]  # Process first 10 meetings
    
    print("# 8am AI Meeting Download Commands for Claude Code")
    print("# Copy and paste these commands one by one into Claude Code")
    print("# " + "="*70)
    
    for i, meeting in enumerate(meetings, 1):
        print(f"\n## Meeting {meeting['number']}: {meeting['title']} ({meeting['date']})")
        print(f"# Folder: ~/Desktop/8-am-ai/{meeting['folder_name']}")
        
        # Create folder command
        print(f"mkdir -p ~/Desktop/8-am-ai/{meeting['folder_name']}")
        
        # Get summary
        print(f"\n# Get summary:")
        print(f"mcp__fireflies__get_summary(transcriptId='{meeting['meeting_id']}', filter=['summary {{ overview }}'])")
        
        # Get audio URL
        print(f"\n# Get audio URL:")
        print(f"mcp__fireflies__get_transcript(transcriptId='{meeting['meeting_id']}', filter=['audio_url'])")
        
        # Download transcript in chunks
        print(f"\n# Get transcript (may need to do in chunks due to size):")
        print(f"mcp__fireflies__get_transcript(transcriptId='{meeting['meeting_id']}', filter=['sentences {{ speaker_name text }}'])")
        
        print(f"\n# After getting the data, save files:")
        print(f"# - Save summary.overview to ~/Desktop/8-am-ai/{meeting['folder_name']}/summary.txt")
        print(f"# - Format sentences as 'Speaker: text' and save to ~/Desktop/8-am-ai/{meeting['folder_name']}/transcript.txt")
        print(f"# - Download audio_url to ~/Desktop/8-am-ai/{meeting['folder_name']}/audio.mp3")
        
        if i < len(meetings):
            print("\n" + "-"*80)

def download_audio_from_url(audio_url: str, output_path: str):
    """Download audio file from Fireflies URL."""
    try:
        response = requests.get(audio_url, stream=True)
        response.raise_for_status()
        
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f"✓ Audio downloaded: {output_path}")
        return True
        
    except requests.RequestException as e:
        print(f"✗ Failed to download audio: {e}")
        return False

def save_summary(summary_text: str, folder_path: str):
    """Save summary to file."""
    Path(folder_path).mkdir(parents=True, exist_ok=True)
    
    with open(f"{folder_path}/summary.txt", 'w') as f:
        f.write(summary_text)
    
    print(f"✓ Summary saved: {folder_path}/summary.txt")

def save_transcript(sentences_data: list, folder_path: str):
    """Format and save transcript from sentences data."""
    Path(folder_path).mkdir(parents=True, exist_ok=True)
    
    transcript_lines = []
    for sentence in sentences_data:
        speaker = sentence.get('speaker_name', 'Unknown')
        text = sentence.get('text', '')
        transcript_lines.append(f"{speaker}: {text}")
    
    with open(f"{folder_path}/transcript.txt", 'w') as f:
        f.write('\n'.join(transcript_lines))
    
    print(f"✓ Transcript saved: {folder_path}/transcript.txt")

if __name__ == "__main__":
    print("Claude Code MCP Helper for 8am AI Meetings")
    print("=" * 50)
    
    meetings = parse_manifest()
    print(f"Found {len(meetings)} meetings to download")
    
    # Generate commands
    generate_claude_commands()
    
    print(f"\n\n# WORKFLOW SUMMARY:")
    print(f"# 1. Run the commands above in Claude Code")
    print(f"# 2. For each meeting, Claude will return:")
    print(f"#    - Summary overview text")
    print(f"#    - Audio URL (with expiration)")
    print(f"#    - Transcript sentences")
    print(f"# 3. Use the helper functions in this script to save the files")
    print(f"# 4. Update manifest status to 'yes' when complete")