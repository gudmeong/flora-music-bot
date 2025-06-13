import asyncio

import speedtest
from WinxMusic import app
from WinxMusic.misc import SUDOERS
from strings import command


@app.on_message(command("SPEEDTEST_COMMAND") & SUDOERS)
async def speedtest_function(client, message):
    m = await message.reply_text("🚀 **Iniciando SpeedTest**...")

    def run_speedtest():
        try:
            test = speedtest.Speedtest()
            test.get_best_server()
            test.download()
            test.upload()
            test.results.share()
            return test.results.dict()
        except Exception as e:
            return {"error": str(e)}

    async def update_status():
        stages = [
            "⏳ Testing **download** ... ⬇️",
            "⏳ Testing **upload** ... ⬆️",
            "↻ Finalizing result... 📊"
        ]

        for stage in stages:
            if not speedtest_task.done():
                try:
                    await m.edit(stage)
                    await asyncio.sleep(3)
                except Exception:
                    pass

    speedtest_task = app.loop.run_in_executor(app.executor, run_speedtest)

    update_task = asyncio.create_task(update_status())

    result = await speedtest_task

    if not update_task.done():
        update_task.cancel()

    if "error" in result:
        await m.edit(f"⚠️ **ERROR:**\n\n`{result['error']}`")
        return

    latency = str(result['server']['latency']).replace('.', ',')
    ping = str(result['ping']).replace('.', ',')

    output = f"""**Speedtest Results** 📊

<u>**Client:**</u>
🌐 **ISP:** {result['client']['isp']}
🏳️ **Country:** {result['client']['country']}

<u>**Servee:**</u>
🌍 **Nome:** {result['server']['name']}
🇦🇺 **Country:** {result['server']['country']}, {result['server']['cc']}
💼 **Sponsor:** {result['server']['sponsor']}
⚡ **Latency:** {latency} ms  
🏓 **Ping:** {ping} ms"""

    try:
        await app.send_photo(
            chat_id=message.chat.id,
            photo=result["share"],
            caption=output
        )
        await m.delete()
    except Exception as e:
        await m.edit(f"⚠️ **An Error occured:**\n\n`{str(e)}`")
