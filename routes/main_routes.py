from flask import Blueprint, render_template, redirect, request, jsonify, session
from auth.strava import exchange_code_access_token
from core.config import CLIENT_ID
import time

main_bp= Blueprint('main', __name__)

@main_bp.route('/')
def home():
    if 'athlete' in session:
        return redirect('/dashboard')
    return render_template('index.html')

@main_bp.route("/connect")
def connect():
    strava_oauth_url=f"http://www.strava.com/oauth/authorize?client_id={CLIENT_ID}&response_type=code&redirect_uri=http://127.0.0.1:5000/callback&approval_prompt=auto&scope=read_all,activity:read_all,profile:read_all"
    return redirect(strava_oauth_url)

@main_bp.route('/callback')
def callback():
    code = request.args.get('code')
    if not code:
        return "Erreur: Aucun code reçu de Strava"
    
    token_data=exchange_code_access_token(code)

    try:
        token_data = exchange_code_access_token(code)
    except Exception as e:
        print(f"[ERREUR CALLBACK] Problème lors de l'échange du code : {e}")
        return "Erreur lors de l'authentification avec Strava.", 500
    
    #stockage dans la session
    session['access_token']=token_data['access_token']
    session['expires_at']=token_data['expires_at']
    session['athlete']=token_data['athlete']

    return redirect('/dashboard')

@main_bp.route('/dashboard')
def dashboard():
    if 'access_token' not in session or time.time()> session['expires_at']:
        return redirect('/connect')

    athlete=session.get('athlete')
    if not athlete:
        return redirect('/')
    
    return redirect('/dashboard/')


@main_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/')

    