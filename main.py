import getCaptions
import getVideosData


def main():
    videos = getVideosData.get_yesterday_videos()

    # Print the result
    for video in videos:
        print(f"Title: {video['title']}, Video ID: {video['videoId']}, Published At: {video['publishedAt']}")
        getCaptions.download_captions(video['videoId'])

if __name__ == "__main__":
    main()