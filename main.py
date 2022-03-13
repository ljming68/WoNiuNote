from flask import Flask

app = Flask(__name__,static_url_path='/',template_folder='template',static_folder='static')


if __name__ == "__main__":
    from controller.index import *
    app.register_blueprint(index)
    app.run(debug=True)