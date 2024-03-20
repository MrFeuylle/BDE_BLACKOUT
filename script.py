import cv2
import os

def create_video_from_images(image_folder, output_video, fps, delay_between_frames):
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))
        cv2.waitKey(delay_between_frames)

    cv2.destroyAllWindows()
    video.release()

image_folder = "./image"
output_video = "./bde.mp4"
fps = 0.1
delay_between_frames = 15000

create_video_from_images(image_folder, output_video, fps, delay_between_frames)
