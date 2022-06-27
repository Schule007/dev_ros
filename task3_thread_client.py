#!/usr/bin/env python

import rospy
from get_function.srv import nil

def time_client():
    rospy.wait_for_service('time')
    try:
        sp = rospy.ServiceProxy('time', nil)
        return sp()
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)

if __name__ == "__main__":
    time_client()
