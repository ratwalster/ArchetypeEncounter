import boto3
import os

# Create a directory to store audio files if it doesn't exist
output_directory = "audio"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Initialize Polly client
polly = boto3.client('polly', region_name='us-east-1')

files = [
    {
        "filename": "audio/scene1_sam.mp3",
        "voice": "Matthew",
        "language": "en-US",
        "ssml": '<speak><prosody rate="0.9">Hey, you look deep in thought there.<break time="0.3s"/> How are you doing?</prosody></speak>'
    },
    {
        "filename": "audio/scene2_lila.mp3",
        "voice": "Joanna",
        "language": "en-US",
        "ssml": '<speak>Honestly, I\'m kind of reeling.<break time="0.4s"/> I just read something pretty amazing, and I\'m trying to process what it could mean.</speak>'
    },
    {
        "filename": "audio/scene3_sam.mp3",
        "voice": "Matthew",
        "language": "en-US",
        "ssml": '<speak>That sounds heavy.<break time="0.3s"/> Archetypes, like<break time="0.2s"/> the hero or the wise old sage kind of thing?</speak>'
    },
    {
        "filename": "audio/scene3_lila.mp3",
        "voice": "Joanna",
        "language": "en-US",
        "ssml": '<speak>Yeah, exactly.<break time="0.3s"/> Like, the writer, the rebel, the caregiver, those kinds of roles.<break time="0.4s"/> This piece had people like Carl Jung and Maya Angelou talking about how we lean into these roles to feel safe, but they can become masks.</speak>'
    },
    {
        "filename": "audio/scene4_sam.mp3",
        "voice": "Matthew",
        "language": "en-US",
        "ssml": '<speak><prosody rate="0.95">I\'m a graphic designer, and sometimes I catch myself playing The Creative One at work, you know?<break time="0.3s"/> Like, I\'ve got to be quirky and spontaneous all the time.</prosody></speak>'
    },
    {
        "filename": "audio/scene4_lila.mp3",
        "voice": "Joanna",
        "language": "en-US",
        "ssml": '<speak>That\'s exactly what they\'re talking about!<break time="0.4s"/> They say we do that because we\'re scared of being seen, really seen, and maybe rejected.<break time="0.3s"/> I\'m Lila, by the way.</speak>'
    },
    {
        "filename": "audio/scene5_sam.mp3",
        "voice": "Matthew",
        "language": "en-US",
        "ssml": '<speak><prosody rate="0.9">No, don\'t apologize, that\'s cool.<break time="0.3s"/> I\'m Sam.<break time="0.3s"/> So, what\'s the big idea in this thing you read?</prosody></speak>'
    },
    {
        "filename": "audio/scene5_lila.mp3",
        "voice": "Joanna",
        "language": "en-US",
        "ssml": '<speak>Okay, so they talk about how we put people in boxes, like, you meet someone and think, Oh, they\'re The Know-It-All or The Complainer.<break time="0.4s"/> And then we stop listening to what they\'re actually saying.</speak>'
    },
    {
        "filename": "audio/scene6_sam.mp3",
        "voice": "Matthew",
        "language": "en-US",
        "ssml": '<speak><prosody rate="0.95">I\'ve got a coworker who\'s always got an opinion, and I just write her off as The Bossy One.<break time="0.3s"/> But maybe I\'m not hearing what she\'s actually trying to say.</prosody></speak>'
    },
    {
        "filename": "audio/scene6_lila.mp3",
        "voice": "Joanna",
        "language": "en-US",
        "ssml": '<speak>Right?<break time="0.3s"/> And it goes both ways.<break time="0.3s"/> Like, I\'m a teacher, and I catch myself playing The Patient Mentor sometimes, especially with tough students.</speak>'
    },
    {
        "filename": "audio/scene7_sam.mp3",
        "voice": "Matthew",
        "language": "en-US",
        "ssml": '<speak><prosody rate="0.9">Yeah, terrifying\'s the word.<break time="0.3s"/> I mean, I\'m sitting here thinking, Don\'t be The Awkward Guy, Sam.</prosody></speak>'
    },
    {
        "filename": "audio/scene7_lila.mp3",
        "voice": "Joanna",
        "language": "en-US",
        "ssml": '<speak>That\'s so real.<break time="0.4s"/> They said in the piece, Marlon Brando, of all people, he was like, Some days I just want someone to see me without having to perform.</speak>'
    },
    {
        "filename": "audio/scene8_sam.mp3",
        "voice": "Matthew",
        "language": "en-US",
        "ssml": '<speak><prosody rate="0.85">What if I just said, Hey, I\'m kind of lonely sometimes?<break time="0.4s"/> Wow, I can\'t believe I just said that to a stranger.</prosody></speak>'
    },
    {
        "filename": "audio/scene8_lila.mp3",
        "voice": "Joanna",
        "language": "en-US",
        "ssml": '<speak>I\'m glad you did.<break time="0.3s"/> That\'s not The Funny Guy.<break time="0.3s"/> That\'s Sam.<break time="0.4s"/> And honestly, I feel that too.</speak>'
    },
    {
        "filename": "audio/scene9_lila.mp3",
        "voice": "Joanna",
        "language": "en-US",
        "ssml": '<speak>They said you\'ve got to hold those archetypes lightly.<break time="0.4s"/> Like, notice when you\'re boxing someone in, or yourself, and then try to focus on the message instead.</speak>'
    },
    {
        "filename": "audio/scene9_sam.mp3",
        "voice": "Matthew",
        "language": "en-US",
        "ssml": '<speak><prosody rate="0.9">A river, huh?<break time="0.3s"/> That\'s kind of freeing.<break time="0.3s"/> Like, I don\'t have to be The Creative Guy or The Funny Guy forever.</prosody></speak>'
    },
    {
        "filename": "audio/scene10_sam.mp3",
        "voice": "Matthew",
        "language": "en-US",
        "ssml": '<speak><prosody rate="0.9">Hey, um<break time="0.3s"/> would you maybe want to keep talking about this stuff?<break time="0.3s"/> Like, grab a coffee sometime?</prosody></speak>'
    },
    {
        "filename": "audio/scene10_lila.mp3",
        "voice": "Joanna",
        "language": "en-US",
        "ssml": '<speak>I\'d like that.<break time="0.3s"/> Let\'s do it.<break time="0.3s"/> No masks, no roles, just<break time="0.2s"/> two people figuring out what it means to be human.</speak>'
    },
]

