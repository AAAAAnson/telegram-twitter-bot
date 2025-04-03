from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import yt_dlp
import os

BOT_TOKEN = "YOUR_BOT_TOKEN"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("欢迎！请发送包含 Twitter 视频的推文链接。")

async def download_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.strip()
    if "twitter.com" not in url:
        await update.message.reply_text("请发送有效的 Twitter 视频链接。")
        return

    await update.message.reply_text("正在下载视频，请稍候...")

    ydl_opts = {
        'format': 'best',
        'outtmpl': '/tmp/%(id)s.%(ext)s',
        'quiet': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            video_path = ydl.prepare_filename(info)

        with open(video_path, 'rb') as f:
            await update.message.reply_video(video=f)
        os.remove(video_path)
    except Exception as e:
        await update.message.reply_text("下载失败，请确认链接有效，或稍后再试。")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_video))
    app.run_polling()

if __name__ == '__main__':
    main()