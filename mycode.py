import pandas as pd
#df = pd.read_csv("data.csv") 

#for the sake of ease, hard coded the dataframe. If you'd like to use CSV data, then uncomment the line above and comment out the CSV
df = pd.DataFrame({                 
'payer': ['DANNON', 'UNILEVER', 'DANNON', 'MILLER COORS', 'DANNON'],
 'points': [1000, 200, -200, 10000, 300],
'timestamp': ["2020-11-02T14:00:00Z", "2020-10-31T11:00:00Z", "2020-10-31T15:00:00Z", "2020-11-01T14:00:00Z", "2020-10-31T10:00:00Z"]
})
df.index.name = 'index'

df.sort_values(by='timestamp', inplace = True)
df = df.reset_index(drop=True)

#everything is sorted by time and organized

for i in range(df.shape[0]):
    row = df.iloc[i]
    if row['points'] < 0: 
        neg = row
        for j in range(i-1, -1, -1):
          r = df.iloc[j]
          if neg['payer'] == r['payer']: #consolidating negative point values with earlier positive ones
            newVal = neg['points'] + r['points']
            df.at[neg.name, 'points'] = newVal
            df = df.drop(index=0)
#used given balance
balance = 5000
for i in range(df.shape[0]):
  row = df.iloc[i]
  if balance > 0: 
    if balance >= row['points']: #if balance is more than a point total
      balance -= row['points']
      df.at[row.name, 'points'] = 0
    else:
      df.at[row.name, 'points'] = row['points'] - balance #if a point total outweighs the balance
      balance = 0
  else:
    break
#remove the timestamp column
df = df.drop(columns = "timestamp")
#make it look pretty
df = df.groupby('payer').sum().reset_index()

print(df)
