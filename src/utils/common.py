import os
import matplotlib.pyplot as plt

def change_to_root_dir():
    os.chdir("../")

def change_to_current_dir(current_dir):
    os.chdir(current_dir)

def show_image(image_array, image_title=None):
    plt.imshow(image_array)
    plt.title(image_title)
    plt.axis('off')
    plt.show()