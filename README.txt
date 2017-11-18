Document: Explanation and Justification.

Revison：
    1.No '_funcReorgKeyword(intKeywordNum)' any more.

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
