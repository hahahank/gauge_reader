import os
import cv2
import glob
import argparse

def main(file_name):
    video_path = '{}.mp4'.format(file_name)
    output_folder = './output/'

    vc = cv2.VideoCapture(video_path)
    fps = vc.get(cv2.CAP_PROP_FPS)
    frame_count = int(vc.get(cv2.CAP_PROP_FRAME_COUNT))
    print(frame_count)
    video = []

    for idx in range(frame_count):
        if idx % 12 == 0:
            vc.set(1, idx)
            ret, frame = vc.read()
            height, width, layers = frame.shape
            size = (width, height)
            if frame is not None:
                img_file_name = '{}-{:08d}.jpg'.format(file_name, idx)
                cv2.imwrite(img_file_name, frame)
            print("\rprocess: {}/{}".format(idx+1 , frame_count), end = '')
    vc.release()



if __name__=='__main__':
    parser = argparse.ArgumentParser(description="get images from video")
    parser.add_argument(  "--file_name",  default=" ", help="mp4 file"    )
 
    args = parser.parse_args()
    main(args.file_name )
 
