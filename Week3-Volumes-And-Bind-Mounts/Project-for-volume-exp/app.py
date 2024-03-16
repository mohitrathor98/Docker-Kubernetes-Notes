from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('feedback.html')


@app.route('/create', methods=['POST'])
def submit():
    if request.method == 'POST':
        feedback_title = request.form['title']
        feedback_text = request.form['text']
        print(feedback_title)
        print(feedback_text)
        return feedback_title + ' ' + feedback_text


if __name__ == "__main__":
    app.run(debug=True)
