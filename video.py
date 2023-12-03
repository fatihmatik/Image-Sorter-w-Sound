import cv2
import os

def images_to_video(numof_sorted_imgs, image_folder, video_name, duration_per_image_ms):
    images = [f"{x}_merged.png" for x in range(0,numof_sorted_imgs+1,1)]

    if not images:
        print(f"No JPEG images found in {image_folder}")
        return

    # Read the first image to get dimensions
    first_image_path = os.path.join(image_folder, images[0])
    first_image = cv2.imread(first_image_path)

    if first_image is None:
        print(f"Error reading the first image: {first_image_path}")
        return

    height, width, layers = first_image.shape
    fps = (1000)/duration_per_image_ms # Calculating the frame per scond for VideoWriter()
    video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    for image in images:
        img_path = os.path.join(image_folder, image)
        img = cv2.imread(img_path)

        if img is not None:
            video.write(img)
        else:
            print(f"Error reading image: {img_path}")

    cv2.destroyAllWindows()
    video.release()
