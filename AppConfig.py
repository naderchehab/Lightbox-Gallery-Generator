'''
Created on Jun 25, 2011

@author: Nader Chehab
'''

import xml.etree.ElementTree as etree

class AppConfig(object):
    '''
    Reads the xml configuration file into the AppConfig object
    '''

    def __init__(self, configFilePath):
        '''
        Constructor
        '''
        tree = etree.parse(configFilePath)
        root = tree.getroot()
        
        self.SourceDir = root.findtext('SourceDir')
        self.DestDir = root.findtext('DestDir')
        self.MaxWidth = root.findtext('MaxWidth')
        self.MaxHeight = root.findtext('MaxHeight')
        self.ThumbPrefix = root.findtext('ThumbPrefix')
        self.MaxThumbWidth = root.findtext('MaxThumbWidth')
        self.MaxThumbHeight = root.findtext('MaxThumbHeight')
        self.DoResize = root.findtext('DoResize')
        self.DoThumb = root.findtext('DoThumb')
        self.TemplatePath = root.findtext('TemplatePath')
        self.GenerateHtml = root.findtext('GenerateHtml')
        self.HtmlDestPath = root.findtext('HtmlDestPath')
