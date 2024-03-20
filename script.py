import cv2
import os
import numpy as np

def resize_with_black(image, new_width, new_height):
    original_height, original_width = image.shape[:2]
    scale_x = new_width / original_width
    scale_y = new_height / original_height
    scale = min(scale_x, scale_y)
    resized_image = cv2.resize(image, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
    black_image = np.zeros((new_height, new_width, 3), dtype=np.uint8)
    start_x = (new_width - int(original_width * scale)) // 2
    start_y = (new_height - int(original_height * scale)) // 2
    black_image[start_y:start_y + resized_image.shape[0], start_x:start_x + resized_image.shape[1]] = resized_image

    return black_image

def create_video_from_images(image_folder, output_video, fps, duration_per_image, target_width=None, target_height=None):
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    if target_width is None:
        target_width = width
    if target_height is None:
        target_height = height

    frames_per_image = int(fps * duration_per_image)
    video = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*'MJPG'), fps, (target_width, target_height))

    for image in images:
        frame = cv2.imread(os.path.join(image_folder, image))
        frame = resize_with_black(frame, target_width, target_height)
        for _ in range(frames_per_image):
            video.write(frame)

    cv2.destroyAllWindows()
    video.release()
image_folder = os.path.join(os.path.dirname(__file__), "image")
output_video = "bde.mkv"
fps = 1
delay_between_frames = 5

create_video_from_images(image_folder, output_video, fps, delay_between_frames)
