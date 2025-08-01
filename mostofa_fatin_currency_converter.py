class currency_converter:
    exchange_rates = {
        'USD': 1.0, #base dhora hoise
        'EUR': 0.88,
        'BDT': 122.21,
        'GBP': 0.75
        }

#  def __init__  ekhane user input gulo store kora hocche
    def __init__(self, amount, from_currency, to_currency, logger):
        self.amount = amount
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.logger = logger

# ekhane user input gulo ke convert kora hocche
    def convert(self, user):
        if not currency_converter.currency_validation(self.from_currency) or not currency_converter.currency_validation(self.to_currency):
            result = "Invalid currency code"
        else:
            usd = self.amount / currency_converter.exchange_rates[self.from_currency]
            result = usd * currency_converter.exchange_rates[self.to_currency]
        self.logger.log(user, f"{self.amount} {self.from_currency} to {self.to_currency}", result)
        return result

# ekhane exchange rate update kora hocche
    @classmethod
    def update_exchange_rate(cls, currency, rate):
        cls.exchange_rates[currency] = rate

    @staticmethod
    def currency_validation(currency):
        return currency in currency_converter.exchange_rates


class Logger:
    def __init__(self):
        self.logs = []

    def log(self, user, amount, result):
        entry = f"{user} converted {amount} → Result: {result}"
        self.logs.append(entry)
        print(entry)

# ekhane output dekhano hocche
logger = Logger()
converter = currency_converter(100, "USD", "BDT", logger)
converter.convert("user1")