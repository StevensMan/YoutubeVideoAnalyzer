from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (TranscriptsDisabled, VideoUnavailable, NoTranscriptFound)


def download_video_captions_all_languages(video_id):
    """
    Fetches captions for all available languages for a YouTube video.

    Args:
        video_id (str): The YouTube video ID.

    Returns:
        dict: A dictionary where keys are language codes and values are lists of captions.
    """
    try:
        # Get available transcript languages for the video
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        captions_by_language = {}

        # Iterate through available transcripts by language
        for transcript in transcript_list:
            try:
                # Fetch the transcript for this language
                language_code = transcript.language_code
                captions = transcript.fetch()
                captions_by_language[language_code] = captions
            except Exception as e:
                print(f"Failed to fetch captions for language {transcript.language_code}: {e}")

        return captions_by_language

    except TranscriptsDisabled:
        print(f"Captions are disabled for video: {video_id}")
        return None
    except VideoUnavailable:
        print(f"Video unavailable: {video_id}")
        return None
    except NoTranscriptFound:
        print(f"No transcripts found for video: {video_id}")
        return None
    except Exception as e:
        print(f"An error occurred for video {video_id}: {e}")
        return None


def save_captions_by_language(captions_by_language, video_id):
    """
    Saves captions for all languages to separate text files.

    Args:
        captions_by_language (dict): Captions grouped by language code.
        video_id (str): The YouTube video ID.
    """
    if captions_by_language:
        for language_code, captions in captions_by_language.items():
            output_file = f"results/{video_id}_{language_code}_captions.txt"
            with open(output_file, "w", encoding="utf-8") as file:
                for entry in captions:
                    file.write(f"[{entry['start']:.2f}] {entry['text']}\n")
            print(f"Captions for language '{language_code}' saved to {output_file}")
    else:
        print("No captions to save.")

def download_captions(video_id):
    captions_by_language = download_video_captions_all_languages(video_id)
    if captions_by_language:
        save_captions_by_language(captions_by_language, video_id)

