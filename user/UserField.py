'''
Created on 2018.12.6

@author: Administrator
'''

from user import UserInfo
import re

class Field(UserInfo.Info):    
    def getSql(self, inputStr):
        searchObj = re.search( r'(?:good|well|skilled|talented)\s*(?:in|at|with)\s*(.*?)\?$', inputStr, 0)
        if (searchObj == None):
            return None        
        return "match (u:user {field:\"" + searchObj.group(1) +"\"}) return u"
