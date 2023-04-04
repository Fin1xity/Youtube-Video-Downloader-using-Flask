from flask import Flask
from home import Home


app = Flask(__name__)

h = Home()


app.add_url_rule('/home','h',h.index)
app.add_url_rule('/','a',h.new)







if __name__ == "__main__":
    app.run(debug=True)