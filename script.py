import cv2
import os

def create_video_from_images(image_folder, output_video, fps=30, delay_between_frames=100):
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))
        cv2.waitKey(delay_between_frames)

    cv2.destroyAllWindows()
    video.release()

# Usage example:
image_folder = "./image"
output_video = "./bde.mp4"
fps = 1  # Frames per second
delay_between_frames = 15000  # Delay between frames in milliseconds

create_video_from_images(image_folder, output_video, fps, delay_between_frames)
