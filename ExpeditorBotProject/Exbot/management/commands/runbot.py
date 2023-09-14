from django.core.management.base import BaseCommand
from django.conf import settings
import telebot


class Command(BaseCommand):
    help = "Run Bot"

    def handle(self, *args, **options):
        bot = telebot.TeleBot(settings.TG_TOKEN)
        bot.send_message(5624258791, "Начало")
        print("YES")
