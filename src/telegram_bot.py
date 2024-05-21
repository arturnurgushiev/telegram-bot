import telebot
import time

class TelegramBot:
    def __init__(self, bot_token, api, analyzer, interval):
        self.bot = telebot.TeleBot(bot_token)
        self.api = api
        self.analyzer = analyzer
        self.user_id = None
        self.interval = interval
        self.is_running = False

        @self.bot.message_handler(commands=['start'])
        def start(message):
            self.is_running = True
            self.user_id = message.chat.id
            self.bot.send_message(self.user_id, f"Bot started. Your user_id is {self.user_id}.")
            self.run()

        @self.bot.message_handler(commands=['stop'])
        def stop(message):
            self.is_running = False
            if self.user_id:
                self.bot.send_message(self.user_id, "Bot stopped.")

    def run(self):
        while self.is_running:
            try:
                currency_data = self.api.get_currency_data()
                significant_changes = self.analyzer.analyze_currency_data(currency_data)
                if significant_changes:
                    message = "Significant currency changes detected:\n"
                    for change in significant_changes:
                        message += (
                            f"{change['currency']}: {change['previous_value']} -> {change['current_value']} "
                            f"({change['change']*100:.2f}%)\n"
                        )
                    if self.user_id:
                        self.bot.send_message(self.user_id, message)
            except Exception as e:
                print(f"Error: {e}")
            time.sleep(self.interval)

    def start_polling(self):
        self.bot.polling()
