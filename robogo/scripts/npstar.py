#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt
PI = 3.14159265358979323
import sys
import turtle
from time import sleep

# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

# def normal_star(size, color, points):
#     if points <= 4:
#         raise ValueError('Not enough points')

#     turtle.color(color)

#     for coprime in range(points // 2, 1, -1):
#         if gcd(points, coprime) == 1:

#             print("({},{})".format(points, coprime), file=sys.stderr)

#             start = turtle.position()

#             for _ in range(points):
#                 turtle.forward(size)
#                 turtle.left(360.0 / points * coprime)

#             turtle.setposition(start)

#             return

#     abnormal_star(size, color, points)

# def abnormal_star(size, color, points):
#     # deal with special cases here
#     print("Exception:", points, file=sys.stderr)

# for points in range(5, 20):
#     turtle.reset()
#     normal_star(200, 'red', points)
#     rospy.sleep(5)

# turtle.exitonclick()


def star(turtle, n, d):
    angle = (180-((180*(n-2))/n))*2
    for i in range(n):
        t.forward(d)
        t.left(angle)
    return angle


speed = 0.5

def move_in_line(side_length,vel_msg,pub):

    vel_msg.linear.x = speed
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    t0 = rospy.Time.now().to_sec()
    distance_travelled = 0
    # rr = rospy.Rate(2)
    while distance_travelled <= side_length:
        pub.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        distance_travelled = speed*(t1-t0)
        # rr.sleep()
    vel_msg.linear.x = 0
    pub.publish(vel_msg)

def rotate(vel_msg,pub, angle):
    angular_speed = 0.1
    vel_msg.angular.z = angular_speed
    t0  = rospy.Time.now().to_sec()
    angle_travelled = 0
    # rr = rospy.Rate(2)
    while ( angle_travelled <= angle ):
        pub.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        angle_travelled = angular_speed*(t1-t0)
        # rr.sleep()
    vel_msg.angular.z = 0
    pub.publish(vel_msg)    

if __name__ == '__main__':
    try:
        rospy.init_node('move_n_points',anonymous = True)
        pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size = 10)
        vel_msg = Twist()
        rr = rospy.Rate(2)
        side_length = 1
        rotations = 1
        n=5
        angle = (180-((180*(n-2))/n))*2
        for _ in range(n):
            move_in_line(side_length,vel_msg,pub)
            # t.forward(d)
            rotate(vel_msg,pub, angle)
            # t.left(angle)

        # current_rotation = 0
        # while current_rotation < rotations:
            
        #     rotate(vel_msg,pub)
        #     current_rotation+=0.25
            # rr.sleep()
    except rospy.ROSInterruptException:
        pass