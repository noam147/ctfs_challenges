from telegram import Update
from telegram.ext import MessageHandler, ContextTypes, filters,Updater,Application
import asyncio
BOT_TOKEN = '7664685884:AAHDjGavBpRHWristKf_u5Om-mUuXFT-ikQ'  # Replace with your actual token
# Handler for all text messages
# Handler for all text messages
async def handle_message(update: Update, context):
    user_message = update.message.text
    if user_message.lower() == "#freepalestine":
        await update.message.reply_text("Right!\nDo not forget the BONUS{FR##_P@LE$T!NE}")
        return
    await update.message.reply_text(f"Hello!\nresistance is the only solution! ")

# Main function to set up and run the bot
def main():
    # Create the Application with the bot token
    app = Application.builder().token(BOT_TOKEN).build()

    # One handler for all text messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()  # Starts polling for messages

# Run the bot
if __name__ == '__main__':
    main()