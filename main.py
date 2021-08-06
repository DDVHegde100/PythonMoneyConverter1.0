from forex_python.converter import CurrencyRates
c = CurrencyRates()
amount = int(input("Enter the amount: "))
starting = input("Enter Beginning Currency Code: ").upper()
ending = input("Enter Ending Currency Code: ").upper()
print(from_currency, " To ", to_currency, amount)
result = c.convert(starting, ending, amount)
print(result)
