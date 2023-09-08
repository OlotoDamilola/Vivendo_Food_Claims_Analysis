import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn
import seaborn as sns

food = pd.read_csv("food_claim_clean.csv")
print(food["time_to_close"])
distr = food["time_to_close"]
sns.set_theme(style="darkgrid")
sns.histplot(data=distr, element="step", color="gray", fill=True).set( xlabel="Days")
plt.text(x=60, y=250, s="Range in number of days", fontsize=12)
plt.show()
#histogram showing range in number of days#

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

food = pd.read_csv("food_claim_clean.csv")
print(food["time_to_close"])
print(food.iloc[2:4])
distr = food["time_to_close"]
sns.set_theme(style="darkgrid")
sns.boxplot(data=food, x="location",y="time_to_close", color="white", showfliers=False).set(xlabel="Location", ylabel="Count")
plt.text(x=0,y=550, s="Range in number of days by location", fontsize=12)
plt.text(x=0,y=450, s="Focused to remove outlying values", fontsize=8)
plt.show()
#box plot focused on removing outliers#

sns.set_theme(style="darkgrid")
sns.boxplot(data=food, x="location",y="time_to_close", color="white").set(xlabel="Location", ylabel="Count")
plt.text(x=0,y=550, s="Range in number of days by location", fontsize=12)
plt.show()
#box plot showing impact of outliers#