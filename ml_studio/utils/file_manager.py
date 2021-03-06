# %%
# =========================================================================== #
#                                FILE MANAGER                                 #
# =========================================================================== #
import os
import time

from matplotlib import animation, rc
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.offline as py

from  ml_studio.utils.misc import snake

def save_fig(fig, directory, filename):
    if os.path.exists(directory):
        path = os.path.join(os.path.abspath(directory), filename)
        fig.savefig(path, facecolor='w', bbox_inches=None)
    else:
        os.makedirs(directory)
        path = os.path.join(os.path.abspath(directory),filename)
        fig.savefig(path, facecolor='w', bbox_inches=None)

def save_gif(ani, directory, filename, fps):
    face_edge_colors = {'facecolor': 'w', 'edgecolor': 'w'}
    path = os.path.join(os.path.abspath(directory), filename)
    if os.path.exists(directory):
        ani.save(path, writer='imagemagick', fps=fps, savefig_kwargs = face_edge_colors)
    else:
        os.makedirs(directory)                
        ani.save(path, writer='imagemagick', fps=fps, savefig_kwargs = face_edge_colors)

def save_csv(df, directory, filename):
    path = os.path.join(os.path.abspath(directory), filename)
    if os.path.exists(directory):
        df.to_csv(path, index=False)
    else:
        os.makedirs(directory)                
        df.to_csv(path, index=False)

def save_numpy(a, directory, filename):
    path = os.path.join(os.path.abspath(directory), filename)
    if os.path.exists(directory):
        np.save(file=path, arr=a)
    else:
        os.makedirs(directory)                
        np.save(file=path, arr=a)

def save_plotly(a, directory, filename):
    path = os.path.join(os.path.abspath(directory), filename)
    if os.path.exists(directory):
        py.plot(a, filename=path, auto_open=False, include_mathjax='cdn')
    else:
        os.makedirs(directory)                
        py.plot(a, filename=path, auto_open=False, include_mathjax='cdn')

def get_filename(instance, fileext, element=None):
        """Creates a standard format filename for saving plots."""    

        # Obtain user id, class name and date time 
        project = "ml_studio_"        
        userhome = os.path.expanduser('~')          
        username = os.path.split(userhome)[-1] + "_"
        clsname = instance.__class__.__name__ + "_"
        if element:
            element = element + "_"
        else:
            element = ""
        timestr = time.strftime("%Y%m%d-%H%M%S")
        # Snake case format filename
        filename = project + username + clsname + element + timestr + fileext
        filename = snake(filename)        
        return filename

