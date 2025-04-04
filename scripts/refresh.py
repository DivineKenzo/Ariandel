#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32, String

def counter():

    rospy.init_node('counter')
    pub = rospy.Publisher('count', Int32, queue_size=10)
    refresh_pub = rospy.Publisher('refresh', String, queue_size=10)
    rate = rospy.Rate(10)
    
    count = 0
    while not rospy.is_shutdown():

        
        if count >= 100:
            refresh = "Counter overflow at %d" % count
            refresh_pub.publish(refresh)
            count = 0
        else:
            pub.publish(count)
            count += 2

        rate.sleep()

if __name__ == '__main__':
    try:
        counter()
    except rospy.ROSInterruptException:
        rospy.logerr("ROS node interrupted.")