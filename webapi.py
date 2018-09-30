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
def returnAll(): 
    return jsonify({'films': films})

@app.route('/films/<string:title>',methods = ['GET'])
def returnFilm(title):
    fff = [film for film in films if film['title'] == title]
    return jsonify({'film':fff[0]})

@app.route('/films', methods = ['POST'])
def addOne():
    fff = {'id':request.json['id'],'title': request.json['title'], 'produser': request.json['produser'],'year': request.json['year']}
    films.append(fff)
    return jsonify({'films':films})

@app.route('/films/<int:id>', methods =['PUT'])
def editOne(id):
    fff = [film for film in films if film['id'] == id]
    fff[0]['title'] = request.json['title']
    return jsonify({'film': fff[0]})

@app.route('/films/<int:id>', methods = ['DELETE'])
def removeOne(id):
    f = [film for film in films if film['id'] == id]
    films.remove(f[0])
    return jsonify({'films':films})
if __name__ == '__main__':
    app.run(port=5000)