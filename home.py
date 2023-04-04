from flask import Flask,render_template,request
from youtube import Youtube


class Home:

    def index(self):
        return render_template('index.html')
    
    def new(self):
        url = request.args.get('url')
        loc = request.args.get('loc')
        yt = Youtube()
        q = f"'{url}'"
        title=yt.info_title(q)
        #length=yt.info_length(q)
        yt.download(q,loc,title)
        return render_template('index.html',act = True)
    
        



    
    
    
    
    