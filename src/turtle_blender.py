#!/usr/bin/env python

import rospy
import socket
import math
from turtlesim.srv import TeleportAbsolute
from geometry_msgs.msg import Twist

host = '127.0.0.1'
port = 2000
# create socket object
sock = socket.socket()
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
            data = sock.recv(2000)
            new_data = str(data).encode('ascii')
            new_data = new_data.split(" ") # get the x and y positions 
            if len(new_data) == 2:
                print(float(new_data[0]), float(new_data[1]))
                turtle_pos(float(new_data[0])+5, float(new_data[1])+3, 0)
                msg.linear.x = float(new_data[0])
                msg.angular.z = float(new_data[1])
                publisher.publish(msg)
            new_data =  float(new_data)
            m = float(new_data)
            msg.linear.x = new_data
        except:
            print ("error")
        sock.close()

if __name__ == '__main__':
    try:
        # Testing our function
        move_turtle()
    except rospy.ROSInterruptException:
        pass
