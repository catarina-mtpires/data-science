# DIRECTORIES
DIR_DRS = 'data/1_physical_activity/6_daily_readiness/*.csv'
DIR_AZM_SED = 'data/1_physical_activity/7_active_zone_minutes/sedentary/*.json'
DIR_AZM_LIGHT = 'data/1_physical_activity/7_active_zone_minutes/light/*.json'
DIR_AZM_MOD = 'data/1_physical_activity/7_active_zone_minutes/moderate/*.json'
DIR_AZM_INT = 'data/1_physical_activity/7_active_zone_minutes/intense/*.json'
DIR_VO2_MAX = 'data/1_physical_activity/8_vo2_max/*.json'
DIR_RHR = 'data/2_heart/2_resting_heart_rate/*.json'
DIR_SLEEP_DATA = 'data/3_sleep/1_sleep_stages/*.json'
DIR_SLEEP_SCORE = 'data/3_sleep/2_sleep_score/*.csv'
DIR_BREATHING = 'data/3_sleep/4_respiratory_rate/*.csv'
DIR_COMP_TEMP = 'data/3_sleep/5_temperature/computed/*.csv'
DIR_DAILY_HRV = 'data/3_sleep/6_heart_rate_variability/daily/*.csv'
DIR_HRV_HIST = 'data/3_sleep/6_heart_rate_variability/histogram/*.csv'
DIR_STRESS_SCORE = 'data/4_stress/1_stress_score/*.csv'

# ORIGINAL DATA COLUMNS
OG_DRS_COL = ['date', 'readiness_score_value', 'srl_normalized_score', 'ff_normalized_score', 'hrv_normalized_score']
OG_SLEEP_SCORE_COL = ['timestamp', 'overall_score', 'composition_score', 'revitalization_score', 'duration_score']
OG_BREATHING_COL = ['timestamp', 'full_sleep_breathing_rate', 'deep_sleep_breathing_rate', 'light_sleep_breathing_rate', 'rem_sleep_breathing_rate']
OG_COMP_TEMP_COL = ['sleep_end', 'nightly_temperature', 'baseline_relative_sample_standard_deviation']
OG_DAILY_HRV_COL = ['timestamp', 'rmssd']
OG_HRV_HIST_COL = ['timestamp', 'bucket_values']
OG_STRESS_SCORE_COL = ['date', 'stress_score', 'sleep_points', 'responsiveness_points', 'exertion_points']

# NEW DATA COLUMNS
NEW_DRS_COL = ['date', 'readiness score', 'readiness sleep score', 'readiness fitness fatigue', 'readiness HRV']
NEW_SLEEP_SCORE_COL = ['date', 'sleep score', 'sleep quality score', 'sleep restoration score', 'sleep duration score']
NEW_BREATHING_COL = ['date', 'total breathing', 'deep sleep breathing', 'light sleep breathing', 'rem sleep breathing']
NEW_COMP_TEMP_COL = ['date', 'temperature', 'temperature std']
NEW_DAILY_HRV_COL = ['date', 'HRV']
NEW_HRV_HIST_COL = ['date', 'HRV histogram']
NEW_STRESS_SCORE_COL = ['date', 'stress score', 'stress sleep points', 'stress responsiveness points', 'stress exertion points']
