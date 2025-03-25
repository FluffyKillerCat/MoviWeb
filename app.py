from flask import Flask, request, jsonify, render_template, redirect, url_for
from datamanager.sqlite_data_manager import SQLiteDataManager
from datamanager.db import db
from routes import register_blueprints
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.abspath('datamanager/db.sqlite')}"
db.init_app(app)

register_blueprints(app)
data_manager = SQLiteDataManager()


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
