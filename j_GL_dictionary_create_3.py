from i_GL_dictionary_create_2 import dictbook


####extract year ##########

# x = dictbook.get('Earned premium')
# print(x)

# for key in dictbook.iterritems():
#     print(f'{key}')


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
        
        
       else:
        pass
    counter=+1
print(dictbook)







labelsc =keylist
paidlossc = paidloss
casereservec = casereserves
ibnrc = ibnrbalance
earnedpremiumc=earnedpremium