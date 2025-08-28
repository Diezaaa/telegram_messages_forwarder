from pyrogram import Client, filters

api_id = 27960228
api_hash = "b8c3132ab61115b00ba2a90974b5cc53"

app = Client("my_account", api_id=api_id, api_hash=api_hash)

SOURCE_CHAT_ID = -4982847299
DEST_CHAT_ID = -4830997657

@app.on_message(filters.chat(SOURCE_CHAT_ID))
def forward_message(client, message):
    client.send_message(chat_id=DEST_CHAT_ID, text=message.text)

app.run()