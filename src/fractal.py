#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897
from math import pow, atan, sqrt


def linear_move(vel_msg, speed, distance, velocity_publisher):
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    current_distance = 0

    t0 = rospy.Time.now().to_sec()
    while(current_distance < distance):
        vel_msg.linear.x = speed
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_distance = speed*(t1-t0)
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)


def rotate(vel_msg, speed_angular, angle, clockwise, velocity_publisher):
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0

    t0 = rospy.Time.now().to_sec()
    #Converting from angles to radians
    angular_speed = speed_angular*2*PI/360
    relative_angle = angle*2*PI/360

    current_angle = 0

    while(current_angle < relative_angle):
        # real_angle = atan(relative_angle)
        # print(real_angle)
        if clockwise:
            vel_msg.angular.z = -abs(angular_speed)
        else :
            vel_msg.angular.z = abs(angular_speed)
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t1-t0)

    vel_msg.angular.z = 0
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    velocity_publisher.publish(vel_msg)


def draw_fractal():
    rospy.init_node('draw_fractal', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    vel_msg = Twist()

    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    speed_linear = 4
    speed_angular = 100  # degrees/sec
    angle1 = 45
    angle2 = 135
    distance_linear = 2
    t0 = rospy.Time.now().to_sec()

    # for i in range(6):
    #     linear_move(vel_msg, speed_linear, distance_linear, velocity_publisher)
    #     rotate(vel_msg, speed_angular, angle, velocity_publisher)
    while not rospy.is_shutdown():    
        linear_move(vel_msg, speed_linear, 4, velocity_publisher)
        rotate(vel_msg, speed_angular, angle2, False, velocity_publisher)
        linear_move(vel_msg, speed_linear, distance_linear, velocity_publisher)
        rotate(vel_msg, speed_angular, angle1, True, velocity_publisher)

if __name__ == '__main__':
    try:
        # Testing our function
        draw_fractal()
    except rospy.ROSInterruptException:
        pass
