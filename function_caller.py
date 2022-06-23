
#!/usr/bin/env python

import rospy
from task1_package.add import add

if __name__ == '__main__':
    rospy.init_node('test_node')
    print(add(1, 2))
    print("You successfully imported a python module")
