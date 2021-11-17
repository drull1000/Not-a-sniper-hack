import mss
from screeninfo import get_monitors
import mss.tools


with mss.mss() as sct:
    # The screen part to capture

    monitors = get_monitors()
    monitor = monitors[0]
    monitorWidth = int(monitor.width/10)
    monitorHeight= int(monitor.height/10)
   #300 100 
    bounding_box = {'top': 490, 'left': 870,
                    'width': monitorWidth, 'height': monitorHeight}

    output = "sct-{top}x{left}_{width}x{height}.png".format(**bounding_box)

    # Grab the data
    sct_img = sct.grab(bounding_box)

    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    print(output)
