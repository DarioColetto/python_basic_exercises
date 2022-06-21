import stock
a = stock.Stock('GOOG', 100, 490.10)
b = stock.Stock('AAPL', 50, 122.34)
c = stock.Stock('IBM', 75, 91.75)

print(b.shares * b.price)
print(c.shares * c.price)
stocks = [a, b, c]
print(stocks)

for s in stocks:
    print(f'{s.name:<10} {s.shares:^} {s.price:>10}')
