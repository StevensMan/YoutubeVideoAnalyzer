# YouTubeVideoAnalyzer

This script allows specifying list of YouTube channels and range of dates
Program will download audio captions for each video and save them into ***results*** directory. It will create a separate folder for each channel where channel ID becomes a folder name. 
Results file are named as follows: **videoID**_**captionsLanguage**_captions.txt 
Please note - captions could exists in different languages, some videos may have captions in multiple languages simultaneously. 

## Usage
Most parameters required to run this program are stored in *config.json* file. Below is the example

    {  
        "YouTubeAPIKey": "AIzaSyCga4YKPtFcYzp839VNDKn6nwDATTJP7y",  
        "YouTubeChannelIDs": ["UCpakYOycn3O5W5S50l-0VIg","UCPY6gj8G7dqwPxg9KwHrj5Q" ],  
        "StartDate": "2024-11-18",  
        "NumberOfDays": 3, 
        "IncludeTimestamps": false,
        "DumpToSingleFile": true
    }

 - *YouTubeAPIKey* -  personal key should be obtained from https://console.cloud.google.com/apis/credentials
 - *YouTubeChannelIDs* - list of channels to pull video captions from, single or multiple channels.  To get a channel ID for a channel use tool similar to https://yt-link.com/stats Enter YouTube user name and click on down arrow symbol to expand channel ID
 - *StartDate* - UTC date of first video to pull, format *2024-11-18*
 - *NumberOfDays* - number of days since start date
 -  *IncludeTimestamps* - can add a timestamp in the transcript to easy identify moment in the video 
 - *DumptToSingleFile* - combines all results for the run to single file per channel

### Example of output file:

> Холодная война - война Добра со Злом  
> https://www.youtube.com/watch?v=7h6_CsHFuw8   Published At:
> 2024-12-01T06:00:06Z      [0.44] Добро пожаловать на Youtube канал
> Сергея   [2.16] любарского термин холодная война впервые   [5.68] был
> использован известным английским   [7.56] писателем джорджем орлом тот
> самый   [10.36] Джордж орл в его иссе 1945 года   [16.64] называется
> где в этом эссе он описывал   [20.44] предсказывал очень абсолютно
> справедливо   [22.48] предсказывал холодную войну которая   [25.96]
> ворит в мире так в мире   [30.44] будет ядерное   [32.08] оружие и те
> из вас которые считают что   [35.96] закончивший в ту или в другую
> сторону   [37.76] Победа или поражением Украины война в   [41.20]
> Европе вернёт всё на свои места и Россия ...

Written with **Python 3.13**  
Install following dependencies to run:

    pip install google-api-python-client  
    pip install youtube-transcript-api

### Below are basic instructions for configuring environment and running a Python program on your computer

#### Prerequisites

1.  **Install Python**
    
    -   On **Windows**:
        -   Download the latest version of Python from [python.org](https://www.python.org/).
        -   During installation, ensure you check the box that says **Add Python to PATH**.
    -   On **macOS**:
        -   Python comes pre-installed, but it’s recommended to install the latest version using [Homebrew](https://brew.sh/).
            
            Copy code
            
            `brew install python` 
            
2.  **Install a Code Editor (Optional)**
    
    -   Use an editor like [Visual Studio Code](https://code.visualstudio.com/) or any other text editor of your choice.

----------

### Step 1: Install Virtual Environment (Recommended)

A virtual environment isolates your project’s dependencies to prevent conflicts with system-wide Python libraries.

1.  Open your terminal:
    
    -   **Windows**: Use the Command Prompt or PowerShell.
    -   **macOS**: Use the Terminal app.
2.  Navigate to your project folder:
    
    bash
    
    Copy code
    
    `cd path/to/your/project` 
    
3.  Create a virtual environment:
    
    Copy code
    
    `python -m venv venv` 
    
4.  Activate the virtual environment:
    
    -   **Windows**:
        
        Copy code
        
        `venv\Scripts\activate` 
        
    -   **macOS**:
        
        bash
        
        Copy code
        
        `source venv/bin/activate` 
        

----------

### Step 2: Install Dependencies

1.  Install `pip` (if not already installed):
    
    css
    
    Copy code
    
    `python -m ensurepip --upgrade` 
    
2.  Upgrade `pip` to the latest version:
    
    css
    
    Copy code
    
    `python -m pip install --upgrade pip` 
    
3.  Install the required libraries:
    
    Copy code
    
    `pip install google-api-python-client youtube-transcript-api` 
    

----------

### Step 3: Run the Python Program

1.  Ensure your Python script is saved in the project folder (e.g., `main.py`).
    
2.  Run the script:
    
    css
    
    Copy code
    
    `python main.py` 
    

----------

### Additional Notes

-   **Exiting the Virtual Environment**:  
    Run the following command:
    
    -   **Windows**:
        
        Copy code
        
        `deactivate` 
        
    -   **macOS**:
        
        Copy code
        
        `deactivate` 
        
-   **Reactivating the Virtual Environment**:  
    Follow the same activation steps as in Step 1.
    

----------

### Troubleshooting

-   If you encounter a "command not found" error for `python`, try using `python3` instead.
-   For issues with `pip install`, ensure your internet connection is active and check for typos in the library names.
-   On macOS, you may need to grant permission to run scripts. If prompted, follow the on-screen instructions.
