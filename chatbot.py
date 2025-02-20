#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

file_path = r'C:\Users\joshua\Desktop\Book1.xlsx'

df = pd.read_excel(file_path)



# In[3]:


df['Revenue Growth (%)'] = df.groupby(['Company'])['Total Revenue'].pct_change() * 100
df['Net Income Growth (%)'] = df.groupby(['Company'])['Net Income'].pct_change() * 100
df.fillna(0, inplace=True)


# In[4]:


summary_stats = df.describe()
print(summary_stats)


# In[5]:


df_info = df.info()
print(df_info)


# In[6]:


avg_rev_growth = df.groupby('Company') ['Revenue Growth (%)'].mean()

print("Average Revenue Growth (%) by Company:")
print(avg_rev_growth)


# In[7]:


df.head(10)


# In[11]:


mean_values = df.groupby(['Company', 'Fiscal Year']).mean()
mean_values


# In[12]:


median_values = df.groupby('Company').median()
print(median_values)


# In[13]:


sum_values = df.groupby('Company').sum()
print(sum_values)


# In[14]:


std_values = df.groupby('Company').std()
print(std_values)


# Findings Summary
# Median Values:
# The median values reflect the central tendency of financial metrics for each company.
# 
# Apple: Highest median revenue and net income.
# Microsoft: Moderate median values.
# Tesla: Lower median values compared to Apple and Microsoft.
# Sum Values:
# The sum values provide the total financial metrics over the analyzed years.
# 
# Apple: Highest total revenue, net income, and cash flow from operating activities.
# Microsoft: Moderate total values.
# Tesla: Lower total values compared to Apple and Microsoft.
# Standard Deviation:
# The standard deviation measures the variability of financial metrics.
# 
# Tesla: Highest variability in total revenue and net income.
# Microsoft: Moderate variability.
# Apple: Lowest variability, indicating more stable performance.
# 
# Tesla: Highest average revenue growth at 23.38%.
# Microsoft: Moderate average revenue growth at 8.28%.
# Apple: Lowest average revenue growth at 1.66%.
# Conclusion
# Our analysis reveals the following key trends:
# 
# Revenue Growth: Tesla experienced significant revenue growth in 2022 and 2023, while Microsoft and Apple showed steady or slight fluctuations in revenue growth.
# Net Income Growth: Tesla's net income growth fluctuated significantly, showing high growth in earlier years. Microsoft and Apple maintained relatively stable net income growth with minor variations.
# Aggregate Analysis: Aggregate functions such as median, sum, and standard deviation provided additional insights into the financial performance and stability of the companies.

# In[ ]:


import pandas as pd

# Load Excel data into pandas DataFrame
try:
    df = pd.read_excel(r'C:\Users\joshua\Desktop\Book1.xlsx')
except FileNotFoundError:
    print("Error: The 'Book1.xlsx' file is not found.")
    exit()
except pd.errors.EmptyDataError:
    print("Error: The 'Book1.xlsx' file is empty.")
    exit()
except pd.errors.ParserError:
    print("Error: Unable to parse 'Book1.xlsx'. Please check the file format.")
    exit()

# Ensure all column names are in a consistent format
df.columns = df.columns.str.strip()

# Calculate Revenue Growth (%) and Net Income Growth (%)
df['Revenue Growth (%)'] = df.groupby('Company')['Total Revenue'].pct_change() * 100
df['Net Income Growth (%)'] = df.groupby('Company')['Net Income'].pct_change() * 100

# Fill any NaN values resulting from the pct_change calculation
df.fillna(0, inplace=True)

# Define a function to handle user queries
def financial_chatbot():
    print("Welcome to the Financial Data Chatbot!")
    print("You can ask questions about financial data. Type 'exit' to end.")

    while True:
        user_query = input("\nWhat would you like to know? ")
        if user_query.lower() == 'exit':
            print("Thank you for using the Financial Data Chatbot. Goodbye!")
            break
        
        response = process_query(user_query)
        print(response)

