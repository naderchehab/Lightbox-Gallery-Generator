'''
Created on Jun 25, 2011

@author: Nader Chehab
'''

import os
from Resizer import Resizer
from HtmlGenerator import HtmlGenerator

class GalleryGenerator(object):
    '''
    Generates a web gallery from folders of images and a template file
    '''


    def __init__(self, sourceDir, destDir, maxWidth, maxHeight, thumbPrefix, maxThumbWidth, maxThumbHeight, doResize, doThumb, generateHtml, templatePath, htmlDestPath):
        '''
        Constructor
        '''       
        self.SourceDir = sourceDir
        self.DestDir = destDir
        self.MaxWidth = maxWidth
        self.MaxHeight = maxHeight
        self.ThumbPrefix = thumbPrefix
        self.MaxThumbWidth = maxThumbWidth
        self.MaxThumbHeight = maxThumbHeight
        self.DoResize = doResize
        self.DoThumb = doThumb
        self.GenerateHtml = generateHtml
        self.TemplatePath = templatePath
        self.HtmlDestPath = htmlDestPath


    
    def GenerateGallery(self):
        '''
        Generates a web gallery from folders of images and a template file
        '''
        
        # create destination directories and copy resized images and thumbnails from source directory to destination directory
        if (self.DoResize == 'True' or self.DoThumb == 'True'):
            for node in os.listdir(self.SourceDir):
                if (os.path.isdir(os.path.join(self.SourceDir, node))):
                    
                    if (not os.path.exists(self.DestDir + "\\" + node)):
                        os.makedirs(os.path.join(self.DestDir, node))
                    
                    if (self.DoResize == 'True'):
                        # generate resized images
                        resizer = Resizer(os.path.join(self.SourceDir, node), os.path.join(self.DestDir, node), self.MaxWidth, self.MaxHeight, '')
                        resizer.Resize()
                    
                    if (self.DoThumb == 'True'):
                        # generate thumbnails
                        resizer = Resizer(os.path.join(self.SourceDir, node), os.path.join(self.DestDir, node), self.MaxThumbWidth, self.MaxThumbHeight, self.ThumbPrefix)
                        resizer.Resize()

        # generate html from tempalte file and folders of images                        
        if (self.GenerateHtml == 'True'):
            htmlGenerator = HtmlGenerator(self.TemplatePath, self.DestDir, self.ThumbPrefix, self.HtmlDestPath)
            htmlGenerator.GenerateHtml()
            
            
        