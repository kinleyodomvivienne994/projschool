import random
class School:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.courses = []
    
    def add_student(self, name, age):
        student = {
            'name': name,
            'age': age,
            'grades': []
        }
        self.students.append(student)
        return student
    
    def add_teacher(self, name, subject):
        teacher = {
            'name': name,
            'subject': subject,
            'classes': []
        }
        self.teachers.append(teacher)
        return teacher
    
    def add_course(self, name, credits):
        course = {
            'name': name,
            'credits': credits,
            'students': []
        }
        self.courses.append(course)
        return course
    
    def assign_student_to_course(self, student, course):
        if student not in self.students:
            raise ValueError('Student does not exist')
        if course not in self.courses:
            raise ValueError('Course does not exist')
        student['grades'].append(course)
        course['students'].append(student)
    
    def display_students(self):
        for student in self.students:
            print(f'Name: {student["name"]}, Age: {student["age"]}')
    
    def display_courses(self):
        for course in self.courses:
            print(f'Course: {course["name"]}, Credits: {course["credits"]}')
    
    def display_teachers(self):
        for teacher in self.teachers:
            print(f'Name: {teacher["name"]}, Subject: {teacher["subject"]}')
