import cv2
import os

def resize_image(image, target_width, target_height):
    return cv2.resize(image, (target_width, target_height))

def create_video_from_images(image_folder, output_video, fps=30, duration_per_image=2, target_width=None, target_height=None):
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    if target_width is None:
        target_width = width
    if target_height is None:
        target_height = height

    video = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*'mp4v'), fps, (target_width, target_height))

    for image in images:
        frame = cv2.imread(os.path.join(image_folder, image))
        frame = resize_image(frame, target_width, target_height)
        video.write(frame)

    cv2.destroyAllWindows()
    video.release()
image_folder = "./image"
output_video = "./bde.mp4"
fps = 0.1
delay_between_frames = 15000

create_video_from_images(image_folder, output_video, fps, delay_between_frames)
