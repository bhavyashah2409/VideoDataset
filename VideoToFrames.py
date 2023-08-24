import os
import math
import cv2 as cv


def get_selective_frame_from_video(input_video: str, fps: int):
    frame_dir = './frames'
    if not os.path.exists(frame_dir):
        os.mkdir(frame_dir)

    # input_video = '/home/bhavyashah/ShipsDatasets/VideoDataset/videos/video_1.mp4'
    video_path = os.path.join(frame_dir, os.path.splitext(os.path.basename(input_video))[0])
    if not os.path.exists(video_path):
        os.mkdir(video_path)

    cap = cv.VideoCapture(input_video)
    input_frames = cap.get(cv.CAP_PROP_FRAME_COUNT)
    input_fps = cap.get(cv.CAP_PROP_FPS)
    print('INPUT VIDEO FPS:', input_fps)

    i = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if i % math.floor(input_fps / fps) == 0:
            cv.imwrite(os.path.join(video_path, f'frame_{i}.jpg'), frame)
        i = i + 1

if __name__ == '__main__':
    FPS = 2
    for video in os.listdir('./videos'):
        path = os.path.join('./videos', video)
        get_selective_frame_from_video(path, FPS)
