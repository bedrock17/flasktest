import os
from flask import Flask
from flask import render_template
from flask import request

from flask import send_from_directory

from flask import redirect, url_for

from random import *
import pickle

import sys
app=Flask(__name__)


count = 0

# app.add_url_rule('/favicon.ico', redirect_to="/favicon.ico")


@app.route('/favicon.ico')
# @app.route('/<name>')
def favicon(name=""):
    return send_from_directory(os.path.join(app.root_path, 'static'), "favicon.ico", mimetype='image/vnd.microsoft.icon')


# @app.route('/favicon.ico')
# def favicon():
#   return redirect(url_for('static', filename='favicon.ico'))

msgLst = []

MSG_FILE_NAME = "msgFile"

def fileLoad(fileName):
    global msgLst   
    with open(fileName, 'rb') as f:
        msgLst = pickle.load(f)

@app.route('/')
@app.route("/index")
def hello(name=""):
  global count
  count +=1
  print("handle! {0} ", count)

  colorCode = "#" + "%06X"%(randint(0, 1<<24))
  countBin = bin(count)[2:]
  return render_template('main.html', name=name, count=countBin, color=colorCode, msgLst=msgLst[::-1][:100])


@app.route('/load', methods=['POST'])
def load():
    global msgLst

    msg = request.form['msg']
    
    fileLoad(msg)

    return "DONE"

@app.route('/del', methods=['POST'])
def delete():
    global msgLst

    msg = request.form['msg']
    
    idx = []
    for i, v in enumerate(msgLst):
        if msg in v:
            idx.append(i)
    
    for i in idx[::-1]:
        del msgLst[i]
    return "DONE"

@app.route('/post', methods=['POST'])
def post():
    global msgLst

    msg = request.form['msg']
    
    if len(msg) > 102400:
        return "MSG TOO LONG"

    print(msg)
    msgLst.append(msg)

    if len(msgLst) > 100:
        msgLst = msgLst[1:]
    with open(MSG_FILE_NAME, 'wb') as f:
         pickle.dump(msgLst, f, pickle.HIGHEST_PROTOCOL)
    return '<script>window.location=document.referrer</script>'

# @app.route("/hello")
  # return "Hello goorm!"

if __name__ == "__main__":
    fileLoad(MSG_FILE_NAME)
    app.run(host='0.0.0.0', port=int(sys.argv[1]))
