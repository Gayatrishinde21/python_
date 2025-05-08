#for standard deviation
import pandas as pd
import openpyxl
import math

data = { 
    "continents": ["Africa","Asia","Europe","North America","Oceania","South America"],
    "1990": [500,600,1200,1000,400,900]
}

#
print(data.get("1990"))
v_sum=data.get("1990")
#value n
print("sum is: ",sum(v_sum))
#sum
length= len(v_sum)
print("sum is: ",length)
#mean
Mean = sum(v_sum)/length
print("Mean is: ",Mean)
#x-x bar difference
for x in v_sum:
    x = x - Mean
    print("difference is: ",x)
#square difference
total = 0
for x in v_sum:
    squr_diff = pow(x - Mean,2)
    total += squr_diff
    print("square difference is: ",squr_diff)
#total
print("total is: ",total)
#variance
variance = total/(length-1)
print("variance is: ",variance)

#standard deviation
std_dev=math.sqrt(variance)
print("standard deviation is: ",std_dev)

# save to excel file
df = pd.DataFrame(data)
df.loc[len(df)] = ["Mean", Mean]  # Adding Mean row
df.loc[len(df)] = ["Total", total]  # Adding Total row
df.loc[len(df)] = ["Standard Deviation", std_dev]  

df.to_excel("output.xlsx", index=False)
