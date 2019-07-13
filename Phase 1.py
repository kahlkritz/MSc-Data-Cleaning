#Libraries
import pandas as pd
import numpy as np

#Variables
wait_days = 7   #Amount of days between incident report and incident committed
wait_hours = 36 #Amount of hours between incident report and incident committed

##########FUNCTIONS#################################################
#Remove duds based on empty province
def remove_duds_loop(df):
   for i in df.index:
       if(df.loc[i,'PROVINCE'] == "P COMM EASTERN CAPE"):# or df.loc[i, 'STATION'] != "HUMEWOOD"):
           #df = df.drop(i, inplace = True)
           df[df.PROVINCE != 'P COMM EASTERN CAPE']
   return df;

def drop_duds(df, year):
    tempInd = df[ df['PROVINCE'] != "P COMM EASTERN CAPE" ].index
    # Delete these row indexes from dataFrame
    df.drop(tempInd , inplace=True)
    print("{} cleaned".format(year))
    return df;

#Find time difference in hours/days between date commited and reported
def addTimeDiff(df):
    df['Time_Diff'] = df['DATE_REPORTED'] - df['DATE_COMMITED']
    df['Time_Diff'] = df['Time_Diff']/np.timedelta64(1,'d')
    return df;

#Remove all entries with larger than specified days difference in report and commit
def remove_days(df, days):
    for i in df.index:
        if(df.loc[i,'Time_Diff'] >= days):
            df.drop(i, inplace = True)
    return df;

#Remove all entries with larger than specified hours difference in report and commit
def remove_hours(df, hours):
    for i in df.index:
        if(df.loc[i,'Time_Diff'] >= hours):
            df.drop(i, inplace = True)
    return df;

#Write to Excel cleaned
def write_to_excel(df):
    print()
    print("Writing to Excel File....")
    df.to_excel(r'C:\Users\Waut\Documents\Python Scripts\DATA\PyDB\PE_Cleaned.xlsx')
    print("Done!")
    return;    

def humewoodhide(df):
#Grab columns from df 
    Humewood = pd.DataFrame()
    Humewood['Station'] = df['STATION']
    Humewood['Suburb'] = df['SUBURB1']
    Humewood['Street'] = df['STREET_NAME1']
    Humewood['Address'] = df['ADRES']
    Humewood['Date'] = df['DATE_COMMITED']
    print("Columns retrieved...")
    print(Humewood.shape)
    return Humewood;

##########FUNCTIONS#################################################

