import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve the API key stored in the .env file for security
API_KEY = os.getenv("API_KEY")

def convert_currency():
    print("\n" + "="*30)
    print(" 🌍  CURRENCY CONVERTER LIVE ")
    print("="*30)
    
    #initalize so program doesnt crash if the try block isnt executed
    rates = {}

    # 📥 Input phase
    initial_currency = input(" 🛫  From (e.g. USD): ").upper()

    url_latest = f"https://api.apilayer.com/fixer/latest?base={initial_currency}"
    headers = {"apikey": API_KEY}

    # 📊 Show a preview of current market rates
    try:
        response = requests.get(url_latest, headers=headers)
        response.raise_for_status()
        symbols = response.json()

        if symbols.get('success'):
            print(f"\n 📈  Current Rates for 1 {initial_currency}:")
            print("-" * 30)   

            rates = symbols.get('rates', {})

            # Limiting to top 10 for better UI
            for i, (currency, rate) in enumerate(rates.items()):
                print(f"  💰 {currency} : {rate:.2f}")
                if i == 9: 
                    print("  ... and more available!")
                    break
        else:
            print(f" ⚠️  Market Preview Error: {symbols['error']['info']}")
        
    except Exception as e:
        print(f" ❌  Couldn't fetch preview: {e}")

    # 🎯 Target Selection
    print("\n" + "-"*30)
    
    while True:
        target_currency = input("\n 🛬  To (e.g. EUR): ").upper()
        
        # If the API call failed or the user typed a fake code:
        if rates and target_currency not in rates:
            print(f" 🚫  '{target_currency}' is not a valid currency. Please choose from the list above.")
            continue
        break 


    while True:
        try:
            amount = float(input(" 💵  Amount to convert: "))
            if amount <= 0:
                print(" 🚫  Amount must be a positive number.")
                continue
            break 
        except ValueError:
            print(" 🔢  Invalid input. Please enter a number.")

    # 🔄 API Conversion request
    url = f"https://api.apilayer.com/fixer/convert?to={target_currency}&from={initial_currency}&amount={amount}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
            
        if data.get('success'):
            # ✨ Final Result
            print("\n" + "✨"*15)
            print(f"  ✅  {amount} {initial_currency} = {data['result']:.2f} {target_currency}")
            print("✨"*15)
        else:
            print(f" ❌  API Error: {data['error']['info']}")
            
    except Exception as e:
        print(f" 📡  Connection Error: {e}")

# 🚀 Start Program
if __name__ == "__main__":
    while True:
        convert_currency()
        
        print("\n" + "—"*30)
        again = input(" 🔄  Convert another? (y/n): ").lower()
        if again != 'y':
            print("\n 👋  Thank you for using PyCurrency! Goodbye!")
            break