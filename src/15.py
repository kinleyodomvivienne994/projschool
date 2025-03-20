class SchoolProject:
    def __init__(self):
        self.students = []

    def add_student(self, name, grade):
        self.students.append({
            "name": name,
            "grade": grade
        })
