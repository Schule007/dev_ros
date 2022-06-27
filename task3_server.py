#!/usr/bin/env python3

from get_function.srv import addtwoints
from get_function.srv import addtwointsRequest
from get_function.srv import addtwointsResponse

import rospy


def handle_add_two_ints(req):
    print("Returning %s(%s + %s) = %s" % (req.gain, req.a, req.b, req.gain*(req.a + req.b)))
    response = addtwointsResponse(req.gain*(req.a + req.b))
    return response

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', addtwoints, handle_add_two_ints)
    print("Ready to run function.")
    rospy.spin()


if __name__ == "__main__":
    add_two_ints_server()
