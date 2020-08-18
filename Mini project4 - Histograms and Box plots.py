#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
reviews = pd.read_csv("Desktop/fandango_scores.csv")
cols = ["FILM", "RT_user_norm", "Metacritic_user_nom", "IMDB_norm", "Fandango_Ratingvalue"]
norm_reviews = reviews[cols]
norm_reviews.head()


# In[3]:


# computing frequency distribution of user Ratings
fandango_freq = norm_reviews["Fandango_Ratingvalue"].value_counts()
imdb_freq = norm_reviews["IMDB_norm"].value_counts()
fandango_distribution = fandango_freq.sort_index()
imdb_distribution = imdb_freq.sort_index()
print(imdb_distribution)
print(fandango_distribution)


# In[12]:


import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.hist(norm_reveiws["Fandango_Ratingvalue"], range=(0,5))
plt.show()


# In[7]:


import matplotlib.pyplot as plt
fig = plt.figure(figsize=(5,20))
ax1 = fig.add_subplot(4,1,1)
ax1.hist(norm_reveiws["Fandango_Ratingvalue"],range=(0,5))
ax1.set_title("Distribution of Fandango Ratings")
ax2 = fig.add_subplot(4,1,2)
ax2.hist(norm_reveiws["RT_user_norm"],20, range=(0,5))
ax2.set_title("Distribution of Rotten Tomaotes Ratings")
ax3 = fig.add_subplot(4,1,3)
ax3.hist(norm_reveiws["Metacritic_user_nom"],20,range=(0,5))
ax3.set_title("Distribution of Metaritic Ratings")
ax4 = fig.add_subplot(4,1,4)
ax4.hist(norm_reveiws["IMDB_norm"],20,range=(0,5))
ax4.set_title("Distribution of IMDB Ratings")
ax.set_ylim([0,50])
plt.show()


# In[9]:


fig ,ax = plt.subplots()
ax.boxplot(norm_reviews["RT_user_norm"])
ax.set_ylim([0,5])
ax.set_xticklabels("Rotten Tomatoes")
plt.show()


# In[10]:


# Multiple boxplots
fig, ax= plt.subplots()
num_cols = ["RT_user_norm", "Metacritic_user_nom", "IMDB_norm", "Fandango_Ratingvalue"]
ax.boxplot(norm_reveiws[num_cols].values)
ax.set_xticklabels(num_cols, rotation=90)
ax.set_ylim([0,5])
plt.show()


# In[ ]:




