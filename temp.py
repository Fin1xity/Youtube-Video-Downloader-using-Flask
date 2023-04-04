# Import the necessary module
from pytube import YouTube

# Provide the YouTube video URL
video_url = "https://youtu.be/6SPIAjNqlTQ"

# Create a YouTube object
yt = YouTube(video_url)

# Print video information
print("Title:", yt.title)
print("Description:", yt.description)
print("Author:", yt.author)
print("Length:", yt.length, "seconds")

# Select the highest resolution stream
stream = yt.streams.get_highest_resolution()

# Set the output path
stream.output_path = '.'

# Define progress function
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = bytes_downloaded / total_size * 100
    print(f'{percentage:0.2f}% downloaded...')

# Download the video
stream.download(output_path='.', filename='new.mp4')

print("Video downloaded successfully!")

