# What Does it Do?
  Shuffles the given image to the input split count and rearranges and creates video file with a sorting algorithm audio.
  
# How it Works:
  Takes the "ex.png" in the directory of the scripts and splits them by the input number.
  Shuffles the split images, then step by step rearranges them and creates a image frame.
  Whilst creating the image frames, creates a frequency based on the index number it is sorting.
  The sorting of the dissolved image is done by the Bubble Sort algorithm.
  At the end the script merges the sound and the frames together to create a video.

# How to Run the script:
  Put an PNG file with the name of "ex.png", that you'd like to see rearranged, inside the directory where all of the .py scripts are located.    
  Run the the main.py from the CLI and enter the number of splits you'd like and desired miliseconds for every image frame.
  The resulting video is going to be the "output_merged.mp4" file.
  
  The directory might get messy after a run, since all of the images created are stored in the same directory of the scripts, but for an another run it shouldn't create a problem.
  Since the this bubblesort algorithm is written in Python without any libraries, it's a bit slow.
  For the missing libraries the pip installer should give the errors about which libraries you should install.


The idea came from "sorting trollface algorithm" uploaded on Apr 11 2022, from Youtube.


