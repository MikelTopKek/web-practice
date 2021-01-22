from flask import Flask, render_template, request, redirect


app = Flask(__name__)

children = {
    'Dan': ['Stan', 'David', 'Ted']
}


@app.route('/')
def main():
    return '<b> Hello world! </b>'


@app.route('/temp')
def template():
    return render_template('index.html', name='Stan')


@app.route('/user/<username>/', methods=['GET'])
def user(username):
    query_params = request.args
    return render_template(
        'form.html',
        name=username,
        surname=query_params.get("surname", ''),
        children=children.get(username, [])
    )


@app.route('/user/<username>/new-child', methods=['POST'])
def add_child(username):
    request_form = request.form
    children[username].append(request_form.get('childNameKey'))
    return redirect(f'/user/{username}/')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True  # Should be set only for development
    )
