from aiohttp import web
from flask import Flask,render_template,request,redirect,session,url_for

app = Flask(__name__)

# "mrx": "123456",
# "gordon": "654321",
# app.debug = True不推荐使用这种写法进行配置
# app.config['debug'] = True#并不是最方便的写法
# app.config.from_pyfile("settings")#也不是最常用的写法
app.config.from_object("setting.DevelopmentConfig")

#暂时用字典代替数据库
dictUser = {

    1:{"name":"miaoruxue", "code":"001", "text":"this is my love"},
    2:{"name":"wufangzhou", "code":"002", "text":"hahaha"}
}
#展示用户表
@app.route('/usr',methods = ['GET'])#有哪些请求则写上
def usr():
    return render_template('usr.html',usr_dict = dictUser)#设置

#用户详情
@app.route('/detail/<int:id>',methods = ['GET'])#有哪些请求则写上,<>里面是变量，int是指定变量类型
def detail(id):
    user = session.get('usr_info')
    if not user:
        return render_template('login.html')
    info = dictUser.get(id)
    return render_template('detail.html',info = info)

#登录页面
@app.route('/login',methods = ['GET','POST'])#,endpoint=l1)#有哪些请求则写上,反向生成器
def login():
    # vUsr = dictUser.get()增加获取字典中的用户名
    if request.method == "GET":
        return render_template('login.html')#从template文件中根据给定的上下文呈现相应的模板
    else:
        user = request.form.get('user')#拿到name为user表单提交的请求数据
        pwd = request.form.get('pwd')
        if user in dictUser and pwd == dictUser[user]:
            session[usr_info] = user#获取到用户名
            return redirect("https://google.com")#重定向url
        return render_template('login.html',error = 'input error')

#首页
@app.route('/index',methods = ['GET'])#有哪些请求则写上
def index():
    return render_template('index.html')

@app.route('/video',methods = ['GET'])#有哪些请求则写上,视频播放
def video():
    return render_template('video.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0',port='9520')