#!/usr/bin/env python

import rospy
from turtlesim.msg import *
from turtlesim.srv import *
from geometry_msgs.msg import Twist
from std_srvs.srv import *
import random
from time import time
from math import atan2, pi, sqrt, pow
import sys

#subscriber call backs
def chaserPose(data):
    global turtle1x, turtle1y, theta1
    turtle1x = data.x
    turtle1y = data.y
    theta1 = data.theta

def chasedPose(data):
    global turtleTargetx, turtleTargety
    turtleTargetx = data.x
    turtleTargety = data.y

def moveChasedTurtle():
    global turtleTargetx, turtleTargety
    turtleTargetx = random.randint(0, 11)
    turtleTargety = random.randint(0, 11)
    spawnTurtle(turtleTargetx, turtleTargety, 0, "turtleTarget")

#Once the chaser finds the chasee reset to the next mess
def resetChase():
    try:
        killTurtle("turtleTarget")
    except:
        pass        
    moveChasedTurtle()

def getDistance(x1, y1, x2, y2):
    return sqrt(pow((x2-x1), 2) + pow((y2-y1), 2))

# Get direction first and then move street to the turtle
def streetChase():
    global motion
    targetTheta = atan2(turtleTargety - turtle1y, turtleTargetx - turtle1x)
    if (targetTheta < 0):
        targetTheta += 2 * pi
    if (abs(targetTheta - theta1) < 0.1):
        motion.linear.x = 10
        motion.angular.z = 0
    else:
        motion.linear.x = 0
        motion.angular.z = 5
    pub.publish(motion)
    
# def randomChase():
#     global motion
#     targetTheta = atan2(turtleTargety - turtle1y, turtleTargetx - turtle1x)

def chase_turtle():
    global turtle1x, turtle1y, turtleTargetx, turtleTargety

    resetChase()

    #Main Loop
    while not rospy.is_shutdown():
        distance = getDistance(turtle1x, turtle1y, turtleTargetx, turtleTargety)

        if (distance <= 1): # minimum distance
            resetChase()
        else:  # Go find the turtle
            streetChase()
            # randomChase()

        rate.sleep()

if __name__ == '__main__':
    try:
        global pub, rate, motion
        rospy.init_node('turtlechase', anonymous=True)
        pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        # Getting the chaser's Pose
        rospy.Subscriber("/turtle1/pose", Pose, chaserPose)
        # Getting the chased's Pose
        rospy.Subscriber("/turtleTarget/pose", Pose, chasedPose)
        rate = rospy.Rate(5)  # The rate of our publishing
        clearStage = rospy.ServiceProxy('/clear', Empty) 
        spawnTurtle = rospy.ServiceProxy('/spawn', Spawn)
        killTurtle = rospy.ServiceProxy('/kill', Kill)
        motion = Twist()  # The variable we send out to publish

        chase_turtle()

    except rospy.ROSInterruptException:
        pass
