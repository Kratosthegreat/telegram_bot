import os
from dotenv import load_dotenv
import google.generativeai as genai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# טוען משתני סביבה
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

# קונפיגורציה ל-Gemini
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# פקודת start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("היי! אני הבוט החכם שלך עם Gemini 🤖 דבר איתי חופשי...")

# שיחה חופשית עם Gemini
async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    try:
        response = model.generate_content(user_text)
        bot_reply = response.text
        await update.message.reply_text(bot_reply)
    except Exception as e:
        await update.message.reply_text(f"❌ שגיאה: {e}")

# הפעלת הבוט
if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
    print("🚀 הבוט רץ... לחץ Ctrl+C לעצירה")
    app.run_polling()

