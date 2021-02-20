# /scripts/get_episode_transcripts.py
# author: Jared Wilber

"""get_episode_transcripts.py

This script scrapes the official Bob Ross YouTube channel for transcripts of
each episode of The Joy of Painting. It uses youtube_transcript_api to
interface with the website.

"""

import pandas as pd

from youtube_transcript_api import YouTubeTranscriptApi


def create_df(file):
    '''Reads in data from external source and creates a dataframe with necesssary
    columns to download transcripts'''
    # Create dataframe from csv file
    data = pd.read_csv(file)
    df = pd.DataFrame(data)
    # Create videoID column. ID starts at pos 30 in string
    df['videoID'] = df['youtube_src'].str.slice(30)
    return df


def get_videoIDs(dataf):
    '''Takes in a dataframe and returns a list of videoIDs'''
    videoIDs = dataf['videoID'].tolist()
    return videoIDs


def downloadTranscript(videoID):
    '''Takes in a YT VideoID and returns the transcript object'''
    transcript_object = YouTubeTranscriptApi.get_transcript(videoID)
    return transcript_object


def generateTranscriptText(transcript_object):
    '''Takes in a transcript object and returns a string of the concatenated
    text'''
    line_count = 0
    transcript_text = ''
    for line in transcript_object:
        transcript_text += (transcript_object[line_count]['text'] + " ")
        line_count += 1
    return transcript_text


def transcript_to_file(videoID, transcript_text):
    '''Takes in a transcript text string and writes it to a file with name
    videoID.txt'''
    with open(f'../data/transcripts/{videoID}.txt', 'w') as f:
        f.write(transcript_text)


def transcript_pipeline(videoID):
    '''Runs suite of transcript functions in order for a single videoID'''
    print('----------')
    # Get transcript object for a video
    transcript_object = downloadTranscript(videoID)
    # Generate a text string for transcript
    transcript_text = generateTranscriptText(transcript_object)
    # Write transcript text to file with name <videoID>.txt
    transcript_to_file(videoID, transcript_text)
    print(f'Video ID: {videoID} has been written to file {videoID}.txt')


def transcriptErrorReport(df, error_list):
    '''Takes in a list of videoIDs and prints user readable information'''
    error_dicts = []
    # Retrieves information about each ID from dataf, saves to list
    for videoID in error_list:
        row = df.loc[df['videoID'] == videoID]
        error_dicts.append(row.to_dict('records')[0])

    # Prints each entry's info from error list
    for entry in error_dicts:
        print(f'''Episode Title: {entry['painting_title']}
        Season: {entry['season']}
        Episode: {entry['episode']}
        Youtube Link: {entry['youtube_src']}
        -----------------------------------''')


# Get transcripts for all videos
def multipleTranscripts(df, videoIDs):
    '''Takes in a list of YT video IDs and runs transcript_pipeline.
    Returns error report after completion'''
    # Empty list to store videoIDs that encounter errors
    error_list = []
    # Iterate over videoIDs and run pipeline
    for videoID in videoIDs:
        try:
            transcript_pipeline(videoID)
        # If failure, print message and save ID to error_list
        except Exception:
            print(f'No transcript found for videoID - {videoID}')
            error_list.append(videoID)

    # Once operation complete, print error report
    transcriptErrorReport(df, error_list)


if __name__ == '__main__':
    # Assign csv filepath and create dataframe
    file = '../data/bob_ross_paintings.csv'
    df = create_df(file)

    # Get list of videoIDs
    videoIDs = get_videoIDs(df)

    # Run transcript pipeline
    multipleTranscripts(df, videoIDs)

    print("Done!")
