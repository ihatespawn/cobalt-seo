from flask import Flask, request, Response, render_template, redirect

app = Flask(__name__)

CRAWLERS = [
    "googlebot", "bingbot", "slurp", "duckduckbot", "baiduspider", "yandexbot",
    "sogou", "exabot", "facebot", "twitterbot"
]

ALTERNATIVES = [
    "4K Video Downloader", "Y2mate", "SaveFrom.net", "ByClick Downloader",
    "WinX YouTube Downloader", "Any Video Converter Free", "Free YouTube Download",
    "aTube Catcher", "iTubeGo", "Catchvideo.net", "VidPaw", "Ymp4", "Acethinker",
    "2conv", "YTMP3", "Y2Meta", "TubeMate", "ClipConverter", "ClipGrab", "youtube-dl"
]

@app.before_request
def block_crawlers():
    user_agent = request.headers.get('User-Agent', '').lower()
    if any(crawler in user_agent for crawler in CRAWLERS):
        if request.path.split('/')[1] == "alternative-to":
            return render_template("alt.html", thing=request.path.split('/')[2], domain=request.headers['Host'])
        else:
            return render_template("seo.html", domain=request.headers['Host'])

@app.route('/')
def home():
    return redirect("https://cobalt.tools", 301) #render_template("seo.html")

def alternative(thing):
    return redirect("https://cobalt.tools", 301) #render_template("alt.html", thing=thing)

with app.app_context():
    for alt in ALTERNATIVES:
        alter = alt.lower().replace(' ', '-')
        path = '/alternative-to/' + alter
        app.add_url_rule(path, alter + '-alternative', view_func=lambda alt=alt: alternative(alt))

if __name__ == '__main__':
    app.run(debug=True)
