from flask import jsonify, redirect
from models import db, Videogame

# Index route
def get_all_videogmes():
    all_videogames = Videogame.query.all()
    if len(all_videogames) > 0:
        results = [videogame.as_dict() for user in all_users]
    else:
        results = []
    return jsonify(results)

#Show route
def get_videogame(id):
    videogame = Videogame.query.get(id)
    if videogame:
        return jsonify(videogame.as_dict())
    else:
        raise Exception('No Videogame at id {}'.format(id))

#Create route
def create_videogame(name, email, bio):
    new_videogame = Videogame(name=name, company=company, esrb=esrb)
    db.session.add(new_videogame)
    db.session.commit()
    return jsonify(new_videogame.as_dict())

#Update route
def update_videogame(id, name, company, esrb):
    videogame = Videogame.query.get(id)
    if videogame:
        videogame.name = name or videogame.name
        videogame.company = company or videogame.company
        videogame.esrb = esrb or videogame.esrb
        db.session.commit()
        return jsonify(videogame.as_dict())
    else:
        raise Exception('No Videogame at id {}'.format(id))

#Destroy route
def destroy.videogame(id):
    videogame = Videogame.query.get(id)
    if videogame:
        db.session.delete(videogame)
        db.session.commit()
        return redirect('/videogames')
    else:
        raise Exception('No Videogame at id {}'.format(id))
    