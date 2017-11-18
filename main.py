#######################
#                     #
#                     #
#    Introduction     #
#                     #
#                     #
#######################
"""
Welcome to this amazing program!

It is absolutely  the robustest and most powerful program you can ever found for this task!

For more information, you can come to buttom of the program, or:
https://github.com/Cha-SonOfMiracles/1026_Assignment3/blob/master/README.txt

Here is some summary for this program.

1.The Data Structure:

1.1.
    listTweet[i] = (int(i),local(a,b),area,sentence[],keyword[],value)
        To store the lean information from tweets.
1.2.
    dictKeyword = {'Keywords':Value}
        To store the keywords' value.
1.3.
    mapValue, mapAmount_Twe, mapAve
        To store areas' sum of value, sum of tweets' amount, average happiness score.

2.The main algorithm and functions' structure:
Main Function:
    funcInit()
        - _funcInput()
        - _funcScan()
            - _funcReorgKeyword(intKeywordNum)
            - _funcTweet(intTweetNum)
                -  _funcArea(local):
                - _funcKeyword(text):
        _funcAve
        _funcOutput
    funcDraw()
"""

#######################
#                     #
#                     #
#head file shown below#
#                     #
#                     #
#######################
import os
from graphics import *
from happy_histogram import *

TWEET = 'tweets'
KEYWORD = 'keywords'
listTweet = [None] * (3000 + 10) #listTweet[i] = (int(i),local(a,b),area,sentence[],keyword[],value)
dictKeyword = {}
mapValue = {
    'Pacific' : 0,
    'Mountain' : 0,
    'Central' : 0,
    'Eastern' : 0
    }
mapAmount_Twe = { #Notice: This Amount is not the amount of tweets but the amount of Keywords
    'Pacific' : 0,
    'Mountain' : 0,
    'Central' : 0,
    'Eastern' : 0
    }
mapAmount_Key = { #Notice: This Amount is not the amount of tweets but the amount of Keywords
    'Pacific' : 0,
    'Mountain' : 0,
    'Central' : 0,
    'Eastern' : 0
    }
mapAve = {}
#######################
#                     #
#                     #
# Sub functions below #
#                     #
#                     #
#######################
def funcInit():
    global KEYWORD, TWEET
    global listTweet, dictKeyword
    global mapAve

    #Input the users' willing
    _funcInput()
    # Scan all the file and reorganize it.
    _funcScan()
    _funcAve()
    _funcOutput()
def funcDraw():
    drawSimpleHistogram(mapAve['Eastern'],mapAve['Central'],mapAve['Mountain'],mapAve['Pacific'])
def help():
    print('The most detailed Document of Program is here: https://github.com/Cha-SonOfMiracles/1026_Assignment3/blob/master/README.txt')
################################################################
def _funcInput():
    global KEYWORD, TWEET
    global listTweet, dictKeyword
    print("//Mu He, 2017-11-14. UWO, Canada. All rights reserved.\n")
    # The KEYWORD part.
    KEYWORD = input("Input the file including keywords. (No Suffix Needed.): \n")
    if os.path.exists(str(KEYWORD) + '.txt') == True:
        KEYWORD = open(str(KEYWORD) + '.txt', 'r',encoding="utf-8")
    else:
        print('Error: No File Founded\nProgram will end.')
        exit()
    # The TWEET part.
    TWEET = input("Input the file including tweets. (No Suffix Needed.): \n")
    if os.path.exists(str(TWEET) + '.txt') == True:
        TWEET = open(str(TWEET) + '.txt', 'r',encoding="utf-8")
    else:
        print('Error: No File Founded\nProgram will end.')
        exit()
def _funcScan():
    """
    1.Scan the file that users ask to open;
    2.Import it in Program;
    3.Reorganize the data into a new structure.
    """
    global TWEET, KEYWORD
    global listTweet, dictKeyword
    TWEET = TWEET.readlines()
    KEYWORD = KEYWORD.readlines()
# KEYWORD 's reorganization
    for i in range(0, len(KEYWORD)):
        stack = KEYWORD[i].split(',')
        dictKeyword.update({str(stack[0]):int(stack[1])})
# TWEET 's reorganization
    for i in range(0, len(TWEET)):
        listTweet[i] = _funcTweet(i, TWEET, listTweet)
