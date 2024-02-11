import pandas as pd
from Data_Collecting import fieldnames # switch with Server_Data if needed
# from Server_Data import fieldnames,data

# we fetch the data from the csv file and request analysis for a specific time
start_time = pd.to_timedelta('16:07:35.078')
end_time = pd.to_timedelta('16:08:22.159')

def fetching_data(start_time,end_time):
    data = pd.read_csv('created_data/data.csv')
    data.columns = fieldnames
    data['input_watt'] = data['input_voltage'] * data['battery_current']
    data['RPM_Motor'] = data['rpm'] /5
    data['El_RPM'] = data['rpm'] /10
    # Convert the 'current_time' column to timedelta
    data['time'] = pd.to_timedelta(data['current_time'])
    # Select only the rows within the desired time range
    selected_data = data[(data['time'] >= start_time) & (data['time'] <= end_time)]

    return selected_data,data

if __name__ == '__main__':

    fetching_data(start_time,end_time)