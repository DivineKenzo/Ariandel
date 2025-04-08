#!/usr/bin/env python3
import rospy
rospy.init_node('lab3')

rospy.set_param('~ros_priv_param', 'Hi, I am private =)')
rospy.set_param('ros_loc_param', 'Hi, I am local =)')
rospy.set_param('/ros_glob_param', 'Hi, I am global =)')

global_param = rospy.get_param('/ros_glob_param')
rospy.loginfo("Global parameter '/ros_glob_param': %s", global_param)
local_param = rospy.get_param('ros_loc_param')
rospy.loginfo("Local parameter 'ros_loc_param': %s", local_param)
private_param = rospy.get_param('~ros_priv_param')
rospy.loginfo("Private parameter '~ros_priv_param': %s", private_param)
