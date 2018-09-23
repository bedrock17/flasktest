from flask import Flask
from flask import render_template
import sys
app=Flask(__name__)


count = 0

@app.route('/')
@app.route('/<name>')
def hello(name=""):
  global count
  count +=1
  print("handle! {0} ", count)
  return render_template('main.html', name=name, count=count)

	

# @app.route("/hello")
  # return "Hello goorm!"

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(sys.argv[1]))