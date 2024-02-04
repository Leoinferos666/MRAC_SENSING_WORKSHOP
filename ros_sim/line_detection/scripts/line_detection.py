#!/usr/bin/python3

''' 
Code to detect and follow a color line  
    
Run the line_detection launch commands before this file 

Execute with python3 line_detection.py 

Complete this template and the template files color_image_line and velocity_line 
'''

import cv2
import numpy as np 
import rospy
from geometry_msgs.msg import Twist 
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

from color_image_line import show_image, get_color_range, detect_color, get_max_contour
from velocity_line import get_velocity


# Variables 
########################################################################
bridge = CvBridge()


# Image callback -> it is called when the topic receives information
################################################################
def image_callback(msg):
    
    rospy.loginfo("Image received")

    # Get image and publisher 
    ##########################################

    # Convert your ros image message to opencv using bridge
    # <COMPLETE>
    show_image(img, "Robot camera")

    # Get half width of the image 
    # <COMPLETE>


    # Create velocity publisher and variable of velocity
    # <COMPLETE>
    
    # Do color detection 
    ##########################################

    # Get color range with get_color_range()
    # <COMPLETE>

    
    # Get color mask using detect_color from color_image_line.py
    # <COMPLETE>


    # Show mask 
    show_image(mask, "Color detection")

    # Get max contour, area and center using get_mask_contour from color_image_line.py
    # <COMPLETE>
    print("Maximum area: ", area)


    # If area is bigger than 0 
    # <COMPLETE>

        # Draw contour and center of the maximum contour
        # <COMPLETE>
        show_image(img, "Contour detection")

        # Get robot velocity using get_velocity from velocity_line.py
        # <COMPLETE>


    # Look for color spinning 
    else:
        print("Looking for color: spinning to the left")
        # Add angular spinning velocity
        # <COMPLETE>

            

    # Publish velocity
    # <COMPLETE>




# Init node and suscribe to image topic 
################################################################   
def main():

    # Create line_detection node
    # <COMPLETE>

    # Suscribe to image topic and add callback + spin
    # <COMPLETE>

    cv2.destroyAllWindows()



if __name__ == '__main__':
    main()
    
    
    
    
    