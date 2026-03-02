"""
Test: Missing pandas import
The AI agent should detect this and add: import pandas as pd
"""

def analyze_sales_data():
    # Using pandas without importing it - will cause NameError
    data = pd.DataFrame({
        'product': ['Laptop', 'Phone', 'Tablet', 'Monitor'],
        'sales': [1200, 800, 450, 300],
        'profit': [240, 160, 90, 60]
    })
    
    print("Sales Data:")
    print(data)
    print("\nSummary Statistics:")
    print(data.describe())
    
    total_sales = data['sales'].sum()
    total_profit = data['profit'].sum()
    
    print(f"\nTotal Sales: ${total_sales}")
    print(f"Total Profit: ${total_profit}")
    print(f"Profit Margin: {(total_profit/total_sales)*100:.2f}%")
    
    return data

if __name__ == '__main__':
    result = analyze_sales_data()
    print("\nBest selling product:", result.loc[result['sales'].idxmax(), 'product'])
