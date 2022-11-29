import os
from datetime import date
from datetime import datetime
today = date.today()
datetoday = today.strftime("%Y-%m-%d")




####FX
import csv
import pandas as pd
import datetime
from forex_python.converter import CurrencyRates
c=CurrencyRates()
# print(c.get_rates("USD"))
date_obj=datetime.datetime(2022, 2, 2, 18, 36, 28, 151012)
dateobjcust=date_obj.strftime("%Y-%m-%d")
print(dateobjcust)
print(c.get_rates('USD', date_obj) )
capture=c.get_rates('USD', date_obj) 
headers=["Rate_Type", "Date", "Currency_From", "Currency_From_Value", "Currency_To", "Currency_To_Value"]
Rate_Type="Spot_Rate"
CurrencyFrom="USD"
# df = pd.read_csv ('_Outputs/FX.csv',"w")
myFile = open('_Outputs/FX.csv',"w")

L=[]
counter=0
for i ,v in capture.items():
  if counter <10:
     print(f'{Rate_Type} {dateobjcust}  {CurrencyFrom}  {i} {v}')
     L.append(f'{Rate_Type} {dateobjcust} {i} {v} {CurrencyFrom} {1/v}')
     counter=counter+1
     print(counter)
  else:
    pass
  
   

print(L)

writer = csv.writer(myFile, delimiter=' ')
writer.writerow(headers)
writer = csv.writer(myFile, delimiter='\n')
writer.writerow(L)
myFile.close()