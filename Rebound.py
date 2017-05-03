import pandas as pd
from matplotlib import pyplot as plt
print('Data source is from a Baltic Sea shoreline near Blankaholm, Kalmar Province, Sweden')
##find and read data
data = pd.read_excel('../../Fennoscandia_rebound.xlsx', header = 14)

#labels!! goal in naming is to combine descriptions with making things
#reasonable to type in later portions of the code
data.columns = ['years_ka_BP','years(AD)','meters','extra']
sea_level = data['meters']
years = data['years_ka_BP']

#finding meters of uplift rather than relative sea level
uplift = []
for i in range(0,len(sea_level)):
    a = sea_level[0] - sea_level[i]
    uplift.append(a)

## Modify the years value given so x label is in years rather than ka  
mod_years = []
for i in range(0,len(years)):
    y = years[i]*1000.0
    mod_years.append(y)

##plot sea level over time
fig1 = plt.figure()
plot1 = fig1.add_subplot(3,1,1)
plot1.plot(mod_years,data['meters'])
plt.gca().invert_xaxis()
plt.title('Relative Sea Level Over Time', fontweight = 'bold')
plt.ylabel('Mean Sea Level (m)')
plt.xlabel('Years Before Present')



##plot meters of uplift over time
plot2 = fig1.add_subplot(3,1,3)
plot2.plot(mod_years,uplift)
plt.gca().invert_xaxis()
plt.title('Meters of Uplift Over Time Due to Isostatic Rebound', fontweight = 'bold')
plt.ylabel('Meters of Uplift Since 5400 kya (m)')
plt.xlabel('Years Before Present')
plt.show()

##Lets see how uplift rate changes with time!

##get the rates
rate = []
for i in range(0,len(sea_level)-1):
    r = ((sea_level[i]-sea_level[i+1])/(mod_years[i]-mod_years[i+1]))
    rate.append(r)

## modify time so there is same amount of data points
mod_year_rate = []
for i in range (1,len(mod_years)):
    m = mod_years[i]
    mod_year_rate.append(m)

## And we plot!
plt.plot(mod_year_rate,rate)
plt.gca().invert_xaxis()
plt.title('Uplift Rate Over Time', fontweight = 'bold')
plt.xlabel('Years Before Present')
plt.ylabel('Uplift Rate, (m/yr)')
plt.show()

                                        
                                        
    