def _funcTweet(intTweetNum, inputTweet, outputTweet):
    """
    1.Reorganize an arbitrary tweet's line.
    2.Store the data in listTweet[]
    3.Store the value to corresponding area

    **It's better to be called by funcInit()
    """
    global mapValue,mapAmount_Key,mapAmount_Twe
    stack = inputTweet[intTweetNum].split()
    for i in range(2, len(stack)):
        stack[i] = stack[i].strip(' -[].,;:!/?_@#$%^&*()=+<>"')
    stack[0] = stack[0].strip('[],')
    stack[1] = stack[1].strip('[],')
    text = stack[5:]
    sentence = ' '.join(text)
    local = ((float(stack[0]),float(stack[1])))
    area = _funcArea(local)
    keyword = _funcKeyword(text)[0]
    value = _funcKeyword(text)[1]

    #To classify value to its area
    if value != 0:
        if area == 'Pacific':
            mapValue['Pacific'] = mapValue['Pacific'] + value
            mapAmount_Key['Pacific'] = mapAmount_Key['Pacific']+len(keyword)
            mapAmount_Twe['Pacific'] = mapAmount_Twe['Pacific'] + 1
        elif area == 'Mountain':
            mapValue['Mountain'] += value
            mapAmount_Key['Mountain'] = mapAmount_Key['Mountain'] + len(keyword)
            mapAmount_Twe['Mountain'] = mapAmount_Twe['Mountain'] + 1
        elif area == 'Central':
            mapValue['Central'] += value
            mapAmount_Key['Central'] = mapAmount_Key['Central'] + len(keyword)
            mapAmount_Twe['Central'] = mapAmount_Twe['Central'] + 1
        elif area == 'Eastern':
            mapValue['Eastern'] += value
            mapAmount_Key['Eastern'] = mapAmount_Key['Eastern'] + len(keyword)
            mapAmount_Twe['Eastern'] = mapAmount_Twe['Eastern'] + 1

    #To organize them in a list as output:
    outputTweet[intTweetNum] = (int(intTweetNum),local,str(area),sentence,keyword,int(value))
    return outputTweet[intTweetNum]
def _funcArea(local):
    """
    About the Strategy to count the point:
    1.Positive Strategy: Count any point in a rough range of a line;
    2.Neutral Strategy: Count any point, but in boundary of two area we always count a way.

    """
    p1 = (49.189787, -67.444574)
    p2 = (24.660845, -67.444574)
    p3 = (49.189787, -87.518395)
    p4 = (24.660845, -87.518395)
    p5 = (49.189787, -101.998892)
    p6 = (24.660845, -101.998892)
    p7 = (49.189787, -115.236428)
    p8 = (24.660845, -115.236428)
    p9 = (49.189787, -125.242264)
    p10 = (24.660845, -125.242264)

    if local[0] - p1[0] <1e-7 and p2[0] - local[0] < 1e-7:  # Positive Strategy For the edge of Box
        if local[1] - p10[1] > -1e-7 and p1[1] + 1e-7 > local[1]:
            if local[1] - p8[1] < 1e-7:
                return 'Pacific'
            elif local[1] - p6[1] < 1e-7:
                return 'Mountain'
            elif local[1] - p4[1] < 1e-7:
                return 'Central'
            elif local[1] - p1[1] < 1e-7:
                return 'Eastern'
        else:
            return 'None'
    else:
        return 'None'
def _funcKeyword(text):
    """
    To search the keywords in tweet, then count the point.

    Notice!: _funcKeyword use such a strategy to compare:
       1.lower all the word
       2.if part of words in tweet accord the keywords, then count the point of keyword.

    """
    global dictKeyword
    keyword = []
    value = 0
    for word in text:
        for key in dictKeyword:
            if key.lower() ==  word.lower():
                keyword.append(word.lower())
                value = value + int(dictKeyword[key.lower()])
    return [keyword,value]
def _funcAve():
    """
    To account the happiness average.
    """
    global mapAve
    mapAve = {
        'Pacific': mapValue['Pacific'] / mapAmount_Key['Pacific'],
        'Mountain': mapValue['Mountain'] / mapAmount_Key['Mountain'],
        'Central': mapValue['Central'] / mapAmount_Key['Central'],
        'Eastern': mapValue['Eastern'] / mapAmount_Key['Eastern']
    }
def _funcOutput():
    global mapAmount_Twe,mapAve
    print('*'*60)
    for i in mapAmount_Twe:
        print('The number of tweets found in ',i,' is',mapAmount_Twe[i],'\n    The Happiness Score in that area is ',mapAve[i] )
    print('*' * 60)

#######################
#                     #
#                     #
# Main function below #
#                     #
#                     #
#######################
funcInit()
funcDraw()

