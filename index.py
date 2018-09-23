from flask import Flask
import sys
app=Flask(__name__)

@app.route("/")
def hello():

	return """ <html>
    <head>
      <title> 호에에에엥 </title>
      <style>
        body {
          color : #fff;
        }
      </style>
    </head>
    <body bgcolor="#000">
      호에에에에에에에에에에에에에에에에에에에에에에에에에에에에에에에에에에엥
    </body>
  </html> """

# @app.route("/hello")
  # return "Hello goorm!"

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(sys.argv[1]))