import enum

from models import db, Person


class ACTION(enum.Enum):
    INSERT = "insert"
    ALTER = "alter"
    DELETE = "delete"


def person_insert(name):
    person = Person(name)
    db.session.add(person)
    db.session.commit()
    return person.id


def person_alter(old_name, name):
    person = Person.query.filter_by(username=old_name).first_or_404()
    person.set_name(name)
    db.session.commit()
    return True


def person_delete(name):
    person = Person.query.filter_by(username=name).first_or_404()
    db.session.delete(person)
    db.session.commit()
    return True


def person_controller(id=None, action=ACTION.INSERT, name=None):
    match action:
        case ACTION.INSERT:
            return person_insert(name)
        case ACTION.ALTER:
            return person_alter(id, name)
        case ACTION.DELETE:
            return person_delete(id)
    raise TypeError
