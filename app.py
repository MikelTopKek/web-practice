from flask import Flask, render_template, request, redirect


app = Flask(__name__)
subject = []
students = []
marks = []


@app.route('/')
def main():
    return render_template(
        'index.html'
    )


@app.route('/add_subject')
def add_subject():
    request_form = request.form
    # Добавлять в список новый предмет
    subject.append()
    return redirect('/')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True  # Should be set only for development
    )
