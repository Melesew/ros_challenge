#! /usr/bin/env python2

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2

def callback(data):
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    gray_pic = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY) # Convert to grayscale
    cv2.imshow("Capturing", gray_pic)
    
    keyctr = cv2.waitKey(1)
    # while True:
        # if (keyctr == ord('q')):
        #     break

rospy.init_node("topic_subscriber")  # initiate a node named 'topic_publisher'

# create a publisher object that will publish on a 'capture' topic
sub = rospy.Subscriber('capture', Image, callback)

rospy.spin()
