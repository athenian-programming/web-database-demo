from json import JSONEncoder


class StudentEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__


class Student:
    def __init__(self, rec_id, created, first, last, email, grad_year):
        self.rec_id = rec_id
        self.created = created
        self.first = first
        self.last = last
        self.email = email
        self.grad_year = grad_year
