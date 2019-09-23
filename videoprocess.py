# test_video.py
#
# Open a video input file and feed each image frame to 'openalpr'
# for license plate recognition.

import numpy as np
import cv2
from openalpr import Alpr


VIDEO_SOURCE = 'vehicles_3_sep/2019-03-09-0850.mp4'
WINDOW_NAME  = 'openalpr'
FRAME_SKIP   = 15

def main():
    alpr = Alpr('tw', 'tx2.conf', '/usr/local/share/openalpr/runtime_data')
    if not alpr.is_loaded():
        print('Error loading OpenALPR')
        sys.exit(1)
    alpr.set_top_n(3)
    #alpr.set_default_region('new')

    cap = cv2.VideoCapture(VIDEO_SOURCE)
    if not cap.isOpened():
        alpr.unload()
        sys.exit('Failed to open video file!')
    cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_AUTOSIZE)
    cv2.setWindowTitle(WINDOW_NAME, 'OpenALPR video test')

    _frame_number = 0
    while True:
        ret_val, frame = cap.read()
        if not ret_val:
            print('VidepCapture.read() failed. Exiting...')
            break

        _frame_number += 1
        if _frame_number % FRAME_SKIP != 0:
            continue
        cv2.imshow(WINDOW_NAME, frame)

        results = alpr.recognize_ndarray(frame)
        for i, plate in enumerate(results['results']):
            best_candidate = plate['candidates'][0]
            print('Plate #{}: {:7s} ({:.2f}%)'.format(i, best_candidate['plate'].upper(), best_candidate['confidence']))

        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()
    cap.release()
    alpr.unload()


if __name__ == "__main__":
    main()
 tw.conf
; 25-45, 35-55, 45-65, 55-75, 65-85
char_analysis_min_pct = 0.25
char_analysis_height_range = 0.20
char_analysis_height_step_size = 0.10
char_analysis_height_num_steps = 5

segmentation_min_speckle_height_percent = 0.3
segmentation_min_box_width_px = 4
segmentation_min_charheight_percent = 0.5;
segmentation_max_segment_width_percent_vs_average = 1.35;

plate_width_mm = 380.0
plate_height_mm = 160.0

multiline = 0

char_height_mm = 94
char_width_mm = 47
char_whitespace_top_mm = 36
char_whitespace_bot_mm = 26

template_max_width_px = 152
template_max_height_px = 64

; Higher sensitivity means less lines
plateline_sensitivity_vertical = 25
plateline_sensitivity_horizontal = 45

; Regions smaller than this will be disqualified
min_plate_size_width_px = 80
min_plate_size_height_px = 35

; Results with fewer or more characters will be discarded
postprocess_min_characters = 4
postprocess_max_characters = 7

ocr_language = ltw

; Override for postprocess letters/numbers regex. 
postprocess_regex_letters = [A-Z]
postprocess_regex_numbers = [0-9]

; Whether the plate is always dark letters on light background, light letters on dark background, or both
; value can be either always, never, or auto
invert = auto
