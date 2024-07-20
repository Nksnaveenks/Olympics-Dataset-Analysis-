#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn


# In[3]:


athletes=pd.read_csv("athlete_events.csv")
regions=pd.read_csv("noc_regions.csv")


# In[4]:


athletes.head()


# In[5]:


regions.head()


# In[6]:


#join the dataframes 
#using pandas merge method
athletes_df=athletes.merge(regions,how="left",on="NOC")
athletes_df


# In[7]:


#shape of the dataframes
athletes_df.shape


# In[8]:


#rename function t0 make the columns name consistent
#athletes_df.columns.str.capitalize()
athletes_df.rename(columns={'region':'Region','notes':'Notes'},inplace=True);


# In[9]:


athletes_df.head()


# In[10]:


#information about the dataframes
athletes_df.info()


# In[11]:


#only describe the numerical value
athletes_df.describe()


# In[12]:


#check null vlaues
#True->messing value
#False->Non Messing values
nan_values=athletes_df.isna()
nan_columns=nan_values.any()
nan_columns


# In[13]:


athletes_df.isnull().sum()


# In[14]:


#Data for specific country
#athletes participate in the olympics from begining for india
athletes_df.query('Team=="India"').head(5)


# In[15]:


athletes_df.query('Team=="Japan"').head(5)


# In[16]:


#Top 10 countries participateing from begining
top_10_countries=athletes_df.Team.value_counts().sort_values(ascending=False).head(10)
top_10_countries


# In[21]:


#plot for the top 10 countries
plt.figure(figsize=(12,6))
plt.title('Overall Participation by Country')
sn.barplot(x=top_10_countries.index,y=top_10_countries,palette="Set1")


# In[27]:


# age Distribution of the participants
import matplotlib.pyplot as plt
plt.figure(figsize=(12,6))
plt.title('Age Distribution of the participants')
plt.xlabel("Age")
plt.ylabel("Number of participants")
plt.hist(athletes_df.Age, bins = np.arange(10,80,2),color="orange",edgecolor="Blue")


# In[19]:


#winter olympics
winter_sports=athletes_df[athletes_df.Season=='Winter'].Sport.unique()
winter_sports


# In[20]:


#summer olympics
summer_sports=athletes_df[athletes_df.Season=='Summer'].Sport.unique()
summer_sports


# In[29]:


#Total numbers of Males and Female Participants
gender_counts=athletes_df.Sex.value_counts()
gender_counts


# In[35]:


#pie plot for male and female athletes
plt.figure(figsize=(12,6))
plt.title('Gendrer Distribution')
#explode=(0.1,0)
plt.pie(gender_counts,labels=gender_counts.index,autopct='%1.1f%%',startangle=150,shadow=True)#,explode=explode)


# In[33]:


#Total medals 
athletes_df.Medal.value_counts()


# In[34]:


#Total number of female athletes in each olympics.
female_participants=athletes_df[(athletes_df.Sex=='F')& (athletes_df.Season=='Summer')][['Sex','Year']]
female_participants=female_participants.groupby('Year').count().reset_index()
female_participants.head()


# In[35]:


female_participants.tail()


# In[36]:


#
womenOlympics=athletes_df[(athletes_df.Sex=='F')&(athletes_df.Season=='Summer')]


# In[27]:


sn.set(style="darkgrid")
plt.figure(figsize=(20,10))
sn.countplot(x='Year',data=womenOlympics,palette="Spectral")
plt.title("Women Participation")


# In[43]:


#
menOlympics=athletes_df[(athletes_df.Sex=='M')&(athletes_df.Season=='Summer')]


# In[45]:


sn.set(style="darkgrid")
plt.figure(figsize=(20,10))
sn.countplot(x='Year',data=menOlympics,palette="Spectral")
plt.title("Men Participation")


# In[28]:


# line graph for female athletes over time
part=womenOlympics.groupby('Year')['Sex'].value_counts()
part.loc[:,'F'].plot()
plt.title("Plot of Female Athletes over Time")


# In[46]:


# line graph for male athletes over time
part=menOlympics.groupby('Year')['Sex'].value_counts()
part.loc[:,'M'].plot()
plt.title("Plot of Male Athletes over Time")


# In[29]:


#Gold medal athletes
goldMedals=athletes_df[(athletes_df.Medal=='Gold')]
goldMedals


# In[30]:


#
nan_values=athletes_df.isna()
nan_columns=nan_values.any()
nan_columns


# In[31]:


athletes_df.isnull().sum()


# In[32]:


athletes_df.isnull().sum()['Age']


# In[33]:


#take only the values that areifferent from NaN
goldMedal=goldMedals[np.isfinite(goldMedals['Age'])]


# In[34]:


#GoldMedals beyond 60(more than 60 years)
goldMedals['ID'][goldMedals['Age']>60].count()


# In[35]:


#GoldMedals with in  60(less than 60 years)
goldMedals['ID'][goldMedals['Age']<60].count()


# In[36]:


#check which sports these goldMedal comes 
sporting_event=goldMedals['Sport'][goldMedals['Age']>60]
sporting_event


# In[37]:


#Gold Medals from each country
totalGoldMedals=goldMedals.Region.value_counts().reset_index(name='Medal').head(8)
totalGoldMedals


# In[38]:


g=sn.catplot(x='Region',y='Medal',data=totalGoldMedals,height=5,kind='bar')
g.set_xlabels('Top 5 countries')
g.set_ylabels('Number of Medals')
plt.title('Gold MEdals per Country')


# In[39]:


#Rio olympics(2016 analysis)
max_year=athletes_df.Year.max()
print(max_year)

team_names=athletes_df[(athletes_df.Year==max_year)&(athletes_df.Medal=='Gold')].Team
team_names.value_counts().head(10)


# In[40]:


#
sn.barplot(x=team_names.value_counts().head(20),y=team_names.value_counts().head(20).index)
plt.xlabel('Countrywise Medals for the year 2016')


# In[41]:


#scatter plot for height and wieght of male and femal authletes 
#to drop all null value in medals column
not_null_medals=athletes_df[(athletes_df['Height'].notnull())&(athletes_df['Weight'].notnull())]


# In[42]:


plt.figure(figsize=(12,10))
axis=sn.scatterplot(x='Height',y='Weight',data=not_null_medals,hue='Sex')
plt.title('Height vs Weight of Olympic Medalists')

