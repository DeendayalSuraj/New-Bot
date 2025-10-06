import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# --- Configuration ---
# Get these values from my.telegram.org
API_ID = os.environ.get("API_ID", 123456)  # Replace with your API_ID
API_HASH = os.environ.get("API_HASH", "YOUR_API_HASH")  # Replace with your API_HASH
BOT_TOKEN = os.environ.get("BOT_TOKEN", "YOUR_BOT_TOKEN")  # Replace with your Bot Token

# --- Initialize the Client ---
app = Client(
    "my_auto_reply_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


# --- Auto-Reply Handler ---
# This function will now trigger on every text message sent in a group.
# - filters.group: Only triggers in group chats.
# - filters.text: Only triggers for text messages (not stickers, photos, etc.).
# - ~filters.bot: Ignores messages sent by other bots (and itself) to prevent loops.
@app.on_message(filters.group & filters.text & ~filters.bot)
async def auto_reply_handler(client, message):
    """
    This function automatically replies to every text message in a group
    with a predefined message and buttons.
    """
    message_text = "✨ **Join our network to get the best content!** ✨"

    # --- Create the Buttons ---
    # IMPORTANT: Replace the placeholder URLs with your actual group/channel links!
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="🎬 Join Movies Group",
                    url="https://t.me/Deendayal_Hindi_Movies"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📺 Join Movies Channel",
                    url="https://t.me/Deendayal_dhakadd"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔔 Join Movies Update Channel",
                    url="https://t.me/+NEOLX5nyXmg4M2Nl"
                )
            ]
        ]
    )

    # --- Send the Reply ---
    # Using quote=True makes it a direct reply to the user's message.
    await message.reply_text(
        text=message_text,
        reply_markup=keyboard,
        disable_web_page_preview=True,
        quote=True
    )


# --- Start the Bot ---
print("Bot is starting with auto-reply feature enabled...")
app.run()
print("Bot has stopped.")

