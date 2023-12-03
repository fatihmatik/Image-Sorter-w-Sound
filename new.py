from PIL import Image
import os, random, time
from pydub import AudioSegment
from pydub.generators import Sine
global sound_file
sound_file = []

def read_images_from_directory(N,directory_path):
    image_list = []

    # Check if the directory exists
    if not os.path.exists(directory_path):
        print(f"Error: Directory '{directory_path}' not found.")
        return image_list
    
    # "tile_{order}.png"

    # Iterate through files in the directory
    for filename in list(f"tile_{y}.png" for y in range(1,N+1,1)) :
        file_path = os.path.join(directory_path, filename)

        # # Check if the file is an image
        # if os.path.isfile(file_path) and any(file_path.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg']):
        #     # Open the image and append it to the list
        image = Image.open(file_path) #
        image_list.append(image) #

    return image_list

def bubble_sort(N, duration_ms, images, idxarr) -> int:
    n = len(idxarr)
    savecount = 1
    # Traverse through all array elements
    for itr in range(n):
        # Last itr elements are already in place, so we don't need to check them
        for jtr in range(0, n - itr - 1):
            # Swap if the element found is greater than the next element
            if idxarr[jtr] > idxarr[jtr + 1]:
                idxarr[jtr], idxarr[jtr + 1] = idxarr[jtr + 1], idxarr[jtr]
                create_sound(duration_ms, idxarr[jtr])
                merged_image_horizontal = merge_images_horizontally(N, images, idxarr)
                merged_image_horizontal.save(f'{savecount}_merged.png')             
                savecount += 1
    return int(savecount)

def create_sound(duration_ms,value):
    # Create an AudioSegment with a duration of 1 second
    sound = AudioSegment.silent(duration=duration_ms)
    # Generate a sine wave for each sorted value and concatenate them
    frequency = value + 150 # Use the sorted value as the frequency directly # + here to increase the base frequency of the notes.
    sound = Sine(frequency).to_audio_segment(duration=duration_ms)  # duration_ms amount of second/s for each tone
        
    sound_file.append(sound)

def merge_images_horizontally(N, images, idxarr):
    # Get the width and height of the first image in the list
    width, height = images[0].size

    # Calculate the total width for the merged image
    total_width = width * len(images)

    # Create a blank image with the calculated total width and the height of the first image
    merged_image = Image.new("RGB", (total_width, height), (255, 255, 255))

    # Paste each image onto the blank image horizontally
    # for i, image in enumerate(images):
    #     merged_image.paste(image, (i * width, 0))
    for itr, jtr in zip(idxarr, [x for x in range(0,N,1)]) :

        merged_image.paste(images[itr], (jtr * width, 0))

    return merged_image