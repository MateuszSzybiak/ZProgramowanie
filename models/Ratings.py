class Rating:
    def __init__(self, parameters):
        self.UserId = parameters[0]
        self.MovieId = parameters[1]
        self.Rating = parameters[2]
        self.Timestamp = str(parameters[3])