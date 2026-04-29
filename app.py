from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, CI/CD World!"

if __name__ == '__main__':
    # host='0.0.0.0' ensures the app is accessible outside the container later
    app.run(host='0.0.0.0', port=5000)