DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/a5aa529850eca1fcca807.jpg"
pm_caption = "`DARKSIDE USERBOT IS:` **ALIVE**\n\n"
pm_caption += "**SYSTEM STATUS**\n"
pm_caption += "`TELETHON VERSION:` **1.22.0**\n"
pm_caption += "✘ ᗩᗷOᑌT ᗰY ՏYՏTᗴᗰ ✘\n\n"
pm_caption += "**DARKSIDE SUPPORT [DARKSIDE]** :(https//t.me/DARKAMANSUPPORT)\n"
pm_caption += f"**My Boss** : {DEFAULTUSER} \n"
pm_caption += "**Made By 😇✨** : @DARKAMAN\n\n"
pm_caption += "Deploy Your Own : [Repo](https://github.com/DARKAMAN5/DARKSIDE)\n"

@borg.on(admin_cmd(pattern=r"alive"))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()

    
@borg.on(admin_cmd(pattern=r"Alive", allow_sudo=True))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)

    
