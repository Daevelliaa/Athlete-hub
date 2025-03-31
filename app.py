from flask import Flask
from routes.main_routes import main_bp
from core.config import SECRET_KEY_FLASK
from dash_app import create_dash_app
from dash_components.dash_callback import register_callbacks

app=Flask(__name__)

app.secret_key=SECRET_KEY_FLASK

app.register_blueprint(main_bp)

dash_app=create_dash_app(app)
register_callbacks(dash_app)

if __name__=="__main__":
    app.run(debug=True)