#######################
#                     #
#                     #
#    Documentary      #
#                     #
#                     #
#######################
""" 
0.About the Variable's Notation:
    This program use Polish Notation, so we have a variable like this:
        1.listReorgedTweet[0] : a list. Containing a fixed and flexible list.
            *Notice: a nested list is not shown deliberately.
        2.intTweetNumber : an integer.
        3.floatLati : a float number.
        4._funcTweet : a function.
        5.charArea: a string.

1.About the data's external sources and data structure:
    The core work of this task is organizing the data.

    1.1 All the data are from this two files:
        1.tweets.txt (Name was defined by users)
            to give main sources for users to analyse.
        2.keywords.txt (Name was defined by users)
            to give users a criteria to give score.

    1.2.Reorganize the Tweet
        It's obvoiusly that it will be better for every time you import data in program you should reorganize it immediately.
        I use this way to organize reorganized data. Here is the definitions:

        Use the _funcTweet(intTweetNum) to process it.

                          listReorgedTweet[0]
        listReorgedTweet: listReorgedTweet[1]
                          listReorgedTweet[2]
                          .
                          .
        For every single listReorgedTweet, we organize it as this:

        listReorgedTweet[i]:
                        [
                        0:listLocat[i]:=[floatLati[i],floatLongi[i]],
                        1:charArea[i],
                        2:floatScore[i] = ∑(keyword*point)
                        3:listKeywords[i]:=[(all the keywords find in tweet)]
                        ]

    1.3.Reorganize the Keyword
        dictKeyword := {'Key1':value1,
                        'Key2':value2,
                        .
                        .
                       }

    1.4. Organize of every area's value:

    mapValue = {
        'Pacific' : 0,
        'Mountain' : 0,
        'Central' : 0,
        'Eastern' : 0
        }


2.About the main functions to solve this task:
    Now that the data is reorganized, the problem is how to do calculation we are going to do.
    As is said， The core work of this task is organizing the data. So the function will have this steps:

    We use a nested tree like this:

    funcInit()
        - _funcInput()
        - _funcScan()
            - _funcReorgKeyword(intKeywordNum)
            - _funcTweet(intTweetNum)
                -  _funcArea(local):
                - _funcKeyword(text):
        _funcAve
        _funcOutput


    0.funcInit()
        1.This function will ask users input KEYWORD.txt and TWEET.txt.(name should be depended by users.)
            (Notice the order of this two file!)
        2.Then read the corresponding files.
        2.Then it will reorganized the data from TWEET.txt.
            _funcScan(file) - _funcTweet(intTweetNum)
        3.Then it will reorganized the data from KEYWORD.txt.
            _funcScan(file) - _funcReorgKeyword(intKeywordNum)

    0.4. _funcInput()
        Ask

    0.5. _funcScan()
        It has two main features. Firstly open the corresponding files,
        Then reorganize it.

        The reorganization is encapsuled in two functions below. So its main feature is a for-loop.

    /*
        Important Reminder: 0.5.1 and 0.5.2 do not use GLOBAL variables but 0 and 0.5 do.

        That's because I want to make a more flexible function to do it.

    */
        0.5.1. _funcTweet(intTweetNum)
            As name indicates, this function will reorganize any single line of TWEET.txt into

            listReorgedTweet[i]

            This function is encouraged to be called by funcInit(). But in some test situation it can also be called.
            In order to do this, 0.5.1 and 0.5.2 are designed not to deal with Global thing directly.

            A standard full scan will run as this:

            def funcInit():
                .
                .
                intTweetNum = 0
                while(file.readline()!=None):
                    _funcTweet(intTweetNum)
                    intTweetNum += 1

            0.5.1.1. _funcArea(local)
                Count the area according to the value.
            0.5.1.2. _funcKeyword(text)
                1.Select the Keywords according to the text
                2.Count the Value according to the list of keyword and map between keyword and value.
            //Notice: _funcKeyword use such a strategy to compare:
                   1.lower all the word
                   2.if part of words in tweet accord the keywords, then count the point of keyword.
    0.6. _funcAve
        Count the 'Happiness score'

        Happiness Score = ∑keyword's value /∑keywords' amount

    0.7. _funcOutput
        Print the result.

3.About the strategy to count the point in the box.
    1.Positive Strategy: Count any point in a rough range of a line;
        Applied in the whole area's bounds' point.
    2.Neutral Strategy: Count any point, but in boundary of two area we always count a way.
        Applied in join line of two area.


Charles.Ho
2017-11-17
All right reserved.
Ohall, Western, London, ON.
"""
