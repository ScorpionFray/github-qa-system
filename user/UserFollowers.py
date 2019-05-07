'''
Created on 2018年12月11日

@author: Administrator
'''

from user import UserInfo
import re
from re import search

class Followers(UserInfo.Info):    
    def getSql(self, inputStr):
        searchObj = re.search( r'(?:followers|follower).*?([0-9]*?)\?$', inputStr, 0)
        if (searchObj != None and len(searchObj.group(1)) > 0):
            return "match (u:user) where u.followers>=" + searchObj.group(1) +" return u"

        searchObj = re.search( r'([0-9]*?)\s* (?:followers|follower)\?$', inputStr, 0)
        if (searchObj != None and len(searchObj.group(1)) > 0):
            return "match (u:user) where u.followers>=" + searchObj.group(1) +" return u"
        return None  