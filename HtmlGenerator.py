'''
Created on Jun 25, 2011

@author: Nader Chehab
'''

import os
import re

class HtmlGenerator(object):
    '''
    Generates an Html gallery according to a template file and folders of images
    '''


    def __init__(self, templatePath, imagesRootPath, thumbPrefix, htmlDestPath):
        '''
        Constructor
        '''
        self.TemplatePath = templatePath
        self.ImagesRootPath = imagesRootPath
        self.ThumbPrefix = thumbPrefix
        self.HtmlDestPath = htmlDestPath
        
        
    def GenerateHtml(self):
        '''
        Generates an Html gallery according to a template file and folders of images
        '''
        
        galleryList = ''
        
        file = open(self.TemplatePath)
        template = file.read()       
        
        galleryRegexPattern = '\$GalleryBegin(.*)\$GalleryEnd'
        imageItemRegexPattern = '\$ImageItemBegin(.*)\$ImageItemEnd'
        
        # precompile the regexes for performance
        galleryRegex = re.compile(galleryRegexPattern,re.MULTILINE|re.DOTALL)
        imageItemRegex = re.compile(imageItemRegexPattern,re.MULTILINE|re.DOTALL)
        
        # extract the gallery section
        galleryTemplate = galleryRegex.search(template).groups()[0]
        
        # extract the image section
        imageItemTemplate = imageItemRegex.search(galleryTemplate).groups()[0]
                                
        # for each folder, create a gallery
        for dir in os.listdir(self.ImagesRootPath):
            if (os.path.isdir(os.path.join(self.ImagesRootPath, dir)) and dir != 'css' and dir != 'js' and dir != 'images'):
                # replace the gallery title and gallery id by the folder name
                gallery = galleryTemplate.replace('$GalleryTitle', dir)
                gallery = gallery.replace('$GalleryId', dir.replace(' ', ''))
                                
                imageItemList = ''
                
                # for each image in the folder, add it to the gallery section
                for file in os.listdir(os.path.join(self.ImagesRootPath, dir)):
                    filepath = os.path.join(self.ImagesRootPath, dir, file)
                    if (os.path.isfile(filepath) and file.endswith('.jpg') and not file.startswith(self.ThumbPrefix)):
                        imageItem = imageItemTemplate.replace('$ImagePath', os.path.join(self.ImagesRootPath, dir, file))
                        imageItem = imageItem.replace('$ThumbPath', os.path.join(self.ImagesRootPath, dir, self.ThumbPrefix + file))
                        imageItemList = imageItemList + imageItem
            
                gallery = re.sub(imageItemRegexPattern, imageItemList.replace('\\', '\\\\'), gallery, 0, re.MULTILINE|re.DOTALL)
                galleryList = galleryList + gallery
            
        html = re.sub(galleryRegexPattern, galleryList.replace('\\', '\\\\'), template, 0, re.MULTILINE|re.DOTALL)
        
        file = open(self.HtmlDestPath, mode='w')
        file.write(html)
            
                            
                        
                

        