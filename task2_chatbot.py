import pandas as pd

# Load processed financial dataset created in Task 1
try:
    df = pd.read_csv('processed_financial_data.csv')
except FileNotFoundError:
    print("[ERROR] 'processed_financial_data.csv' not found. Please run task1 script first.")
    exit()

def simple_chatbot(user_query):
    query = user_query.lower()
    
    # 1. Total Revenue Queries
    if "total revenue" in query or "revenue" in query:
        if "microsoft" in query:
            res = df[df['Company'] == 'Microsoft'][['Fiscal Year', 'Total Revenue ($M)']]
            return f"Microsoft's Total Revenue ($M):\n{res.to_string(index=False)}"
        elif "apple" in query:
            res = df[df['Company'] == 'Apple'][['Fiscal Year', 'Total Revenue ($M)']]
            return f"Apple's Total Revenue ($M):\n{res.to_string(index=False)}"
        elif "tesla" in query:
            res = df[df['Company'] == 'Tesla'][['Fiscal Year', 'Total Revenue ($M)']]
            return f"Tesla's Total Revenue ($M):\n{res.to_string(index=False)}"
        else:
            res = df[['Company', 'Fiscal Year', 'Total Revenue ($M)']]
            return f"Total Revenue for all companies ($M):\n{res.to_string(index=False)}"

    # 2. Net Income / Profit Queries
    elif "net income" in query or "profit" in query:
        if "microsoft" in query:
            res = df[df['Company'] == 'Microsoft'][['Fiscal Year', 'Net Income ($M)']]
            return f"Microsoft's Net Income ($M):\n{res.to_string(index=False)}"
        elif "apple" in query:
            res = df[df['Company'] == 'Apple'][['Fiscal Year', 'Net Income ($M)']]
            return f"Apple's Net Income ($M):\n{res.to_string(index=False)}"
        elif "tesla" in query:
            res = df[df['Company'] == 'Tesla'][['Fiscal Year', 'Net Income ($M)']]
            return f"Tesla's Net Income ($M):\n{res.to_string(index=False)}"
        else:
            res = df[['Company', 'Fiscal Year', 'Net Income ($M)']]
            return f"Net Income for all companies ($M):\n{res.to_string(index=False)}"

    # 3. Year-over-Year (YoY) Growth Queries
    elif "growth" in query or "yoy" in query:
        res = df[['Company', 'Fiscal Year', 'Revenue Growth (%)', 'Net Income Growth (%)']]
        return f"Year-over-Year Growth Rates:\n{res.to_string(index=False)}"

    # 4. Profit Margin Queries
    elif "margin" in query or "profit margin" in query:
        res = df[['Company', 'Fiscal Year', 'Net Profit Margin (%)']]
        return f"Net Profit Margins:\n{res.to_string(index=False)}"

    # Fallback Handling for Unrecognized Queries
    else:
        return "Sorry, I can only provide financial information on predefined queries regarding Revenue, Net Income, Growth rates, and Profit Margins for Microsoft, Apple, and Tesla."

# CLI Interaction Demonstration
if __name__ == "__main__":
    print("=== BCGX GenAI Financial Chatbot Prototype Initialized ===")
    print("Predefined Queries Supported: Revenue, Net Income, YoY Growth, Profit Margins.\n")
    
    sample_queries = [
        "What is the total revenue for Microsoft?",
        "Show me Apple net income",
        "What are the YoY growth rates?",
        "Tell me about profit margins"
    ]
    
    for q in sample_queries:
        print(f"User Question: {q}")
        print(f"Chatbot Response:\n{simple_chatbot(q)}")
        print("-" * 60)