import os
from dotenv import load_dotenv
import openai
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# טוען משתני סביבה
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_KEY

# פקודת התחלה
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("היי! אני הבוט החכם שלך 🤖 דבר איתי חופשי...")

# כל הודעה -> נשלחת למודל
async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",   # מודל קליל וזול
            messages=[{"role": "user", "content": user_text}]
        )
        bot_reply = response.choices[0].message.content
        await update.message.reply_text(bot_reply)

    except Exception as e:
        await update.message.reply_text(f"❌ שגיאה: {e}")

# הפעלת הבוט
if __name__ == "__main__":
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
    print("🚀 הבוט רץ... לחץ Ctrl+C לעצירה")
    app.run_polling()
