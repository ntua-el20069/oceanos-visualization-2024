import pandas as pd
import numpy as np
from Demands import *

selected_data,data = fetching_data(start_time,end_time) 

def max_min_values(time_values,limit):
    # Calculate the maximum values for each fieldname
    if limit == 'max':
        max_elements = time_values.max()
    elif limit == 'min':
        max_elements = time_values.min()
    else :
        print('Invalid Argument')
        return

    max_times = {}

    # calclulate the time each max value occurred
    for field in data.columns:
        try:
            # Find the time range where the value of the field is always greater than 95% of its maximum value
            greater_than_threshold = time_values[field] > 0.99 * max_elements[field]
            start_time = time_values.loc[greater_than_threshold, 'time'].min()
            end_time = time_values.loc[greater_than_threshold, 'time'].max()

            max_times[field] = (start_time, end_time-start_time)
        except:
            max_times[field] = ("N/A", "N/A")

    # Create a DataFrame with fieldnames and their corresponding maximum values
    max_df = pd.DataFrame({"Fieldname": data.columns, "Max Value": max_elements})

    # Add max_times as the third column "Max Time"
    max_df["Max Time"] = max_df["Fieldname"].map(lambda x: max_times[x][0])

    # Add max_times as the fourth column "Duration"
    max_df["Duration"] = max_df["Fieldname"].map(lambda x: max_times[x][1])

    max_df.to_csv(f"results/{limit}_values.csv", index=False)
    return max_df

if __name__ == '__main__':

    max_min_values(selected_data,'max') # if you want to check all data switch selected_data with data
    # max_min_values(selected_data,'min')