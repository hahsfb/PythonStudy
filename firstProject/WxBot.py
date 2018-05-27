from wxpy import Bot, Tuling, embed, ensure_one

bot = Bot(cache_path=True)

# 想和机器人聊天的好友的备注
# my_friend = ensure_one(bot.search('Say Hello'))

# 记得把名字改成想用机器人的群
my_group = bot.groups().search('chatbot')[0]
tuling = Tuling(api_key='29fcb3f764504aea9301df5630ed52dd')


# 使用图灵机器人自动与指定好友聊天
@bot.register(my_group, except_self=False)
def reply_my_friend(msg):
    tuling.do_reply(msg)

embed()
