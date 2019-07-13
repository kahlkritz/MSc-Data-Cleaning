import numpy as np
import pandas as pd

##############FUNCTIONS####################
def write_to_excel(df):
    print()
    print("Writing to Excel File....")
    df.to_excel(r'C:\Users\Waut\Documents\Python Scripts\DATA\PyDB\grouped_test.xlsx')
    print("Written to Excel file")
    return; 
    
def groupby_category(df):
    subcount = df.groupby(['Suburb']).count()
    subcount.to_excel(r'subcount.xlsx')
    print("DONE")
    return subcount;

def empty(orged, raw):
    for i in orged.index:
        for j in raw.index:
            if(raw.loc[i,'Date'] == orged.loc[j,'Date']):
                if(raw.loc[j,'Suburb'] == "summerstrand"):
                    orged.loc[i,'Summerstrand'] = orged.loc[i,'Summerstrand'] + 1
                if(raw.loc[j,'Suburb'] == "humewood"):
                   orged.loc[i,'Humewood'] = orged.loc[i,'Humewood'] + 1
                if(raw.loc[j,'Suburb'] == "walmer"):
                   orged.loc[i,'Walmer'] = orged.loc[i,'Walmer'] + 1
                if(raw.loc[j,'Suburb'] == "south end"):
                   orged.loc[i,'Southend'] = orged.loc[i,'Southend'] + 1
                if(raw.loc[j,'Suburb'] == "schoenmakerskop"):
                   orged.loc[i,'Schoenmakerskop'] = orged.loc[i,'Schoenmakerskop'] + 1 
    return;    
    
#orged['Summerstrand'] = 0
#orged['Humewood'] = 0
#orged['Walmer'] = 0
#orged['Southend'] = 0
#orged['Schoenmakerskop'] = 0
    
#df['date_minus_time'].resample('D', how='sum')
#df['count'].resample('W', how='sum')
#df['count'].resample('M', how='sum')    

#Group by unique date	
#new = df.set_index(df["Date"],inplace=True)
#new = df.groupby(df.index).count()
#new = df.groupby(['Suburb']).count()
#new = df.groupby(['Date','Suburb']).size().reset_index().groupby('Date')[[0]].count()    
    
#orged = orged.fillna(0)
#orged['Humewood'].fillna(0, inplace=True)
#orged['Humewood'] = orged['Humewood'].fillna(0)
#orged['Humewood'] = orged['Humewood'].replace(np.nan, 0)
    
##############FUNCTIONS####################
    
# Read From Excel
print()
print("Reading From Excel...")
raw = pd.read_excel (r"C:\Users\Waut\Documents\Python Scripts\DATA\PyDB\suburbs_EDIT.xlsx", sheet_name="Sheet1")
raw["Date"] = pd.to_datetime(raw["Date"])
print("raw read: {}".format(raw.shape))
print()

# Create an array of zeros and then convert it into a dataframe
a = np.zeros(shape=(7607,6))
orged = pd.DataFrame(a,columns=['Date', 'Summerstrand', 'Humewood', 'Walmer', 'South End', 'Schoenmakerskop'])

# Convert the values to integer
convert_dict = {'Summerstrand': int, 'Humewood': int, 'Walmer': int, 'South End': int, 'Schoenmakerskop' : int}  
orged = orged.astype(convert_dict)

#Convert index to type Date
orged["Date"] = pd.to_datetime(orged["Date"])

# Declare index and value variables
temp = raw.loc[0,'Date']
tempind = 0
orged.loc[0,'Date'] = temp
print("Temp defined")

for i in raw.index: #Loop through raw
    if(raw.loc[i,'Date'] == temp):  # If the raw index's date is the same as the temp date...
        if(raw.loc[i,'Suburb'] == "summerstrand"):  #Check if the suburb correlating to date is Sumstrand
            orged.loc[tempind,'Summerstrand'] = orged.loc[tempind,'Summerstrand'] + 1   #Increment the incident count for this date and suburb
            
        if(raw.loc[i,'Suburb'] == "humewood"):
            orged.loc[tempind,'Humewood'] = orged.loc[tempind,'Humewood'] + 1
            
        if(raw.loc[i,'Suburb'] == "walmer"):
            orged.loc[tempind,'Walmer'] = orged.loc[tempind,'Walmer'] + 1
            
        if(raw.loc[i,'Suburb'] == "south end"):
            orged.loc[tempind,'South End'] = orged.loc[tempind,'South End'] + 1
            
        if(raw.loc[i,'Suburb'] == "schoenmakerskop"):
            orged.loc[tempind,'Schoenmakerskop'] = orged.loc[tempind,'Schoenmakerskop'] + 1
    else:      
        temp = raw.loc[i+1,'Date']  #Assign next date in raw to temp
        tempind = tempind + 1   #Assign next index value to tempind
        orged.loc[tempind, 'Date'] = temp   #Assign temp to next orged date
        
        if(raw.loc[i,'Suburb'] == "summerstrand"):  #Check if the suburb correlating to date is Sumstrand
            orged.loc[tempind,'Summerstrand'] = orged.loc[tempind,'Summerstrand'] + 1   #Increment the incident count for this date and suburb
            
        if(raw.loc[i,'Suburb'] == "humewood"):
            orged.loc[tempind,'Humewood'] = orged.loc[tempind,'Humewood'] + 1
            
        if(raw.loc[i,'Suburb'] == "walmer"):
            orged.loc[tempind,'Walmer'] = orged.loc[tempind,'Walmer'] + 1
            
        if(raw.loc[i,'Suburb'] == "south end"):
            orged.loc[tempind,'South End'] = orged.loc[tempind,'South End'] + 1
            
        if(raw.loc[i,'Suburb'] == "schoenmakerskop"):
            orged.loc[tempind,'Schoenmakerskop'] = orged.loc[tempind,'Schoenmakerskop'] + 1
               
print()
print("Orged: ")
print(orged)
print("Finished")

write_to_excel(orged)