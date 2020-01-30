#!/usr/bin/env python3
from flask import Flask,jsonify,request
from flask import abort

app=Flask(__name__)

diaries=[
    {
        'id':1,
        'title':u'It was a nice day',
        'body':u'Today was a reaaly nice day,I did not encounter ny blockers and the code is coming on well' 
    },
    {
        'id':2,
        'title':u'I learnt a lot today',
        'body':'While onsuming todays API,I got to interact more with other dbs'
    }
]

@app.route('/todo/api/v1.0/diaries', methods=['GET'])
def get_diary():
    return jsonify({'diaries':diaries})


@app.route('/todo/api/v1.0/diaries/<int:diary_id>', methods=['GET'])
def get_task(diary_id):
    diary = [diary for diary in diaries if diary ['id'] == diary_id]
    if len(diary) == 0:
        abort(404)
    return jsonify({'diary':diary[0]})


@app.route('/todo/api/v1.0/diaries', methods=['POST'])
def create_diary():
    if not request.json or not 'title' in request.json:
        abort(400,'My custom message',custom='Diary is lacking some fields')
    diary={
        'id':diaries[-1]['id'] + 1,
        'title':request.json['title'],
        'body':request.json.get('body',""),  
    }
    diaries.append(diary)
    return jsonify({'diary':diary}),201

@app.route('/todo/api/v1.0/diaries/<int:diary_id>', methods=['PUT'])
def update_diary(diary_id):
    diary = [diary for diary in diaries if diary ['id'] == diary_id]
    if len(diary) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != str:
        abort(400)
    if 'body' in request.json and type(request.json['body']) is not str:
        abort(400)
    diary[0]['title'] =request.json.get('title',diary[0]['title'])
    diary[0]['body']=request.json.get('body',diary[0]['body'])
    return jsonify({'diary':diary[0]})

@app.route('/todo/api/v1.0/diaries/<int:diary_id>', methods=['DELETE'])
def delete_diary(diary_id):
    diary = [diary for diary in diaries if diary ['id'] == diary_id]
    if len(diary) == 0:
        abort(404)
    diaries.remove(diary[0])
    return jsonify({'result':True})


if __name__ == '__main__':
    app.run(debug=True)