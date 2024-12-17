import os
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (TranscriptsDisabled, VideoUnavailable, NoTranscriptFound)

def ensure_directory_exists(directory_path):
    """
    Ensure that a directory exists, creating it if necessary.

    Args:
        directory_path (str): Path to the directory.
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Directory created: {directory_path}")


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


def save_captions_by_language(captions_by_language, channel, video_id, title, published_at, include_timestamps, dump_to_single_file):
    results_directory = f"results/{channel}"
    ensure_directory_exists(results_directory)
    if captions_by_language:
        for language_code, captions in captions_by_language.items():


            output_file =  f"{results_directory}/{video_id}_{language_code}_captions.txt"
            with open(output_file, "w", encoding="utf-8") as file:
                file.write(f"{title}\nhttps://www.youtube.com/watch?v={video_id}\nPublished At: {published_at}\n\n")
                for entry in captions:
                    # file.write(f"[{entry['start']:.2f}] {entry['text']}\n")
                    if include_timestamps:
                        file.write(f"[{entry['start']:.2f}] {entry['text']}\n")
                    else:
                        file.write(f"{entry['text']}\n")
            print(f"Captions for language '{language_code}' saved to {output_file}")
    else:
        print("No captions to save.")

    if dump_to_single_file:
        combined_output_file = os.path.join(results_directory, "combined_transcripts.txt")
        combine_transcripts_from_files(results_directory, combined_output_file)
        print(f"All transcripts combined into a single file: {combined_output_file}")

def download_captions(channel, video_id, title, published_at, include_timestamps, dump_to_single_file):
    captions_by_language = download_video_captions_all_languages(video_id)
    if captions_by_language:
        save_captions_by_language(captions_by_language, channel, video_id, title, published_at, include_timestamps, dump_to_single_file)


def combine_transcripts_from_files(output_directory, combined_output_file):
    """
    Combine all transcript files in the output directory into a single file.

    Args:
        output_directory (str): Path to the directory containing transcript files.
        combined_output_file (str): Path to the combined output file.
    """
    with open(combined_output_file, "w", encoding="utf-8") as combined_file:
        for filename in os.listdir(output_directory):
            if filename.endswith("_captions.txt"):
                video_id = filename.replace("_captions.txt", "")
                combined_file.write(f"\n=== Transcripts for video: {video_id} ===\n")
                with open(os.path.join(output_directory, filename), "r", encoding="utf-8") as file:
                    combined_file.write(file.read())