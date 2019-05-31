# Plot
import matplotlib
import matplotlib.pyplot as plt
import math
import numpy as np

# GIF
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage

from tools import create_time_serie, cos_sum, tabulate, get_time_series
from gramian_angular_field import transform

# Jupyter
# %matplotlib inline

# Global iteration
iteration = 0

if __name__ == "__main__":

    time_serie = get_time_series()
    size_time_serie = time_serie.size
    gaf, phi, r, scaled_time_serie = transform(time_serie)

    ax = plt.subplot(111)
    plt.imshow(gaf)
    plt.show()
