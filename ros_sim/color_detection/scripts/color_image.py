#!/usr/bin/python3

'''
FUNCTIONS FOR COLOR DETECTION CODE
'''

import cv2 

# Resize and show image 
def show_image(img, window_name): 
    img_res = cv2.resize(img, None, fx=0.3, fy=0.3)
    cv2.imshow(window_name, img_res)
    cv2.waitKey(1)


# Get color limits
def get_color_range(color):
    
    # Complete only for the color you want to detect 

    #if(color == 'red'):
    #    lower_range = # <COMPLETE>
    #    upper_range = # <COMPLETE>
 
    #elif(color == 'green'):
    #    lower_range = # <COMPLETE>
    #    upper_range = # <COMPLETE>

    if(color == 'blue'):
        lower_range = (H,0,0)# <COMPLETE>
        upper_range = (H,255,255)
    #else: # Yellow 
    #    lower_range = # <COMPLETE>
    #    upper_range = # <COMPLETE>
    
    return lower_range, upper_range



# Detects the color 
def detect_color(img, lower_range, upper_range):

    # Perform a Gaussian filter 
    image_gauss = cv2.GaussianBlur(img,)
    # <COMPLETE>

    # Convert gauss image to HSV
    hsv_image = cv2.cvtColor(...,cv2.COLOR_BGR2HSC)
    # <COMPLETE>

    # Get color mask 
    mask = cv2.inRange()
    # <COMPLETE>

    # Define rectangular kernel 25x25
    kernel = cv2.getStructuringElement (rectangular,(25,25))
    # <COMPLETE>

    # Apply openning to mask 
    
    # <COMPLETE>

    return mask



# Get maximum contour, area and its center 
def get_max_contour(mask): 

    contour_max = []
    area_max = 0
    center = (-1,-1)

    
    # Find contours
    # <COMPLETE>

    # For each contour
    for cnt in contours:
        
    # <COMPLETE>
    
        # Get area of the contour 
        # <COMPLETE>

        # If area is bigger than area_max 
        if (area > area_max ):
        # <COMPLETE>
            # Update area max value 
            area_max =
            # <COMPLETE>

            # Update contour_max value
            contour_max= cnt
            # <COMPLETE>

            # Get center of the contour using cv2.moments
            # <COMPLETE>


    return contour_max, area_max, center