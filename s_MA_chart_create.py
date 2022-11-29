import os
from datetime import date
from datetime import datetime
today = date.today()
datetoday = today.strftime("%Y-%m-%d")








from r_MA_dictionary_create_3 import earnedpremiumc, labelsc, ultimatelossratio, paidlossc, casereservec, ibnrc

import matplotlib.pyplot as plt

# create figure and axis objects with subplots()
fig,ax = plt.subplots()
# make a plot


print(earnedpremiumc)


# ax.plot(labelsc,earnedpremiumc, label='Earned premium')
# ax.plot(labelsc,earnedpremiumc, label='Earned premium')
ax.plot(labelsc,ultimatelossratio,label='Ulimate Loss Ratio',color="red")   
# set x-axis label
ax.set_xlabel("year", fontsize = 14)
# set y-axis label
ax.set_ylabel("Ulimate loss ratio split",
              color="red",
              fontsize=14)



# twin object for two different y-axis on the sample plot
ax2=ax.twinx()

ax2.bar(labelsc,paidlossc,label='Paid losses')
ax2.bar(labelsc,casereservec,label='Case reserves')
ax2.bar(labelsc,ibnrc,label='IBNR balance') 

# make a plot with different y-axis using second axis object
# ax2.plot(labelsc,earnedpremiumc, label='Earned premium')
# ax2.plot(gapminder_us.year, gapminder_us["gdpPercap"],color="blue",marker="o")
ax2.set_ylabel("EArned Premium",color="blue",fontsize=14)
# plt.show()
# save the plot as a file
fig.savefig('_Outputs/MA_Ultimate_Loss_Ratio_'+str(datetoday)+'.jpg',
            format='jpeg',
            dpi=100,
            bbox_inches='tight')





