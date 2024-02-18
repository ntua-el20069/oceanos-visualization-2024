import pandas as pd
import numpy as np
import time

def readCSV(csv_url, fieldnames, realTime = True, delay = 1.0) -> dict:
    data = pd.read_csv(csv_url, delimiter=',')  # diabazw to arxeio
    ######## Random Index for Demo
    frequency = 1 / delay
    index = -1 if realTime else int(frequency * time.time()) % len(data)  

    #print(f"\nIndex is: ########################      ######################  {counter}\n")
    # ftiaxnw dianysma me tis times apo thn teleytaia seira tou arxeiou
    data1 = np.array(data.iloc[index].values)    #### CHANGE !!!!! counter to -1 for real time last data

    #print(str(data1.size)+"---------------------------------------------------")
    # bazw se ka8e metablhth thn antistoixh timh apo to panw dianusma se morfh str gia na emfanizetai sthn o8onh swsta
    ### Return Dictionary with data now
    return {label : str(x) for label, x in zip(fieldnames, data1)}

def MEBC_data_from_total(data: dict, team_token: str) -> dict:
    return {
        "temp1": data["battery_temperature"],
        "voltage" : data["battery_voltage"],
        "current": data["battery_current"],
        "lat" : data["latitude"],
        "lon" : data["longitude"],
        "team" : team_token
    }