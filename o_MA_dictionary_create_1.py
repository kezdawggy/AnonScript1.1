from n_MA_fix_header import headerstats, headerstatsfinal
from lb_MA_gather_stats import prem_stats
from m_MA_gather_year import year
####Build MA-np Dictionary  Stats
import json
import os
from datetime import date
from datetime import datetime
today = date.today()
datetoday = today.strftime("%Y-%m-%d")
import csv
print("Blights ")
print("test",prem_stats)

# print(data)
# print([dict(zip(headerstatsfinal, i)) for i in prem_stats])
dictstats=[dict(zip(headerstatsfinal, i)) for i in prem_stats]
print(dictstats)
# print(dictstats)
dictstats=[dict(zip(year, dictstats))]
# print(dictstats)
# dictcapture={}
# line_of_business=['GL-np']
# dictstats=[dict(zip(line_of_business, dictstats))]
# print(dictstats)
# for i in data:
#     print(i) 
#     print(headerstatsfinal)
    
# #    dictcapture=dict(zip(i,headerstatsfinal)
# print(dictcapture)
from collections import ChainMap

dictstats = dict(ChainMap(*dictstats))
print(dictstats)

# dictstats.to_csv("GL-np")

####add last elements to Dictionary
counter=0
for key in dictstats:
    print(key)
    for i , v in enumerate(year):
        print(f'{i} {key} {counter}')
        if i == (counter):
#           print("testtest")
#           print(i+counter)
            yeardict={"Year":v}
            compname={'CompanyName':'XYZ'}
            lob={'LineofBusiness': 'MA-np'}
            dwcrreatedDate={"DWCreatedDate":datetoday}
            dwcreatedby={"DWCreatedBy":"KDKelly"}
            dictstats[key].update(yeardict)
            dictstats[key].update(compname)
            dictstats[key].update(dwcrreatedDate)
            dictstats[key].update(dwcreatedby)
            dictstats[key].update(lob)
     
        else:
            pass  
    counter=counter+1 
        
# csv_file=f"_Outputs/MA_Claim_Development_Fact_Statistical "+str(datetoday)+".csv"  

# csv_columns=[12, 24 ,36, 48, 60, 72, 84, 96, 108, 120, 132, 144, 'Gross written premium', 'DWCreatedBy', 'Year', 'CompanyName', 'DWCreatedDate']

# csv_columns=["CompanyName", "Year", "LineofBusiness",12, 24 ,36, 48, 60, 72, 84, 96, 108, 120, 132, 144, 'Gross written premium', 'DWCreatedBy', 'DWCreatedDate']



# try:
#     with open(csv_file, 'w') as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
#         writer.writeheader()
#         for data in dictstats:
          
#             writer.writerow(dictstats[key])
# except IOError:
#     print("I/O error")



# print(dictstats)


print("jsontest")
print(json.dumps(dictstats))

 
FileNameJsonMAStat=f"_Outputs/MA_Claim_Development_Fact_Statistical "+str(datetoday)+".json"
 
with open(FileNameJsonMAStat, "w") as outfile:
    json.dump(dictstats, outfile)





