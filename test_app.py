import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from database.models import Movie, Actor, setup_db

PRODUCER_JWT_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InU0bVp5bXMtbWhQQk9aWjkyemJJTyJ9.eyJpc3MiOiJodHRwczovL2Rldi0zaXF4NDN1YW92NjhwaXNkLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDVlNmI0NDM1MDY5YjgyZTIwNmVmZDUiLCJhdWQiOiJjb2ZmZWUtc2hvcCIsImlhdCI6MTY4MzkxMDQwMiwiZXhwIjoxNjgzOTk2ODAxLCJhenAiOiJxVkxXOWwxYzB1Q1pnNGE1c09lMk1WWUhFT2o1MHk1OCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.bb8Fbk1dLcoz2aS1VHXJpBMyp5c-LMPhj5nUm0-ZPWmFaBKNwzkYLVwmiosOcSnmzmSi__s6okZIWhAO1vOM6jh7mS-0xMtDMtvTZxvPIiYGESvRLCV6uV7noZSOYrOd4Ghr3Du47XBPQyG2cwKADzEQ0pvpdHxxG0CuK4OVLxSWY8Wq8GluiBKgNxCxbkm5-LCiKjanEjBSVGwS4QoS8q_mlsdS2-9iXp94hIK3M1Ysz1Dhs1iToDXCiwALnx0ktW3UikNayZGv-awxWtCNyUknDWbMpc_ZsPAAxbfNobHxWaKTDAJBpLADGNww_anjAgA8982l8VGurCGYEq9VJg'
PRODUCER_HEADERS = {
    'Authorization': 'Bearer ' + PRODUCER_JWT_TOKEN
}

ASSISTANT_JWT_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InU0bVp5bXMtbWhQQk9aWjkyemJJTyJ9.eyJpc3MiOiJodHRwczovL2Rldi0zaXF4NDN1YW92NjhwaXNkLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDVlZDFjZjQ5MWMwMGUwMTY3NWU4ZTAiLCJhdWQiOiJjb2ZmZWUtc2hvcCIsImlhdCI6MTY4MzkzOTA0OCwiZXhwIjoxNjg0MDI1NDQ3LCJhenAiOiJxVkxXOWwxYzB1Q1pnNGE1c09lMk1WWUhFT2o1MHk1OCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.PkYk84gP8nYcDA0n7TD9mpLmngYhk0LyJ0es9UhXTgLsjIgmUM-hlPGY7wFEmOpvrW72JlkMOTjNswkboUoYOi-ml4ul32i7WaMXqdHA-wvsqJDjtDV3ksU1hb4i4RpcEeKRm4wSySCykgWu8mP53AqEBfV6NMwgQIDd2uzIt-TL593rp5dXWRqAZr9gH-Ne7iQwW68l54D6tLrn_WceDHp5vIyHeVmV5bnvI3UAI3DQEfIM_mxl02Mqi2WxqW4VKRbasOxAJk2G7zED1kVaV8g2iXQOoPNHkVbbBvJu3Z6TEWYqvKalAaeXuyp0kBwJmxwSHvPMB2EsXPq5gPc3Jw'
ASSISTANT_HEADERS = {
    'Authorization': 'Bearer ' + ASSISTANT_JWT_TOKEN
}

DIRECTOR_JWT_TOKEN = ''
DIRECTOR_HEADERS = {
    'Authorization': 'Bearer ' + DIRECTOR_JWT_TOKEN
}


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "fsnd_capstone_test"
        self.database_path = "postgresql://{}/{}".format(
            'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        request_body = {
            "title": "You",
            "release_date": "2009-09-24",
        }
        self.client().post('/movies', json=request_body, headers=PRODUCER_HEADERS)

        request_body = {
            "title": "The vow",
            "release_date": "2009-09-23",
        }
        self.client().post('/movies', json=request_body, headers=PRODUCER_HEADERS)

        request_body = {
            "name": "Le Thi An",
            "age": 18,
            "gender": "female",
            "movie_id": 1
        }
        self.client().post('/actors', json=request_body, headers=PRODUCER_HEADERS)

        request_body = {
            "name": "Le Thi An",
            "age": 18,
            "gender": "female",
            "movie_id": 1
        }
        self.client().post('/actors', json=request_body, headers=PRODUCER_HEADERS)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    Movies end points testing
    """

    def test_create_movie(self):
        request_body = {
            "title": "You",
            "release_date": "2009-09-24",
        }
        res = self.client().post('/movies', json=request_body, headers=PRODUCER_HEADERS)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_400_failed_create_movie(self):
        res = self.client().post('/movies', headers=PRODUCER_HEADERS)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad request')

    def test_get_movies(self):
        res = self.client().get('/movies', headers=PRODUCER_HEADERS)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_update_movie(self):
        request_body = {
            "title": "You",
            "release_date": "2009-09-25"
        }
        res = self.client().patch('/movies/1', json=request_body, headers=PRODUCER_HEADERS)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_404_failed_update_movie(self):
        res = self.client().patch('/movies/771', headers=PRODUCER_HEADERS)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    def test_delete_movie(self):
        res = self.client().delete('/movies/2', headers=PRODUCER_HEADERS)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])

    def test_404_delete_an_movie(self):
        res = self.client().delete('/movies/711', headers=PRODUCER_HEADERS)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    """
    Actors end points testing
    """

    def test_create_actor(self):
        request_body = {
            "name": "Le Thi An",
            "age": 18,
            "gender": "female",
            "movie_id": 1
        }
        res = self.client().post('/actors', json=request_body, headers=PRODUCER_HEADERS)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_400_failed_create_actor(self):
        res = self.client().post('/actors', headers=PRODUCER_HEADERS)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad request')

    def test_get_actors(self):
        res = self.client().get('/actors', headers=PRODUCER_HEADERS)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_update_actor(self):
        request_body = {
            "name": "Le Thi An",
            "age": 18,
            "gender": "female",
            "movie_id": 1
        }
        res = self.client().patch('/actors/1', json=request_body, headers=PRODUCER_HEADERS)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_404_failed_update_actor(self):
        res = self.client().patch('/actors/771', headers=PRODUCER_HEADERS)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    def test_delete_actor(self):
        res = self.client().delete('/actors/2', headers=PRODUCER_HEADERS)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])

    def test_404_delete_an_actor(self):
        res = self.client().delete('/actors/711', headers=PRODUCER_HEADERS)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    """
    Actors end points testing
    """

    def test_casting_assistant_create_movie(self):
        request_body = {
            "title": "The vow",
            "release_date": "2009-09-24",
        }
        res = self.client().post('/movies', json=request_body, headers=ASSISTANT_HEADERS)
        self.assertEqual(res.status_code, 403)

    def test_casting_assistant_delete_actor(self):
        res = self.client().delete('/actors/1', headers=ASSISTANT_HEADERS)
        self.assertEqual(res.status_code, 403)

    def test_casting_director_create_movie(self):
        request_body = {
            "title": "The vow",
            "release_date": "2009-09-24",
        }
        res = self.client().post('/movies', json=request_body, headers=DIRECTOR_HEADERS)
        self.assertEqual(res.status_code, 401)

    def test_casting_director_delete_movie(self):
        res = self.client().delete('/movies/1', headers=DIRECTOR_HEADERS)
        self.assertEqual(res.status_code, 401)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
