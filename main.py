from pyrogram import Client, filters
from config import BOT_TOKEN, API_ID, API_HASH, CHANNEL_ID
from downloader import download_video
from uploader import upload_to_telegram

bot = Client("sameer_bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

@bot.on_message(filters.private & filters.command("start"))
async def start_handler(client, message):
    await message.reply_text("👋 Namaste! SAMEER JI ALL ROUNDER BOT ready hai!\n\n/video <link> <quality> <batch> bhejo!")

@bot.on_message(filters.private & filters.command("video"))
async def video_handler(client, message):
    try:
        _, link, quality, batch = message.text.split(maxsplit=3)
        file_path = await download_video(link, quality, batch)
        await upload_to_telegram(bot, message.from_user.id, file_path, batch)
    except Exception as e:
        await message.reply_text(f"⚠️ Error: {e}")

bot.run()
