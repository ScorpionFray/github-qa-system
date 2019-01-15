'''
Created on 2018年12月6日

@author: Administrator
'''

from user import UserInfo
from user import UserName
from user import UserEmail
from user import UserRegion
from user import UserField
from user import UserRepositories
from user import UserStars
from user import UserFollowers
from user import UserFollowing

import re

def getUserSql(inputStr):
    if re.search("who|user", inputStr, 0)  == None:
        return None
    
    #print("question is about user")
    allInfo = [UserName.Name(), UserEmail.Email(), UserRegion.Region(), UserField.Field(), UserRepositories.Repositories(), UserStars.Stars(), UserFollowers.Followers(), UserFollowing.Following()]
    for info in allInfo:
        resSql = info.getSql(inputStr)
        if resSql != None:
            return resSql
    return None