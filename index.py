import os
from flask import Flask
from flask import render_template

from flask import send_from_directory

from flask import redirect, url_for

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

@app.route('/')
# @app.route('/<name>')
def hello(name=""):
  global count
  count +=1
  print("handle! {0} ", count)
  return render_template('main.html', name=name, count=count)

# @app.route("/hello")
  # return "Hello goorm!"

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(sys.argv[1]))