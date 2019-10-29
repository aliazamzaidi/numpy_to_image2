from PIL import Image
import numpy as np
import os

def main():
    list_of_images = os.listdir("Images")
    
    array_of_images = []
    for i in range(len(list_of_images)):
        temp_image = Image.open(f"Images\{list_of_images[i]}")
        temp_image = temp_image.resize((200,200))
        array_of_images.append(temp_image)
    
    np_array_of_images = np.zeros((20,200,200,3))
    for i in range(len(array_of_images)):
        np_array_of_images[i] = array_of_images[i]
    
    print(np_array_of_images)
    
if __name__ == "__main__":
    main()