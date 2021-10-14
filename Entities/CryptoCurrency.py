class CryptoCurrency():
    def __init__(self, name, symbol, slug, is_active, last_updated, quote):
        self.name = name
        self.symbol = symbol
        self.slug = slug
        self.is_active = is_active
        self.last_updated = last_updated
        self.quote = Quote(self)