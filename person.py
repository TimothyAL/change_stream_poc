from flask import Blueprint, request, Response

from business import person_controller, ACTION
from models import Person

people = Blueprint('people', __name__, url_prefix='/people')


@people.route('/', methods=['POST'])
def insert():
    json = request.json
    result = person_controller(None, ACTION.INSERT, json['name'])
    if result:
        return Response(f'INSERTED person {result}: {json["name"]}', 200)


@people.route('/<name>', methods=['GET'])
def get_person_by_id(name):
    print(f'get person {name}')
    person = Person.query.filter_by(username=name).first_or_404()
    return Response(person.username, 200)

@people.route('/<name>', methods=['PUT'])
def alter(name):
    json = request.json
    result = person_controller(name, ACTION.ALTER, json['name'])
    if result:
        return Response(f'ALTERED person {id}: {json["name"]}', 200)


@people.route('/<name>', methods=['DELETE'])
def delete(name):
    result = person_controller(name, ACTION.DELETE)
    if result:
        return Response(f'DELETED person {name}', 200)
