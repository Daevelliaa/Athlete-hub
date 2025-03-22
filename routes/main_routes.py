from flask import Blueprint, Flask, render_template, redirect, request, jsonify
from auth.strava import exchange_code_access_token

main_bp= Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('index.html')

@main_bp.route("/connect")
def connect():
    strava_oauth_url="http://www.strava.com/oauth/authorize?client_id=149550&response_type=code&redirect_uri=http://127.0.0.1:5000/callback&approval_prompt=force&scope=read_all,activity:read_all,profile:read_all"
    return redirect(strava_oauth_url)

@main_bp.route('/callback')
def callback():
    code = request.args.get('code')
    if not code:
        return "Erreur: Aucun code reçu de Strava"
    
    token_data=exchange_code_access_token(code)
    return jsonify(token_data)
    