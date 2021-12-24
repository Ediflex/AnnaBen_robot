import os
from pyrogram import Client, filters
from pyrogram.types import Message, User



@Client.on_message(filters.new_chat_members)
async def welcome(bot,message):
	chatid= message.chat.id
	await bot.send_message(text=f" Hey Welcome {message.from_user.mention} to {message.chat.username} , 📺 Movie Bus 📺",chat_id=chatid)
	
@Client.on_message(filters.left_chat_member)
async def goodbye(bot,message):
	chatid= message.chat.id
	await bot.send_message(text=f"Bye ,  {message.from_user.mention} , പോയിട്ട് Vada ഞാൻ നിന്നെ Wait ചെയ്യുന്നുണ്ട്",chat_id=chatid)
	

