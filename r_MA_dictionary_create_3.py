from q_MA_dictionary_create_2 import dictbook
import os
from datetime import date
from datetime import datetime
today = date.today()
datetoday = today.strftime("%Y-%m-%d")
import json


paidloss=[]
keylist=[]
casereserves=[]
ibnrbalance=[]
earnedpremium=[]
ultimatelossratio=[]
for key in dictbook:
  print(key)
  print(dictbook[key]['Paid losses'])
  paidloss.append( dictbook[key]['Paid losses']*100)
  keylist.append(key)
  casereserves.append( dictbook[key]['Case reserves']*100)
  ibnrbalance.append( dictbook[key]['IBNR'])
  earnedpremium.append( dictbook[key]['Earned premium']*100)
  ultimatelossratiosum= dictbook[key]['IBNR']+dictbook[key]['Paid losses']+dictbook[key]['Case reserves']
  ultimatelossratio.append(ultimatelossratiosum*100)  
# print(paidloss)
# print(keylist)
# print(casereserves)
# print(ibnrbalance)
# print(earnedpremium)
# print(ultimatelossratio)
print(dictbook)
print("end")
# dictbook=[dict(zip(dictbook, ultimatelossratio))]
ultimate=["Ultimate Loss Ratio"]
# dictbook={dict(zip(ultimate, i)) for i in dictbook}     
# print(dictbook)        


####add calulcated ulitmate loss ratio
counter=0
for key in dictbook:
    for i , v in enumerate(ultimatelossratio):
       if i == (counter):
#         print("testtest")
#         print(i+counter)
         ultimatedict={"Ultimate Loss Ratio":v}
         dictbook[key].update(ultimatedict)
         lob={'LineofBusiness': 'GL-np'}   ##yes
         createdDate={"DWCreatedDate":datetoday} ##yes
         dwcreatedby={"DWCreatedBy":"KDKelly"}   ###yes
         dictbook[key].update(createdDate)
         dictbook[key].update(dwcreatedby)
         dictbook[key].update(lob)        
        
       else:
        pass
    counter=+1
print(dictbook)

FileNameJsonMABook=f"_Outputs/MA_Claim_Development_Fact_Data "+str(datetoday)+".json"
 
with open(FileNameJsonMABook, "w") as outfile:
    json.dump(dictbook, outfile)





labelsc =keylist
paidlossc = paidloss
casereservec = casereserves
ibnrc = ibnrbalance
earnedpremiumc=earnedpremium