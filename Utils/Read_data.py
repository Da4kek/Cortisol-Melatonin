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
