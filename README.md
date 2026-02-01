# currency_converter

# 🌍 PyCurrency Live Converter

A lightweight, real-time Currency Converter CLI application. This tool allows users to view current market rates for a base currency and perform precise conversions using live data from the Fixer API.

## ✨ Features
* **Live Market Preview:** Fetches and displays the top 10 exchange rates for your starting currency.
* **Real-time Conversion:** Uses the `/convert` endpoint for accurate, up-to-date calculations.
* **Secure Configuration:** Environment variables (`.env`) are used to protect your API keys.
* **User-Friendly CLI:** Includes emoji support and clear visual separators for a better terminal experience.
* **Robust Error Handling:** Validates currency codes, handles non-numeric inputs, and catches API connection issues.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Libraries:** `requests`, `python-dotenv`
* **API:** [Fixer API](https://fixer.io/)

## 🚀 Getting Started

### 1. Prerequisites
You will need a free API key from [APILayer/Fixer](https://apilayer.com/marketplace/fixer-api).

### 2. Installation
```Clone the repository:

bash
git clone [https://github.com/yourusername/currency-converter.git](https://github.com/yourusername/currency-converter.git)
cd currency-converter```

Install dependencies:

```bash```
pip install requests python-dotenv

```3. Configuration```
Create a .env file in the root directory and add your API key:

```Code snippet```
API_KEY=your_actual_api_key_here

```4. Usage```
Run the script:

```Bash```
python currency_converter_chatgpt.py
