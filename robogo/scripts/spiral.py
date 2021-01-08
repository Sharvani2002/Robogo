#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt
PI = 3.14159265358979323



x=5.544444561
y=5.544444561

def callback(msg):
	global x
	global y
    # print "x: ",msg.x, "y: ",msg.y,"theta: ",msg.theta
	x=msg.x
	y=msg.y

def main():

	rospy.init_node('node_turtle', anonymous=True)

	publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	vel = Twist()

	#speed = (radius)*(angular velocity)
	#inear speed in x direction
	vel.linear.x=0.5
	vel.linear.y=0
	vel.linear.z=0
	vel.angular.x=0
	vel.angular.y=0
	#angular velocity in z direction
	vel.angular.z=3.5


	#Subscriber to the topic '/turtle1/pose'
	subscriber = rospy.Subscriber("/turtle1/pose", Pose, callback)
	rr = rospy.Rate(1)

	#Initialising the current distance to 0
	current_distance= 0

	print("The turtle has started moving")
	threshold = 2*PI*1*4

	#initial time
	t0= rospy.Time.now().to_sec()
	t2= t0+0.001
	# rospy.sleep(2)
	while current_distance<=threshold:
		t1 = rospy.Time.now().to_sec()
		
		vel.linear.x = vel.linear.x*2
		current_distance = vel.linear.x*(t1-t0)
		# current_distance= (t1-t0)
		# print(t1,t0)
		# t2=t1
		publisher.publish(vel)
		t2=t1
		rr.sleep()



	
	#Stopping the turtle
	vel.linear.x=0
	vel.angular.z=0
	publisher.publish(vel)
	print("Goal reached!")



if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

