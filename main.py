from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World makale!'

@app.route('/greet/<name>')
def greet(name):
    return f'Hello Good Morning, {name}!'

if __name__ == '__main__':
    app.run(debug=True)