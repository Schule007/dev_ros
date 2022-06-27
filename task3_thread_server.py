#!/usr/bin/env python


import rospy
from get_function.srv import nil
from std_msgs.msg import String


def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        hello_str = "Current time is %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

def handle_talker(nothing):
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
    
def time_srv():
    rospy.init_node('time_srv')
    s = rospy.Service('time', nil, handle_talker)
    rospy.spin()

if __name__ == "__main__":
    time_srv()
