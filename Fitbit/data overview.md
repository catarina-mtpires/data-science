# Fitbit Data Overview

This document contains an overview of the data extracted from Fitbit. This dataset contains my personal Fitbit data, collected with Fitbit Sense since December 2021.

Sense is a health smartwatch that includes the following sensors:
- Multi-path optical heart rate sensor;
- Multipurpose electrical sensors for EDA (electrodermal activity) and ECG (electrocardiography);
- Red and infrared sensors for oxygen saturation monitoring;
- Gyroscope;
- Altimeter;
- 3-axis accelerometer;
- Skin temperature sensor;
- Ambient light sensor;
- Built-in GPS;
- Microphone.

With these sensors, Sense can provide information about health and fitness of the user. We will use the following data for this project:
1. Activity Tracking Data - includes steps, distance, floors, calories, exercise, daily readiness score, active zone minutes, and VO2 max;
2. Heart Data - includes heart rate tracking (BPM measurements), resting heart rate, and ECG signals;
3. Sleep Data - includes sleep stages, sleep score, snore and noise detection, breathing rate, temperature, and heart rate variability;
4. Stress Data - includes stress management score, and electrodermal activity;
5. Oxygen Variation Data - includes estimated oxygen variation.

Next, we have a detailed description of each parameter.

## 1. Activity Tracking Data

### Steps

Sense counts the number of steps the user takes each day using a 3-axis accelerometer. This sensor allows Sense to determine the frequency, duration, intensity, and patterns of the user's movement. 

Steps data extracted from Fitbit is in the <i>.json</i> format and contains timestamps and the number of steps taken between timestamps. The difference between timestamps can be as little as 1 minute. 

### Distance

Sense calculates distance based on the number of steps or the GPS data. Usually, sense calculates the distance travelled each day by multiplying the number of steps by the stride lenght. However, when the user tracks an activity with GPS, Sense uses GPS data to calculate distance.

Distance data extracted from Fitbit is in the <i>.json</i> format and contains timestamps and the correspondent distance (in centimeters, cm) walked between timestamps. The difference between timestamps can be as little as 1 minute. 

### Floors

Sense has an altimeter sensor that tracks altitude and converts it to floors climbed along the day, considering one floor is equivalent to 3 meters. 

Floors data extracted from Fitbit is in the <i>.json</i> format and contains timestamps and the number of floors climed between timestamps. The difference between timestamps can be as little as 1 minute. However, it only presents data when the number of floors is one or higher.

### Calories

Sense estimates the number of calories burned daily by combining the user's basal metabolic rate (rate at which calories are burned at rest to maintain vital body functions) and activity data. The user's BMR (basal metabolic rate) is based on physical data entered by the user, such as height, weight, sex, and age.

Calories data extracted from Fitbit is in the <i>.json</i> format and contains timestamps and the number of calories (in kilocalories, kcal) burned between timestamps. The difference between timestamps is 1 minute and the number of calories burned at rest per minute is 0.92kcal.

### Exercise

Sense can track exercise of 20 different modes (run, walk, hike, bike, swim, etc.). For each activity the user records, Sense tracks: number of minutes in each activity level (sedentary, light activity, moderate activity, and intense activity), average heart rate, number of calories burned, duration of the workout, number of steps taken, heart rate zones (out of range, fat burn, cardio, and peak), active zone minutes, elevation gain, and start and end time of the workout. Exercise data extracted from Fitbit is in the <i>.json</i> format.

### Daily Readiness Score

Sense calculates a daily readiness score that indicates how prepared the user is for physical activity that day. It contains three readiness ranges:

1. Low Readiness (from 1 to 29) - the user should prioritize recovery and avoid overexertion;
2. Good Readiness (from 30 to 64) - the user is ready for a normal amount of exercise, but should not push beyond personal limits;
3. Excellent readiness (from 65 to 100) - the user is ready to take a challenging workout.

Daily readiness Score data extracted from Fitbit is in the <i>.csv</i> format and contains the date of the score, the final score level (1 per day), and the normalized scores of sleep, fitness fatigue, and heart rate variabilities components, which are used to calculate the final score.

### Active Zone Minutes

