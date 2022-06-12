from flask import Flask,render_template,redirect,request, url_for, abort,session,flash,jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import os
from collections import namedtuple
app = Flask(__name__)
app.debug = True

c_list = []

class client():
    def __init__(self,id,pw,name):
        self.id = id
        self.pw = pw
        self.name = name 

class items_():
    def __init__(self ,name, key, image, seller):
        self.s_name = name
        self.s_key = key
        self.s_image = image
        self.s_seller = seller

#items = namedtuple("items", "s_name s_key s_image s_seller")

        
item_list = []
item1 = items_('아이패드','태블릿','image','전산전자') 
item_list.append(item1)  


@app.route('/')
def itemm():
    return render_template('items.html', items_list = item_list)


@app.route('/login')
def log_in():
    id = '\0'
    pw = '\0'
    if request.method == "POST":
        if not request.form['id'] or not request.form['pw']:
            flash('아이디와 비밀번호를 모두 입력하세요.')
        elif request.form['id'] not in c_list:
            flash('아이디를 확인하세요')
        else:
            resp = make_response(render_template("/"))
            resp.set_cookie('id', id)
    return render_template("log_in.html")
                
@app.route('/sign_up')
def signup():
    if request.method == "POST":
        if not request.form['id'] or not request.form['pw'] or not request.form['nm']:
            flash('빈칸을 모두 입력하세요.')
        else:
            cli = client(request.form['id'], request.form['pw'], request.form['nm'])
            c_list.append(cli)
            flash('success')
            return redirect(url_for("itemm"))
    return render_template("sign_up.html")

if __name__ == '__main__':
    app.run()


