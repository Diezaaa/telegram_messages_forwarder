from pyrogram import Client, filters

api_id = 27960228
api_hash = "b8c3132ab61115b00ba2a90974b5cc53"

app = Client("my_account", api_id=api_id, api_hash=api_hash)

SOURCE_CHAT_ID = -4982847299
DEST_CHAT_ID = -4905406251

@app.on_message(filters.chat(SOURCE_CHAT_ID))
def get_chat_id(client, message):
    message.forward(chat_id=DEST_CHAT_ID)

app.run()