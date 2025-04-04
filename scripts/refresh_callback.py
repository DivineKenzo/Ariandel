#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def refresh_callback(msg):
    rospy.loginfo("Received refresh message: %s", msg.data)

def refresh_listener():
    
    rospy.init_node('refresh_listener')
    rospy.Subscriber('refresh', String, refresh_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        refresh_listener()
    except rospy.ROSInterruptException:
        rospy.logerr("ROS node interrupted.")
