from tkinter import *
import random
import time
from CarClass import Car
from CarClass import Enemy



# Create the main window
tk = Tk()
tk.title("Car Dodge Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=500, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
bg = canvas.create_rectangle(0, 0, 500, 500, fill='grey')
for i in range(100,500,100):
    canvas.create_line(i, 0, i, 500, fill='white', width=5)
for j in range(100,600,100):
    for i in range(0,500,100):
        canvas.create_rectangle(j-50, i, j-50, 50+i, fill='yellow', outline='yellow')





# Create the Car instance
player = Car(canvas, 'blue')
canvas.bind_all('<KeyPress-Left>', player.move_left)
canvas.bind_all('<KeyPress-Right>', player.move_right)

# Create the Enemy instance
enemies = []
num_enemies = 9

for i in range(num_enemies):
    enemies.append(Enemy(canvas, 'red'))
    enemies[i].enemy_spawn()
    

def check_enemy_coords():
    for i in enemies:
        if canvas.coords(i.id)[1] > 500:
            i.enemy_reset()


def check_collision():
    global game_over
    player_coords = canvas.coords(player.id)
    for enemy in enemies:
        enemy_coords = canvas.coords(enemy.id)
        if player_coords[1] < enemy_coords[3] and player_coords[3] > enemy_coords[1] and player_coords[0] < enemy_coords[2] and player_coords[2] > enemy_coords[0]:
            game_over = True
            break

game_over = False
score = 0
printed_score = 0
while not game_over:
    check_enemy_coords()
    for i in enemies:
        i.enemy_move()
        check_collision()
        tk.update()
        time.sleep(0.005)
        score += 1
        if printed_score % 5 == 0 and not 0:
            for i in enemies:
                i.speed += 0.03

        if score % 200 == 0:
            printed_score += 1
            blank = canvas.create_rectangle(5, 0, 500, 50, fill='grey', outline='grey')
            show_score = canvas.create_text(40, 25, text=f'Score:{printed_score}', font=('Helvetica', 13), fill='white')

        

overbg = canvas.create_rectangle(0, 0, 500, 500, fill='black')
over = canvas.create_text(250, 250, text='GAME OVER', font=('Helvetica', 30), fill='red')
end_score = canvas.create_text(250, 300, text=f'Your score was {printed_score}', font=('Helvetica', 20), fill='white')


tk.mainloop()