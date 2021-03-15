from flask import Flask, render_template
app = Flask(__name__)

data = [
    {
        'content' : 'This was the thing that happened today!',
        'author' : 'clickbait kevin'
    }
    ,
    {
        'content' : 'THis is a placeholder',
        'author' : 'cool david!'
    }
]

@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)