'''
Created on Jun 25, 2011

@author: Nader Chehab
'''
from GalleryGenerator import GalleryGenerator
from AppConfig import AppConfig

if __name__ == '__main__':
    
    # Read xml configuration file into an AppConfig object
    appConfig = AppConfig('GalleryGenerator.xml')
    
    # Create gallery generator according to configuration file
    galleryGenerator = GalleryGenerator(appConfig.SourceDir, appConfig.DestDir, 
                                 appConfig.MaxWidth, appConfig.MaxHeight, 
                                 appConfig.ThumbPrefix,
                                 appConfig.MaxThumbWidth, appConfig.MaxThumbHeight,
                                 appConfig.DoResize, appConfig.DoThumb,
                                 appConfig.GenerateHtml, appConfig.TemplatePath, appConfig.HtmlDestPath)
    
    # Generate gallery
    galleryGenerator.GenerateGallery()