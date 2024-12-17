import getCaptions
import getVideosData

import json
from datetime import datetime, timedelta

def load_config(config_file):
    """
    Load configuration from a JSON file.

    Args:
        config_file (str): Path to the configuration file.

    Returns:
        dict: Parsed configuration parameters.
    """
    with open(config_file, "r") as file:
        return json.load(file)

def display_config_parameters(config):
    """
    Display configuration parameters.

    Args:
        config (dict): Configuration parameters.
    """
    print("YouTube API Key:", config.get("YouTubeAPIKey"))
    print("List of YouTube Channel IDs:", config.get("YouTubeChannelIDs"))
    print("Start Date:", config.get("StartDate"))
    print("Number of Days:", config.get("NumberOfDays"))
    print("Including timestamps:", config.get("IncludingTimestamps"))
    print("Dumpting to single file:", config.get("DumpToSingleFile"))



def main():

    config_file = "config.json"  # Path to your configuration file
    config = load_config(config_file)

    # Display parameters from configuration file
    display_config_parameters(config)

    getVideosData.API_KEY = config.get("YouTubeAPIKey")
    include_timestamps = config.get("IncludeTimestamps", False)
    dump_to_single_file = config.get("DumpToSingleFile", True)
    channels = config.get("YouTubeChannelIDs")
    for channel in channels:
        try:
            # Fetch the transcript for this language
            videos = getVideosData.get_videos(config.get("StartDate"), config.get("NumberOfDays"), channel )
            # Print the result
            for video in videos:
                print(f"Title: {video['title']}, Video ID: {video['videoId']}, Published At: {video['publishedAt']}")
                getCaptions.download_captions(channel, video['videoId'], video['title'], video['publishedAt'],
                                              include_timestamps, dump_to_single_file)
        except Exception as e:
            print(f"Failed to fetch videos for channel {channel}: {e}")


if __name__ == "__main__":
    main()