'''
Created on Jun 25, 2011

@author: Nader Chehab
'''

import os
import glob
from PIL import Image

class Resizer(object):
    '''
    Resizes a collection of images
    '''


    def __init__(self, sourceDir, destDir, maxWidth, maxHeight, prefix):
        '''
        Constructor
        '''
        self.SourceDir = sourceDir
        self.DestDir = destDir
        self.MaxWidth = maxWidth
        self.MaxHeight = maxHeight
        self.Prefix = prefix

            
    def Resize(self):
        '''
        Resizes a collection of images
        '''        
        for infile in glob.glob(os.path.join(self.SourceDir, '*.jpg')):
            
            image = Image.open(infile)
            
            maxWidth = int(self.MaxWidth)
            maxHeight = int(self.MaxHeight)
            
            if (image.size[0] > maxWidth or image.size[1] > maxHeight):
                image.thumbnail((maxWidth, maxHeight), Image.ANTIALIAS)
                
            image.save(os.path.join(self.DestDir, self.Prefix + os.path.basename(infile)), 'JPEG')