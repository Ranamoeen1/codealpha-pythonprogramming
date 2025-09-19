
stock_prices = {
    "AAPL": 180,   
    "TSLA": 250,   
    "MSFT": 310,   
    "GOOGL": 140   

# Dictionary to store user's portfolio
portfolio = {}

print("📊 Welcome to Stock Portfolio Tracker 📊")
print("Available stocks and their prices:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

while True:
    stock_name = input("\nEnter stock symbol (or 'done' to finish): ").upper()
    if stock_name == "DONE":
        break
    if stock_name not in stock_prices:
        print("❌ Stock not found. Please choose from the list.")
        continue
    
    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        continue

    # Add to portfolio
    if stock_name in portfolio:
        portfolio[stock_name] += quantity
    else:
        portfolio[stock_name] = quantity

# Calculate total investment
total_value = 0
print("\n📌 Your Portfolio:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_value += value
    print(f"{stock} - {qty} shares × ${stock_prices[stock]} = ${value}")

print("\n💰 Total Investment Value:", total_value)

# Ask user to save result
save_choice = input("\nDo you want to save the result? (yes/no): ").lower()
if save_choice == "yes":
    file_choice = input("Save as (txt/csv): ").lower()
    filename = f"portfolio.{file_choice}"

    if file_choice == "txt":
        with open(filename, "w", encoding="utf-8") as f: 
            f.write("📊 Portfolio Report 📊\n")
            for stock, qty in portfolio.items():
                f.write(f"{stock} - {qty} shares × ${stock_prices[stock]} = ${stock_prices[stock] * qty}\n")
            f.write(f"\n💰 Total Investment Value: ${total_value}")
    elif file_choice == "csv":
        import csv
        with open(filename, "w", newline="", encoding="utf-8") as f:   
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price", "Value"])
            for stock, qty in portfolio.items():
                writer.writerow([stock, qty, stock_prices[stock], stock_prices[stock] * qty])
            writer.writerow(["Total", "", "", total_value])
    else:
        print("❌ Invalid file type. Skipping save.")

    print(f"✅ Portfolio saved as {filename}")
else:
    print("❌ Portfolio not saved.")
