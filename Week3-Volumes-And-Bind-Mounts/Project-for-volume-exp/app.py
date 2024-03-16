import os

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('feedback.html')


@app.route('/exists')
def exist():
    return render_template('exists.html')


@app.route('/create', methods=['POST'])
def submit():
    if request.method == 'POST':
        feedback_title = request.form['title']
        feedback_text = request.form['text']

        with open(f"temp/{feedback_title}.txt", 'w') as fd:
            fd.write(feedback_text)

        if f"{feedback_title}.txt" in os.listdir('feedback'):
            return redirect('/exists')

        with open(f"feedback/{feedback_title}.txt", 'w') as fd:
            fd.write(feedback_text)

        return redirect('/')


@app.route('/<path:file_path>')
def view_file(file_path):
    try:
        # Open the file and read its contents
        with open(file_path, 'r') as file:
            file_contents = file.read()
        return render_template('file_view.html', file_contents=file_contents)
    except FileNotFoundError:
        return "404 File Not found"


if __name__ == "__main__":
    app.run(debug=True)
