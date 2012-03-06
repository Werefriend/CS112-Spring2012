#!/usr/bin/env python

class Student(object):
    def __init__(self, name = "Jane Doe"):
        self.name = name

    def say(self, message):
        print self.name + ": " + message
    
    def say_to(self, other, message):
        self.say(message + ", " + other.name)

    def printing(self):
        print self.name

class Course(object):
    def __init__(self, name):
        self.name = name
        self.enrolled = []

    def enroll(self, student):
        self.enrolled.append(student)

    def printMe(self):
        for student in self.enrolled:
            student.printing()

bob = Student("Bob")
fred = Student("Fred")
cs112 = Course("CS112")


bob.say_to(fred, "Hi")
fred.say_to(bob, "Go away")

cs112.enroll(bob)
cs112.enroll(fred)
cs112.printMe()
