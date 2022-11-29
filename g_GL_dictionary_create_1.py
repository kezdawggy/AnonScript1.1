####Build GL-np Dictionary  Stats
from d_GL_gather_stats import prem_stats
from f_fix_header import headerstatsfinal
from e_GL_gather_year import year
import json
import os
from datetime import date
from datetime import datetime
today = date.today()
datetoday = today.strftime("%Y-%m-%d")

# print(data)
# print([dict(zip(headerstatsfinal, i)) for i in prem_stats])
dictstats=[dict(zip(headerstatsfinal, i)) for i in prem_stats]
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
            lob={'LineofBusiness': 'GL-np'}
            dwcrreatedDate={"DWCreatedDate":datetoday}
            dwcreatedby={"DWCreatedBy":"KDKelly"}
            dictstats[key].update(yeardict)
            dictstats[key].update(compname)
            dictstats[key].update(dwcrreatedDate)
            dictstats[key].update(dwcreatedby)
     
        else:
            pass  
    counter=counter+1 
        
    


# print(dictstats)


print("jsontest")
print(json.dumps(dictstats))













# Method 1
import pandas as pd
df = pd.DataFrame(dictstats)
df.to_csv('my_file.csv', index=False, header=True)