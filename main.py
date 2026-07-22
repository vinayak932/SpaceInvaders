import turtle
from player import Player
from enemy import Enemy
from bullet  import Bullet
import time
import random
from scorecard import Scorecard

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("SPACE INVADERS")
screen.tracer(0)

player = Player((0,-250))
enemies = []
player_bullet = Bullet()
enemy_bullet = Bullet()
scorecard = Scorecard()
IS_GAME = True
bullet_active = False
enemy_direction = 10
WALL_HIT = False
enemy_bullet_active = False

def fire():
    global bullet_active
    if not bullet_active:
        player_bullet.goto(player.xcor(), player.ycor() + 20)
        player_bullet.showturtle()
        bullet_active = True

screen.listen()
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")
screen.onkey(fire, "space")

start_x = -170
start_y = 150

for row in range(2):
    for col in range(8):
        enemy = Enemy()
        x = start_x + col * 43
        y = start_y - row * 30
        enemy.goto(x,y)
        enemies.append(enemy)

while IS_GAME:
    
    if bullet_active:
        player_bullet.move_bullet()

    if bullet_active:
        for enemy in enemies:
            if player_bullet.distance(enemy) < 20:
                player_bullet.hideturtle()
                player_bullet.goto(0, -350)
                scorecard.increase_score()
                enemy.hideturtle()
                enemies.remove(enemy)

                bullet_active = False
                break

    if player_bullet.ycor() > 290:
        player_bullet.hideturtle()
        player_bullet.goto(0,-350)
        bullet_active = False

    for enemy in enemies:
        if enemy.xcor() > 390 or enemy.xcor() < -390:
            WALL_HIT = True
            break

    if WALL_HIT:
        enemy_direction *= -1

        for enemy in enemies:
            enemy.goto(enemy.xcor(), enemy.ycor() - 20)
        WALL_HIT = False

    for enemy in enemies:
        enemy.goto(enemy.xcor() + enemy_direction, enemy.ycor())

    if enemies and not enemy_bullet_active:
        enemies_bullet = random.choice(enemies)
        enemy_bullet.goto(enemies_bullet.xcor(), enemies_bullet.ycor() - 20)
        enemy_bullet.showturtle()
        enemy_bullet_active = True

    if enemy_bullet_active:
        enemy_bullet.move_enemy_bullet()

    if enemy_bullet.ycor() < -380:
       enemy_bullet.hideturtle()
       enemy_bullet.goto(0,-450)
       enemy_bullet_active = False


    if enemy_bullet.distance(player) < 20:
        IS_GAME = False
        scorecard.game_over()
        break

    for enemy in enemies:
        if enemy.distance(player) < 20:
            IS_GAME =False
            scorecard.game_over()
            break

    screen.update()
    time.sleep(0.05)

screen.mainloop()

