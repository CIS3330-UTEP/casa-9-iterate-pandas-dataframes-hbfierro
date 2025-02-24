import pandas as pd
filename = "./Session_08/big-mac-full-index.csv"

data = {'Name': ['Mexico', 'Japan', 'Russia'],'Local Price': [20.9, 294, 39.5],'Dollar Price': [2.22, 2.77, 1.39]}
df = pd.DataFrame(data)

for index, row in df.iterrows():
    total_cost = row['Local Price'] * row['Dollar Price']
    print(f"{row['Name']} Total Cost: ${total_cost}")

def calculate_total_cost(row):
    return f"{row['Name']} Total Cost: ${row['Local Price'] * row['Dollar Price']}"

# Applying the function row-wise
result = df.apply(calculate_total_cost, axis=1)
for res in result:
    print(res)

