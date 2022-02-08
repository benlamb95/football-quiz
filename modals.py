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
    Creates a team with users name,
    the points they get and position
    in a table based on points
    """

    def __init__(self, name, points, position):
        self.name = name
        self.points = points
        self.position = position