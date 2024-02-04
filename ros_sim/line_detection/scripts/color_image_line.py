#!/usr/bin/python3


import cv2



# Show image 
def show_image(img, window_name): 
    cv2.imshow(window_name, img)
    cv2.waitKey(1)


# Get red color limits
def get_color_range():
    lower_range = # <COMPLETE>
    upper_range = # <COMPLETE>
    
    return lower_range, upper_range


# Detects the color 
def detect_color(img, lower_range, upper_range):

    # Perform a Gaussian filter 
    # <COMPLETE>

    # Convert image to HSV
    # <COMPLETE>

    # Get color mask
    # <COMPLETE>

    # Define rectangular kernel 5x5
    # <COMPLETE>

    # Apply openning
    # <COMPLETE>

    # Apply dilation
    # <COMPLETE>s

    return mask


# Get maximum contour, area and its center 
def get_max_contour(mask): 

    contour_max = []
    area_max = 0
    center = (-1,-1)
    # Find contours
    # <COMPLETE>

    # For each contour
    # <COMPLETE>

        # Get area of the contour 
        # <COMPLETE>


        # If area is bigger than area_max
        # <COMPLETE>
            # Update area_max value 
            # <COMPLETE>

            # Update contour_max value
            # <COMPLETE>

            # Get center of the contour using cv2.moments
            # <COMPLETE>


    return contour_max, area_max, center