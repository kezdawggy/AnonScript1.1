from p_MA_gather_book import booked_data, bookedheader
from m_MA_gather_year import year


# print(data)
# print([dict(zip(headerstatsfinal, i)) for i in prem_stats])
dictbook=[dict(zip(bookedheader, i)) for i in booked_data]
# print(dictbook)
dictbook=[dict(zip(year, dictbook))]
# print(dictbook)
# dictcapture={}
# line_of_business=['GL-np']
# dictbook=[dict(zip(line_of_business, dictbook))]
# print(dictbook)
# for i in data:
#     print(i) 
#     print(headerstatsfinal)
    
# #    dictcapture=dict(zip(i,headerstatsfinal)
# print(dictcapture)


from collections import ChainMap

dictbook = dict(ChainMap(*dictbook))
print(dictbook)