'''
Created on 2018.12.6

@author: Administrator
'''

from user import UserInfo
import re

class Email(UserInfo.Info):    
    def getSql(self, inputStr):
        searchObj = re.search( r'(?:e-mail|email).*?(?:is|are)\s*(.*?)\?$', inputStr, 0)
        if (searchObj == None):
            return None        
        return "match (u:user {email:\"" + searchObj.group(1) +"\"}) return u"