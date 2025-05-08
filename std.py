import pandas as pd
import csv
import openpyxl
import math

data = { 
    "continents": ["Africa","Asia","Europe","North America","Oceania","South America"],
    "1990": [500,600,1200,1000,400,900]
}

print(data.get("1990"))
v_sum=data.get("1990")

print("sum is: ",sum(v_sum))

length= len(v_sum)
print("sum is: ",length)

Mean = sum(v_sum)/length
print("Mean is: ",Mean)

for x in v_sum:
    x = x -Mean
    print("difference is: ",x)

total = 0
for x in v_sum:
    squr_diff = pow(x - Mean,2)
    total += squr_diff
    print("square difference is: ",squr_diff)

print("total is: ",total)
variance = total/(length-1)
print("variance is: ",variance)

std_dev=math.sqrt(variance)
print("standard deviation is: ",std_dev)

# save to excel file
filename = "output.xlsx"

df = pd.DataFrame(data)

df = pd.read_excel('output.xlsx')
df.loc[len(df)] = ['Total']
new_row = pd.DataFrame(['total'], columns=df.columns)
df = pd.concat(df.iloc[:6]).reset_index(drop=True) # Replace index
df.to_excel('output.xlsx', index=False) 


# variance = total/(length)
# print("variance is: ",variance)

# std_dev = pow(variance,1/2)
# print("standard deviation is: ",std_dev)
    
# df = pd.DataFrame(data)
# print(df)
# df.to_excel('output.xlsx', index=False)

# length = len(data)

# # mean
# Mean = sum(data.values) / length
# print("\nx̄:",Mean)

# # calculate difference
# for x in data.values():
#     x = (x - Mean) 
#     print("(x - x̄):",x)

# # calculate square of difference
# total = 0
# for x in data.values():
#     squr_diff = pow(x - Mean,2) 
#     sum += squr_diff
#     print("(x - x̄)2:",squr_diff)
# print("\ntotal:",total)

# # calculate variance
# variance = sum/length
# print("\nVariance is:",variance)

# # calculate standard deviation
# std_dev = pow(variance,1/2)
# print("\nStandard Deviation is:",std_dev)

# #save in csv

# filename = "standard_deviation.xlsx"

# def to_excel(data, filename):
#     with open(filename, 'w', newline='') as excelfile:
#         writer = csv.writer(excelfile)
#         writer.writerow(["Total","Mean","Standard Deviation"])
#         writer.writerow([total,Mean,std_dev])

# to_excel(data,filename)
# print(f"Standard deviation calculated and saved to {filename}")

