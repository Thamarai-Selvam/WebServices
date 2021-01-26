#install flask via pip install flask

from flask import Flask, request,Response, make_response,jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
  return "<p>Hey</p>", 200

@app.route('/json', methods=['GET'])
def homejson():
  message = 'God of Programming Veno'
  return {'message' : message }, 200

@app.route('/json2', methods=['GET'])
def homejson2():
  message = 'God of Programming Veno'
  return jsonify(message), 200

@app.route('/1', methods=['GET'])
def home1():
  return make_response("<p>Hey 1, From => make_response('',200)</p>",200)


@app.route('/2', methods=['GET'])
def home2():
  return Response("<p>Hey 2, From => Response('',200)</p>",200)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Page not found.</p>", 404

if __name__ == '__main__':
  app.run()