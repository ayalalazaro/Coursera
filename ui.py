# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 17:30:49 2014
@author: HAL
"""
try:
    from PySide import QtCore, QtGui
except ImportError:
    from PyQt4 import QtCore, QtGui

def gui_fname(dir=None):
    """Select a file via a dialog and returns the file name.
    """
    if dir is None: dir ='./'
    fname = QtGui.QFileDialog.getOpenFileName(None, "Select data file...", 
            dir, filter="All files (*)")
    return fname[0]