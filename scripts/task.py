#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def counter():

    rospy.init_node('counter')
    pub = rospy.Publisher('count', Int32, queue_size=10)
    rate = rospy.Rate(10)
    
    count = 0
    
    while not rospy.is_shutdown():
    
        rospy.loginfo("Counting: %d", count)
        pub.publish(count)
        count += 2
        rate.sleep()

if __name__ == '__main__':
    try:
        counter()
    except rospy.ROSInterruptException:
        rospy.logerr("ROS node interrupted.")