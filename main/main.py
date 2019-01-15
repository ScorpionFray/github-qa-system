'''
Created on 2018.12.6

@author: gym
'''

from user import GetUserSql

from py2neo import Graph,Node,Relationship



def getSql(inputStr):
    inputStr.lower()
    resSql = GetUserSql.getUserSql(inputStr) 
    if resSql != None:
        return resSql
    return None


'''
graph_test = Graph(
    "http://localhost:11003",
    username="neo4j",
    password="1234"
)
''' 

allQ = ["I want to know who's names    are bob?"
        , "tell me who's email is 7@nju.edu.cn?"
        , "whose region is bj?"
        , "who is good at java?"
        , "who has repositories more than 500?"
        , "who has 100 repository?"
        , "who has more than 50 stars?"
        , "who has 100 followers?"
        #, "who following 10 users?"    #出错 识别不出后面的users
        , "who has 10 following?"
        ]
for q in allQ:
    resSql = getSql(q)
    print(resSql)
    #resSql = "match (n:user{name:'Bob'}) return n"
    '''
    test_node = graph_test.evaluate(resSql) 
    test_node = graph_test.run(resSql).data()
    if (len(test_node)>0) :
        print(test_node[0])
    '''

