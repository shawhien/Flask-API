from models import app, Videogame
from flask import jsonify, request
from crud.videogame_crud import get_all_videogames, get_videogame, create_videogame, update_videogame, destroy_videogame

@app.errorhandler(Exception)
def unhandled_exception(e):
    app.logger.error('Unhandled Exception: %s', (e))
    message_str = e.__str__()
    return jsonify(message=message_str.split(':'[0]))

@app.route('/videogames', methods=['GET', 'POST'])
def videogame_index_create():
    if request.method =='GET':
        return get_all_videgames()
    if request.method == 'POST':
        return create_videogame()

@app.route('/videogames/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def videogame_show_update_delete(id):
    if request.method == 'GET':
        return get_videogame(id)
    if request.method == 'GET':
        return update_videogame(
            id=id,
            name=request.form['name'],
            company=request.form['company',]
            esrb=request.form['esrb']
        )
    if request.method == 'DELETE':
        return destroy_videogame