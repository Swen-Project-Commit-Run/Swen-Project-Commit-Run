from flask import Blueprint, render_template

index_views = Blueprint('index_views', __name__)

@index_views.route('/')
def index():
    return render_template('index.html')