def process_query(user_query):
    if "total revenue" in user_query.lower() and "all years" in user_query.lower():
        return handle_total_revenue_all_years(user_query)
    
    elif "total revenue" in user_query.lower():
        return handle_total_revenue(user_query)

    elif "net income" in user_query.lower() and "growth" in user_query.lower() and "average" in user_query.lower():
        return handle_average_net_income_growth(user_query)

    elif "net income" in user_query.lower():
        return handle_net_income(user_query)

    elif "total assets" in user_query.lower():
        return handle_total_assets(user_query)

    elif "total liabilities" in user_query.lower():
        return handle_total_liabilities(user_query)

    elif "cash flow" in user_query.lower():
        return handle_cash_flow(user_query)

    elif "revenue growth" in user_query.lower() and "average" in user_query.lower():
        return handle_average_revenue_growth(user_query)
    
    elif "revenue growth" in user_query.lower():
        return handle_revenue_growth(user_query)
    
    elif "average net income growth" in user_query.lower():
        return handle_average_net_income_growth(user_query)
    
    elif "average" in user_query.lower():
        return handle_average(user_query)
    
    elif "highest total revenue" in user_query.lower():
        return handle_highest_total_revenue(user_query)
    
    elif "lowest total revenue" in user_query.lower():
        return handle_lowest_total_revenue(user_query)
    
    elif "performed well" in user_query.lower():
        return handle_best_performance(user_query)
    
    elif "didn't perform well" in user_query.lower() or "did not perform well" in user_query.lower():
        return handle_worst_performance(user_query)

    else:
        return "Sorry, I can only provide information on total revenue, net income, total assets, total liabilities, cash flow, revenue growth, averages, and company performance."
def handle_total_revenue_all_years(company):
    total_revenue = df[df['Company'] == company]['Total Revenue'].sum() * 1_000_000  # Convert to actual dollars
    return f"The total revenue of {company} for all years combined is ${total_revenue:,.2f}."

def handle_total_revenue_all_years(user_query):
    company = extract_company(user_query)
    if company:
        total_revenue = df[df['Company'] == company]['Total Revenue'].sum() * 1_000_000  # Convert to actual dollars
        return f"The total revenue for {company} for all years combined is ${total_revenue:,.2f}."
    else:
        return "Please specify a company to retrieve its total revenue for all years."

def handle_total_revenue(user_query):
    company, fiscal_year = extract_company_and_year(user_query)
    if company:
        if fiscal_year:
            total_revenue = df[(df['Company'] == company) & (df['Fiscal Year'] == fiscal_year)]['Total Revenue'].sum() * 1_000_000  # Convert to actual dollars
            return f"The total revenue for {company} in {fiscal_year} is ${total_revenue:,.2f}."
        else:
            avg_revenue = df[df['Company'] == company]['Total Revenue'].mean() * 1_000_000
            return f"The average total revenue for {company} is ${avg_revenue:,.2f}."
    else:
        total_revenue = df['Total Revenue'].sum() * 1_000_000  # Convert to actual dollars
        return f"The total revenue across all companies is ${total_revenue:,.2f}."

def handle_net_income(user_query):
    company, fiscal_year = extract_company_and_year(user_query)
    if company and fiscal_year:
        net_income = df[(df['Company'] == company) & (df['Fiscal Year'] == fiscal_year)]['Net Income'].sum() * 1_000_000
        return f"The net income for {company} in {fiscal_year} is ${net_income:,.2f}."
    elif company:
        net_income = df[df['Company'] == company]['Net Income'].mean() * 1_000_000
        return f"The average net income for {company} is ${net_income:,.2f}."
    else:
        return "Please specify both company and fiscal year to retrieve net income information."

