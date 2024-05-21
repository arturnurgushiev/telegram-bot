from src.currency_api import CurrencyAPI
from src.currency_analyzer import CurrencyAnalyzer
from src.telegram_bot import TelegramBot


class MainApp:
    def __init__(self, api_url, bot_token, threshold, interval):
        self.api = CurrencyAPI(api_url)
        self.analyzer = CurrencyAnalyzer(threshold)
        self.bot = TelegramBot(bot_token, self.api, self.analyzer, interval)

    def main(self):
        self.bot.start_polling()

if __name__ == "__main__":
    API_URL = "https://open.er-api.com/v6/latest/RUB"
    BOT_TOKEN = "7021892817:AAHvmuI0sCD6-oqbJA6XBK32Az36I1npots"

    THRESHOLD = 0.05  # Пороговое значение для значительных изменений (например, 5%)
    INTERVAL = 3600  # Интервал проверки данных (например, 1 час)

    app = MainApp(API_URL, BOT_TOKEN, THRESHOLD, INTERVAL)
    app.main()

