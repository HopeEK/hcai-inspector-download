import requests
import pandas as pd

# Replace with actual endpoint
url = "https://hcai.ca.gov/path-to-inspector-data.csv"

response = requests.get(url)
with open("inspectors.csv", "wb") as f:
    f.write(response.content)

df = pd.read_csv("inspectors.csv")
df.to_excel("inspectors.xlsx", index=False)
