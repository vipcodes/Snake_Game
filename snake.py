import random
from turtle import Turtle

COLOR = ["red", "green", "blue", "white", "cyan", "magenta"]

STARTING_POSITIONS = [(0, 0), (-10, 0), (-20, 0)]
MOVE_POSITION = 10
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    def __init__(self):
        self.x = 0
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_POSITION)

    def add_segment(self, position):
        new_seg = Turtle("square")
        new_seg.color("red")
        new_seg.shapesize(.5)
        new_seg.penup()
        new_seg.speed("fastest")
        new_seg.goto(position)
        self.segments.append(new_seg)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.x += 1
        return self.x

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
