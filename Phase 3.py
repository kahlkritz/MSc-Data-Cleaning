import numpy as np
import pandas as pd
import datetime

##############FUNCTIONS####################
def write_to_excel(df):
    print()
    print("Writing to Excel File....")
    df.to_excel(r'C:\Users\Waut\Documents\Python Scripts\DATA\PyDB\OrgByDate_test.xlsx')
    print("Written to excel file")
    return; 
    
def groupby_category(df):
    subcount = df.groupby(['Suburb']).count()
    subcount.to_excel(r'subcount.xlsx')
    print("DONE")
    return subcount;  
    
#df['date_minus_time'].resample('D', how='sum')
#df['count'].resample('W', how='sum')
#df['count'].resample('M', how='sum')
##############FUNCTIONS####################
    
#Read From Excel
print()
print("Reading From Excel...")
df = pd.read_excel (r"C:\Users\Waut\Documents\Python Scripts\DATA\PyDB\Humewood Suburbs.xlsx", sheet_name="Sheet1")
print("station read: {}".format(df.shape))
print()

#Convert to datetime objects
df["Date"] = pd.to_datetime(df["Date"])

#Remove time and leave only date
print("Before re-indexing: ")
df['Date'] = df["Date"].apply( lambda df : datetime.datetime(year=df.year, month=df.month, day=df.day))


#Group by unique date	
#df.set_index(df["Date"],inplace=True)
#new = df.groupby(df.index).count()
df.groupby(['Suburb']).count()

#df.groupby(['Date','Suburb']).size().reset_index().groupby('Date')[[0]].count()

print("After re-indexing: ")
print(df.shape)
write_to_excel(df)