#Read DB's from Excel
df2016 = pd.read_excel (r"C:\Users\Waut\Documents\Python Scripts\DATA\TASK 7307 Thefts and Physical harm to humans and property PE 2016.xls", sheet_name="2016")
print("2016 read")
df2015 = pd.read_excel (r"C:\Users\Waut\Documents\Python Scripts\DATA\TASK 7307 Thefts and Physical harm to humans and property PE 2015.xls", sheet_name="2015")
print("2015 read")
df2014 = pd.read_excel (r"C:\Users\Waut\Documents\Python Scripts\DATA\TASK 7307 Thefts and Physical harm to humans and property PE 2014.xls", sheet_name="2014")
print("2014 read")
df2013 = pd.read_excel (r"C:\Users\Waut\Documents\Python Scripts\DATA\TASK 7307 Thefts and Physical harm to humans and property PE 2013.xls", sheet_name="2013")
print("2013 read")
df2012 = pd.read_excel (r"C:\Users\Waut\Documents\Python Scripts\DATA\TASK 7307 Thefts and Physical harm to humans and property PE 2012.xls", sheet_name="2012")
print("2012 read")
df2011 = pd.read_excel (r"C:\Users\Waut\Documents\Python Scripts\DATA\TASK 7307 Thefts and Physical harm to humans and property PE 2011.xls", sheet_name="2011")
print("2011 read")
df2010 = pd.read_excel (r"C:\Users\Waut\Documents\Python Scripts\DATA\TASK 7307 Thefts and Physical harm to humans and property PE 2010.xls", sheet_name="2010")
print("2010 read")
df2009 = pd.read_excel (r"C:\Users\Waut\Documents\Python Scripts\DATA\TASK 7307 Thefts and Physical harm to humans and property PE 2009.xls", sheet_name="2009")
print("2009 read")
df2008 = pd.read_excel (r"C:\Users\Waut\Documents\Python Scripts\DATA\TASK 7307 Thefts and Physical harm to humans and property PE 2008.xls", sheet_name="2008")
print("2008 read")
df2007 = pd.read_excel (r"C:\Users\Waut\Documents\Python Scripts\DATA\TASK 7307 Thefts and Physical harm to humans and property PE 2007.xls", sheet_name="2007")
print("2007 read")
df2006 = pd.read_excel (r"C:\Users\Waut\Documents\Python Scripts\DATA\TASK 7307 Thefts and Physical harm to humans and property PE 2006.xls", sheet_name="2006")
print("2006 read")
df2005 = pd.read_excel (r"C:\Users\Waut\Documents\Python Scripts\DATA\TASK 7307 Thefts and Physical harm to humans and property PE 2005.xls", sheet_name="2005")
print("2005 read")
df2004 = pd.read_excel (r"C:\Users\Waut\Documents\Python Scripts\DATA\TASK 7307 Thefts and Physical harm to humans and property PE 2004.xls", sheet_name="2004")
print("2004 read")
df2003 = pd.read_excel (r"C:\Users\Waut\Documents\Python Scripts\DATA\TASK 7307 Thefts and Physical harm to humans and property PE 2003.xls", sheet_name="2003")
print("2003 read")
df2002 = pd.read_excel (r"C:\Users\Waut\Documents\Python Scripts\DATA\TASK 7307 Thefts and Physical harm to humans and property PE 2002.xls", sheet_name="2002")
print("2002 read")
df2001 = pd.read_excel (r"C:\Users\Waut\Documents\Python Scripts\DATA\TASK 7307 Thefts and Physical harm to humans and property PE 2001.xls", sheet_name="2001")
print("2001 read")
df2000 = pd.read_excel (r"C:\Users\Waut\Documents\Python Scripts\DATA\TASK 7307 Thefts and Physical harm to humans and property PE 2000.xls", sheet_name="2000")
print("2000 read")
df1999 = pd.read_excel (r"C:\Users\Waut\Documents\Python Scripts\DATA\TASK 7307 Thefts and Physical harm to humans and property PE 1999.xls", sheet_name="1999")
print("1999 read")
df1998 = pd.read_excel (r"C:\Users\Waut\Documents\Python Scripts\DATA\TASK 7307 Thefts and Physical harm to humans and property PE 1998.xls", sheet_name="1998")
print("1998 read")
df1997 = pd.read_excel (r"C:\Users\Waut\Documents\Python Scripts\DATA\TASK 7307 Thefts and Physical harm to humans and property PE 1997.xls", sheet_name="1997")
print("1997 read")
df1996 = pd.read_excel (r"C:\Users\Waut\Documents\Python Scripts\DATA\TASK 7307 Thefts and Physical harm to humans and property PE 1996.xls", sheet_name="1996")
print("1996 read")
print()

#REMOVE DUDS
df2016 = drop_duds(df2016, "2016")
df2016['SUBURB_FINAL'] = df2016['SUBURB1'].map(str) +' '+ df2016['SUBURB'].map(str)

df2015 = drop_duds(df2015, "2015")
df2015['SUBURB_FINAL'] = df2015['SUBURB1'].map(str) +' '+ df2015['SUBURB'].map(str)

df2014 = drop_duds(df2014, "2014")
df2014['SUBURB_FINAL'] = df2014['SUBURB1'].map(str) +' '+ df2014['SUBURB'].map(str)

df2013 = drop_duds(df2013, "2013")
df2013['SUBURB_FINAL'] = df2013['SUBURB1'].map(str) +' '+ df2013['SUBURB'].map(str)

