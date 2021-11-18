import mss
from screeninfo import get_monitors
import mss.tools

# this file is made for checking the screenshot of the area
# that the program will use to detect the changes.
with mss.mss() as sct:
    # The screen part to capture

    monitors = get_monitors()
    monitor = monitors[0]

    monitorWidth = int(monitor.width/30)
    monitorHeight= int(monitor.height/30)
    bounding_box = {'top': 520, 'left': 930,
                    'width': monitorWidth, 'height': monitorHeight}

    output = "pic{top}x{left}_{width}x{height}.png".format(**bounding_box)

    # Grab the data
    sct_img = sct.grab(bounding_box)

    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    print(output)
