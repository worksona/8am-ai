#!/usr/bin/env python3
"""
Format the transcript sentences into proper transcript.txt format
"""

# Sample transcript data from the MCP response
transcript_data = """transcript sentence format: {Time} {SpeakerName}: {Content}. Time is in seconds.
    
    9.2: Bibiana Souza: Good morning. 10.32: Scott Morton: Good morning. 10.96: Scott Morton: How are you? 12.32: Bibiana Souza: I'm doing awesome. 15.04: Bibiana Souza: Pretty early. 17.28: Bibiana Souza: Are you in Vancouver? 19.04: Scott Morton: No, I'm in Calgary. 24.24: David Olsson: Good morning. 25.6: David Olsson: Morning. 25.96: David Olsson: Hey, David and welcome bb. 30.58: David Olsson: Hello. 32.5: Bibiana Souza: You're an early bird, David. 34.18: Bibiana Souza: I was catching up on my messages and I'm like, oh my God. 36.9: Bibiana Souza: 4:30. 38.98: Bibiana Souza: How's he doing? 40.74: Scott Morton: Where are you? 41.5: Scott Morton: It's 4:30 in the morning. 42.86: Scott Morton: Are you in Hawaii or something? 44.34: Bibiana Souza: Vancouver. 44.98: Bibiana Souza: Vancouver. 45.54: David Olsson: Oh, Vancouver. 46.3: David Olsson: Okay. 46.7: David Olsson: Yeah. 46.9: Bibiana Souza: No, but David was up at 4:30. 48.58: Scott Morton: Oh yeah, I get up at 4:30 too. 52.18: David Olsson: Yeah. 52.58: Bibiana Souza: How do you guys do it? 55.24: David Olsson: Among some peers here. 56.4: David Olsson: But yeah, like it just happened and. 59.92: Scott Morton: Then sometimes you just wake up. 61.84: David Olsson: Right, David? 62.4: Scott Morton: You wake up and you're like, oh, I gotta do this thing and you just go and do it. 66.76: David Olsson: When I first started waking up, I woke up very awake and I was like, I'm not, I'm not tired. 73.4: David Olsson: Okay, get up. 74.52: David Olsson: So it was energizing. 75.96: David Olsson: And then my pattern of life changed and all the other things. 79.08: David Olsson: But yeah, sometimes I'm like, I should hold off on posting because that's people's response. 85.42: David Olsson: I'm like, yeah, it's good for the east coast. 88.58: Scott Morton: Yeah, yeah, exactly. 89.94: David Olsson: Yeah. 90.34: David Olsson: Yeah, that's funny. 92.9: David Olsson: That's funny. 93.58: David Olsson: But yes, Scott's in Calgary. 96.54: David Olsson: Yes, or Calgary specifically. 98.18: David Olsson: You live in Calgary? 99.3: David Olsson: Yeah. 99.74: Scott Morton: Yeah, just south of Calgary. 101.06: David Olsson: Yep. 102.26: David Olsson: And. 103.22: David Olsson: And Jason, this is bb. 105.3: David Olsson: BD and I work together now. 106.74: David Olsson: And Jason lives here in Calgary and he's a good friend. 111.44: Scott Morton: Hey Jason. 115.68: David Olsson: Yeah, it's about that time. 117.12: David Olsson: Everybody's doing that. 118.8: David Olsson: And Folio's dealing with family stuff right. 121.64: David Olsson: Now, so he's not going to join us. 122.92: David Olsson: And Hanif is in Mexico with his son. 126.64: David Olsson: Oh yeah. 128.24: David Olsson: So that's a good thing. 131.44: David Olsson: He actually submitted an application for his project, Stone Maps and he had a. 139.11: David Olsson: Well, he. 139.59: David Olsson: He vibe coded himself a lovable.dev website. 144.11: David Olsson: And it takes money. 146.19: David Olsson: Yep. 146.91: David Olsson: It's functional. 147.79: David Olsson: It does something. 148.91: David Olsson: He says it only takes his. 150.35: David Olsson: So far it's only taken his money. 153.95: David Olsson: I'm like, that's. 155.23: David Olsson: Welcome to the show, man. 157.07: Scott Morton: Yeah, that's awesome. 158.43: Scott Morton: That's. 158.99: Scott Morton: That's how it goes for a little bit anyways. 161.79: David Olsson: Yeah. 162.19: David Olsson: But yeah, in this environment we kind. 166.3: David Olsson: Of talk about the stuff that's going on with the AI. 170.58: David Olsson: Initially it was about trying to teach people and everybody is learning on their own path. 175.02: David Olsson: And what I mentioned, bb, is that things are getting different for us at Atomic because you're coming on board and we're scaling now with four people that. 182.38: David Olsson: Are working in development and Fulvio has just cranked a wheel he's turned a corner and he, he figured out what he can do now in terms of his superpowers. 193.3: David Olsson: So he's building shit. 194.86: David Olsson: But I wanted to show you this, which is. 196.86: David Olsson: I think I've showed this before. 197.9: David Olsson: But we're in the throes of trying to define what works on is. 201.66: David Olsson: And so I've been able to use Claude code to ask. 206.7: David Olsson: It to figure. 207.82: David Olsson: Out what works on it by starting the APIs. 210.14: David Olsson: And then I take whatever that corpus is. 212.78: David Olsson: So it gives me something. 213.98: David Olsson: And I built out using cloud code marketing websites. 218.46: David Olsson: Bing, bing, bing, bing, bing. 223.9: David Olsson: Pow. 224.46: Scott Morton: Oh, wow. 227.58: David Olsson: And it just keeps going because it's. 230.02: David Olsson: Not a lot of work. 231.5: David Olsson: Yeah."""

def format_transcript_from_fireflies(transcript_text):
    """Convert Fireflies transcript format to Speaker: Text format"""
    lines = []
    
    # Extract the actual transcript part (after the format description)
    content_start = transcript_text.find('9.2: Bibiana Souza:')
    if content_start == -1:
        return "Could not find transcript content"
    
    content = transcript_text[content_start:]
    
    # Split by timestamps and reformat
    import re
    
    # Find all timestamp patterns like "123.45: Speaker Name: Text"
    pattern = r'(\d+\.?\d*): ([^:]+): ([^0-9]*?)(?=\d+\.?\d*:|$)'
    matches = re.findall(pattern, content, re.DOTALL)
    
    for timestamp, speaker, text in matches:
        text = text.strip()
        if text:  # Only add non-empty text
            lines.append(f"{speaker}: {text}")
    
    return '\n'.join(lines)

if __name__ == "__main__":
    formatted = format_transcript_from_fireflies(transcript_data)
    print(formatted[:1000] + "..." if len(formatted) > 1000 else formatted)