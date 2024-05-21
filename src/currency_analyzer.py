class CurrencyAnalyzer:
    def __init__(self, threshold):
        self.interesting = ["USD", "EUR", "CNY", "HKD"]
        self.threshold = threshold
        self.previous_data = None

    def analyze_currency_data(self, current_data):
        if not self.previous_data:
            self.previous_data = current_data['rates']
            return []

        significant_changes = []
        for currency, value in current_data['rates'].items():
            if currency in self.previous_data and currency in self.interesting:
                previous_value = self.previous_data[currency]
                change = (value - previous_value) / previous_value
                if abs(change) >= self.threshold:
                    significant_changes.append({
                        'currency': currency,
                        'previous_value': previous_value,
                        'current_value': value,
                        'change': change
                    })

        self.previous_data = current_data['rates']
        return significant_changes