failed_files = []

for file_info in files:
    filename = file_info["filename"]
    try:
        raw_voice_name = file_info["voice"]
        if raw_voice_name in ['Matthew', 'Joanna']:
            engine_type = 'neural'
            cleaned_voice_id = raw_voice_name
        else:
            cleaned_voice_id = raw_voice_name
            engine_type = 'standard'

        print(f"DEBUG: Processing {filename}")
        print(f"DEBUG: Using VoiceId: {cleaned_voice_id}, Engine: {engine_type}, SSML length: {len(file_info['ssml'])}")

        response = polly.synthesize_speech(
            Text=file_info["ssml"],
            VoiceId=cleaned_voice_id,
            OutputFormat='mp3',
            TextType='ssml',
            Engine=engine_type
        )

        audio_stream = response.get('AudioStream')
        if audio_stream:
            audio_content = audio_stream.read()
            if audio_content:
                with open(filename, 'wb') as audio_file:
                    audio_file.write(audio_content)
                print(f"SUCCESS: Generated {filename}")
            else:
                error_message = f"Polly returned an empty audio stream. Check SSML: {file_info['ssml'][:100]}..."
                print(f"ERROR: {filename}: {error_message}")
                failed_files.append({"filename": filename, "error": error_message, "ssml": file_info['ssml']})
        else:
            error_message = "No 'AudioStream' key in Polly response."
            print(f"ERROR: {filename}: {error_message}")
            failed_files.append({"filename": filename, "error": error_message, "ssml": file_info['ssml']})

    except Exception as e:
        error_message = f"An unhandled error occurred: {e}"
        print(f"CRITICAL ERROR: {filename}: {error_message}")
        failed_files.append({"filename": filename, "error": error_message, "ssml": file_info['ssml']})

print("\n--- Summary of Failures ---")
if failed_files:
    for fail in failed_files:
        print(f"File: {fail['filename']}")
        print(f"  Error: {fail['error']}")
        print(f"  SSML: {fail['ssml']}")
        print("-" * 30)
    print(f"\n{len(failed_files)} file(s) failed to generate. Check SSML for specific errors.")
else:
    print("All audio files generated successfully!")
