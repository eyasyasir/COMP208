# Author: Eyas Hassan
# Assignment 4

import random
import numpy as np
import skimage.io as io

# Note: Do not put any code between these functions.
# Keep all testing code at the bottom of the file.

def denoise(filename):
    # splitting string in order to seperate file name from its extension
    filename = filename.split(".")
    
    # creating a list with elements "image_name_N.png", where N is a number in the range [0, 19]
    batch = [filename[0] + "_{}.png".format(i) for i in range(20)] 
    
    # importing each image and storing it in a list
    batch = [io.imread(image) for image in batch]
    
    # storing the dimension of the image (since all images are the same dim, one variable can represent dim for all)
    dimensions = batch[0].shape
    
    # creating an empty array of size = dimensions (essentially a black image which is what will later be
    # "coloured" to become the denoised image.
    avg_rgb = np.zeros(dimensions)

    for r in range(dimensions[0]):
        for c in range(dimensions[1]):
            number_of_stacks = 0  
            # iterating through the batch
            for i in range(20):
                image = batch[i]
                # boolean to check if pixel at coordinate (r, c) is not white and keeping count of
                # how many images this is true for
                if sum(image[r, c]) != 765:
                    # summation of rgb components at pixel (r, c) for all images which satisfy condition above
                    avg_rgb[r][c] += image[r, c]
                    number_of_stacks += 1
            # averaging out the rgb components of pixel (r,c) to produce denoised pixel
            avg_rgb[r, c] = avg_rgb[r, c] / number_of_stacks
            
    return avg_rgb

def add_random_white_pixels(filename, whiteout_prob):
    # reading and storing array of filename in variable image
    image = io.imread(filename)
    
    # storing the dimension of the image (since all images are the same dim, one variable can represent dim for all)
    dimensions = image.shape
    
    # creating an array of size dimensions (without rgb component). Each cell contains
    # 0 or 1 with probabilities (1 - whiteout_prob) and (whiteout_prob) respectively. A cell with 1 means the pixel
    # of the image at that coordinate will be turned white, otherwise; it will be untouched.
    rand_white_location = np.random.choice(2, (dimensions[0], dimensions[1]), p = [1 - whiteout_prob, whiteout_prob])
    
    # iterating through rand_white_location
    for r in range(dimensions[0]):
        for c in range(dimensions[1]):
            # rand_white_location[r][c] is equal to one, pixel of image at same location (r, c) will be turned white
            if rand_white_location[r][c] == 1:
                image[r][c] = np.array([255, 255, 255])
    
    return image
    
def add_white_regions(filename, num_regions):
    image = io.imread(filename)
    
    dimensions = image.shape
    
    # nested list of regions where each element conforms to: [(x-pos, y-pos), array(region width, region height)]
    # where (x-pos, y-pos) is a tuple denoting top left corner coordinates of region
    regions = [[(random.randint(1, dimensions[0]), random.randint(1, dimensions[1])), np.array(np.zeros((random.randint(1, dimensions[0] // 4), random.randint(1, dimensions[1] // 4))).shape)] for i in range(num_regions)]
    
    # correcting region dimensions based on coordinates of region in order to avoid an "out of bounds" region
    for region in regions:
        if region[0][0] + region[1][0] > dimensions[0]:
            region[1][0] = dimensions[0] - region[0][0]
        
        if region[0][1] + region[1][1] > dimensions[1]:
            region[1][1] = dimensions[1] - region[0][1]
           
        for r in range(region[0][0], region[0][0] + region[1][0]):
            for c in range(region[0][1], region[0][1] + region[1][1]):
                # turning pixels of the image in the specified region white
                image[r][c] = np.array([255, 255, 255])
    
    return image
        

# Testing code - uncomment to test each function
# When you are ready to submit, please comment out or delete all the lines below.

# filename = "tractor_beam.png"
# denoised_image = denoise(filename).astype(np.uint8)
# io.imsave("tractor_beam_final.png", denoised_image)

# filename = "tractor_beam_final.png" # Note: We can only load this file if the above function works.
# image_with_random_white_pixels = add_random_white_pixels(filename, 0.4)
# io.imsave("tractor_beam_whitepixels.png", image_with_random_white_pixels)

# filename = "tractor_beam_final.png"
# image_with_white_regions = add_white_regions(filename, 50)
# io.imsave("tractor_beam_whiteregions.png", image_with_white_regions)

