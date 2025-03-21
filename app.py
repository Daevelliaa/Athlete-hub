from flask import Flask, render_template, redirect, request

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/connect")
def connect():
    strava_oauth_url="http://www.strava.com/oauth/authorize?client_id=149550&response_type=code&redirect_uri=http://127.0.0.1:5000/callback&approval_prompt=force&scope=read_all,activity:read_all,profile:read_all"
    return redirect(strava_oauth_url)

@app.route('/callback')
def callback():
    error = request.args.get('error')
    code = request.args.get('code')

    if error == 'access_denied':
        return "L'utilisateur a refusé la connexion à Strava ❌"
    elif code:
        return f"Connexion réussie ! Code reçu : {code}"
    else:
        return "Erreur inconnue"


if __name__=="__main__":
    app.run(debug=True)