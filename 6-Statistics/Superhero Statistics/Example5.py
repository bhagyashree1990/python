#Statistics for Survival
#Header files
from Example4 import super_best
from Example4 import plt
#Code starts here
fig, (ax_1, ax_2, ax_3) = plt.subplots(3,1, figsize=(20,10))
ax_1.boxplot(super_best['Intelligence'])
ax_1.set_title('Intelligence')
ax_2.boxplot(super_best['Speed'])
ax_2.set_title('Speed')
ax_3.boxplot(super_best['Power'])
ax_3.set_title('Power')
plt.show()