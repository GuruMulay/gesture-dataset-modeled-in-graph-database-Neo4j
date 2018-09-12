import Tkinter as Tk
from Widgets import *

class View():
    def __init__(self, master):
        self.menubar = MenuBar(master)
        self.layout = Window(master)
        #self.sidepanel = LabelFrames(master)
