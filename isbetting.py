import requests,json,time,numpy,pyautogui,os
from columnar import columnar
from click import  style
# from sklearn import tree
import pandas as pd
# clf = tree.DecisionTreeClassifier()
import time
from fetchjs import *




##########____________Pyautogui,________________________



def quit_game(mes):
    import sys
    sys.exit(mes)
    
def calculate(moneys ):
    numbervnd100 = moneys//100
    moneys = moneys%100
    numbervnd50 = moneys//50
    moneys = moneys%50
    numbervnd10 = moneys//10 
    return numbervnd100,numbervnd50,numbervnd10

def get_index(name):
    confirm = input("Is {} in this position?".format(name))
    if confirm == "":
        print(pyautogui.position())
        return pyautogui.position()
    return None

def moveclick_and_moveclicks(index1,index2,number2):
    pyautogui.moveTo(index1)
    pyautogui.click()

    pyautogui.moveTo(index2)
    pyautogui.click(clicks = number2,interval=2 )

def bets():
    global predict,moneys,indexBIG,indexSMALL,indexVND10K,indexVND50K,indexVND100K
    if moneys == 0 or predict == None:
        return
    numbervnd100,numbervnd50,numbervnd10 = calculate(moneys)
    if predict == "BIG":
        index = indexBIG
    else:
        index = indexSMALL
    moveclick_and_moveclicks(indexVND100K,index,numbervnd100)
    moveclick_and_moveclicks(indexVND50K,index,numbervnd50)
    moveclick_and_moveclicks(indexVND10K,index,numbervnd10)


##########____________API________________________


def make_predict():
    global predict
    lastjs = get_the_last_json()
    betTypeResult = get_betTypeResult(lastjs)
    predict = betTypeResult.split(",")[0]
    print(predict)



##########____________DRAW________________________




def is_ended():
    timeBetCountdown =  get_timeBetCountdown(get_json_1())
    time.sleep(timeBetCountdown)
    return True
def is_betting():
    while True:
        timeBetCountdown =  get_timeBetCountdown(get_json_1())
        if timeBetCountdown>=30:
            return True
        else:
            time.sleep(1)


###########################



try:
    moneys = int(input("moneys: "))
    indexBIG = get_index("BIG")
    indexSMALL = get_index("SMALL")
    indexVND10K = get_index("VND10K")
    indexVND50K = get_index("VND50K")
    indexVND100K = get_index("VND100K")
except:
    moneys = 0


predict = None
time.sleep(get_timeBetCountdown(get_json_1()))


while True:
    if is_ended():
        if is_betting():
            make_predict()
            bets()
            time.sleep(get_timeBetCountdown(get_json_1()))


