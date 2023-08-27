import pandas as pd

fixed_holidays = [
                    (12, 31), # New Year's Eve
                    (1, 1),  # New Year's Day
                    (7, 3),  # Independence Day
                    (7, 4),  # Independence Day
                    (12, 24), # Christmas Eve
                    (12, 25) # Christmas
                  ]

def is_holiday(row):
    return (row['month'], row['day']) in fixed_holidays

def is_rush_hour(row):
    if row['a_dow_type'] == 'Weekday':
        return (row['hour'] >= 7 and row['hour'] <= 9) or (row['hour'] >= 16 and row['hour'] <= 18)
    else:
        return False

def add_features(df):
    df['holiday'] = df.apply(is_holiday, axis=1).astype(int)
    df['rush_hour'] = df.apply(is_rush_hour, axis=1).astype(int)
    df['age_over_21'] = (df['age'] > 21).astype(int)
    
    return df
