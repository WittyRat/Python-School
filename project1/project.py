"""1. Define the Core Game Mechanics

Decide the basic rules of your simulator:

Starting balance (e.g., $10,000 fake money)
Whether players can:
Buy stocks
Sell stocks
View price history
View portfolio performance
How often stock prices refresh (every minute? every day?)
Real vs. historical price tracking

c — Current Price

The most recent trading price.

This is what you use when buying/selling in your simulator.

d — Change

How much the price has moved today (in dollars).

Formula: current price − previous close
Example: If yesterday the stock closed at 150 and today it’s 155, d = 5.

dp — Percent Change

The same change, but in percentage.

Formula: (d / previous close) × 100
Example: If the stock is up 5 dollars on a 150 previous close:
dp = 3.33

h — High Price of the Day

The highest price the stock has reached today.

l — Low Price of the Day

The lowest price the stock has reached today.

o — Open Price of the Day

The price when the market opened today.

pc — Previous Close

The final trading price from the previous trading day.

t — Timestamp

The time of the latest price update.

Stored as a Unix timestamp (seconds since 1970).

Convert using Python’s datetime if needed.
"""

import requests

from pathlib import Path




class StockMarketGame:
    def __init__(self, starting_balance=10000):
        self.balance = starting_balance
        self.portfolio = {}
        self.transaction_log = []

    def fetch_price(self, symbol):
        API_KEY = Path("project1/apikey.txt").read_text(encoding="utf-8").strip()
        URL = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={API_KEY}"
        try:
            response = requests.get(URL)
            data = response.json()
            return data
        except Exception as e:
            print("Network/API error:", e)
            return None
    
    def print_info(self, symbol):
        print(f"The current price is {self.fetch_price(symbol)["c"]}$ per share")
        print(f"{symbol} price has moved today {self.fetch_price(symbol)["d"]}$ ({self.fetch_price(symbol)["dp"]}%)")
        print(f"Highest price of the day: {self.fetch_price(symbol)["h"]}$")
        print(f"Lowest price of the day: {self.fetch_price(symbol)["l"]}$")



    def buy_stock(self, money_to_be_used, symbol):
        if self.fetch_price(symbol) is None:
            print("Cannot buy - price unavailable.")
            return 0.0
        
        if money_to_be_used > self.balance:
            print("You do not have the sufficient funds to purchase this amount", self.balance)
            return 0.0
        
        amount_of_shares = money_to_be_used / self.fetch_price(symbol)["c"]

        self.balance -= money_to_be_used
        self.portfolio[symbol] = self.portfolio.get(symbol, 0) + amount_of_shares
        
        self.transaction_log.append({
            "action": "buy",
            "symbol": symbol,
            "price": self.fetch_price(symbol)["c"],
            "shares": amount_of_shares,
            "money": money_to_be_used
        })

        print(f"Bought {amount_of_shares} shares of {symbol} at {self.fetch_price(symbol)["c"]} each.")
        return amount_of_shares
    
    def sell_stock(self):
        pass

    def view_portfolio(self):
        print(self.portfolio)
        input()

def random_stocks():
    import random
    with open("project1/stockList.csv") as f:
        contents = f.read()
    stocks = contents.split(",")
    [print(f"{random.choice(stocks)}\t", end="") for i in range(5)] # add current prices to stocks

def main():
    while True:
        random_stocks()
        print("\n1. View stock info")
        print("2. Buy Stock")
        print("3. Sell Stock")
        print("4. View portfolio")
        print("5. View balance")
        print("6. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            symbol = input("What is the symbol of the stocks you want information on? ")
            game.print_info(symbol) #WHEN INFO IS PRINTED DONT LEAVE THIS AND LET USER ASK FOR INFO AGAIN OR LEAVE THIS CHOICE
            
        elif choice == "2":
            symbol = input("Enter the symbol of the stock you want to buy: ")
            amount = input("Enter the amount of money you want to use: ")
            game.buy_stock(float(amount), symbol)
        elif choice == "3":
            pass
        elif choice == "4":
            game.view_portfolio()    
        elif choice == "5":
            print(game.balance)
        else:
            break



if __name__ == "__main__":
    game = StockMarketGame()
    main()
#game = StockMarketGame()
#game.buy_stock(1000, "AAPL")
#print(game.balance)
#game.view_portfolio()
#print(game.transaction_log)



"""
2. Choose Your Data Source

Decide where to pull real market prices from. Options:

Yahoo Finance (via a Python library, easy, no API key)

A free API (e.g., Alpha Vantage, Finnhub)

A premium API (if you want faster updates)

Questions to answer:

Do you need real-time data or delayed?

How many stock symbols do you want to support?

Will the game run offline or online?

3. Plan the Game State Structure

Decide how you'll store the game’s information, such as:

Player balance

Portfolio (stocks owned, number of shares, average cost)

Price history (if needed)

Transaction logs

You should decide:

Will this be saved to a file (JSON)?

Reset every time the game restarts?

Allow loading/saving progress?

4. Design the User Interface

Pick the type of interface:

A. Console-Based Menu

Simple text interactions:

Type "buy" to buy a stock

Type “portfolio” to view holdings

B. GUI

Using:

Tkinter

PyQt

Kivy

Plan your screens:

Dashboard with balance + total value

Stock search

Buy/sell interface

Portfolio view

C. Web App

Using:

Flask

FastAPI

Streamlit

Plan web pages:

Home (game overview)

Buy/Sell page

Portfolio page

Performance graphs

5. Build the Price Update System

Plan how prices will be retrieved and refreshed:

Automated update every X minutes

Manual “Refresh Prices” button

Background thread if necessary (for continuous updating)

Handling network errors or API limits

6. Plan the Buy & Sell System

You need rules for:

Buying

Check if the player has enough money

Subtract cost

Add shares to portfolio

Selling

Check if the player owns enough shares

Add money back

Remove shares from portfolio

Track profit/loss on each sale

Also decide:

Do you track average cost per share?

Are fractional shares allowed?

7. Portfolio Tracking & Valuation

Plan features for showing:

Current total value

Total profit/loss

Value of each stock

Percentage changes

Lifetime performance graphs (optional)

Decide whether to show:

Real-time updates

Daily or historical charts

Market summaries

8. Add Game Features (Optional Enhancements)

Ideas you may want to include:

Daily income or bonuses

Achievements or milestones

Random news events affecting prices

Missions/challenges (e.g., grow $10k to $20k)

Short selling

Margin trading

Simulated trading fees

9. Design the Save/Load System

Decide how user progress is saved:

JSON files

SQLite database

Cloud storage (for a web version)

Plan for:

Auto-save on every transaction

Save on exit

Load on startup

10. Final Testing & Balancing

Test for:

Errors in buy/sell logic

Handling invalid stock symbols

API outages

Infinite loops or slow UI

Fairness and fun factor

Then refine:

Starting balance

Difficulty

Update speed

Any game events"""
