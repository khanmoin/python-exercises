"""
   Priting current date and time using datetime
"""

import datetime

if __name__ == '__main__':
    c_date = datetime.date.today()
    c_time = datetime.datetime.now().time()
    print(f'Today is: {c_date}')
    print(f'Time is:  {c_time}')
