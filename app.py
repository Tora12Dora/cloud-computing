from flask import Flask, jsonify, request
app = Flask(__name__)
app.config["DEBUG"] = True

films = [
       {'id':0,
       'title': 'Mummy',
       'produser': 'Name_1',
       'year': '1998'},
       {'id':1,
       'title': 'Ip-Man',
       'produser': 'Name_1',
       'year': '1997'},
       {'id':2,
       'title': 'Other',
       'produser': 'Name_2',
       'year': '2005'}
]

@app.route('/films',methods = ['GET'])
def returnFilms():
  return jsonify({'films': films})

@app.route('/films/<string:title>',methods = ['GET'])
def returnFilm(Title):
  fff = [film for film in films if film['title'] == Title]
  return jsonify({'film':fff[0]})

@app.route('/films', methods = ['POST'])
def PostOne():
  fff = {'id':request.json['id'],'title' : request.json['title'], 'produser': request.json['produser'],'year': request.json['year']}
  films.append(fff)
  return jsonify({'films':films})


@app.route('/films/<string:title>_<string:year>', methods =['PUT'])
def Update(title,year):
  fff = [film for film in films if film['year'] == year  and film['title']== title]
  fff[0]['year'] = request.json['year']
  return jsonify({'film': fff[0]})

@app.route('/film/<title>', methods = ['DELETE'])
def Delete(title):
  fff = [film for film in films if film['title'] == title] 
  films.remove(fff[0])
  return jsonify({'films':films})

if __name__ == '__main__':
 app.run(port=5000)