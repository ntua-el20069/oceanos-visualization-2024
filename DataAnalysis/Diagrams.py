import pandas as pd
import numpy as np
import plotly.express as px
from Demands import *
from Data_Analysis import max_min_values
from plotly.subplots import make_subplots
import plotly.graph_objs as go


def plotting_values(time_values,field,type):

    # Plot with color based on the condition
    if type == 'scatter':
        fig = px.scatter(time_values, x='current_time', y=field, title=field)
    elif type == 'line':
        fig = px.line(time_values, x='current_time', y=field, title=field)
    else: 
        print('Invalid Argument')
        return

    # To save the plot as an HTML file
    fig.write_html(f'diagrams/{type}/{field}.html')

def current_with_temp(time_values):

    for field in ['motor_tempMotor','motor_tempMosfet']:
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        # Add traces
        fig.add_trace(
            go.Scatter(x=time_values.current_time, y=time_values.motor_current,mode='markers', name="motor_current"),
            secondary_y=False,
        )

        fig.add_trace(
            go.Scatter(x=time_values.current_time, y=time_values[field],mode='markers', name=field),
            secondary_y=True,
        )

        # Add figure title
        fig.update_layout(
            title_text=f"Motor Current with {field}"
        )

        # Set x-axis title
        fig.update_xaxes(title_text="time")

        # Set y-axes titles
        fig.update_yaxes(title_text="<b>Motor Current</b>", secondary_y=False)
        fig.update_yaxes(title_text=f"<b>{field}</b>", secondary_y=True)

        fig.write_html(f'diagrams/current_with_temp/motor_current_with_{field}.html')

def current_with_temp2(start_time,end_time):

    selected_data,data = fetching_data(start_time,end_time)

    for field in ['motor_tempMotor','motor_tempMosfet']:
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        # Add traces
        fig.add_trace(
            go.Scatter(x=selected_data.current_time, y=selected_data.motor_current,mode='markers', name="motor_current"),
            secondary_y=False,
        )

        fig.add_trace(
            go.Scatter(x=selected_data.current_time, y=selected_data[field],mode='markers',marker=dict(color='green'), name=field),
            secondary_y=True,
        )
        # Add max point and annotations
        max_df = max_min_values(selected_data, 'max')
        max_point_time = max_df[max_df['Fieldname'] == field]['Max Time'].iloc[0]
        max_point_value = max_df[max_df['Fieldname'] == field]['Max Value'].iloc[0]
        duration = max_df[max_df['Fieldname'] == field]['Duration'].iloc[0]

        try: 
            max_point_time_timestamp = selected_data.index[selected_data['time'] == max_point_time][0]
            time = selected_data.current_time[max_point_time_timestamp]
            fig.add_trace(go.Scatter(x=[time], y=[max_point_value], mode='markers', marker=dict(color='red'), name='Max Point'), secondary_y=True)
            fig.add_annotation(x=max_point_time_timestamp, y=max_point_value, text=f'Max Value: {max_point_value}', showarrow=True, arrowhead=1, ax=0, ay=-40)
            fig.add_annotation(x=max_point_time_timestamp, y=max_point_value, text=f'Time: {max_point_time}', showarrow=True, arrowhead=1, ax=0, ay=-60)
            fig.add_annotation(x=max_point_time_timestamp, y=max_point_value, text=f'Duration: {duration}', showarrow=True, arrowhead=1, ax=0, ay=-80)
        except Exception as e:
            print(f"Error occurred: {e}")

        # Add figure title
        fig.update_layout(
            title_text=f"Motor Current with {field}"
        )

        # Set x-axis title
        fig.update_xaxes(title_text="time")

        # Set y-axes titles
        fig.update_yaxes(title_text="<b>Motor Current</b>", secondary_y=False)
        fig.update_yaxes(title_text=f"<b>{field}</b>", secondary_y=True)

        fig.write_html(f'diagrams/current_with_temp/motor_current_with_{field}.html')

def statistics_plots(start_time,end_time,field,type):
    
    selected_data,data = fetching_data(start_time,end_time)
    '''Here you make the plot depending on the  start_time -> end_time   time duration,
     you should make an html written like {field}.html that includes 
     plot time-field, max value and time obtained, min value and time obtained, duration,...'''
    # Plot with color based on the condition
    if type == 'scatter':
        fig = px.scatter(selected_data, x='current_time', y=field, title=field)
        # Add max point with a different color
        max_df = max_min_values(selected_data,'max')
        max_point_time = max_df[max_df['Fieldname'] == field]['Max Time'].iloc[0]
        max_point_value = max_df[max_df['Fieldname'] == field]['Max Value'].iloc[0]
        duration = max_df[max_df['Fieldname'] == field]['Duration'].iloc[0]
        try: 
            max_point_time_timestamp = selected_data.index[selected_data['time'] == max_point_time][0]
            time = selected_data.current_time[max_point_time_timestamp]
            max_point = {'current_time': [time], f'{field}': [max_point_value]}
            fig.add_trace(px.scatter(max_point, x='current_time', y=field, color_discrete_sequence=['red']).data[0])
            fig.add_annotation(x=max_point_time_timestamp, y=max_point_value, text=f'Max Value: {max_point_value}', showarrow=True, arrowhead=1, ax=0, ay=-40)
            fig.add_annotation(x=max_point_time_timestamp, y=max_point_value, text=f'Time: {max_point_time}', showarrow=True, arrowhead=1, ax=0, ay=-60)
            fig.add_annotation(x=max_point_time_timestamp, y=max_point_value, text=f'Duration: {duration}', showarrow=True, arrowhead=1, ax=0, ay=-80)
        except:
            pass
    elif type == 'line':
        fig = px.line(selected_data, x='current_time', y=field, title=field)
        # Add max point with a different color
        max_df = max_min_values(selected_data,'max')
        max_point_time = max_df[max_df['Fieldname'] == field]['Max Time'].iloc[0]
        max_point_value = max_df[max_df['Fieldname'] == field]['Max Value'].iloc[0]
        duration = max_df[max_df['Fieldname'] == field]['Duration'].iloc[0]
        try: 
            max_point_time_timestamp = selected_data.index[selected_data['time'] == max_point_time][0]
            time = selected_data.current_time[max_point_time_timestamp]
            max_point = {'current_time': [time], f'{field}': [max_point_value]}
            fig.add_trace(px.scatter(max_point, x='current_time', y=field, color_discrete_sequence=['red']).data[0])
            fig.add_annotation(x=max_point_time_timestamp, y=max_point_value, text=f'Max Value: {max_point_value}', showarrow=True, arrowhead=1, ax=0, ay=-40)
            fig.add_annotation(x=max_point_time_timestamp, y=max_point_value, text=f'Time: {max_point_time}', showarrow=True, arrowhead=1, ax=0, ay=-60)
            fig.add_annotation(x=max_point_time_timestamp, y=max_point_value, text=f'Duration: {duration}', showarrow=True, arrowhead=1, ax=0, ay=-80)
        except:
            pass
    else: 
        print('Invalid Argument')
        return

    # To save the plot as an HTML file
    fig.write_html(f'diagrams/statics/{type}/{field}.html')


if __name__ == '__main__':

    # if you don't want all data but just a single plot comment the for loop and place on field the value you wish
    # to make lines instead of dots replace 'scatter' with 'line'
    # for field in data.columns: 
    #    plotting_values(selected_data,field,'scatter')

    # plots motor current with the corresponding temperatures
    # current_with_temp2(start_time,end_time)

    selected_data,data = fetching_data(start_time,end_time)

    for field in data.columns: 
        statistics_plots(start_time,end_time,field,'line')