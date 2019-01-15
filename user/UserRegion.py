'''
Created on 2018.12.6

@author: Administrator
'''

from user import UserInfo
import re

class Region(UserInfo.Info):    
    def getSql(self, inputStr):
        searchObj = re.search( r'region.*?(?:is|are)\s*(.*?)\?$', inputStr, 0)
        if (searchObj == None):
            return None        
        return "match (u:user {region:\"" + searchObj.group(1) +"\"}) return u"
