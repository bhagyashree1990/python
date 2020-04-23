#Education Matters!
from Example2 import *
high = census[census[:,1] > 10]
low = census[census[:,1] <= 10]
avg_pay_high = high.mean(axis=0)[7]
avg_pay_low = low.mean(axis=0)[7]
print(avg_pay_high == avg_pay_low)