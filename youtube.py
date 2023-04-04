from pytube import YouTube

class Youtube:
    def video(self):
        pass
        
    def on_progress(stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage = bytes_downloaded / total_size * 100
        print(f'{percentage:0.2f}% downloaded...')
        
        
    def info_title(self,url):
        yt = YouTube(url)
        return yt.title
    
    def info_length(self,url):
        yt = YouTube(url)
        return yt.length
    
    def download(self,url,loc,title):
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.output_path = "."
        stream.download(output_path=f"{loc}",filename=f'{title}.mp4')
        
    
    
    