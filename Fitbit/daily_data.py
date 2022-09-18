import datetime
import numpy as np
import pandas as pd
import utils.constants as c
import utils.file_to_df as f2df


# daily readiness score
df_drs = f2df.get_dataframe_csv(c.DIR_DRS, c.OG_DRS_COL, c.NEW_DRS_COL, 'date', '%Y-%m-%d')
# VO2 max
df_vo2_max = f2df.get_dataframe_daily_json(c.DIR_VO2_MAX, 'VO2 max', value='filteredDemographicVO2Max')
# resting heart rate
df_rhr = f2df.get_dataframe_daily_json(c.DIR_RHR, 'RHR')
# sleep score
df_sleep_score = f2df.get_dataframe_csv(c.DIR_SLEEP_SCORE, c.OG_SLEEP_SCORE_COL, c.NEW_SLEEP_SCORE_COL, 'timestamp', '%Y-%m-%dT%H:%M:%SZ')
# breathing rate
df_breathing = f2df.get_dataframe_csv(c.DIR_BREATHING, c.OG_BREATHING_COL, c.NEW_BREATHING_COL, 'timestamp', '%Y-%m-%dT%H:%M:%S')
# temperature
df_comp_temp = f2df.get_dataframe_csv(c.DIR_COMP_TEMP, c.OG_COMP_TEMP_COL, c.NEW_COMP_TEMP_COL, 'sleep_end', '%Y-%m-%dT%H:%M:%S')
# heart rate variability
df_daily_hrv = f2df.get_dataframe_csv(c.DIR_DAILY_HRV, c.OG_DAILY_HRV_COL, c.NEW_DAILY_HRV_COL, 'timestamp', '%Y-%m-%dT%H:%M:%S')
df_hist_hrv = f2df.get_dataframe_csv(c.DIR_HRV_HIST, c.OG_HRV_HIST_COL, c.NEW_HRV_HIST_COL, 'timestamp', '%Y-%m-%dT%H:%M:%S')
# stress management score
df_stress_score = f2df.get_dataframe_csv(c.DIR_STRESS_SCORE, c.OG_STRESS_SCORE_COL, c.NEW_STRESS_SCORE_COL, 'date', '%Y-%m-%dT%H:%M:%S')

# Active Zone Minutes
dates, sedentary_min = f2df.get_dataframe_json(c.DIR_AZM_SED, create_df=False)
_, light_min = f2df.get_dataframe_json(c.DIR_AZM_LIGHT, create_df=False)
_, moderate_min = f2df.get_dataframe_json(c.DIR_AZM_MOD, create_df=False)
_, intense_min = f2df.get_dataframe_json(c.DIR_AZM_INT, create_df=False)
df_azm = pd.DataFrame({'date': dates, 'AZM sedentary': sedentary_min, 'AZM light': light_min,
                       'AZM moderate': moderate_min, 'AZM intense': intense_min})

# sleep stages
sleep_data = f2df.read_json_files(c.DIR_SLEEP_DATA)
date, start_time, end_time, asleep_min, time_in_bed, awake_min, awake_30_avg, light_min, light_30_avg, deep_min, \
deep_30_avg, rem_min, rem_30_avg, = [], [], [], [], [], [], [], [], [], [], [], [], []
for sample in sleep_data:
    if sample['mainSleep'] == True and 'wake' in sample['levels']['summary'].keys():
        date += [datetime.datetime.strptime(sample['dateOfSleep'], '%Y-%m-%d')]
        start_time += [datetime.datetime.strptime(sample['startTime'], '%Y-%m-%dT%H:%M:%S.000')]
        end_time += [datetime.datetime.strptime(sample['endTime'], '%Y-%m-%dT%H:%M:%S.000')]
        asleep_min += [sample['minutesAsleep']]
        time_in_bed += [sample['timeInBed']]
        awake_min += [sample['levels']['summary']['wake']['minutes']]
        awake_30_avg += [sample['levels']['summary']['wake']['thirtyDayAvgMinutes']]
        light_min += [sample['levels']['summary']['light']['minutes']]
        light_30_avg += [sample['levels']['summary']['light']['thirtyDayAvgMinutes']]
        deep_min += [sample['levels']['summary']['deep']['minutes']]
        deep_30_avg += [sample['levels']['summary']['deep']['thirtyDayAvgMinutes']]
        rem_min += [sample['levels']['summary']['rem']['minutes']]
        rem_30_avg += [sample['levels']['summary']['rem']['thirtyDayAvgMinutes']]

df_sleep_data = pd.DataFrame({'date': date, 'start sleep': start_time, 'end sleep': end_time, 'min asleep': asleep_min,
                              'min in bed': time_in_bed, 'min awake': awake_min, '30 day avg awake': awake_30_avg,
                              'min light': light_min, '30 day avg light': light_30_avg, 'min deep': deep_min,
                              '30 day avg deep': deep_30_avg, 'min rem': rem_min, '30 day avg rem': rem_30_avg})
df_sleep_data = df_sleep_data.sort_values(by='date')

total_data = [df_drs, df_azm, df_vo2_max, df_rhr, df_sleep_data, df_sleep_score, df_breathing, df_comp_temp, df_daily_hrv, df_hist_hrv, df_stress_score]
cols = []
for df in total_data:
    cols += list(df.columns[1:])

dates = pd.date_range(start="2021-12-22", end="2022-09-10")
daily_data = pd.DataFrame(np.empty((len(dates), len(cols))) * np.nan, columns=cols)
daily_data.insert(0, 'date', dates)

for date, i in zip(dates, range(len(dates))):
    for df in total_data:
        index = df[df['date'] == date].index.tolist()
        if index:
            for col in df.columns[1:]:
                daily_data[col][i] = df[col][index[0]]

daily_data.to_csv('data/daily_data.csv', index=False)
