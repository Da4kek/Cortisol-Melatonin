import pandas as pd
import numpy as np 


def create_dataset(users, file_name, replace_na=True):
    df_concat = pd.DataFrame()
    for user in users:
        try:
            df = pd.read_csv('DataPaper/%s/%s.csv' %
                                 (user, file_name))
            df['user'] = user
            df_concat = pd.concat([df_concat, df])
        except:
            print('NO data for %s' % user)
            pass

    del df_concat['Unnamed: 0']
    # df_concat = df_concat.set_index('user')

    if replace_na == True:
        df_concat = df_concat.replace(0, np.nan)

    return (df_concat)


def convert_Actigraph_datetime(row):
    return pd.to_datetime(row['time'], format='%H:%M:%S').time()


def convert_Activity_Start_datetime(row):
    if row['Start'] == '24:00':
        return pd.to_datetime('0:00', format='%H:%M').time()
    else:
        return pd.to_datetime(row['Start'], format='%H:%M').time()


def convert_Activity_End_datetime(row):
    if row['End'] == '24:00':
        return pd.to_datetime('0:00', format='%H:%M').time()
    elif pd.isnull(row['End']):
        return row['Start']
    else:
        return pd.to_datetime(row['End'], format='%H:%M').time()


def label_actigraph(row, df):
    day = row['day']
    time = row['time']
    mask = df[(df['Day'] == day) & (df['Start'] <= time) & (df['End'] >= time)]

    if mask.empty:
        return mask['Activity'].iloc[0]
    else:
        return None


def RMSSD(RR_list):
    return np.sqrt(np.sum((np.diff((np.array(RR_list)*1000))**2)/(len(RR_list)-1)))


def correct_day(row):
    if (row['day'] != 1) and (row['day'] != 2):
        return 2
    else:
        return row['day']
