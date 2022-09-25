import datetime
import numpy as np
import pandas as pd
import utils.constants as c
import utils.file_to_df as f2df


# physical activity
exercise_data = f2df.read_json_files(c.DIR_EXERCISE)
act_name, avg_hr, cal, dur, steps, start_time, sed_min, light_min, mod_min, int_min, oor_min, oor_cal, fat_burn_min, \
fat_burn_cal, cardio_min, cardio_cal = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
for sample in exercise_data:
    act_name += [sample['activityName']]
    avg_hr += [int(sample['averageHeartRate'])]
    cal += [int(sample['calories'])]
    dur += [sample['duration']]
    start_time += [datetime.datetime.strptime(sample['startTime'], '%m/%d/%y %H:%M:%S')]
    sed_min += [sample['activityLevel'][0]['minutes']]
    light_min += [sample['activityLevel'][1]['minutes']]
    mod_min += [sample['activityLevel'][2]['minutes']]
    int_min += [sample['activityLevel'][3]['minutes']]
    oor_min += [sample['heartRateZones'][0]['minutes']]
    oor_cal += [sample['heartRateZones'][0]['caloriesOut']]
    fat_burn_min += [sample['heartRateZones'][1]['minutes']]
    fat_burn_cal += [sample['heartRateZones'][1]['caloriesOut']]
    cardio_min += [sample['heartRateZones'][2]['minutes']]
    cardio_cal += [sample['heartRateZones'][2]['caloriesOut']]
    steps += [int(sample['steps'])]

df_exercise = pd.DataFrame({'activity name': act_name, 'start time': start_time, 'duration': dur,
                            'average heart rate': avg_hr, 'calories': cal, 'steps': steps, 'sedentary minutes': sed_min,
                            'light minutes': light_min, 'moderate minutes': mod_min, 'intense minutes': int_min,
                            'out of range minutes': oor_min, 'out of range calories': oor_cal,
                            'fat burn minutes': fat_burn_min, 'fat burn calories': fat_burn_cal,
                            'cardio minutes': cardio_min, 'cardio calories': cardio_cal})
df_exercise = df_exercise[df_exercise['duration'] >= 15*60*1000]

# ecg signals
df_ecg = f2df.get_dataframe_csv(c.DIR_ECG, c.OG_ECG_COL, c.OG_ECG_COL, 'reading_time', '%a %b %d %H:%M:%S %Z %Y', daily=False)
df_ecg['waveform_samples'] = [np.array(signal[1:-1].split()).astype(int) for signal in df_ecg['waveform_samples']]

# snore and noise detection
df_noise = f2df.get_dataframe_csv(c.DIR_NOISE, c.OG_NOISE_COL, c.OG_NOISE_COL, 'timestamp', '%Y-%m-%dT%H:%M:%S', daily=False)

# electrodermal activity
df_eda = f2df.get_dataframe_csv(c.DIR_EDA, c.OG_EDA_COL, c.OG_EDA_COL, 'timestamp', '%Y-%m-%dT%H:%M:%S', daily=False)
df_eda['scl_values'] = [np.array(signal[1:-1].split(sep=', ')).astype(float) for signal in df_eda['scl_values']]

# Round timestamp to the closest 1 min interval
df_exercise = f2df.round_timestamp(df_exercise, time_var='start time')
df_ecg = f2df.round_timestamp(df_ecg, time_var='reading_time')
df_eda = f2df.round_timestamp(df_eda)

# Write data into csv
df_exercise.to_csv('data/recorded_exercises.csv', index=False)
df_ecg.to_csv('data/ecg_signals.csv', index=False)
df_noise.to_csv('data/noise_signals.csv', index=False)
df_eda.to_csv('data/eda_signals.csv', index=False)
