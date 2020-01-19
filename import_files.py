import datetime as dt
import pandas as pd
import numpy as np

# Prices
basic_price = 5
delux_price = 6

# Importing the data
basic = pd.read_csv("Basic.txt", header=0, names=['Basic Cupcake:'])
delux = pd.read_csv("Delux.txt", header=0, names=['Delux Cupcake:'])
day_received = pd.read_csv("Total.txt", header=0, names=['Day Total:'])

# Joining in one dataframe
df_cupcake = pd.concat([basic,delux,day_received], axis=1)

# Adding the date to the dataframe
start_date = dt.date.today()-dt.timedelta(days=len(df_cupcake)-1)
df_cupcake['Date:'] = pd.date_range(start=start_date, periods= len(df_cupcake), freq = 'D')

# Putting date first
cols = df_cupcake.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_cupcake = df_cupcake[cols]

# Calculating cupcake type totals
df_cupcake['Basic Cupcake Total:'] = df_cupcake['Basic Cupcake:'] * basic_price
df_cupcake['Delux Cupcake Total:'] = df_cupcake['Delux Cupcake:'] * delux_price

# Year calculations
df_year = pd.DataFrame({'year': df_cupcake['Date:'].dt.year, 'total': df_cupcake['Day Total:'], 'basic': df_cupcake['Basic Cupcake Total:'], 'delux': df_cupcake['Delux Cupcake Total:']})
df_year = df_year.groupby(['year']).sum()

# Month calculations
df_month = pd.DataFrame({'month': df_cupcake['Date:'].dt.strftime('%Y-%m'), 'total': df_cupcake['Day Total:'], 'basic': df_cupcake['Basic Cupcake Total:'], 'delux': df_cupcake['Delux Cupcake Total:']})
df_month = df_month.groupby(['month']).sum()

# Weekly Calculations
df_week = pd.DataFrame({'week': df_cupcake['Date:'].dt.strftime('%U'), 'year': df_cupcake['Date:'].dt.year, 'total': df_cupcake['Day Total:'], 'basic': df_cupcake['Basic Cupcake Total:'], 'delux': df_cupcake['Delux Cupcake Total:']})
df_week = df_week.groupby(['year','week']).sum()

print("Yearly Revenue Total:")
print(df_year)
print("\nMonthly Revenue Total:")
print(df_month)
print("\nWeekly Revenue Total:")
print(df_week)
