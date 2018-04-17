#!/usr/bin/env python

import rospy
import socket
import math
from turtlesim.srv import TeleportAbsolute
from geometry_msgs.msg import Twist
import sys

host = "localhost"
port = 2000

# create socket object

sock = socket.socket()
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((host, port))


def call_back():
    global sock
    while True:
        data = sock.recv(port)
    sock.close()


def move_turtle():
    rospy.init_node("turtle_blender", anonymous=False)
    rate = rospy.Rate(1)

    publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    msg = Twist()
    rospy.wait_for_service('/turtle1/teleport_absolute')
    turtle_pos = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)

    while not rospy.is_shutdown():
        
        try:
            data = sock.recv(port)

            coordinates = data.decode('ascii')
   
            xcoordinate, ycoordinate = coordinates.split(" ")[0], coordinates.split(" ")[1]  # get the x and y positions

            if (xcoordinate, ycoordinate):
                print(float(xcoordinate), float(ycoordinate))
                turtle_pos(float(xcoordinate)+5, float(ycoordinate)+3, 0)
        except:
            print ("error")
        # sock.close()

if __name__ == '__main__':
    try:
        move_turtle()
    except rospy.ROSInterruptException:
        pass
