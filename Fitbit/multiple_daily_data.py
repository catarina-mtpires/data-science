import datetime
import pandas as pd
import utils.constants as c
import utils.file_to_df as f2df

# steps, distance, floors, calories
df_steps = f2df.get_dataframe_json(c.DIR_STEPS, var_name='steps')
df_distance = f2df.get_dataframe_json(c.DIR_DISTANCE, var_name='distance')
df_floors = f2df.get_dataframe_json(c.DIR_FLOORS, var_name='floors')
df_calories = f2df.get_dataframe_json(c.DIR_CALORIES, var_name='calories')

# heart rate
hr_data = f2df.read_json_files(c.DIR_HR)
timestamps, values = [], []
for sample in hr_data:
    timestamps += [datetime.datetime.strptime(sample['dateTime'], '%m/%d/%y %H:%M:%S')]
    values += [sample['value']['bpm']]
df_hr = pd.DataFrame({'timestamp': timestamps, 'HR': values})
df_hr = df_hr.drop_duplicates()

# sleep stages
sleep_data = f2df.read_json_files(c.DIR_SLEEP_STAGES)
timestamps, stages = [], []
for sample in sleep_data:
    if sample['mainSleep'] == True and 'wake' in sample['levels']['summary'].keys():
        for stage in sample['levels']['data']:
            timestamps += [datetime.datetime.strptime(stage['dateTime'], '%Y-%m-%dT%H:%M:%S.000')]
            stages += [stage['level']]
df_sleep_stages = pd.DataFrame({'timestamp': timestamps, 'sleep stage': stages})

# temperature
df_wrist_temp = f2df.get_dataframe_csv(c.DIR_WRIST_TEMP, c.OG_WRIST_TEMP_COL, c.NEW_WRIST_TEMP_COL, 'recorded_time', '%Y-%m-%dT%H:%M', daily=False)

# heart rate variability
df_hrv = f2df.get_dataframe_csv(c.DIR_HRV, c.OG_HRV_COL, c.NEW_HRV_COL, 'timestamp', '%Y-%m-%dT%H:%M:%S', daily=False)

# estimated oxygen variation
df_o2_var = f2df.get_dataframe_csv(c.DIR_O2_VAR, c.OG_O2_VAR_COL, c.NEW_O2_VAR_COL, 'timestamp', '%m/%d/%y %H:%M:%S', daily=False)

# Round timestamp to the closest 1 min interval
df_hr = f2df.round_timestamp(df_hr)
df_sleep_stages = f2df.round_timestamp(df_sleep_stages, insert_col=False)
df_o2_var = f2df.round_timestamp(df_o2_var, insert_col=False)

# Group heart rate values by rounded timestamp and calculate average value
new_df_hr = round(df_hr.groupby('rounded timestamp').mean().reset_index())
new_df_hr.columns = ['timestamp', 'HR']

# Create list with all data
total_data = [df_steps, df_distance, df_floors, df_calories, df_wrist_temp, df_hrv, new_df_hr, df_sleep_stages, df_o2_var]

# Create range of dates within the data (from December 22, 2021, to September 10, 2022)
timestamps = pd.date_range(start="2021-12-22", end="2022-09-11", freq='1min')

# Merge data into a single dataframe
multiple_daily_data = pd.DataFrame(timestamps, columns=['timestamp'])
multiple_daily_data = f2df.merge_data(total_data, multiple_daily_data, 'timestamp')
multiple_daily_data.drop(multiple_daily_data.tail(1).index, inplace=True)

# Write data into csv
multiple_daily_data.to_csv('data/multiple_daily_data.csv', index=False)
df_hr.to_csv('data/hr_data.csv', index=False)
