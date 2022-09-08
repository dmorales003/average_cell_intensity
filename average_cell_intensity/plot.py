import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

fp = '/Users/dmorales/Documents/data/microscopy/2022_08_23_jeanette/result/analyze_1/export.csv'
fp_bv = '/Users/dmorales/Documents/data/microscopy/2022_08_23_jeanette/result/analyze_1/bivariate.csv'

df = pd.read_csv(fp_bv, ',')
df2 = pd.read_csv(fp,',')
# restructure data 
# sample, number, c1 intesnity, c2 intensity, area
colors = ['#38761d','#cc0000']
sns.set_palette(sns.color_palette(colors))

sns.kdeplot(
    data=df2[df2['channel']=='C1'],
    x='log',
    hue = 'sample',
    fill = True
    )



sns.histplot(
    data = df2[df2['sample']=='sample3'],
    x = 'log',
    hue = 'channel',
    fill = True,
    stat = 'count'
)


ax = sns.scatterplot(
    data = df,
    x = 'logC1',
    y = 'logC2',
    hue = 'sample'
)
ax.set(xlabel = 'Green Fluorescence Log(a.u.)', ylabel = 'Red Fluorescence Log(a.u.)')
plt.legend(bbox_to_anchor=(1.02, 0.7), loc='upper left', borderaxespad=0)

sns.set(rc = {'figure.figsize':(10,6)})
ax = sns.boxplot(
    data = df,
    x = 'sample',
    y = 'C1C2log',
    orient = 'v'
)3
ax.set(xlabel = 'Sample', ylabel = 'Log(Green/Red)')

