from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?start=help",
            ),
            InlineKeyboardButton(
                text=_["S_B_2"], callback_data="settings_helper"
            ),
        ],
    ]
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                InlineKeyboardButton(
                    text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text=_["S_B_3"], url=f"{SUPPORT_GROUP}"
                ),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"
                    )
                ]
            )
        if SUPPORT_GROUP:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_3"], url=f"{SUPPORT_GROUP}"
                    )
                ]
            )
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✚ Click here to Summon Me",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(text="📨 Support", url=f"{SUPPORT_GROUP}"),
            InlineKeyboardButton(
                text="📨 Updates", url=f"{SUPPORT_CHANNEL}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🔍 How to use ? Commands", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="🏳️‍🌈 Owner", user_id=OWNER),
            InlineKeyboardButton(
                text="🌐 GitHub", url=f"https://github.com/UnknownMortal/Yukki-Clone"
            ),
        ],
     ]
    return buttons
