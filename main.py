# This is a sample Python script.
import select

from Project import Project
from Task import Task
from User import User

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

user = User("Vasya")

project = Project("Alpha")

print(project.getName())

task = Task()















# a = User('Vasya', 15)
# b = User("Petya", 20)


class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        pass


class AnimalDB:
    def get_animal(self) -> Animal:
        pass

    def save(self, animal: Animal):
        pass
