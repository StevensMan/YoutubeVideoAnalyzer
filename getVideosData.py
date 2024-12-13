import datetime
from datetime import datetime, timedelta
from googleapiclient.discovery import build

# create your API key at https://console.cloud.google.com/apis
API_KEY =  'YOUR_YOUTUBE_API_KEY'
CHANNEL_ID = 'UCPY6gj8G7dqwPxg9KwHrj5Q'  # Суспільне Новини 'TARGET_CHANNEL_ID'

def get_videos_by_date_range(start_date, end_date):
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    request = youtube.search().list(
        part="snippet",
        channelId=CHANNEL_ID,
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


# Define yesterday's date range
def get_yesterday_date_range():
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    start_date = datetime(yesterday.year, yesterday.month, yesterday.day, 0, 0, 0)
    end_date = datetime(today.year, today.month, today.day, 0, 0, 0)
    return start_date, end_date


def get_yesterday_videos():
    global videos
    # Get the date range for yesterday
    start_date, end_date = get_yesterday_date_range()
    # Call the function
    videos = get_videos_by_date_range(start_date, end_date)

    return videos

get_yesterday_videos()




