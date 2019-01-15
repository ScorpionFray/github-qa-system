'''
Created on 2018年12月11日

@author: Administrator
'''

from repository import repository_contributor
from repository import repository_fork
from repository import repository_language
from repository import repository_name
from repository import repository_star
from repository import repository_watch

import re

def get_sql(input_str):
    if re.search("repository|repositories", input_str, 0)  == None:
        return None
    
    allInfo = [repository_contributor.Contributor(), repository_fork.Fork(), repository_language.Language(), repository_name.Name(), repository_star.Star(), repository_watch.Watch()]
    for info in allInfo:
        resSql = info.get_sql(input_str)
        if resSql != None:
            return resSql
    return None