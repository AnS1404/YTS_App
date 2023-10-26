from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline 
from flask import Flask, request
 
''' This is document naming. Something that is required to use flask effectively '''
transcript = Flask(__name__)

''' Whenever you use an api it requests something. Here we are calling api to request summary. '''
@transcript.get('/summary')

def summary_api():
    ''' will get url of video which we want to summarize '''
    url = request.args.get('url', '')
    ''' Transcript api uses video id to fetch tanscript '''
    video_id = url.split('=')[1]
    summary = get_summary(get_transcript(video_id))
    return summary, 200

''' Function defined to fetch transcript from api from given video id and include it into the list '''
def get_transcript(video_id):
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    transcript = ''.join([d['text']] for d in transcript_list)
    return transcript

''' There is a limitation at at one time it can only summarize 1000 characters so this function breaks the given texts into 1000 char and summarizes the text '''
def get_summary(transcript):
    summariser = pipeline('summarization')
    summary = ''
    ''' Breaks the transcript again and again and joins it into resultant summary text '''
    for i in range(0,(len(transcript)//1000)+1):
        summary_text = summariser(transcript[i*1000:(i+1)*1000])[0]['summary_text']
        summary = summary + summary_text + ''
    return summary

if __name__ == '__main__':
    transcript.run()

