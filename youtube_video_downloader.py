import yt_dlp

import time



video_url_list_file="video_list.txt"
storage_dir="./videos"

def download_video(url, output_path='./videos'):
    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


# Read the text file and download each video
with open(video_url_list_file, 'r') as file:
    urls = file.readlines()

for url in urls:
    url = url.strip()  # Remove any leading/trailing whitespace or newlines
    if url:  # Ensure the URL is not empty
        download_video(url)
        time.sleep(10) 

print("All downloads completed!")



