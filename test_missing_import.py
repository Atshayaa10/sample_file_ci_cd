def analyze_sales_data():
    data = pd.DataFrame({
        'product': ['Laptop', 'Phone', 'Tablet', 'Monitor'],
        'sales': [1200, 800, 450, 300],
        'profit': [240, 160, 90, 60]
    })
    
    print("Sales Data:")
    print(data)
    print("\nTotal Sales:", data['sales'].sum())
    
    return data

if __name__ == '__main__':
    analyze_sales_data()
