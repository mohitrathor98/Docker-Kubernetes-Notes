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


if __name__ == "__main__":
    app.run(debug=True)
