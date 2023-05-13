from flask import Flask, abort, request, jsonify
from models import setup_db
from flask_cors import CORS

from models import Movie, Actor
from auth import requires_auth, AuthError


def create_app(test_config=None):
    # create app and database
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Headers',
                             'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    '''
    POST /movies
        it should create a new row in the movies table
        it should require the 'post:movies' permission
    returns status code 200 and json {"success": True, "movies": movie} where movies an array containing only the newly created movie
        or appropriate status code indicating reason for failure
    '''
    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def create_movie(jwt):
        body = request.get_json()
        if body is None:
            abort(400)

        new_title = body.get('title', None)
        new_release_date = body.get('release_date', None)
        if new_title is None or new_release_date is None:
            abort(400)

        try:
            movie = Movie(title=new_title,
                          release_date=new_release_date)
            movie.insert()

            return jsonify({
                'success': True,
                'movies': [movie.format()]
            }), 200
        except:
            abort(422)

    '''
    GET /movies
        it should be a public endpoint
    returns status code 200 and json {"success": True, "movies": movies} where movies is the list of movies
        or appropriate status code indicating reason for failure
    '''
    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(jwt):
        try:
            movies = Movie.query.order_by(Movie.id).all()

            return jsonify({
                'success': True,
                'movies': [movie.format() for movie in movies]
            }), 200
        except:
            abort(422)

    '''
    PATCH /movies/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:movies' permission
    returns status code 200 and json {"success": True, "movies": movie} where movies an array containing only the updated movie
        or appropriate status code indicating reason for failure
    '''
    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movie(jwt, movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        if movie is None:
            abort(404)

        body = request.get_json()
        if body is None:
            abort(400)

        new_title = body.get('title', None)
        new_release_date = body.get('release_date', None)
        if new_title is None or new_release_date is None:
            abort(400)

        try:
            movie.title = new_title
            movie.release_date = new_release_date
            movie.update()

            return jsonify({
                'success': True,
                'movies': [movie.format()]
            }), 200
        except:
            abort(422)

    '''
    DELETE /movies/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:movies' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
    '''
    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(jwt, movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        if movie is None:
            abort(404)

        try:
            movie.delete()

            return jsonify({
                'success': True,
                'deleted': movie_id
            }), 200
        except:
            abort(422)

    '''
    POST /actors
        it should create a new row in the actors table
        it should require the 'post:actors' permission
    returns status code 200 and json {"success": True, "actors": actor} where actors an array containing only the newly created actor
        or appropriate status code indicating reason for failure
    '''
    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def create_actor(jwt):
        body = request.get_json()
        if body is None:
            abort(400)

        new_name = body.get('name', None)
        new_age = body.get('age', None)
        new_gender = body.get('gender', None)
        new_movie_id = body.get('movie_id', None)
        if new_name is None or new_age is None or new_gender is None or new_movie_id is None:
            abort(400)

        try:
            actor = Actor(name=new_name, age=new_age,
                          gender=new_gender, movie_id=new_movie_id)
            actor.insert()

            return jsonify({
                "success": True,
                "actors": [actor.format()]
            }), 200
        except:
            abort(422)

    '''
    GET /actors
        it should be a public endpoint
    returns status code 200 and json {"success": True, "actors": actors} where actors is the list of actors
        or appropriate status code indicating reason for failure
    '''
    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(jwt):
        try:
            actors = Actor.query.order_by(Actor.id).all()

            return jsonify({
                'success': True,
                'actors': [actor.format() for actor in actors]
            }), 200
        except:
            abort(422)

    '''
    PATCH /actors/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:actors' permission
    returns status code 200 and json {"success": True, "actors": actor} where actors an array containing only the updated actor
        or appropriate status code indicating reason for failure
    '''
    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actor(jwt, actor_id):
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        if actor is None:
            abort(404)

        body = request.get_json()
        if body is None:
            abort(400)

        new_name = body.get('name', None)
        new_age = body.get('age', None)
        new_gender = body.get('gender', None)
        new_movie_id = body.get('movie_id', None)
        if new_name is None or new_age is None or new_gender is None or new_movie_id is None:
            abort(400)

        try:
            actor.name = new_name
            actor.age = new_age
            actor.gender = new_gender
            actor.movie_id = new_movie_id
            actor.update()

            return jsonify({
                'success': True
            }), 200
        except:
            abort(422)

    '''
    DELETE /actors/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:actors' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
    '''
    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(jwt, actor_id):
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        if actor is None:
            abort(404)

        try:
            actor.delete()

            return jsonify({
                'success': True,
                'deleted': actor_id
            }), 200
        except:
            abort(422)

    # Error Handling
    '''
    Example error handling for unprocessable entity
    '''
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable"
        }), 422

    '''
        each error handler should return (with approprate messages):
                jsonify({
                        "success": False,
                        "error": 404,
                        "message": "resource not found"
                        }), 404
    '''
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Resource not found'
        }), 404

    @app.errorhandler(401)
    def unauthorize(error):
        return jsonify({
            'success': False,
            'error': 401,
            'message': 'Unauthorize'
        }), 401

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'Bad request'
        }), 400

    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        """
        Receive the raised authorization error and propagates it as response
        """
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response

    return app


app = create_app()

app.app_context().push()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
