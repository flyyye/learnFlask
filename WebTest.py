from aiohttp import web
from flask import Flask,render_template,request,redirect

app = Flask(__name__)

@app.route('/home',methods = ['GET'])
def home():
    if request.methods == "GET":
        return render_template('home.html')#从template文件中根据给定的上下文呈现相应的模板
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='9520')