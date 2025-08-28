import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot Token
TOKEN = "8120240806:AAGiWmgAHk9XGGm2MucMIPBfH1xBgARwAmc"

# Links
TELEGRAM_CHANNEL = "https://t.me/intex_A"
TELEGRAM_GROUP = "https://t.me/Intex_chat"
TWITTER = "https://x.com/INTEX_029?t=xBT7Lt_wCqKVuK4HfKRWtQ&s=09"

# Start command
async def start(update: Update, context: CallbackContext):
    user = update.effective_user
    keyboard = [
        [InlineKeyboardButton("📢 Join Telegram Channel", url=TELEGRAM_CHANNEL)],
        [InlineKeyboardButton("💬 Join Telegram Group", url=TELEGRAM_GROUP)],
        [InlineKeyboardButton("🐦 Follow Twitter", url=TWITTER)],
        [InlineKeyboardButton("✅ Done", callback_data="done")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        f"👋 Hello {user.first_name}!\n\nWelcome to **INTEX Airdrop Bot** 🚀\n\n"
        f"Complete the tasks below to join the airdrop:",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

# Done button handler
async def button(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    if query.data == "done":
        ref_link = f"https://t.me/{context.bot.username}?start={query.from_user.id}"
        await query.edit_message_text(
            text=(
                "🎉 Congratulations! You have completed the tasks.\n\n"
                f"🔗 Your referral link:\n{ref_link}\n\n"
                "Invite friends and earn more rewards!"
            )
        )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    app.run_polling()

if __name__ == "__main__":
    main()
