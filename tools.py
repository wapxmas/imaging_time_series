# Math
import math
import numpy as np
import pandas as pd
from numpy import array
import pyodbc


# Tools
def tabulate(x, y, f):
    """Return a table of f(x, y). Useful for the Gram-like operations."""
    return np.vectorize(f)(*np.meshgrid(x, y, sparse=True))


def cos_sum(a, b):
    """To work with tabulate."""
    return math.cos(a+b)


def create_time_serie(size, time):
    """Generate a time serie of length size and dynamic with respect to time."""
    # Generating time-series
    support = np.arange(0, size)
    serie = np.cos(support + float(time))
    return serie


def connect(host, db, user, pwd, port):
    conn = mysql.connector.connect(host=host, database=db, user=user, password=pwd, port=port)
    return conn


def get_time_series():
    '''
    cnxn = pyodbc.connect('Driver={SQL Server};'
                          'Server=127.0.0.1;'
                          'Database=ivap2025;'
                          'Trusted_Connection=yes;')
    cursor = cnxn.cursor()

    cursor.execute("SELECT [id],[timestamp],[uid],[weight] FROM [ivap2025].[dbo].[ivap_weight_cells]")
    for row in cursor.fetchall():
        print (row)

    :return:
    '''
    file = r'D:\TUM\MITI\imaging_time_series\data.xlsx'

    # Load spreadsheet
    xl = pd.ExcelFile(file)

    # Load a sheet into a DataFrame by name: df1
    df = xl.parse('ECB')

    # define input sequence
    in_seq = array(df.iloc[:]['value'])
    in_seq = in_seq.reshape((len(in_seq), 1))
    print(np.shape(in_seq))

    support = np.arange(0, 30)
    serie = np.cos(support / 30 * (2 * math.pi))
    size = 30
    ins = serie.reshape((len(serie), 1))

    return ins
