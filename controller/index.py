from flask import Blueprint,render_template

index = Blueprint('index',__name__)

@index.route('/')
def index_show():

    return render_template('test.html')