df2012 = drop_duds(df2012, "2012")
df2012['SUBURB_FINAL'] = df2012['SUBURB1'].map(str) +' '+ df2012['SUBURB'].map(str)

df2011 = drop_duds(df2011, "2011")
df2011['SUBURB_FINAL'] = df2011['SUBURB1'].map(str) +' '+ df2011['SUBURB'].map(str)

df2010 = drop_duds(df2010, "2010")
df2010['SUBURB_FINAL'] = df2010['SUBURB1'].map(str) +' '+ df2010['SUBURB'].map(str)

df2009 = drop_duds(df2009, "2009")
df2009['SUBURB_FINAL'] = df2009['SUBURB1'].map(str) +' '+ df2009['SUBURB'].map(str)

df2008 = drop_duds(df2008, "2008")
df2008['SUBURB_FINAL'] = df2008['SUBURB1'].map(str) +' '+ df2008['SUBURB'].map(str)

df2007 = drop_duds(df2007, "2007")
df2007['SUBURB_FINAL'] = df2007['SUBURB1'].map(str) +' '+ df2007['SUBURB'].map(str)

df2006 = drop_duds(df2006, "2006")
df2006['SUBURB_FINAL'] = df2006['SUBURB1'].map(str) +' '+ df2006['SUBURB'].map(str)

df2005 = drop_duds(df2005, "2005")
df2005['SUBURB_FINAL'] = df2005['SUBURB1'].map(str) +' '+ df2005['SUBURB'].map(str)

df2004 = drop_duds(df2004, "2004")
df2004['SUBURB_FINAL'] = df2004['SUBURB1'].map(str) +' '+ df2004['SUBURB'].map(str)

df2003 = drop_duds(df2003, "2003")
df2003['SUBURB_FINAL'] = df2003['SUBURB1'].map(str) +' '+ df2003['SUBURB'].map(str)

df2002 = drop_duds(df2002, "2002")
df2002['SUBURB_FINAL'] = df2002['SUBURB1'].map(str) +' '+ df2002['SUBURB'].map(str)

df2001 = drop_duds(df2001, "2001")
df2001['SUBURB_FINAL'] = df2001['SUBURB1'].map(str) +' '+ df2001['SUBURB'].map(str)

df2000 = drop_duds(df2000, "2000")
df2000['SUBURB_FINAL'] = df2000['SUBURB1'].map(str) +' '+ df2000['SUBURB'].map(str)

df1999 = drop_duds(df1999, "1999")
df1999['SUBURB_FINAL'] = df1999['SUBURB1'].map(str) +' '+ df1999['SUBURB'].map(str)

df1998 = drop_duds(df1998, "1998")
df1998['SUBURB_FINAL'] = df1998['SUBURB1'].map(str) +' '+ df1998['SUBURB'].map(str)

df1997 = drop_duds(df1997, "1997")
df1997['SUBURB_FINAL'] = df1997['SUBURB1'].map(str) +' '+ df1997['SUBURB'].map(str)

df1996 = drop_duds(df1996, "1996")
df1996['SUBURB_FINAL'] = df1996['SUBURB1'].map(str) +' '+ df1996['SUBURB'].map(str)

print("Duds dropped and suburbs merged")
print()

#CONCACENATE
df = pd.concat([df2016, df2015, df2014, df2013, df2012, df2011, df2010, df2009, df2008, df2007, df2006, df2005, df2004, df2003, df2002, df2001, df2000, df1999, df1998, df1997, df1996], axis=0)
print("Concacenated: {}".format(df.shape))
print()

PE = pd.DataFrame()
PE['Station'] = df['STATION']
PE['Suburb'] = df['SUBURB_FINAL']
PE['Street'] = df['STREET_NAME1']
PE['Address'] = df['ADRES']
PE['Date'] = df['DATE_COMMITED']
print("Columns retrieved: {}".format(PE.shape))
print()

#print(PE.groupby('Suburb').count())
write_to_excel(PE)