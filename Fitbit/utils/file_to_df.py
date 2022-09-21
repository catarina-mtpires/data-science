import json
import glob
import datetime
import pandas as pd


def read_json_files(dir_files):
    files = glob.glob(dir_files)
    data = []
    for file in files:
        with open(file) as json_file:
            data += json.load(json_file)

    return data


def get_dataframe_daily_json(dir_files, v_name, value='value', format='%m/%d/%y %H:%M:%S'):
    data = read_json_files(dir_files)
    dates, values = [], []
    for sample in data:
        dates += [datetime.datetime.strptime(sample['dateTime'], format)]
        values += [sample['value'][value]]
    df = pd.DataFrame({'date': dates, v_name: values})

    return df


def get_dataframe_json(dir_files, create_df=True):
    data = read_json_files(dir_files)
    timestamps, values = [], []
    for sample in data:
        timestamps += [datetime.datetime.strptime(sample['dateTime'], '%m/%d/%y %H:%M:%S')]
        values += [float(sample['value'])]

    if create_df:
        return pd.DataFrame({'timestamp': timestamps, 'value': values})
    else:
        return timestamps, values


def get_dataframe_csv(dir_files, old_col, new_col, time_var, time_format, daily=True):
    files = glob.glob(dir_files)
    df = pd.DataFrame()
    for file in files:
        data = pd.read_csv(file)[old_col]
        data[time_var] = [datetime.datetime.strptime(date, time_format) for date in data[time_var]]
        df = df.append(data)
    df = df.sort_values(by=time_var)
    df = df.reset_index(drop=True)
    if daily:
        df[time_var] = [dt.date() for dt in df[time_var]]
    df.columns = new_col

    return df


def round_timestamp(df, time_var='timestamp', interval=1, unit='min'):
    round_ts = []
    if unit == 'min':
        for ts in df[time_var]:
            discard = datetime.timedelta(minutes=ts.minute % interval, seconds=ts.second, microseconds=ts.microsecond)
            ts -= discard
            if discard >= datetime.timedelta(minutes=interval/2):
                ts += datetime.timedelta(minutes=interval)
            round_ts += [ts]
    elif unit == 'sec':
        for ts in df[time_var]:
            discard = datetime.timedelta(minutes=ts.minute, seconds=ts.second % interval, microseconds=ts.microsecond)
            ts -= discard
            if discard >= datetime.timedelta(seconds=interval/2):
                ts += datetime.timedelta(seconds=interval)
            round_ts += [ts]
    df.insert(0, 'rounded timestamp', round_ts)

    return df
