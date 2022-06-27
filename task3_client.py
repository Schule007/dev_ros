#!/usr/bin/env python3

from get_function.srv import addtwoints
from get_function.srv import addtwointsRequest
from get_function.srv import addtwointsResponse

import rospy 
import sys

def add_two_ints_client(x, y):
    rospy.wait_for_service('add_two_ints')
    try: #service proxy sends information to the server
        sp = rospy.ServiceProxy('add_two_ints', addtwoints) 
        resp1 = sp(z, x, y)
        return resp1.func
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)
         
if __name__ == "__main__":
    z = rospy.get_param('gain')
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print("%s [z x y]" % sys.argv[0])
        sys.exit(1)
    print("Requesting %s(%s + %s)" % (z, x, y))
    s = add_two_ints_client(x, y)
    print("%s(%s + %s) = %s" % (z, x, y, s))
