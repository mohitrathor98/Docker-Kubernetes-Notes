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
        script_dir = os.getcwd()
        feedback_title = request.form['title']
        feedback_text = request.form['text']

        temp_feedback_file = os.path.join(
            script_dir, 'temp',
            f'{feedback_title}.txt')

        with open(temp_feedback_file, 'w') as fd:
            fd.write(feedback_text)

        feedback_dir = os.path.join(script_dir, 'feedback')
        if f"{feedback_title}.txt" in os.listdir(feedback_dir):
            return redirect('/exists')

        feedback_file = os.path.join(feedback_dir, f"{feedback_title}.txt")
        with open(feedback_file, 'w') as fd:
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
