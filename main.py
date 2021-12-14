from flask import Flask
from flask_restful import Resource, Api
from services.utils import read_file
from models.Movie import Movie
from models.Links import Link
from models.Tags import Tag
from models.Ratings import Rating
app = Flask(__name__)
api = Api(app)


def path_class(path, cls):
    data = read_file(path)
    elements = []
    for line in data[1:]:
        temp = line.split(',')
        temp[-1] = temp[-1].replace("\n", "")
        elements.append(cls(temp).__dict__)
    return elements


class Movies(Resource):
    def get(self):
        return path_class('files/movies.csv', Movie)


class Links(Resource):
    def get(self):
        return path_class('files/links.csv', Link)


class Tags(Resource):
    def get(self):
        return path_class('files/tags.csv', Tag)


class Ratings(Resource):
    def get(self):
        return path_class('files/ratings.csv', Rating)


api.add_resource(Movies, '/movies')
api.add_resource(Links, '/links')
api.add_resource(Tags, '/tags')
api.add_resource(Ratings, '/ratings')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
