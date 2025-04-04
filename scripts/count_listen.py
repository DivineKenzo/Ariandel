#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def count_listen (msg):
    rospy.loginfo(msg.data)

def counting_listener():
    
    rospy.init_node('counting_listener')
    rospy.Subscriber('count', Int32, count_listen)
    rospy.spin()

if __name__ == '__main__':
    try:
        counting_listener()
    except rospy.ROSInterruptException:
        rospy.logerr("ROS node interrupted.")
