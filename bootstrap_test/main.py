from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('bootstrap.html')

@app.route('/images/<path:path>')
def send_image(path):
    return send_from_directory('images', path)

# @app.route('/about')
# def about():
#     return render_template('about.html')
#
# @app.route('/blog')
#
#
# @app.route('/portfolio')


if __name__ == '__main__':
    app.run()
