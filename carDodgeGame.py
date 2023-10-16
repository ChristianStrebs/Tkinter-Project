from tkinter import *
import random
import time

# Create the main window
tk = Tk()
tk.title("Car Dodge Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=500, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
bg = canvas.create_rectangle(0, 0, 500, 500, fill='grey')

# Create the Car class
class Car:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(10, 10, 50, 50, fill=color)
        self.canvas.move(self.id, 225, 325)

    def draw(self):
        pass

    def move_left(self, event):
        if event.keysym == 'Left':
            canvas.move(self.id, -10, 0)

    def move_right(self, event):
        if event.keysym == 'Right':
            canvas.move(self.id, 10, 0)
    
class Enemy:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(10, 10, 50, 50, fill=color)
        self.canvas.move(self.id, 225, 0)
        self.speed = random.randint(5, 15)
    
    def enemy_draw(self):
        pass

    def enemy_move(self):
        canvas.move(self.id, 0, self.speed)

    def enemy_spawn(self):
        self.canvas.move(self.id, random.randint(-225, 225), 0)

    def enemy_reset(self):
        self.canvas.move(self.id, random.randint(-225, 225), -500)



# Create the Car instance
player = Car(canvas, 'blue')
canvas.bind_all('<KeyPress-Left>', player.move_left)
canvas.bind_all('<KeyPress-Right>', player.move_right)

# Create the Enemy instance
enemies = []
num_enemies = 7

for i in range(num_enemies):
    enemies.append(Enemy(canvas, 'red'))
    enemies[i].enemy_spawn()

def spawn_enemy():
    for i in range(1):
        enemies.append(Enemy(canvas, 'red'))
        enemies[i].enemy_spawn()

def check_enemy_coords():
    for i in range(num_enemies):
        if canvas.coords(enemies[i].id)[1] > 500:
            enemies[i].enemy_reset()


def check_collision():
    global game_over
    player_coords = canvas.coords(player.id)
    for enemy in enemies:
        enemy_coords = canvas.coords(enemy.id)
        if player_coords[1] < enemy_coords[3] and player_coords[3] > enemy_coords[1] and player_coords[0] < enemy_coords[2] and player_coords[2] > enemy_coords[0]:
            game_over = True
            break

game_over = False

while not game_over:
    for i in range(num_enemies):
        enemies[i].enemy_move()
        check_enemy_coords()
        check_collision()
        tk.update()
        time.sleep(0.005)

overbg = canvas.create_rectangle(0, 0, 500, 500, fill='black')
over = canvas.create_text(250, 250, text='GAME OVER', font=('Helvetica', 30), fill='red')


tk.mainloop()