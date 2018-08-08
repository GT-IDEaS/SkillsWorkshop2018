#Assignment 4 
import pandas as pd 
from matplotlib import pyplot as plt
#The chosen Final Challenge is "Challenge - Distributions"
#1. Plot taxa 
#2. Plot taxa by sex
surveys_df = pd.read_csv("surveys.csv")
species_df = pd.read_csv("species.csv")
head = surveys_df.columns.values
#print(head)
#taxa is index 3
merged_inner = pd.merge(left=surveys_df,right=species_df, left_on='species_id', right_on='species_id')
#head = merged_inner.columns.values
#print(head)
species_counts = merged_inner.groupby('species_id')['taxa'].count()
species_counts.plot(kind='bar')
plt.title('Species ID vs. Taxa')
plt.xlabel('Species ID')
plt.ylabel('Taxa Count')
plt.savefig('ACHOI_03_01')
Female = merged_inner.loc[merged_inner['sex'] == 'F']
Male = merged_inner.loc[merged_inner['sex'] == 'M']
Fpd = Female.groupby('species_id')['taxa'].count()
Mpd = Male.groupby('species_id')['taxa'].count()
Fpd.plot(kind='bar',label = 'Female',hatch="/",alpha = 0.7)
Mpd.plot(kind='bar', label = 'Male',hatch=".", alpha = 0.7)
plt.legend()
plt.savefig('ACHOI_03_02')