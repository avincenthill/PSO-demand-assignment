#PSO Demand Assignment
#Alex "AVH" Vincent-Hill

import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
import pandas as pd

#UUID v4 comparator regexes for ios and google ids - I think these regexes are too strict for this assignment and are rejecting valid google_aids
iospattern = r"^[0-9A-F]{8}-[0-9A-F]{4}-[4][0-9A-F]{3}-[89AB][0-9A-F]{3}-[0-9A-F]{12}$"
googlepattern = r"^[0-9a-f]{8}-[0-9a-f]{4}-[4][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"

#read csv into dataframe
df = pd.read_csv('./data/Sample-click-log.csv', encoding='latin1')

#filter df with regex id validations
fdf = df[(df['ios_ifa'].str.contains(iospattern, regex=True)) ^ (df['google_aid'].str.contains(googlepattern, regex=True))]

#remove duplicates from fdf to create dataframe of uniques, udf
udf = fdf.drop_duplicates(subset={'ios_ifa','google_aid'})

#1a - for every affiliate_id(Col B), calculate the unique ios_ifa(Col K) & google_aid(Col L) present in the data
uniqueaffiliateids = df.affiliate_id.unique()

for affiliateid in uniqueaffiliateids:
	tempdfgoogle = udf[(udf.affiliate_id == affiliateid) & (udf['google_aid'].str.contains(googlepattern, regex=True))]
	tempdfios  = udf[(udf.affiliate_id == affiliateid) & (udf['ios_ifa'].str.contains(iospattern, regex=True))] 
pprint('1a. See source.')

#1b - calculate how many valid google_aid & ios_ifa exist in the dataset
numvalidgoogle = len(udf.google_aid.value_counts())
numvalidios = len(udf.ios_ifa.value_counts())
pprint('1b. There are ' + str(numvalidgoogle) + ' valid google_aids in the dataset')
pprint('1b. There are ' + str(numvalidios) + ' valid ios_ifas in the dataset')

#2.1 -  plot a histogram from the data obtained from exercise 1a
#need to do this
iddata = pd.DataFrame(columns = ['affiliate_ids', 'numuniqueiosifas', 'numuniquegoogleaids'])
for i, affiliateid in enumerate(uniqueaffiliateids):
	numuniqueiosifas = len(df[(df.affiliate_id == affiliateid)].ios_ifa.unique())
	numuniquegoogleaids = len(df[(df.affiliate_id == affiliateid)].google_aid.unique())
	iddata.loc[i] = [affiliateid, numuniqueiosifas, numuniquegoogleaids]

iddata.plot(legend = True, kind = 'bar', x='affiliate_ids', title = '2.1 affiliate_id vs. num_unique_ids')

#2.2 -  plot a histogram of the no. of clicks v/s affiliate_id in the dataset
clickdata = pd.DataFrame(columns = ['affiliate_ids', 'clicks'])
for i, affiliateid in enumerate(uniqueaffiliateids):
	clicks = len(fdf[fdf.affiliate_id == affiliateid])
	clickdata.loc[i] = [affiliateid, clicks]	

clickdata.plot(legend = False, kind = 'bar', x='affiliate_ids', y='clicks', title = '2.2 #clicks vs. affiliate_id')
plt.show() 

#I don't think I'm catching all valid ids as the data seems like compared to Excel insanity checks, but I don't have a lot of time to work on assignments like these. Also the graphs included at the end of the assigment seem unrelated to the pdf problem set, perhaps I'm missing more questions?
