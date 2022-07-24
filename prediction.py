import fetchjs as fet
import pandas as pd
import numpy

from sklearn import tree
clf = tree.DecisionTreeClassifier()

# dataframe = pd.DataFrame(fet.get_json_150())
# dataframe_short = dataframe[["id","startAt","endAt","startAtDate","endAtDate","dealerName","roundCode","resultRaw","betTypeResult"]]


def make_predict():

    js150 = fet.get_json_150()

    dataframe = pd.DataFrame(js150)
    dataframe.sort_values('id', ascending=True,inplace=True)

    dataframe_short = dataframe[["id","startAtDate","endAtDate","dealerName","roundCode","betTypeResult"]]
    dealerNameList = [dealer for dealer in set(dataframe_short["dealerName"])]

    dataframe_short = dataframe_short.values 

    for record in dataframe_short:
        record[3] = dealerNameList.index(record[3])
        record[4] = int(record[4])

    data = dataframe_short[0:len(dataframe_short)-1]
    # print(data)
    label = data[:,5]#done
    data = data[:,0:5]
    # print(data)
    test = dataframe_short[-1]
    test = [test[0:len(test)-1]] #done


    clf.fit(data,label)
    prd = clf.predict(test)[0]
    if "BIG" in prd:
        return "BIG"
    return "SMALL"