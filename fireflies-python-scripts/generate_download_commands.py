#!/usr/bin/env python3
"""
Generate MCP commands for downloading 8am AI meetings

This script reads the manifest and generates the MCP function calls
that you can run in Claude Code to download the meetings.
"""

import re
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
                # Get meetings that are not yet completed
                if meeting['status'] in ['no', 'in_progress']:
                    meetings.append(meeting)
        elif in_table and not line.startswith('|'):
            break
    
    return meetings

def generate_commands():
    """Generate download commands for all pending meetings."""
    meetings = parse_manifest()
    
    if not meetings:
        print("No pending meetings found")
        return
    
    print(f"Found {len(meetings)} meetings to download")
    print("\n" + "="*80)
    print("DOWNLOAD COMMANDS FOR CLAUDE CODE")
    print("="*80)
    
    for i, meeting in enumerate(meetings, 1):
        meeting_id = meeting['meeting_id']
        date = meeting['date']
        title = meeting['title']
        folder_name = meeting['folder_name']
        
        print(f"\n--- Meeting {meeting['number']}: {title} ({date}) ---")
        
        # Create folder command
        folder_path = f"~/Desktop/8-am-ai/{folder_name}"
        print(f"mkdir -p {folder_path}")
        
        # Generate MCP function calls
        print(f"\n# Get summary for meeting {meeting_id}")
        print("mcp__fireflies__get_summary", {
            "transcriptId": meeting_id,
            "filter": ["summary { overview }"]
        })
        
        print(f"\n# Get transcript for meeting {meeting_id}")
        print("mcp__fireflies__get_transcript", {
            "transcriptId": meeting_id,
            "filter": ["sentences { speaker_name text }", "audio_url"]
        })
        
        print(f"\n# Save files to: {folder_path}")
        print("# - Save summary.overview to summary.txt")
        print("# - Format sentences as 'Speaker: text' lines and save to transcript.txt")
        print("# - Download audio_url to audio.mp3")
        
        if i < len(meetings):
            print("\n" + "-"*60)

def generate_batch_script():
    """Generate a single batch command for Claude Code."""
    meetings = parse_manifest()
    
    if not meetings:
        print("No pending meetings found")
        return
    
    print(f"\nFound {len(meetings)} meetings to process")
    print("\nBATCH DOWNLOAD SCRIPT:")
    print("="*50)
    
    # First, get all the meeting IDs that need processing
    meeting_ids = [m['meeting_id'] for m in meetings[:5]]  # Process first 5
    
    print("Please run these MCP functions in Claude Code:")
    print("\n1. Get summaries for all meetings:")
    for meeting in meetings[:5]:
        print(f"mcp__fireflies__get_summary(transcriptId='{meeting['meeting_id']}', filter=['summary {{ overview }}'])")
    
    print("\n2. Get transcripts for all meetings:")
    for meeting in meetings[:5]:
        print(f"mcp__fireflies__get_transcript(transcriptId='{meeting['meeting_id']}', filter=['sentences {{ speaker_name text }}', 'audio_url'])")
    
    print("\n3. Meeting details for folder creation:")
    for meeting in meetings[:5]:
        print(f"Meeting {meeting['number']}: {meeting['meeting_id']} -> {meeting['folder_name']} ({meeting['date']})")

if __name__ == "__main__":
    print("8am AI Meeting Download Command Generator")
    print("==========================================")
    
    generate_batch_script()