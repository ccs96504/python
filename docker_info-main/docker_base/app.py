from flask import Flask,request
app = Flask(__name__)


@app.get('/index')
def get_stores():
    return "hello world"

if __name__ =="__main__":
    app.run('0.0.0.0',debug=True)