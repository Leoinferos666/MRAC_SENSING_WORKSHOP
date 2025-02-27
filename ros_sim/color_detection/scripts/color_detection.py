#!/usr/bin/python3

''' 
Code to detect and follow a color 
    
Run the color_detection launch commands before this file 

Execute with python3 color_detection.py 

Complete this template and the template files color_image and velocity
'''

# Import libraries
########################################################################
import cv2
import numpy as np 
import rospy
from geometry_msgs.msg import Twist 
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

from color_image import show_image, get_color_range, detect_color, get_max_contour
from velocity import get_velocity


# Variables 
########################################################################
bridge = CvBridge()
w = 640
# min_detection = 
# <COMPLETE> 


# Image callback -> it is called when the topic receives information
################################################################
def image_callback(msg):
    
    rospy.loginfo("Image received")

    # Get image and publisher 
    ##########################################

    # Convert your ros image message to opencv using bridge
    img = bridge.imgmsg_to_cv2(msg, "bgr8")
    # <COMPLETE> 

    # Show image using show_image function
    show_image(img, "window_name")
    # <COMPLETE> 

    # Get half width of the image 
    mid_width = w / 2
    # <COMPLETE> 

    # Create velocity publisher and variable of velocity
    pub = rospy.Publisher("/cmd_vel", Twist , queue_size=10 )
    vel = Twist()
    # <COMPLETE> 

    
    # Do color detection 
    ##########################################

    # Get color range using get_color_range from color_image.py
    lower_range, upper_range = get_color_range('blue')
    # <COMPLETE> 
    
    # Get color mask using detect_color from color_image.py
    mask = detect_color(img, lower_range, upper_range)
    # <COMPLETE>

    # Show mask 
    show_image (mask, "2window_name")
    # <COMPLETE>

    # Find contours and get max area using get_max_contours from color_image.py 
    # <COMPLETE>
    contour_max, area_max, center = get_max_contour(mask)
    # print("Maximum area: ", area)


    # Get robot speed     
    ##########################################

    # If the area of the detected color is big enough
    if area_max > minimum_detection:
        print("Cylinder detected")

        # Draw contour and center of the detection and show image 
        cv2.drawContours(img, [contour_max], 0, (0, 255, 0), 3)
        # draw center
        cv2.circle(img, center, 5, (0, 0, 255), -1)
        show_image(img, "window_name")
        # <COMPLETE>

        # Gets the color speed and direction depending on the color detection using get_velocity from velocity.py
        vel = get_velocity(vel, area_max, center[0], mid_width)
        # <COMPLETE>

    # If the area of the detected color is not big enough, the robot spins 
    else:
        print("Looking for color: spinning")
        vel.angular.z = 1

    # Publish velocity
    pub.publish(vel)
    # <COMPLETE> 


# Init node and subscribe to image topic 
################################################################
def main():
    # Init node 'color_detection'
    rospy.init_node('color_detection')
    # <COMPLETE>

    # Subscribe to image topic and add callback + spin
    rospy.Subscriber("/camera/rgb/image_raw", Image, image_callback)
    # <COMPLETE>
    rospy.spin()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
