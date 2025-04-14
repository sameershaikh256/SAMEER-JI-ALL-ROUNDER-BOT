from config import CHANNEL_ID
import os

async def upload_to_telegram(bot, user_id, file_path, batch):
    caption = f"🎥 Batch: {batch}\n📁 File: {os.path.basename(file_path)}"
    await bot.send_video(chat_id=CHANNEL_ID, video=file_path, caption=caption)
    await bot.send_message(chat_id=user_id, text="✅ Upload done!")
    os.remove(file_path)
