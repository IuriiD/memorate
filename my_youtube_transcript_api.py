# This is not an official approach, captions are fetched without authorization
# Is used for POC only
# Example: https://www.youtube.com/watch?v=L8U-pm-vZ4c
# Autoplay between start and stop time, show captions
# https://www.youtube.com/embed/L8U-pm-vZ4c?start=60&end=70&autoplay=1&hl=en&cc_lang_pref=en

from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id, lang_code='en'):
  try:
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    en_transcript = transcript_list.find_transcript([lang_code])
    if not en_transcript:
      print('[getYoutubeCaptions] No English transcript found, halting')
      return None
    transcript = en_transcript.fetch()
    print(f'''[getYoutubeCaptions] Got Youtube captions for the video {video_id}:
    {transcript}''')
    return transcript
  except Exception as e:
    print(f'[getYoutubeCaptions] Error getting youtube captions: ', e)
    return None

def join_yt_transcripts(transcripts):
    text_only = [piece['text'] for piece in transcripts]
    return ' '.join(text_only)

# t = get_transcript('L8U-pm-vZ4c')
# print(join_yt_transcripts(t))

url = 'https://www.youtube.com/watch?v=L8U-pm-vZ4c'

def get_yuotube_video_id(youtube_url):
  return youtube_url.split('v=')[1]

print(get_yuotube_video_id(url))