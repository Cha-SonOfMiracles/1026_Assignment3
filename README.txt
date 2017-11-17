Document: Explanation and Justification.

0.About the Variable's Notation:
    This program use Polish Notation, so we have a variable like this:
        1.listReorgedTweet[0] : a list. Containing a fixed and flexible list.
            *Notice: a nested list is not shown deliberately.
        2.intTweetNumber : an integer.
        3.floatLati : a float number.
        4.funcReorgTweet : a function.
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

        Use the _funcReorgTweet(intTweetNum) to process it.

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




2.About the main functions to solve this task:
    Now that the data is reorganized, the problem is how to do calculation we are going to do.
    As is said， The core work of this task is organizing the data. So the function will have this steps:

    We use a nested tree like this:

    funcInit()
        - _funcInput()
        - _funcScan()
            - _funcReorgKeyword(intKeywordNum)
            - _funcReorgTweet(intTweetNum)
                -  _funcArea(local):

                - _funcKeyword(text):

                - _funcValue(keyword):


    0.funcInit()
        1.This function will ask users input KEYWORD.txt and TWEET.txt.(name should be depended by users.)
            (Notice the order of this two file!)
        2.Then read the corresponding files.
        2.Then it will reorganized the data from TWEET.txt.
            _funcScan(file) - _funcReorgTweet(intTweetNum)
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

    0.5.1. _funcReorgTweet(intTweetNum)
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
                funcReorgTweet(intTweetNum)
                intTweetNum += 1

        0.5.1.1. _funcArea(local)
            Count the area according to the value.
        0.5.1.2. _funcKeyword(text)
            Select the Keywords according to the text
        0.5.1.3. _funcValue(keyword, map)
            Count the Value according to the list of keyword and map between keyword and value.

    0.5.2. _funcReorgKeyword(intKeywordNum)
         As name indicates, this function will reorganize any single line of KEYWORDS.txt into

         listReorgedKeyword[i]



