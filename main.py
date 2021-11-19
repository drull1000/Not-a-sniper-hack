import numpy as np
import cv2
from mss import mss
from PIL import Image
from screeninfo import get_monitors
from skimage.metrics import structural_similarity as compare_ssim
from time import sleep
from beepy import beep
import typer
import math
import pyautogui

app = typer.Typer()


@app.command()
def start(sensitivity: float = 0.50, post_beep_sleep: float = 3, inter_frame_sleep: float = 0.0):
    """
    A reasonable value for SENSITIVITY would be 0.50, but make your own tests.
    """
    monitors = get_monitors()
    monitor = monitors[0]

    # general loop: https://stackoverflow.com/a/54246290

    monitorWidth = int(monitor.width/30)
    monitorHeight= int(monitor.height/30)
    bounding_box = {'top': 520, 'left': 930,
                    'width': monitorWidth, 'height': monitorHeight}

    sct = mss()
    try:
        typer.echo("Screen monitoring go brr")
        mat = np.array(sct.grab(bounding_box))
        prev_image = cv2.cvtColor(
            np.array(sct.grab(bounding_box)), cv2.COLOR_BGR2GRAY)
        while True:
            curr_image = cv2.cvtColor(
                np.array(sct.grab(bounding_box)), cv2.COLOR_BGR2GRAY)

            (score, diff) = compare_ssim(curr_image, prev_image, full=True)
            prev_image = curr_image.copy()

            if score < sensitivity:
                pyautogui.click(1,1)
                beep(sound='coin')
                sleep(post_beep_sleep)
            else:
                sleep(inter_frame_sleep)

    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
start()
