import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

films = [
{'id':0,
 'title': 'Mummy',
 'produser': 'Name_1',
 'year': 1998},
{'id':1,
 'title': 'Ip-Man',
 'produser': 'Name_1',
 'year': 1997},
{'id':2,
 'title': 'Other',
 'produser': 'Name_2',
 'year': 2005}
]

@app.route('/films',methods = ['GET'])
def returnAll():
  return jsonify({'films': films})

@app.route('/films/<string:title>',methods = ['GET'])
def returnOne(Title):
  fff = [film for film in films if film['title'] == Title]
  return jsonify({'film':fff[0]})

@app.route('/films', methods = ['POST'])
def addOne():
  film = {'id':request.json['id'],'title' : request.json['title'], 'produser': request.json['produser'],'year': request.json['year']}
  films.append(film)
  return jsonify({'films':films})


@app.route('/films/<string:title><string:produser><string:year>', methods =['PUT'])
def editOne(title,produser,year):
  fff = [film for film in films if film['year'] == year]
  fff[0]['year'] = request.json['year']
  return jsonify({'film': fff[0]})

@app.route('/film/<string:title><string:produser>', methods = ['DELETE'])
def removeOne(title, produser):
  fff = [film for film in films if film['title'] == title and film['produser'] == produser]
  films.remove(fff[0])
  return jsonify({'films':films})

if __name__ == '__main__':
 app.run(debug=True, port=5000)