def handle_total_assets(user_query):
    company, fiscal_year = extract_company_and_year(user_query)
    if company and fiscal_year:
        total_assets = df[(df['Company'] == company) & (df['Fiscal Year'] == fiscal_year)]['Total Assets'].sum() * 1_000_000
        return f"The total assets for {company} in {fiscal_year} are ${total_assets:,.2f}."
    elif company:
        total_assets = df[df['Company'] == company]['Total Assets'].mean() * 1_000_000
        return f"The average total assets for {company} are ${total_assets:,.2f}."
    else:
        return "Please specify both company and fiscal year to retrieve total assets information."

def handle_total_liabilities(user_query):
    company, fiscal_year = extract_company_and_year(user_query)
    if company and fiscal_year:
        total_liabilities = df[(df['Company'] == company) & (df['Fiscal Year'] == fiscal_year)]['Total Liabilities'].sum() * 1_000_000
        return f"The total liabilities for {company} in {fiscal_year} are ${total_liabilities:,.2f}."
    elif company:
        total_liabilities = df[df['Company'] == company]['Total Liabilities'].mean() * 1_000_000
        return f"The average total liabilities for {company} are ${total_liabilities:,.2f}."
    else:
        return "Please specify both company and fiscal year to retrieve total liabilities information."

def handle_cash_flow(user_query):
    company, fiscal_year = extract_company_and_year(user_query)
    if company and fiscal_year:
        cash_flow = df[(df['Company'] == company) & (df['Fiscal Year'] == fiscal_year)]['Cash Flow from Operating Activities'].sum() * 1_000_000
        return f"The cash flow from operating activities for {company} in {fiscal_year} is ${cash_flow:,.2f}."
    elif company:
        cash_flow = df[df['Company'] == company]['Cash Flow from Operating Activities'].mean() * 1_000_000
        return f"The average cash flow from operating activities for {company} is ${cash_flow:,.2f}."
    else:
        return "Please specify both company and fiscal year to retrieve cash flow information."

def handle_revenue_growth(user_query):
    company, fiscal_year = extract_company_and_year(user_query)
    if company and fiscal_year:
        try:
            growth_rate = df[(df['Company'] == company) & (df['Fiscal Year'] == fiscal_year)]['Revenue Growth (%)'].sum()
            return f"The revenue growth rate for {company} in {fiscal_year} is {growth_rate:.2f}%."
        except KeyError:
            return "Error: 'Revenue Growth (%)' column not found in the dataset."
    elif company:
        try:
            growth_rates = df[df['Company'] == company]['Revenue Growth (%)']
            if not growth_rates.empty:
                return f"The revenue growth rates for {company} are:\n" + "\n".join(f"{year}: {rate:.2f}%" for year, rate in zip(df['Fiscal Year'].unique(), growth_rates))
            else:
                return "N/A (No sufficient data for revenue growth rates)"
        except KeyError:
            return "Error: 'Revenue Growth (%)' column not found in the dataset."
    else:
        return "Please specify both company and fiscal year to retrieve revenue growth information."

def handle_average_revenue_growth(user_query):
    company = extract_company(user_query)
    if company:
        try:
            growth_rates = df[df['Company'] == company]['Revenue Growth (%)']
            if not growth_rates.empty:
                avg_growth_rate = growth_rates.mean()
                return f"The average revenue growth rate for {company} is {avg_growth_rate:.2f}%."
            else:
                return "N/A (No sufficient data for average revenue growth rate)"
        except KeyError:
            return "Error: 'Revenue Growth (%)' column not found in the dataset."
    else:
        return "Please specify a company to retrieve its average revenue growth rate."

def handle_average_net_income_growth(user_query):
    company = extract_company(user_query)
    if company:
        try:
            growth_rates = df[df['Company'] == company]['Net Income Growth (%)']
            if not growth_rates.empty:
                avg_growth_rate = growth_rates.mean()
                return f"The average net income growth rate for {company} is {avg_growth_rate:.2f}%."
            else:
                return "N/A (No sufficient data for average net income growth rate)"
        except KeyError:
            return "Error: 'Net Income Growth (%)' column not found in the dataset."
    else:
        return "Please specify a company to retrieve its average net income growth rate."

