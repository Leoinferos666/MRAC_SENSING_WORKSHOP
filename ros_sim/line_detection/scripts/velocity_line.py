#!/usr/bin/python3


'''
FUNCTIONS FOR LINE DETECTION CODE
'''

# Gets the robot speed and direction depending on the color detection 
##############################################
# Parameters:                                #
# - vel: Twist vector to modify velocity     #
# - x: x coordinate of the contour center    #
# - mid_width: middle width of the image     # 
##############################################
def get_velocity(vel, x, mid_width): 

    # Add an offset so the robot only turns when the center of the contour has deviated a specific distance to the right or left
    offset = # <COMPLETE>

    # If the color detected is on the right part of the image + an offset
    # <COMPLETE>
        # Go straight and spin to the right 
        print("Go straight and spin to the right")
        # <COMPLETE> 


    # If the color detected is on the left part of the image + an offset
    # <COMPLETE>
        # Go straight and spin to the left
        print("Go straight and spin to the left")
        # <COMPLETE> 


    # Go straight 
    else:
        print("Go straight ")
        # <COMPLETE>

    
    return vel
    
