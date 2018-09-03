# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 14:36:35 2018

@author: z3525552
"""


def css_styling(filename):
    """This function is use for modifying the Jupyter notebook default css 
    properties. Input is filename and return modified version of css styling
    properties as specified in the filename.
    
    Parameters
    ----------
    filename : str
             local or remote host filename
    
    Returns
    -------
    styles : html
             css properties of html file 
    """
    
    
    from IPython.core.display import HTML
    
    styles = open(filename, 'r').read()
    
    return HTML(styles)
