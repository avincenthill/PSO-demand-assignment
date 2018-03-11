#PSO Demand Assignment
#Alex "AVH" Vincent-Hill

import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
import pandas as pd

#UUID v4 comparator regexes for ios and google ids
iospattern = r"^[0-9A-F]{8}-[0-9A-F]{4}-[4][0-9A-F]{3}-[89AB][0-9A-F]{3}-[0-9A-F]{12}$"
googlepattern = r"^[0-9a-f]{8}-[0-9a-f]{4}-[4][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"

#read csv into dataframe
df = pd.read_csv('./data/Sample-click-log.csv', encoding='latin1')

#filter df with regex id validations
fdf = df[(df['ios_ifa'].str.contains(iospattern, regex=True)) ^ (df['google_aid'].str.contains(googlepattern, regex=True))]

#remove duplicates from fdf
udf = fdf.drop_duplicates(subset={'ios_ifa','google_aid'})

#1a for every affiliate_id(Col B), calculate the unique ios_ifa(Col K) & google_aid(Col L) present in the data
uniqueaffiliateids = udf.affiliate_id.unique()

for affiliateid in uniqueaffiliateids:
	tempdfgoogle = udf[(udf.affiliate_id == affiliateid) & ~(udf.google_aid.empty)]
	tempdfios  = udf[(udf.affiliate_id == affiliateid) & (udf.device_os == 'iOS')] 
	count = len(tempdfgoogle)
	countios = len(tempdfios)
	#pprint(count)
	#pprint(countios)


#1b calculate how many valid google_aid & ios_ifa exist in the dataset



#2.1 plot a histogram from the data obtained from exercise 1a



#2.2 plot a histogram of the no. of clicks v/s affiliate_id in the dataset
clickdata = pd.DataFrame(columns = ['affiliate_ids', 'clicks'])
for i, affiliateid in enumerate(uniqueaffiliateids):
	clicks = len(fdf[fdf.affiliate_id == affiliateid])
	clickdata.loc[i] = [affiliateid, clicks]	

clickdata.plot(kind = 'bar', x='affiliate_ids', y='clicks')
plt.show() 
