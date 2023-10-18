
from tkinter import *
import random
import time


class Car:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(10, 10, 50, 50, fill=color)
        self.canvas.moveto(self.id, 235, 375)

    def draw(self):
        pass

    def move_left(self, event):
        if event.keysym == 'Left':
            self.canvas.move(self.id, -100, 0)
            if self.canvas.coords(self.id)[0] < 35:
                self.canvas.moveto(self.id, 35, 375)

    def move_right(self, event):
        if event.keysym == 'Right':
            
            self.canvas.move(self.id, 100, 0)
            if self.canvas.coords(self.id)[0] > 435:
                self.canvas.moveto(self.id, 435, 375)
            

class Enemy:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(10, 10, 50, 50, fill=color)
        self.canvas.move(self.id, 225, 0)
        self.speed = random.randint(5, 15)
    
    def enemy_draw(self):
        pass

    def enemy_move(self):
        self.canvas.move(self.id, 0, self.speed)

    
    
    def enemy_spawn(self):
        self.canvas.moveto(self.id, random.choice([35,135,235,335,435]), 0)
        if self.canvas.coords(self.id)[0] < 0:
            self.canvas.moveto(self.id, 350, 0)
        elif self.canvas.coords(self.id)[0] > 500:
            self.canvas.moveto(self.id, 200, 0)

    def enemy_reset(self):
        self.canvas.moveto(self.id, random.choice([35,135,235,335,435]), -500)