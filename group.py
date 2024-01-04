from flask import Flask

group = Flask(__name__)
@group.route("/")
def Hello():
  return "<p>Hello, World!</p>"

@group.route("/anand")
def HelloWorld():
  return "<h1>Hello, World!</h1><h2>Hello World</h2><h3>Hello World<h3>"

@group.route("/arjun")
def HelloWorlds():
  return "<h1>Nothing</h1><h2>To</h2><h3>Write Now<h3>"
  
if __name__ == '__main__':
  # app.run(host='0.0.0.0', port=8080)
  print("Hello!")