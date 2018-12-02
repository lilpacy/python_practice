# coding:utf-8
from flask import Flask, jsonify, abort, make_response, request
from peewee import *
from datetime import date

db = MySQLDatabase('peewee_test', user='root', passwd='')

class UnknownField(object):
    def __init__(self, *_, **__): pass

class Person(Model):
    name = CharField()
    birthday = DateField()
    class Meta:
        database = db

class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets')
    name = CharField()
    animal_type = CharField()
    class Meta:
        database = db

api = Flask(__name__)

# example http://0.0.0.0:5000/person/?name=kazuma&birthday=1994-1-1
@api.route('/person/', methods=['GET'])
def insertPerson():
    name = request.args.get('name', default = 'noname', type = str)
    birthday = request.args.get('birthday', default = '1900-1-1', type = str)

    db.connect()

    try:
        new_one = Person(name=name, birthday=birthday)
        new_one.save()

    except Items.DoesNotExist:
        db.close()
        abort(404)

    result = {
        "result": True,
        "status": "success"
    }
    db.close()
    return make_response(jsonify(result))

@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    api.run(host='0.0.0.0', debug=False) #host=0.0.0.0 makes it possible to access from another ip
