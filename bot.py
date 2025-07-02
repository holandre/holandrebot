
import os
import telebot
from flask import Flask, request

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))
BTC_ADDRESS = os.getenv("BTC_ADDRESS")
LTC_ADDRESS = os.getenv("LTC_ADDRESS")
PAYPAL_LINK = os.getenv("PAYPAL_LINK")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Bienvenue sur HolandreBot !\n\nProduits disponibles :\n1. Ebook complet ewhoring - 20€\n2. Logiciel de la préfecture carte d'identité - 35€\n\nClique sur /produits pour voir les détails.")

@bot.message_handler(commands=["produits"])
def send_products(message):
    bot.reply_to(message, "📦 *Produits disponibles :*\n\n1️⃣ *Ebook complet ewhoring* - 20€\n📥 Livraison automatique après paiement.\n\n2️⃣ *Logiciel de la préfecture carte d'identité* - 35€\n📥 Livraison manuelle après confirmation.\n\nCommande avec /payer", parse_mode="Markdown")

@bot.message_handler(commands=["payer"])
def send_payment(message):
    bot.reply_to(message, f"💸 *Méthodes de paiement disponibles :*\n\n1. Bitcoin (BTC)\nAdresse : `{BTC_ADDRESS}`\n\n2. Litecoin (LTC)\nAdresse : `{LTC_ADDRESS}`\n\n3. PayPal : {PAYPAL_LINK}\n\nAprès paiement, envoie une preuve à @L1007.", parse_mode="Markdown")

@bot.message_handler(commands=["aide"])
def send_help(message):
    bot.reply_to(message, "Besoin d'aide ? Contacte le support : @L1007")

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "OK", 200

@app.route("/", methods=["GET"])
def index():
    return "Bot en ligne."

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=os.getenv("APP_URL") + "/" + TOKEN)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
