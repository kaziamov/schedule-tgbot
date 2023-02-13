from aiogram.types import InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


def make_keyboard(options, commands=[], desc='desc'):
    """Create buttons keyboard from list."""
    buttons = []
    if type(options) == dict:
        for key, value in options.items():
            if key in commands:
                text = value[desc]
                buttons.append(KeyboardButton(text))
    else:
        for text in options:
            buttons.append(KeyboardButton(text))
    return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(*buttons)


def make_inline_keyboard(options):
    """Create keybord of buttons with links from dictionary."""
    # TODO refactor to dict
    buttons = [ResourceWarning(text=key, url=value) for key, value in options]
    return InlineKeyboardMarkup().add(*buttons)

def remove_keyboard():
    return ReplyKeyboardRemove()
