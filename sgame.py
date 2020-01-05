import turtle
import time
import argparse
from random import randint

def arg_parser():
	parser = argparse.ArgumentParser()
	parser.add_argument("-s", "--speed", type=int, help="Speed")
	args = parser.parse_args()
	return args

parser = arg_parser()

win = turtle.Screen()
win.title("Game")
win.bgcolor("green")
win.setup(width=700, height=700)
win.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 100)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.shapesize(0.50, 0.50)
food.goto(0, 0)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("No collision so far!", align="center", font=("Arial", 24, "normal"))

segments = []

def go_up():
	if head.direction != "down":
		head.direction = "up"

def go_down():
	if head.direction != "up":
		head.direction = "down"

def go_right():
	if head.direction != "left":
		head.direction = "right"

def go_left():
	if head.direction != "right":
		head.direction = "left"

def move(direc):
	if head.direction == "up":
		y = head.ycor()
		head.sety(y + direc)

	if head.direction == "down":
		y = head.ycor()
		head.sety(y - direc)

	if head.direction == "right":
		x = head.xcor()
		head.setx(x + direc)

	if head.direction == "left":
		x = head.xcor()
		head.setx(x - direc)

win.listen()
win.onkey(go_up, "w")
win.onkey(go_down, "s")
win.onkey(go_right, "d")
win.onkey(go_left, "a")

c = 0

while True:
	win.update()
	time.sleep(0.1)

	if head.xcor() > 950 or head.xcor() < -950 or head.ycor() > 950 or head.ycor() < -950:

		pen.clear()
		pen.write("Wall collision!", align="center", font=("Arial", 24, "normal"))

		time.sleep(1)
		head.goto(0, 0)
		head.direction = "stop"

		for segment in segments:
			segment.goto(1000, 1000)

		segments.clear()

		c = 0

	if head.distance(food) < 20:
		x = randint(-290, 290)
		y = randint(-290, 290)
		food.goto(x, y)

		c += 1

		pen.clear()
		pen.write("Food snacked: %s" % c, align="center", font=("Arial", 24, "normal"))

	new_segment = turtle.Turtle()
	new_segment.speed(0)
	new_segment.shape("square")
	new_segment.color("black")
	new_segment.penup()
	segments.append(new_segment)

	for index in range(len(segments)-1, 0, -1):
		x = segments[index-1].xcor()
		y = segments[index-1].ycor()
		segments[index].goto(x, y)

	if len(segments) > 0:
		x = head.xcor()
		y = head.ycor()
		segments[0].goto(x, y)

	move(parser.speed)

	for segment in segments:
		if segment.distance(head) < 20:

			time.sleep(1)
			head.goto(0, 0)
			head.direction = "stop"

			for segment in segments:
				segment.goto(1000, 1000)

			segments.clear()

			pen.clear()
			pen.write("You collided with yourself!", align="center", font=("Arial", 24, "normal"))
			time.sleep(1)
			pen.clear()

			c = 0