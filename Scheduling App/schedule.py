import numpy as np
import pandas as pd
from calendar import day_abbr

"""
Columns = Mon, Tues, Wed, Thurs, Fri, Sat, Sun
Rows = time of the shift
"""

days_of_week = range(7)
cols = [day_abbr[i] for i in days_of_week]
rows = ['Morning', 'Mid', 'Evening', 'Overnight']


def empty_schedule():
    df = pd.DataFrame(columns=cols, index=rows)
    df.replace(np.nan, 'Open Shift', True)
    return df


def shift(day, shift_type, coverage):
    return """%s - %s - %s""" % (day, shift_type, coverage)
