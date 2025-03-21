from flask import Flask, render_template, redirect

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/connect")
def connect():
    strava_oauth_url="http://www.strava.com/oauth/authorize?client_id=149550&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=read"
    return redirect(strava_oauth_url)


if __name__=="__main__":
    app.run(debug=True)