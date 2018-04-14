#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time
from turtlesim.msg import Pose
from math import pow, atan2, sqrt
from appJar import gui

# def rotate(angle):
    
def move_turtle(distance, angle):
	rospy.init_node('gui_node', anonymous=True)
	vel_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=100)
	vel_msg = Twist() 
	vel_msg.linear.x = distance
	vel_msg.angular.z = angle

	vel_publisher.publish(vel_msg)

def handler(button):
	if button == "Forward":
		move_turtle(3, 0)
	elif button == "Backward":
		move_turtle(-3, 0)
	elif button == "c_clockwise":
		move_turtle(0, 2)
	elif button == "clockwise":
		move_turtle(0, -2)
	elif button == "Stop":
		move_turtle(0, 0)


if __name__ == '__main__':
    try:
        turtle_gui = gui()
        turtle_gui.setPadding(10, 10)
        turtle_gui.addButtons(["Forward"], handler)
        turtle_gui.addButtons(["c_clockwise", "Stop", "clockwise"], handler)
        turtle_gui.addButtons(["Backward"], handler)
        turtle_gui.go()
    except rospy.ROSInterruptException:
    	pass
