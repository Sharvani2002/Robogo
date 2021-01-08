#!/usr/bin/env python
import turtle
import math
def ellipse(a, b, h=None, k=None, angle=None, angle_unit=None):
  myturtle = turtle.Turtle()
  if h is None:
    h = 0
  if k is None:
    k = 0
  # Angle unit can be degree or radian
  if angle is None:
    angle = 360
    converted_angle = angle*0.875
  if angle_unit == 'd' or angle_unit is None:
    converted_angle = angle * 0.875
  # We are multiplying by 0.875 because for making a complete ellipse we are plotting 315 pts according
  # to our parametric angle value
  elif angle_unit == "r":
    converted_angle = (angle * 0.875 * (180/math.pi))
  # Converting radian to degrees.
  for i in range(int(converted_angle)+1):
    if i == 0:
      myturtle.up()
    else:
      myturtle.down()
    myturtle.setposition(h+a*math.cos(i/50), k+b*math.sin(i/50))
  turtle.done()


ellipse(200,100)