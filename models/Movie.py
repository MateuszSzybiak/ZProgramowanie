class Movie:
    def __init__(self, parameters):
        self.Id = int(parameters[0])
        self.title = str(parameters[1])
        self.genres = parameters[2]
