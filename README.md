# 🌍 PyCurrency — Live Currency Converter

A lightweight, real-time command-line currency converter built in Python. It fetches live exchange rates from the Fixer API, previews the top 10 market rates for your chosen base currency, and performs precise conversions in seconds.

---

## ✨ Features

- **Live Market Preview** — Displays the top 10 current exchange rates for your chosen base currency before you convert
- **Real-Time Conversion** — Uses the Fixer `/convert` endpoint for accurate, up-to-date results
- **Input Validation** — Validates currency codes against live data, rejects non-numeric amounts, and enforces positive values
- **Secure Configuration** — API keys are stored in a `.env` file and never hardcoded
- **Repeat Conversions** — Prompts the user to run another conversion without restarting the program
- **Friendly CLI** — Clear visual separators and emoji indicators for a polished terminal experience

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.x |
| HTTP Requests | `requests` |
| Environment Variables | `python-dotenv` |
| Exchange Rate Data | [Fixer API via APILayer](https://apilayer.com/marketplace/fixer-api) |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/currency-converter.git
cd currency-converter
```

### 2. Install Dependencies

```bash
pip install requests python-dotenv
```

### 3. Get an API Key

Sign up for a free API key at [APILayer — Fixer API](https://apilayer.com/marketplace/fixer-api).

### 4. Configure Environment Variables

Create a `.env` file in the project root directory:

```
API_KEY=your_actual_api_key_here
```

> ⚠️ Never commit your `.env` file to version control. Add it to `.gitignore`.

### 5. Run the Application

```bash
python currency_converter_enhanced.py
```

---

## 💻 Example Session

```
==============================
 🌍  CURRENCY CONVERTER LIVE
==============================
 🛫  From (e.g. USD): USD

 📈  Current Rates for 1 USD:
------------------------------
  💰 EUR : 0.92
  💰 GBP : 0.79
  💰 JPY : 149.50
  💰 CAD : 1.36
  ... and more available!

------------------------------
 🛬  To (e.g. EUR): EGP
 💵  Amount to convert: 100

✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨
  ✅  100.0 USD = 4875.00 EGP
✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨

——————————————————————————————
 🔄  Convert another? (y/n):
```

---

## 📁 Project Structure

```
currency-converter/
├── currency_converter_enhanced.py   # Main application file
├── requirements.txt                 # Python dependencies
├── .env                             # API key (not committed to git)
├── .gitignore
└── README.md
```

---

## ⚠️ Known Limitations & Potential Improvements

- **Free tier rate limits** — The free Fixer plan has monthly request limits and may not support all base currencies (EUR only on some tiers)
- **No offline mode** — The app requires an active internet connection and will fail gracefully if unavailable
- **CLI only** — A GUI or web frontend could make the tool more accessible to non-technical users
- **No conversion history** — Past conversions are not saved between sessions

---

## 🤝 Contributing

Feel free to fork this project and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

---

## 👤 Author

Developed by **Omar Farouk**
