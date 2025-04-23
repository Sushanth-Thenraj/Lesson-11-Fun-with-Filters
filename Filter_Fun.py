import cv2
import numpy as np

def apply_filter(image, filter_type):
    
    filtered_image= image.copy()
    
    # Apply filter based on filter type sent by user
    if filter_type == "red_tint":
        #Create a red tint filter
        filtered_image[:, :, 0]= 0#Reduce intensity of blue channel
        filtered_image[:, :, 1]= 0#Reduce intensity of green channel
    elif filter_type == "blue_tint":
        #Create a blue tint filter
        filtered_image[:, :, 1]= 0#Reduce intensity of green channel 
        filtered_image[:, :, 2]= 0#Reduce intensity of red channel
    elif filter_type == "green_tint":
        #Create a green tint filter
        filtered_image[:, :, 0]= 0#Reduce intensity of blue channel
        filtered_image[:, :, 2]= 0#Reduce intensity of red channel
    elif filter_type == "increase_red":
        #Increase the intensity of red channel
        filtered_image[:, :, 2]= cv2.add(filtered_image[:, :, 2], 50)
    elif filter_type == "decreased_blue":
        #Decrease the intensity of blue channel
        filtered_image[:, :, 0]= cv2.subtract(filtered_image[:, :, 0,],50)
    return filtered_image

#Load an image
image_path= "Filter_Fun.jpg"
image= cv2.imread(image_path)

if image is None:
    print("Error: Could not load image.")
else:
    filter_type= "original"
    
    print("Input any of the following letters to apply the filter: \n")
    print("r= red_tint \nb= blue_tint \ng= green_tint \ni= increase_red \nd= decrease_blue \nq= quit")
    
    while True:
        #Apply the selected filter
        filtered_image= apply_filter(image,filter_type)
        #Display the filtered image
        cv2.imshow("Filtered Image", filtered_image)
        #Wait for user input
        key= cv2.waitKey(0) & 0xFF
        if key== ord("r"):
            filter_type= "red_tint"
        elif key== ord("b"):
            filter_type= "blue_tint"
        elif key== ord("g"):
            filter_type= "green_tint"
        elif key== ord("i"):
            filter_type= "increase_red"
        elif key== ord("d"):
            filter_type= "decrease_blue"
        elif key== ord("q"):
            break
        else:
            print("That is an invalid input, Please try again")

cv2.destroyAllWindows()