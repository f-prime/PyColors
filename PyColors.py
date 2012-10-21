#!/usr/bin/python env
#PyColors is a module that makes it easier to use Terminal and CMD colors.
#Version 1.0

import sys, os

class windows():
  def __init__(self):
    self.colors = {'black':'0', 'blue':'1', 'green':'2', 'aqua':'3', 'red':'4','purple':'5','yellow':'6','white':'7','gray':'8','light_blue':'9','light_green':'a','light_aqua':'b','light_red':'c','light_purple':'d','light_yellow':'e','bright_white':'f'}
  def color(self, textcolor=None, background=None):
    coloring = "color {0}{1}".format(self.colors[textcolor], self.colors[background])
    os.system(coloring)

class linux():
  def __init__(self):
    self.colors = {"grey":'30',"red":'31', "green":'32',"yellow":'33',"blue":'34', 'magenta':'35','cyan':'36', 'white':'37'}
    self.other = {"bold":'1', 'dark':'2','underline':'4', 'highlight':'7', 'hide':'8'}
    self.highlights = {"grey":'40','red':41,'green':'42','yellow':'43','blue':'44','magenta':'45','cyan':'46', 'white':'47'}
  def color(self, color=None, highlight=None, text=None, other=None):
    if color:
      text = "\033[{0}m{1}".format(self.colors[color], text)
    if highlight:
      text = "\033[{0}m{1}".format(self.highlights[highlight], text)
    if other:
      text = "\033[{0}m{1}".format(self.other[other], text)
    return text + "\033[0m"



