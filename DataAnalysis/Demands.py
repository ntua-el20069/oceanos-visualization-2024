import pandas as pd
import os

def fetching_data(start_time,end_time, fieldnames, csv_relative_url):
    data = pd.read_csv(csv_relative_url)
    data.columns = fieldnames
    data['input_watt'] = data['input_voltage'] * data['battery_current']
    data['RPM_Motor'] = data['rpm'] /5
    data['El_RPM'] = data['rpm'] /10
    # Convert the 'current_time' column to timedelta
    data['time'] = pd.to_timedelta(data['current_time'])
    # Select only the rows within the desired time range
    selected_data = data[(data['time'] >= start_time) & (data['time'] <= end_time)]

    return selected_data,data

