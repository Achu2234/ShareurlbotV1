import urllib
from pyrogram import Client, filters
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent)
from config import Config

bot = Client(
    'shareurl-generator',
    bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH
)


@bot.on_message(filters.command(['start']))
def start(client, message):
    rep = f"**Hi {message.from_user.username}**\n\n**Am a bot to convert __text into Shareable telegram link__.**\nWorks on both **in pm and in Inline😊**\n\nClick __/help__ if needed.."
    message.reply_text(
        text=rep, 
        quote=False,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Updates Channel', url='https://t.me/Animemusicarchive6')],[InlineKeyboardButton("Search Here", switch_inline_query_current_chat=""),InlineKeyboardButton("Go Inline", switch_inline_query="")], [InlineKeyboardButton('Share Me', url='https://t.me/share/url?url=Click%20to%20CopY%E2%AC%87%EF%B8%8F%E2%AC%87%EF%B8%8F%20%0A%0Ahttps%3A//t.me/share/url%3Furl%3D%252A%252Ahello%2520sir%2520%25F0%259F%2591%258B%252A%252A%250A%250A__i%2520just%2520found%2520a%2520bot%2520to%2520convert__%2520%252A%252Atext%2520as%2520a%2520shareable%2520text%2520link%252A%252A%2520__format%2520%25F0%259F%25A4%25A9.%2520hope%2520it%2520would%2520be%2520very%2520helpful%2520for%2520u%2520too...%25F0%259F%25A4%2597%25F0%259F%25A4%2597__%250A%250A%252A%252Abot%2520link%253A%2520%2540shareururlbyyeagerist_bot%2520%25F0%259F%25A5%25B0%252A%252A')]]))

@bot.on_message(filters.command(['help']))
def help(client, message):
    message.reply_text("**Nothing Complicated..🤓**\n\n**For PM:**\n__Send your desired text to this bot to get your link.__\n\n**For Inline Method:**\n__Type__  `@Shareururlbyyeagerist_bot your text`\n__in any chats keyboard and hit the inline result.__", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Channel', url='https://t.me/Animemusicarchive6')]]))

@bot.on_message(filters.command(['about']))
def about(client, message):
    message.reply_text(f"""**• Bot Info •**
**My Name** :- `Yᴇᴀɢᴇʀɪsᴛ Share Url Generator`
**Creator** :- @Amalbiju154
**Language** :- `Python3`
**Library** :- `Pyrogram 1.2.8`
**Server** :- `Heroku.com`
**Build Status** :- `V 0.2`

**• User Info •**
**Name** :- `{message.from_user.first_name} {message.from_user.last_name}`
**ID** :- `{message.from_user.id}`
**Username** :- @{message.from_user.username}
**DC ID** :- `{message.from_user.dc_id}`""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Channel', url = 'https://t.me/Animemusicarchive6')]]))


@bot.on_message(filters.text)
def shareurl(client, message):
    query = message.text
    url = urllib.parse.quote(query)
    rpl = f"https://t.me/share/url?url={url}"
    rslt = f"""**Click to CopY ⬇️⬇️** \n\n```{rpl}```"""
    message.reply_text(text=rslt, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Click to Try on This Link ⬆️⬆️', url=f'{rpl}')]]))

@bot.on_inline_query()
def inline(client, message): 
  query = message.query.lower()
  if query == "":
        result= [InlineQueryResultArticle(title = "Help !!",
                     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Search Here", switch_inline_query_current_chat=""),InlineKeyboardButton("Go Inline", switch_inline_query="")]]),
                     description ="How t0 usE meH !!",
                     thumb_url="https://telegra.ph/file/99d8f16a777c2ee2781c1.jpg",
                     input_message_content = InputTextMessageContent(message_text ="**Nothing Complicated..**🤓\n\nType `@Shareururlbyyeagerist_bot your text` \nin any chats keyboard and hit the inline result.\n\nNote: __U can also use Me in PM!__"))
                ] 
        message.answer(result) 
        return
  else:
     url = urllib.parse.quote(query)
     rpl = f"https://t.me/share/url?url={url}"
     rslt = f"""**Click to CopY⬇️⬇️** \n\n```{rpl}```"""
     result = [InlineQueryResultArticle(title = f'{query}',
               description =f'{rpl}',                        
               reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Click to Try on This linK ⬆️⬆️', url=f'{rpl}')], [InlineKeyboardButton("Search Again", switch_inline_query_current_chat=""),InlineKeyboardButton("Go Inline", switch_inline_query="")]]),
               input_message_content = InputTextMessageContent(message_text = rslt))
              ]
  
  message.answer(result)

bot.run()
