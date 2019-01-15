'''
Created on 2018.12.6

@author: Administrator
'''

from user import UserInfo
import re

class Name(UserInfo.Info):    
    def getSql(self, inputStr):
        searchObj = re.search( r'name.*?(?:is|are)\s*(.*?)\?$', inputStr, 0)
        if (searchObj == None):
            return None        
        return "match (u:user {name:\"" + searchObj.group(1) +"\"}) return u"

