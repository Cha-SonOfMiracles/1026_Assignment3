#######################
#                     #
#                     #
# head file shown here#
#                     #
#                     #
#######################
import os

TWEET = 'None.txt'
KEYWORD = 'None.txt'
listTweet = [None] * (3000 + 10)
dictKeyword = {}


#######################
#                     #
#                     #
# Sub functions below #
#                     #
#                     #
#######################

################################################################
def funcInit():
    global KEYWORD, TWEET
    global listTweet, dictKeyword
    #Input the users' willing
    _funcInput()
    # Scan all the file and reorganize it.
    _funcScan()


################################################################
def _funcInput():
    global KEYWORD, TWEET
    global listTweet, dictKeyword
    # The KEYWORD part.
    KEYWORD = input("Input the file including keywords (Notice: No Suffix Needed): ")
    if os.path.exists(str(KEYWORD) + '.txt') == True:
        KEYWORD = open(str(KEYWORD) + '.txt', 'r')
    else:
        print('Error: No File Founded\nProgram will end.')
        exit()
    # The TWEET part.
    TWEET = input("Input the file including tweets (Notice: No Suffix Needed): ")
    if os.path.exists(str(TWEET) + '.txt') == True:
        TWEET = open(str(TWEET) + '.txt', 'r')
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
        listTweet[i] = _funcReorgTweet(i, TWEET, listTweet)

# def _funcReorgKeyword(intKeywordNum, inputKeyword, outputKeyword):
#     """
#     Reorganize an arbitrary keyword's line.
#     Store the data in dictKeyword[]
#     It's better to be called by funcInit()
#     """
#     inputword = inputKeyword[intKeywordNum].split()
#     outputKeyword[intKeywordNum] = \
#         outputKeyword[intKeywordNum].update({inputword[0]:inputword[1]})
#     return outputKeyword[intKeywordNum]

def _funcReorgTweet(intTweetNum, inputTweet, outputTweet):
    """
    Reorganize an arbitrary tweet's line.
    Store the data in listTweet[]
    It's better to be called by funcInit()
    """
    stack = inputTweet[intTweetNum].split()
    stack[0] = stack[0].strip('[,]')
    stack[1] = stack[1].strip('[,]')
    text = []
    text = stack[5:]
    area = 'Area: Pending'
    value = -1
    keyword = ['Key: Pending']

# def _funcArea(local):
#
# def _funcKeyword(text):
#
# def _funcValue(keyword):

    outputTweet[intTweetNum] = (int(intTweetNum),(float(stack[0]),float(stack[1])),area,' '.join(text),keyword,float(value))
    return outputTweet[intTweetNum]

def _funcArea(local):
    return
def _funcKeyword(text):
    return
def _funcValue(keyword, map):
    return

################################################################



#######################
#                     #
#                     #
# Main function below #
#                     #
#                     #
#######################

funcInit()
# for i in dictKeyword:
#     print(i)
print(listTweet)
print(dictKeyword)

print("\n\nMain Function Successfully works.")
