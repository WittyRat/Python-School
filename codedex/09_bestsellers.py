"""We've all seen, perhaps bought, one of our favorite products with a "Bestseller" sticker. 🏅

Let’s write a program to read a CSV file and find the best-selling book of all time. 🔍

Download this CSV file of all-time bestselling books data!
Open the Bestseller - Sheet1.csv file in "read" mode.
Use the CSV reader to navigate through the data and find the book with the highest sales, via the sales in millions column.
Create a new file called bestseller_info.csv with the CSV writer.
In the new file, use .writerow() to add new CSV data.
Up next, let’s learn about what to do in the face of the unexpected, we'll be exploring error handling."""

import csv

max_sales = 0


with open("Bestseller.csv", "r", encoding="utf8") as file:
    file.readline()
    csv_reader = csv.reader(file)
    
    
    for row in csv_reader:
        current_sales = float(row[4])
        if current_sales > max_sales:
            max_sales = current_sales
            best_selling_book = row

with open("bestseller_info.csv", "w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Book", "Author", "Sales in Millions"])
    csv_writer.writerow([best_selling_book[0], best_selling_book[1], best_selling_book[4]])