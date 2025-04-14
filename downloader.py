import os
import asyncio
from datetime import datetime

async def download_video(link, quality, batch):
    folder = f"downloads/{batch}"
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f"{folder}/{timestamp}.mp4"
    
    cmd = f'yt-dlp -f "bestvideo[height<={quality}]+bestaudio/best[height<={quality}]" "{link}" -o "{output_path}"'
    process = await asyncio.create_subprocess_shell(cmd)
    await process.communicate()
    
    if not os.path.exists(output_path):
        raise Exception("Download failed!")
    return output_path
