import fetchjs as fet
import pandas as pd

# dataframe = pd.DataFrame(fet.get_json_150())
# dataframe_short = dataframe[["id","startAt","endAt","startAtDate","endAtDate","dealerName","roundCode","resultRaw","betTypeResult"]]

def get_id(js):
    return int(js["id"])

def get_resultRaw(js):
    if "resultRaw" in js:
        return js["resultRaw"]
    return ""

def get_betTypeResult(js):
    if "betTypeResult" in js:
        return js["betTypeResult"]
    return ""

def get_status(js):
    return js["status"]

def get_timeBetCountdown(js):
    return js["timeBetCountdown"]
def get_dealerName(js):
    return js["dealerName"]
def get_the_last_json():

    return get_json_150()[1]

def get_xxx(js):
    resultRaw = get_resultRaw(js)
    return int(resultRaw[0]),int(resultRaw[2]),int(resultRaw[4])
def get_type(js):
    betTypeResult = get_betTypeResult(js)
    return betTypeResult.split(",")[0],betTypeResult.split(",")[1]
js150 = fet.get_json_150()


def get_info(js):
    idgame = get_id(js)


print(get_type(js150[-1]))