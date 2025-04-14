# Don't Remove Credit Telegram - @ASHIQI_092
import time
import math
import os
from pyrogram.errors import FloodWait
from datetime import datetime, timedelta

class Timer:
    def __init__(self, time_between=5):
        self.start_time = time.time()
        self.time_between = time_between

    def can_send(self):
        if time.time() > (self.start_time + self.time_between):
            self.start_time = time.time()
            return True
        return False

def hrb(value, digits=2, delim="", postfix=""):
    if value is None:
        return None
    chosen_unit = "B"
    for unit in ("KiB", "MiB", "GiB", "TiB"):
        if value > 1000:
            value /= 1024
            chosen_unit = unit
        else:
            break
    return f"{value:.{digits}f}" + delim + chosen_unit + postfix

def hrt(seconds, precision=0):
    pieces = []
    value = timedelta(seconds=seconds)

    if value.days:
        pieces.append(f"{value.days}d")

    seconds = value.seconds

    if seconds >= 3600:
        hours = int(seconds / 3600)
        pieces.append(f"{hours}h")
        seconds -= hours * 3600

    if seconds >= 60:
        minutes = int(seconds / 60)
        pieces.append(f"{minutes}m")
        seconds -= minutes * 60

    if seconds > 0 or not pieces:
        pieces.append(f"{seconds}s")

    if not precision:
        return "".join(pieces)

    return "".join(pieces[:precision])

timer = Timer()

async def progress_bar(current, total, reply, start):
    if timer.can_send():
        now = time.time()
        diff = now - start
        if diff < 1:
            return
        perc = f"{current * 100 / total:.1f}%"
        elapsed_time = round(diff)
        speed = current / elapsed_time
        remaining_bytes = total - current
        eta = hrt(remaining_bytes / speed, precision=1) if speed > 0 else "-"
        sp = str(hrb(speed)) + "/s"
        tot = hrb(total)
        cur = hrb(current)
        bar_length = 11
        completed_length = int(current * bar_length / total)
        remaining_length = bar_length - completed_length
        progress_bar = "►" * completed_length + "▷" * remaining_length

        try:
            await reply.edit(
                f'<b>\n ╭──⌯════⬇️𝗨𝗣𝗟𝗢𝗔𝗗𝗜𝗡𝗚⬇️═════⌯──╮ \n'
                f'├⚡ {progress_bar}|﹝{perc}﹞ \n'
                f'├🚀 Speed » {sp} \n'
                f'├📟 Processed » {cur}\n'
                f'├🧲 Size - ETA » {tot} - {eta} \n'
                f'├🤖 Bot Made By » @ASHIQI_092\n'
                f'╰─═══ ✪👨🏻‍💻𝗗𝗢𝗖𝗧𝗢𝗥👨🏻‍💻✪ ═══─╯\n\n'
                f'🥺हम इतने बुरे हो गए याद भी नहीं आते है किसी को 😭</b>'
            )
        except FloodWait as e:
            time.sleep(e.x)