def handle_highest_total_revenue(user_query):
    fiscal_year = extract_fiscal_year(user_query)
    if fiscal_year:
        highest_revenue_company = df[df['Fiscal Year'] == fiscal_year].sort_values(by='Total Revenue', ascending=False).iloc[0]
        highest_revenue = highest_revenue_company['Total Revenue'] * 1_000_000  # Convert to actual dollars
        return f"The company with the highest total revenue in {fiscal_year} is {highest_revenue_company['Company']} with a total revenue of ${highest_revenue:,.2f}."
    else:
        return "Please specify a fiscal year to retrieve the company with the highest total revenue."

def handle_lowest_total_revenue(user_query):
    fiscal_year = extract_fiscal_year(user_query)
    if fiscal_year:
        lowest_revenue_company = df[df['Fiscal Year'] == fiscal_year].sort_values(by='Total Revenue').iloc[0]
        lowest_revenue = lowest_revenue_company['Total Revenue'] * 1_000_000  # Convert to actual dollars
        return f"The company with the lowest total revenue in {fiscal_year} is {lowest_revenue_company['Company']} with a total revenue of ${lowest_revenue:,.2f}."
    else:
        return "Please specify a fiscal year to retrieve the company with the lowest total revenue."

def handle_best_performance(user_query):
    fiscal_year = extract_fiscal_year(user_query)
    if fiscal_year:
        best_performing_company = df[df['Fiscal Year'] == fiscal_year].sort_values(by=['Revenue Growth (%)', 'Net Income Growth (%)'], ascending=False).iloc[0]
        return f"The best performing company in {fiscal_year} is {best_performing_company['Company']} with a revenue growth of {best_performing_company['Revenue Growth (%)']:.2f}% and net income growth of {best_performing_company['Net Income Growth (%)']:.2f}%."
    else:
        return "Please specify a fiscal year to retrieve the best performing company information."

def handle_worst_performance(user_query):
    fiscal_year = extract_fiscal_year(user_query)
    if fiscal_year:
        worst_performing_company = df[df['Fiscal Year'] == fiscal_year].sort_values(by=['Revenue Growth (%)', 'Net Income Growth (%)']).iloc[0]
        return f"The worst performing company in {fiscal_year} is {worst_performing_company['Company']} with a revenue growth of {worst_performing_company['Revenue Growth (%)']:.2f}% and net income growth of {worst_performing_company['Net Income Growth (%)']:.2f}%."
    else:
        return "Please specify a fiscal year to retrieve the worst performing company information."

def handle_average(user_query):
    metric = extract_metric(user_query)
    if metric:
        avg_value = df[metric].mean() * 1_000_000  # Convert to actual dollars
        return f"The average {metric.replace('_', ' ').lower()} across all companies is ${avg_value:,.2f}."
    else:
        return "Please specify a valid metric to retrieve its average."

def extract_company_and_year(user_query):
    company = extract_company(user_query)
    fiscal_year = extract_fiscal_year(user_query)
    return company, fiscal_year

def extract_company(user_query):
    try:
        companies = df['Company'].unique()
    except KeyError:
        print("Error: 'Company' column not found in the dataset.")
        return None

    for company in companies:
        if company.lower() in user_query.lower():
            return company
    return None

def extract_fiscal_year(user_query):
    fiscal_years = df['Fiscal Year'].unique()
    for year in fiscal_years:
        if str(year) in user_query:
            return year
    return None

def extract_metric(user_query):
    metrics = {
        "total revenue": "Total Revenue",
        "net income": "Net Income",
        "total assets": "Total Assets",
        "total liabilities": "Total Liabilities",
        "cash flow": "Cash Flow from Operating Activities"
    }
    for key, value in metrics.items():
        if key in user_query.lower():
            return value
    return None

# Main execution
if __name__ == "__main__":
    financial_chatbot()


# In[ ]:




