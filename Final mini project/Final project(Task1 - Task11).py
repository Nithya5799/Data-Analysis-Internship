#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Task 1

import pandas as pd
df_activities = pd.read_csv("Desktop/cardioActivities.csv", parse_dates=["Date"], index_col=["Date"])
df_activities

print(df_activities.sample())

print(df_activities.info())

cols_to_drop = ["Friend's Tagged", "Route Name"]

df_activities.drop(cols_to_drop, axis=1, inplace=True)
df_activities.head(3)


# In[9]:


# Task 2

# calculating the activity type
counts = df_activities["Type"].value_counts()
print(counts)

# Renaming the " Other " type in "Type " column to " Unicycling "
df_activities["Type"] = df_activities["Type"].replace(["Other"],"Unicycling")
df_activities["Type"].value_counts()

# calculating missing values in our dataset
df_activities.isnull().sum()

#dropping more columns which we don't need
cols_drop = ["Notes", "Activity Id", "Calories Burned", "GPX File"]
df_activities.drop(cols_drop, inplace=True, axis=1)

df_activities


# In[6]:


# Task 3

# calculating mean for each activity Type

import matplotlib.pyplot as plt
avg_hr_cycle = df_activities[df_activities["Type"]== "Running"]["Average Heart Rate (bpm)"].mean()
avg_hr_cycle

# filterring the df_cycle value
df_cycle = df_activities[df_activities["Type"]=="Cycling"].copy()
df_cycle

# filling in the missing values
df_cycle["Average Heart Rate (bpm)"].fillna(int(avg_hr_cycle), inplace=True)

#dropping more columns
df_cycle.drop(["Route Name","Friend's Tagged"], inplace=True,axis=1)

# checking for mising values after the filteratio
df_cycle.isnull().sum()

# Similar operations for df_run
avg_hr_run = df_activities[df_activities["Type"]=="Running"]["Average Heart Rate (bpm)"].mean()
df_run = df_activities[df_activities["Type"] == "Running"].copy()
df_run["Average Heart Rate (bpm)"].fillna(int(avg_hr_run), inplace=True)

#dropping unnecessary columns in df_run
df_run.drop(["Route Name", "Friend's Tagged"], inplace=True, axis=1)
df_run.isnull().sum()


# In[7]:


# Task 4

## plotting the runnin Data

import matplotlib.pyplot as plt
# subsetting the data from 2013 to 2018
runs_subset_2013_2018 = df_run.loc["20190101":"20130101"]

# plotting
runs_subset_2013_2018.plot(subplots=True, sharex=False, figsize=(12,16), marker="o", markersize=3)
plt.show()


# In[10]:


#Task 5

#subplotting from 2015 - 2018
runs_subset_2015_2018 = df_run.loc["20190101":"20150101"]
# Anuual statitics
print("Average of my stats from last 4 years")
display(runs_subset_2015_2018.resample("A").mean())

# Weekly Statistics
print("Weekly stats of last 4 years")
display(runs_subset_2015_2018.resample("W").mean().mean())

# Mean Weekly counts for Distance
weekly_counts_average = runs_subset_2015_2018["Distance (km)"].resample("W").count().mean()
weekly_counts_average


# In[11]:


# Task 6

# subsetting the data
runs_distance = runs_subset_2015_2018["Distance (km)"]
runs_hr = runs_subset_2015_2018["Average Heart Rate (bpm)"]
# createing plot

fig, (ax1,ax2) = plt.subplots(2, sharex=True, figsize=(12,8))
# First subplot
runs_distance.plot(ax=ax1)
ax1.set(ylabel="Dsitance (km)", title="historica Data with Avergaes")
ax1.axhline(runs_distance.mean(),color="red", linewidth=1, linestyle="-.")

# Second Subplot
runs_hr.plot(ax=ax2, color="gray")
ax2.set(xlabel="Date", ylabel="Average Heart Rate (bpm)")
ax2.axhline(runs_hr.mean(), color="blue", linewidth=1, linestyle="-.")

plt.show()


# In[12]:


# Task 7

# reampling the Data
df_run_dist_annual = df_run.sort_index()["20130101":"20181231"]["Distance (km)"].resample("A").sum()
fig = plt.figure(figsize=(8,5))
# customizing the plot
ax = df_run_dist_annual.plot(marker="*", markersize=14, linewidth=0, color="blue")
ax.set(ylim=[0,800],xlim=["2012","2019"],ylabel="Distance (km)", xlabel="years", title="Annual Years for distance")
ax.axhspan(0,800, color="red", alpha=0.2)
plt.show()


# In[13]:


# Task 8

import statsmodels.api as sm
df_run_dist_wikly = df_run.loc["20190101":"20130101"]["Distance (km)"].resample("W").bfill()
fig = plt.figure(figsize=(12,5))
ax = df_run_dist_wikly.plot(label="Trend", linewidth=2)
ax.legend()
ax.set_title("Running distance trend")
plt.show()


# In[14]:


# Task 9

df_run_hr_all = df_run.loc["20190101":"20150301"]["Average Heart Rate (bpm)"]
# xtick labels
hr_zones = [100,125,133,142,151,173]
zone_names = ["Eazy", "Moderate", "hard", "Very Hard", "maximal","Extreme"]
fig , ax = plt.subplots(figsize=(8,5))
ax.grid(True)
ax.hist(df_run_hr_all,bins=hr_zones)
ax.xaxis.set(ticks=hr_zones)
ax.set(title="Dsitribution of HR", ylabel="Number of runs")
ax.set_xticklabels(labels=zone_names, rotation=-30, ha="left")
plt.show()


# In[15]:


# Task 10

# creating the walk dataframe
df_walk = df_activities[df_activities["Type"]=="Walking"].copy()
df_walk["Average Heart Rate (bpm)"].fillna(110,inplace=True)
df_walk.drop(["Route Name","Friend's Tagged"], inplace=True, axis=1)

# checking for null values
print(df_walk.isnull().sum())

# concatenating the df_run, df_walk & df_cycle DataFrame
df_run_walk_cycle = df_run.append([df_walk, df_cycle]).sort_index(ascending=False)

dist_climb_cols, speed_col = ["Distance (km)","Climb (m)"],["Average Heart Rate (bpm)"]

# calcultating total distance and climb in each activity type
df_totals = df_run_walk_cycle.groupby("Type")[dist_climb_cols].sum()
display(df_totals)

# full summary report
df_summary = df_run_walk_cycle.groupby("Type")[dist_climb_cols + speed_col].describe()

# total summary 
for i in dist_climb_cols:
  df_summary[i, "total"] = df_totals[i]
print("Total Statistics")
df_summary.stack()


# In[16]:


# Task 11

# average shoes for lifetime
average_shoes_lifetime = 5224/7

#number of shoes for forest run
shoes_for_forrest_run = 24700//average_shoes_lifetime
print(shoes_for_forrest_run)


# In[ ]:




