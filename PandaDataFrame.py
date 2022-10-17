import pandas as pd
studets_details = {
    'DOB': ['1/1/2014', '3/6/2010', '6/7/2009', '23/8/2012', '12/5/2016', '15/3/2013'],
    'Marks': [32, 35, 40, 49, 38, 42],
    'Sports': ['Football', 'Hokey', 'Badminton', 'Chess', 'Ludo', 'Pool'],
    'Name': ['Tony', 'Sonu', 'Priya', 'Khush', 'Diya', 'Mansi']
}
df = pd.DataFrame(studets_details)
print(df)
print("\n", df.head(3))         # Starting rows
print("\n", df.tail(2))         # Ending rows
print("\n", df['DOB'])          # Particular column
print("\n", df.dtypes)          # Data types
print("\n", df.columns)         # Column names
print("\n", df[1:4])            # Slicing
print("\n", df['Marks'].max())  # Max for particular field
print("\n", df['Marks'].min())  # Min for particular field
print("\n", df['Marks'].mean())  # Mean