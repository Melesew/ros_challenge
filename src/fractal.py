#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist, Vector3
import math
from math import cos, sin, tan, atan, pi, sqrt
from turtlesim.srv import TeleportAbsolute
import sys

# def orient_turtle():
rospy.wait_for_service('turtle1/teleport_absolute')
turtle1_teleport_absolute = rospy.ServiceProxy('turtle1/teleport_absolute', TeleportAbsolute)
resp1 = turtle1_teleport_absolute(5.54, 5.54, 0.0)


def get_vel(t):

    # if((t//1) % 4 == 0.0):
    #     velocity_linear = 2*sin(t)
    #     velocity_angular = 12*cos(t)
    # else:
    #     velocity_linear = -2*sin(t)

    #     velocity_angular = -12*cos(t)

    if((t//1) % 4 == 0.0):
        velocity_linear = 2
        velocity_angular = 0
    else:
        velocity_linear = -2
        velocity_angular = -12

    # if ((t//1) % 64 == 0.0):
    #     velocity_linear = 0
    #     velocity_angular = 0

    return [velocity_linear, velocity_angular]

def send_vel_command():

    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('draw_fractal', anonymous=True)
    r = rospy.Rate(62.5)  # 62.5hz
    while not rospy.is_shutdown():

        t = rospy.get_time()
        print((t//1) % 4)
        velocity_linear = get_vel(t)[0]
        velocity_angular = get_vel(t)[1]

        velocities = Twist(Vector3((velocity_linear), 0, 0), Vector3(0, 0, (velocity_angular)))
        rospy.loginfo(velocities)
        pub.publish(velocities)

        r.sleep()


if __name__ == '__main__':

    try:
        send_vel_command()
    except rospy.ROSInterruptException:
        pass
