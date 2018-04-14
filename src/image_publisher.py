#!/usr/bin/env python2

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2

def publish():
    captr = cv2.VideoCapture(0)
    pub = rospy.Publisher('capture', Image)
    rospy.init_node('publisher_node', anonymous=True)
    rate = rospy.Rate(2) # 10hz
    
    while True:
        check, frame = captr.read()
        bridge = CvBridge()
        pub.publish(bridge.cv2_to_imgmsg(frame, "bgr8"))
        cv2.imshow("Capturing", frame)
        
        # rospy.loginfo(frame)
        key = cv2.waitKey(1)
        if (key == ord('q')):
            break
        rate.sleep()

if __name__ == '__main__':
    try:
        publish()
    except rospy.ROSInterruptException:
        pass
