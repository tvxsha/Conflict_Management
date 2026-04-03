from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/written')
def written():
    return render_template('written.html')

@app.route('/visual')
def visual():
    return render_template('visual.html')

@app.route('/audio')
def audio():
    return render_template('audio.html')

if __name__ == '__main__':
    app.run(debug=True)