Sense uses active zone minutes to track the user's time in a heart-pumping activity, having a goal of 150 minutes of moderate activity or 75 minutes of intense activity per week. Sense adds Active Zone Minutes for time spent in the fat burn, cardio, or peak heart rate zones, which are personalized based on the user's fitness level and age.

Active zone minutes data extracted from Fitbit is in the <i>.json</i> format and contains the date and the total number of minutes spent in each zone (sedentary, light activity, moderate activity, and intense activity) per day.

### VO2 Max

Sense can estimate the user's VO2 max, which is the maximum amount of oxygen the body can use during exercise. VO2 max is based on the user's resting heart rate and profile (such as age, gender, and weight) and it measures cardio fitness level. The higher the value, the better the cardio fitness level. Cardio fitness level can be improved with exercise and healthy weight loss and it has 6 different levels, ranging from poor to excellent:
1. Poor - VO2 max < 31.2;
2. Fair - 31.2 < VO2 max ≤ 35.9;
3. Average - 35.9 < VO2 max ≤ 40.8;
4. Good - 40.8 < VO2 max ≤ 45.6;
5. Very Good - 45.6 < VO2 max ≤ 50.2;
6. Excellent - VO2 max > 50.2.

VO2 max data extracted from Fitbit is in the <i>.json</i> format and contains dates and the correspondent VO2 max value (1 per day).

## 2. Heart Data

### Heart Rate Tracking

Sense has an optical heart rate sensor that tracks the user's heart rate (how many times the heart beats in a minute) 24/7.

Heart rate data extracted from Fitbit is in the <i>.json</i> format and contains timestamps and the correspondent heart rate (in beats per minute, bmp). The difference between timestamps can be as little as 5 seconds. 

### Resting Heart Rate

Resting heart Rate is the number of times the heart beats per minute at rest. Typically, resting heart rate ranges from 60 to 100 bpm and it can be an important indicator of fitness level and overall cardiovascular health.

Resting heart rate data extracted from Fitbit is in the <i>.json</i> format and contains dates and the correspondent resting heart rate (in beats per minute, bmp) per day.

### ECG Signals

Sense can record an ECG signal and analyse it to look for signs of atrial fibrillation (AFib), which is a type of arrhytmia.

ECG data extracted from Fitbit is in the <i>.csv</i> format and contains ECG readings, each one with a duration of 30 seconds, and the user's heart rate during the readings.

## 3. Sleep Data

### Sleep Stages

Sense tracks the user's sleep stages (awake, light sleep, deep sleep, and REM sleep) using a combination of the user's movement and heart rate patterns.
- Light sleep is the entry point into sleep each night and begins within minutes of falling asleep. Breathing and heart rate typically decrease slightly during this stage. It promotes mental and physical recovery.
- Deep sleep typically occurs in the first few hours of sleep - breathing becomes slower and muscles relax while heart rate usually becomes more regular. It promotes physical recovery and aspects of memory and learning.
- REM sleep (rapid eye movement sleep) occurs after deep sleep and the brain becomes more active. Dreams mainly occur in this phase where the heart rate increases and breathing becomes more irregular. REM sleep plays an important role in mood regulation, learning, and memory, as the brain processes and consolidates information from the previous day so that it can be stroed in long-term memory.

Sleep stages data extracted from Fitbit is in the <i>.json</i> format and contains the date of the record, start and end time of sleep, number of minutes to fall asleep, awake, after awake, and time in bed, and information about each sleep stage: number of times in each stage, number of minutes, and thirty day average minutes. Besides that, it also contains timestamps and the correspondent sleep stage, as well as the duration in seconds.

### Sleep Score

Based on the sleep stages and heart rate, Sense calculates a sleep score for each night that measures sleep quality. It helps the user understand the sleep each night and find trends in it and ranges from 0 to 100:
1. Poor - Less than 60;
2. Fair - 60 to 79;
3. Good - 80 to 89;
4. Excellent - 90 yo 100.

The overall sleep score is a sum of the user's individual scores in sleep duration, sleep quality, and restoration:
- Duration considers time asleep and awake;
- Quality considers deep and REM sleep;
- Restoration considers sleeping heart rate and restlessness.

Sleep score data extracted from Fitbit is in the <i>.csv</i> format and contains the date of the score, the overall score, duration, sleep quality, and restoration scores, deep sleep duration in minutes, and resting heart rate.

