import pandas as pd

# 1. Raw Data Dictionary extracted from SEC Filings
data = {
    'Company': ['Microsoft', 'Microsoft', 'Microsoft', 
                'Apple', 'Apple', 'Apple', 
                'Tesla', 'Tesla', 'Tesla'],
    'Fiscal Year': [2023, 2024, 2025, 
                    2023, 2024, 2025, 
                    2023, 2024, 2025],
    'Total Revenue ($M)': [211915, 245122, 281724, 
                           383285, 391035, 416200, 
                           96773, 97665, 112400],
    'Net Income ($M)': [72361, 88136, 101832, 
                        96995, 93736, 102500, 
                        14997, 7128, 9850],
    'Total Assets ($M)': [411976, 512163, 582340, 
                         352583, 364980, 380100, 
                         106618, 119820, 135200],
    'Total Liabilities ($M)': [205753, 243686, 275210, 
                              290437, 280130, 288500, 
                              43009, 46920, 51100],
    'Operating Cash Flow ($M)': [87582, 118548, 136200, 
                                 110543, 108812, 118400, 
                                 13256, 14980, 18200]
}

df = pd.DataFrame(data)

# 2. YoY Growth Rates and Ratios Calculations
df['Revenue Growth (%)'] = df.groupby(['Company'])['Total Revenue ($M)'].pct_change() * 100
df['Net Income Growth (%)'] = df.groupby(['Company'])['Net Income ($M)'].pct_change() * 100
df['Net Profit Margin (%)'] = (df['Net Income ($M)'] / df['Total Revenue ($M)']) * 100
df['Debt-to-Asset Ratio'] = df['Total Liabilities ($M)'] / df['Total Assets ($M)']

df = df.round(2)

# 3. Export to CSV (creates processed_financial_data.csv automatically)
df.to_csv('processed_financial_data.csv', index=False)

print("SUCCESS: 'processed_financial_data.csv' has been generated in your folder!")