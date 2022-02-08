"""File containing Classes"""

class Question:
    """
    Class for question which provides both,
    question asked and answer
    """
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


class Team:
    """
    Creates a team with the points they 
    get and position in a table 
    based on points
    """

    def __init__(self, points, position):
        self.points = 0
        self.position = 21

    
    def add_point(self):
        self.points += 1