### Snore and Noise Detection

Sense detect snore and noise during the user's sleep, through the built-in microphone. It can measure sound intensity (to determine the baseline noise level), and snoring events (by looking for snore-specific noises) 

Snore and noise detection data extracted from Fitbit is in the <i>.csv</i> format and contains timestamps with 30 seconds interval, the correspondent mean, maximum, and minimum noise level measured between timestamps (in decibels A, dBA), and the number of sound and snoring events between timestamps.

### Breathing Rate

Sense measures the user's breathing rate while sleeping, that is, the number of breaths taken per minute. Breathing rate is typically between 12 and 20 breaths per minute.

Breathing rate data extracted from Fitbit is in the <i>.csv</i> format and contains dates, the correspondent breathing rate for the entire sleep, deep sleep, light sleep, and REM sleep (1 value per day).


### Temperature

Sense tracks skin temperature each night to show how it varies from the user's personal baseline, creating trends over time. Sense uses 30 nights of temperature data to estimate the user's temperature baseline and creates the user's personal range between plus and minus 2 standard deviations from the baseline.

Temperature data extracted from Fitbit is in the <i>.csv</i> format and contains timestamps with 1 minute interval, the correspondent deviation from the baseline (in degree Celsius, °C), and the baseline value (°C) and correspondent standard deviation.

### Heart Rate Variability

Heart rate variability (HRV) is the variation in time between heartbeats and it is measured by the variation in the beat-to-beat interval. Sense tracks HRV during night to see if the user's body is showing potential signs of stress, illness, or fatigue. Higher HRV is related to better cardiovascular fitness. On the other hand, a significant drop in HRV may indicate illness, stress, depression, or anxiety.

HRV data extracted from Fitbit is in the <i>.csv</i> format and contains two types of data:
1 - Detailed HRV - includes timestamps with 5 minutes interval, correspondent HRV, low frequency (measures long term variations in heart rate and reflects activity from both the sympathetic and parasympathetic branches), and high frequency (measures short term variations in heart rate and captures parasympathetic activity);
2 - Histogram - includes histograms that show the spread in the beat-to-beat intervals during sleep. Histograms are composed by 29 bins with an interval of 0.05s and starting at 0.3s. 

## 4. Stress Data

### Stress Management Score

Sense calculates a daily stress management score to help the user understand how the body is handling stress. The score ranges from 1 to 100, where a higher number means the user's body is showing fewer physical signs of stress. Sense stress management score is based on the user's responsiveness, exertion balance, and sleep patterns:
- Responsiveness considers HRV during deep sleep from the night before, elevated heart rate while at rest from the day before, sleeping heart rate above resting heart rate from the night before, and EDA from the day before; 
- Exertion considers daily steps, weekly activity level, and fitness level vs. exercise fatigue;
Sleep patterns considers total sleep over the previous week, restlessness and other indicators of disrupted sleep from the night before, and time spent in REM and deep sleep from the night before.

Stress management score data extracted from Fitbit is in the <i>.csv</i> format and contains the date of the score, the stress score (1 per day), and points from responsiveness, sleep, and exertion components, which are used to calculate the final score.

### Electrodermal Activity

Sense detects electrodermal activity (EDA) through the on-wrist EDA Scan, which may indicate the user's response to stress. EDA responses are tiny changes in the sweat level of the skin, which may happen due to stress or other factors. The calmer a person is, the fewer EDA responses the person will have. 

Estimated electrodermal activity data extracted from Fitbit is in the <i>.csv</i> format and contains timestamps and their correspondent average SCL value. The difference between timestamps is 1 second. 


## 5. Oxygen Variation Data

### Estimated Oxygen Variation

Estimated oxygen variation approximates the changes in the user's blood oxygen saturation, which measures the percent of blood that is saturated with oxygen. Typically, it is at 95-100%, meaning the blood is carrying as much oxygen as it can. Sense has red and infrared sensors that can estimate the variability of blood oxygen saturation level - richly oxygenated blood is red and reflects more red light than infrared light; poorly oxygenated blood is bluish red and reflects more infrared light than red light.

Estimated oxygen variation data extracted from Fitbit is in the <i>.csv</i> format and contains timestamps and their correspondent infrared to red signal ratio. The difference between timestamps can be as little as 1 minute. 