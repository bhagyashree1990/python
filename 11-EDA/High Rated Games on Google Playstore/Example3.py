#Category vs Rating
from Example2 import data
import seaborn as sns

#Code starts here
chart = sns.catplot(x="Category",y="Rating",data=data,kind="box",height=10).set(
    title='Rating vs Category [BoxPlot]')
chart.set_xticklabels(rotation=90)

#Code ends here