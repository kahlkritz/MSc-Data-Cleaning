#LIBRARIES
import pandas as pd

#VARIABLES

########FUNCTIONS#############

def drop_duds(df, year):
    tempInd = df[ df['PROVINCE'] != "P COMM EASTERN CAPE" ].index
    # Delete these row indexes from dataFrame
    df.drop(tempInd , inplace=True)
    print("{} cleaned".format(year))
    return df;

def drop_suburbs(df):
    temp = df[df["Suburb"] != "PORT ELIZABETH CENTRAL"].index
    df.drop(temp, inplace=True)
    return temp;

def groupby_category(df):
    subcount = df.groupby(['Suburb']).count()
    subcount.to_excel(r'subcount.xlsx')
    print("DONE")
    return subcount;
    
def write_to_excel(df):
    print()
    print("Writing do Excel File....")
    df.to_excel(r'C:\Users\Waut\Documents\Python Scripts\DATA\PyDB\Humewood Station.xlsx')
    print("Written to excel file")
    return;  

########FUNCTIONS#############

#Read DB's from Excel
print("Reading from Excel....")
PE = pd.read_excel (r"C:\Users\Waut\Documents\Python Scripts\DATA\PyDB\PE 96-16.xlsx")
print("cleaned read into PE:")
print(PE.shape)
print()

#Extract using key words
#summerstrandEng = PE
summerstrandEng = PE.set_index('Suburb').filter(like='SUM', axis=0)
for i in summerstrandEng.index:
    summerstrandEng.loc[i,'Suburb'] = "summerstrand"
print("Summerstrand shape")
print(summerstrandEng.shape)

#summerstrandAfr = PE
summerstrandAfr = PE.set_index('Suburb').filter(like='SOM', axis=0)
for i in summerstrandAfr.index:
    summerstrandAfr.loc[i,'Suburb'] = "summerstrand"
print("Somerstrand shape")
print(summerstrandAfr.shape)

#walmer = PE
walmer = PE.set_index('Suburb').filter(like='WALM', axis=0)
for i in walmer.index:
    walmer.loc[i,'Suburb'] = "walmer"
print("Walmer shape")
print(walmer.shape)

#humewood = PE
humewood = PE.set_index('Suburb').filter(like='HUME', axis=0)
for i in humewood.index:
    humewood.loc[i,'Suburb'] = "humewood"
print("Humewood shape")
print(humewood.shape)

#schoenmakerskop = PE
schoenmakerskop = PE.set_index('Suburb').filter(like='SKOP', axis=0)
for i in schoenmakerskop.index:
    schoenmakerskop.loc[i,'Suburb'] = "schoenmakerskop"
print("Schoenies shape")
print(schoenmakerskop.shape)

#southendEng = PE
southendEng = PE.set_index('Suburb').filter(like='SOUTH', axis=0)
for i in southendEng.index:
    southendEng.loc[i,'Suburb'] = "south end"
print("Southend shape")
print(southendEng.shape)

#southendAfr = PE
southendAfr = PE.set_index('Suburb').filter(like='SUID', axis=0)
for i in southendAfr.index:
    southendAfr.loc[i,'Suburb'] = "south end"
print("Southend shape")
print(southendAfr.shape)

#airport = PE
airport = PE.set_index('Suburb').filter(like='AIRP', axis=0)
for i in airport.index:
    airport.loc[i,'Suburb'] = "airport"
print("Airport shape")
print(airport.shape)

#Concatenate
print()
humestation = pd.concat([summerstrandEng, summerstrandAfr, walmer, humewood, schoenmakerskop, southendEng, southendAfr, airport], axis=0)
print("Station:")
print(humestation.shape)

print()
print("Writing do Excel File....")
humestation.to_excel(r'C:\Users\Waut\Documents\Python Scripts\DATA\PyDB\Humewood Station_test.xlsx')
print("Written to excel file")