import wfc_2019f.wfc.wfc_control as wfc_control
from PIL import Image
import numpy as np


image = Image.open("grass.png")
image = np.array(image)
wfc_control.execute_wfc(image=image, log_stats_to_output=True)