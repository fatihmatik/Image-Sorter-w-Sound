from image import *
from new import *
from video import *
from video_sound_merger import *
import time
import os

if __name__ == "__main__":
    start_time = time.time()

    # Example usage:
    image_path = 'ex.png'  # Replace with the actual path to your image file
    N = int(input("Number of Vertical Tiles: "))  # Specify the number of vertical tiles
    duration_ms = int(input("Duration of every Frame(in miliseconds): "))

    # Split the image vertically
    vertical_tiles = split_image_vertically(image_path, N)

    # Save or display the individual tiles
    for i, tile in enumerate(vertical_tiles):
        tile.save(f'tile_{i + 1}.png')  # Save each tile with a unique name
        # Alternatively, you can display the tiles using:
        # tile.show()

    directory_path = os.getcwd()
    images = read_images_from_directory(N, directory_path)
    print(f"Number of images found: {len(images)}")

    idxarr = [x for x in range(0,N,1)]
    print(idxarr)
    
    # Shuffle the images list
    random.shuffle(idxarr)
    print(idxarr)

    ## MERGE THE IMAGES

    # # Merge the images horizontally
    merged_image_horizontal = merge_images_horizontally(N, images, idxarr)

    # # Save the horizontally merged image as a PNG file
    # # save the photo as "itr_merged.png"
    merged_image_horizontal.save('0_merged.png')

    numof_sorted_imgs = bubble_sort(N=N, duration_ms=duration_ms, images=images, idxarr=idxarr)
    numof_sorted_imgs = numof_sorted_imgs
    tot_sound = AudioSegment.silent(duration=duration_ms)
    for val in sound_file:
        tot_sound += val

    # Export the sound file to a WAV file
    tot_sound.export("sorted_sound.wav", format="wav")

    image_folder = ""
    video_name = 'output_video.mp4'

    images_to_video(numof_sorted_imgs, image_folder, video_name, duration_ms)
    

    video_path = 'output_video.mp4'
    audio_path = 'sorted_sound.wav'
    output_path = 'output_merged.mp4'
    merge_video_audio(video_path, audio_path, output_path)
    
    print(f"Execution Time:{time.time() - start_time}")