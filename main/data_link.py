from user import GetUserSql
import ResStruct
from py2neo import Graph,Node,Relationship,NodeMatcher
import pandas as pd
import pickle
from user import UserStruct

def getSql(inputStr):
    inputStr.lower()
    resSql = GetUserSql.getUserSql(inputStr)
    if resSql != None:
        return resSql
    return None


    "http://localhost:7474",

graph_test = Graph(
    username="neo4j",
    password="12345"
)

'''
allQ = ["I want to know who's names    are bob?"
        , "tell me who's email is 7@nju.edu.cn?"
        , "whose region is bj?"
        , "who is good at java?"0.
        , "who has repositories more than 500?"
        , "who has 100 repository?"
        , "who has more than 50 stars?"
        , "who has 100 followers?"
        #, "who following 10 users?"    #出错 识别不出后面的users
        , "who has 10 following?"
        ]
'''
def send_to(q,hp):
    resSql = getSql(q)
    print(resSql)
    test_node = graph_test.evaluate(resSql)
    test_node = graph_test.run(resSql).data()
    result = result_input(test_node)
    #print("homepage=",ResStruct.res_storage.homepage)
    if ResStruct.res_storage.homepage != '':
        hp.append(ResStruct.res_storage.homepage)
    return result

def result_input(input_res):
    if (len(input_res)>0):
        ResStruct.res_storage=UserStruct.User(str(input_res[0]))
        #print("homepage=",ResStruct.res_storage.homepage)
        return ResStruct.res_storage.ans_phase()
    else:
        #ResStruct.res_storage.clean()
        return "Can't find answer"