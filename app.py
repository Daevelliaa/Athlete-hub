from flask import Flask
from routes.main_routes import main_bp
from core.config import SECRET_KEY_FLASK
from dash_app import create_dash_app

app=Flask(__name__)

app.secret_key=SECRET_KEY_FLASK

app.register_blueprint(main_bp)

dash_app=create_dash_app(app)

if __name__=="__main__":
    app.run(debug=True)