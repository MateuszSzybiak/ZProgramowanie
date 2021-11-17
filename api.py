from flask import Flask
from flask_restful import Resource, Api
from services.utils import read_file
from models.Movie import Movie
app = Flask(__name__)
api = Api(app)


class Movies(Resource):
    def get(self):
        data = read_file('files/movies.csv')
        movies = []
        for line in data[1:]:
            temp = line.split(',')
            temp[2] = temp[2].replace("\n", "")
            movies.append(Movie(temp[0], temp[1], temp[2]).__dict__)
        return movies


api.add_resource(Movies, '/')

if __name__ == '__main__':
    app.run(debug=True)
