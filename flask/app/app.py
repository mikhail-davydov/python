from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__, instance_relative_config=True)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    name = request.args.get("name", "noname")
    return f"Hello, {escape(name)}!"


@app.get('/login')
def login_get():
    return render_template('login.html')


@app.post('/login')
def login_post():
    name = request.form['username'] if request.form['username'] else 'noname'
    return f"Hello, {escape(name)}!"


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


@app.route('/json')
def show_json():
    name = request.args.get("name", "noname")
    order_id = request.args.get("order_id", "None")
    # apply auto jsonify to dict response
    return {
        'name': escape(name),
        'orderId': escape(order_id),
        'path': request.path,
    }
    # return jsonify({
    #     'name': escape(name),
    #     'orderId': escape(order_id),
    #     'path': request.path,
    # })


if __name__ == '__main__':
    app.run()
