
# coding: utf-8

# In[1]:


import pandas as pd
surveys_df = pd.read_csv("data/surveys.csv",
                         keep_default_na=False, na_values=[""])
species_df = pd.read_csv("data/species.csv",
                         keep_default_na=False, na_values=[""])


# In[3]:


merged_data = pd.merge(left=surveys_df,right=species_df, how='left', left_on='species_id', right_on='species_id')


# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[21]:


taxa_v_plot = merged_data.groupby('plot_id')['taxa'].nunique()
taxa_v_plot_sex = merged_data.groupby(['sex','plot_id'])['taxa'].nunique()


# In[14]:


plot_1 = taxa_v_plot.plot(kind = 'bar', title = 'Unique Taxa by Plot ID')
plot_1.set_ylabel("Number of Unique Taxa")


# In[22]:


plot_2 = taxa_v_plot_sex.plot(kind = 'bar', title = 'Unique Taxa by Plot ID and Sex')
plot_2.set_ylabel("Number of Unique Taxa")




# In[38]:


count = 0
start_year = 1977
for year in surveys_df['year'].unique():
    if year == start_year + (5*count):
        surveys_year = surveys_df[surveys_df.year == year].dropna()
        filename = 'data/yearly_files/' + str(year) + '.csv'
        surveys_year.to_csv(filename)
        count += 1


# In[42]:


for species in surveys_df['species_id'].unique():
    surveys_species = surveys_df[surveys_df.species_id == species].dropna()
    filename = 'data/species_files/' + str(species) + '.csv'
    surveys_species.to_csv(filename)
        


# In[44]:


bouldercreek_df = pd.read_csv("bouldercreek.txt", sep = "\t", names = ('agency','site_no','date_time','tz_cd', '04_00060','04_00060_cd'))
bouldercreek_df


# In[50]:


discharge_df = bouldercreek_df.drop(['agency','tz_cd','04_00060_cd'], axis = 1)
discharge_df['date'] = bouldercreek_df['date_time'].str.split(" ").str[0]
discharge_df['time'] = bouldercreek_df['date_time'].str.split(" ").str[1]
discharge_df


# In[51]:


from matplotlib import pyplot as plt


# In[54]:


plt.plot(discharge_df['date_time'],discharge_df['04_00060'])
plt.xlabel('Measurement Date & Time')
plt.ylabel('Water Discharge (ft^3/s)')
plt.title ('Water Dicharge for September 2013')


# In[60]:


flood_df = discharge_df[(discharge_df['date'] >= '2013-09-09') & (discharge_df['date'] <= '2013-09-15')]

plt.plot(flood_df['date_time'],flood_df['04_00060'])
plt.xlabel('Measurement Date & Time')
plt.ylabel('Water Discharge (ft^3/s)')
plt.title ('Water Dicharge During Flood')


# In[70]:


for measurement, time in discharge_df.groupby('time'):
    plt.plot(x = time['date'], y= time['04_00060'], title = measurement)    


# In[85]:


max_discharge = discharge_df.groupby('date')['04_00060'].max() 
min_discharge = discharge_df.groupby('date')['04_00060'].min() 
avg_discharge = discharge_df.groupby('date')['04_00060'].mean() 

plt.figure(1)

plt.subplot(3,1,1)
plt.plot(max_discharge)
plt.title('Maximum Water Discharge')
plt.xticks([]);

plt.subplot(3,1,2)
plt.plot(min_discharge)
plt.title('Minimum Water Discharge')
plt.xticks([])
plt.ylabel ('Water Discharge ft^3/s)')

plt.subplot(3,1,3)
plt.plot(avg_discharge)
plt.title('Averge Water Discharge')
plt.xticks(rotation = 45);
plt.xlabel('Measurement Date')

