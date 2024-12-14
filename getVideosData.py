import json
import datetime
from datetime import datetime, timedelta
from googleapiclient.discovery import build

# create your API key at https://console.cloud.google.com/apis
API_KEY = ''

def get_videos_by_date_range(start_date, end_date, channel):
    youtube = build('youtube', 'v3', developerKey=API_KEY)


    request = youtube.search().list(
        part="snippet",
        channelId=channel,
        publishedAfter=start_date.isoformat() + "Z",
        publishedBefore=end_date.isoformat() + "Z",
        maxResults=50
    )

    response = request.execute()
    videos = [
        {"videoId": item["id"]["videoId"], "title": item["snippet"]["title"],
         "publishedAt": item["snippet"]["publishedAt"]}
        for item in response.get("items", []) if item["id"]["kind"] == "youtube#video"]
    return videos


def calculate_date_range(start_date_str, number_of_days):
    """
    Convert start date string to datetime and calculate end date.

    Args:
        start_date_str (str): Start date in string format (YYYY-MM-DD).
        number_of_days (int): Number of days to add to start date.

    Returns:
        tuple: Start date and end date as datetime objects.
    """
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = start_date + timedelta(days=number_of_days)
    return start_date, end_date

def get_videos(start_date, number_of_days, channel):
    global videos
    start_date, end_date = calculate_date_range(start_date, number_of_days)

    videos = get_videos_by_date_range(start_date, end_date, channel)

    return videos





