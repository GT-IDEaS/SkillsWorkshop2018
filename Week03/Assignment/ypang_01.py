#!/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

#############################################
#         Challenge - Distributions         #
#############################################

surveys_df = pd.read_csv("data/surveys.csv")
species_df = pd.read_csv("data/species.csv")

merge_df = pd.merge(left=surveys_df, right=species_df, left_on="species_id",
        right_on="species_id")

# 1. taxa by plot
taxa_count = merge_df.groupby("taxa")["record_id"].count()
print(taxa_count)

fig = plt.figure()
ax = fig.add_axes([0.1, 0.4, 0.8, 0.55])
taxa_count.plot(kind="bar")

fig.savefig('ypang_01-1.png')
plt.show()

# 2. taxa by sex by plot
#for s in pd.unique(merge_df['sex']):
taxa_count = merge_df.groupby(["sex","taxa"])["record_id"].count()
#print(s)
print(taxa_count)

fig = plt.figure()
ax = fig.add_axes([0.1, 0.4, 0.8, 0.55])
taxa_count.plot(kind="bar")

fig.savefig('ypang_01-2.png')
plt.show()

