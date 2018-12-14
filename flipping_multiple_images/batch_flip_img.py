# flipping the images without retaining the filename
# to retain the image sequence in naming/numbering, it must have same filename length

# import modules
from datetime import datetime
import numpy as np
import glob
import cv2

# directory path to images
training_images = glob.glob("original_images/*.jpg")
# load the images into an array
image_array = np.array([cv2.imread(file) for file in training_images])
# find how many contents exist inside the array
array_length = len(image_array)

# flip the images and save to flipped_images/ folder
for x in range(array_length):

    # get the current time
    timestr = datetime.now().strftime("%Y%m%d%H%M%S%f")
    
    # flip the image and save
    flipped = np.flip(image_array[x], 1)
    cv2.imwrite('flipped_images/' + timestr + '.jpg', flipped)


# flipping the images while retaining the filename

# # import modules
# import numpy as np
# import glob
# import cv2

# # directory path to images
# training_images = glob.glob("original_images/*.jpg")

# for filename in training_images:
#   image = np.array(cv2.imread(filename))
#   flipped = np.flip(image, 1)
#   out_path = filename.replace("original_images","flipped_images")
#   cv2.imwrite(out_path, flipped)