


@bot.message_handler(commands=["start"])
def start(message):
    driving_completed = False
    markup = types.InlineKeyboardMarkup()
    wake_up = types.InlineKeyboardButton(text="ПРОСНУТЬСЯ", callback_data="wake_up")
    markup.add(wake_up)
    bot.send_message(message.chat.id, "Начало", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def delete_message(message):
    bot.delete_message(message.chat.id, message.message_id)


@bot.callback_query_handler(func=lambda call: call.data == "wake_up")
def wake_up(call):
    markup1 = types.InlineKeyboardMarkup()
    go_to_storage = types.InlineKeyboardButton(text="ВЫЕХАТЬ НА СКЛАД", callback_data="go_to_storage")
    markup1.add(go_to_storage)
    bot.edit_message_text("Вы проснулись", call.message.chat.id, call.message.message_id, reply_markup=markup1)


@bot.callback_query_handler(func=lambda call: call.data == "go_to_storage")
def go_to_storage(call):
    markup2 = types.InlineKeyboardMarkup()
    arrive_to_storage = types.InlineKeyboardButton(text="ПРИБЫТЬ НА СКЛАД", callback_data="arrive_to_storage")
    markup2.add(arrive_to_storage)
    bot.edit_message_text("Вы выехали на склад", call.message.chat.id, call.message.message_id, reply_markup=markup2)


@bot.callback_query_handler(func=lambda call: call.data == "arrive_to_storage")
def arrive_to_storage(call):
    markup3 = types.InlineKeyboardMarkup()
    load = types.InlineKeyboardButton(text="ПОГРУЗИТЬСЯ", callback_data="load")
    markup3.add(load)
    bot.edit_message_text("Вы прибыли на склад", call.message.chat.id, call.message.message_id, reply_markup=markup3)


@bot.callback_query_handler(func=lambda call: call.data == "load")
def load(call):
    markup4 = types.InlineKeyboardMarkup()
    say_address = types.InlineKeyboardButton(text="СООБЩИЛИ АДРЕС", callback_data="say_address")
    markup4.add(say_address)
    bot.edit_message_text("Вы погрузились", call.message.chat.id, call.message.message_id, reply_markup=markup4)


@bot.callback_query_handler(func=lambda call: call.data == "say_address")
def say_address(call):
    markup5 = types.InlineKeyboardMarkup()
    arrive_to_point = types.InlineKeyboardButton(text="ПРИБЫТЬ НА ТОЧКУ", callback_data="arrive_to_point")
    markup5.add(arrive_to_point)
    bot.edit_message_text("Вам сообщили адрес", call.message.chat.id, call.message.message_id, reply_markup=markup5)


@bot.callback_query_handler(func=lambda call: call.data == "arrive_to_point")
def arrive_to_point(call):
    markup6 = types.InlineKeyboardMarkup()
    unload = types.InlineKeyboardButton(text="РАЗГРУЗИТЬСЯ", callback_data="unload")
    markup6.add(unload)
    bot.edit_message_text("Вы прибыли на точку", call.message.chat.id, call.message.message_id, reply_markup=markup6)


@bot.callback_query_handler(func=lambda call: call.data == "unload")
def unload(call):
    markup7 = types.InlineKeyboardMarkup()
    yes = types.InlineKeyboardButton(text="ДА", callback_data="yes")
    no = types.InlineKeyboardButton(text="НЕТ", callback_data="no")
    markup7.add(yes, no)
    bot.edit_message_text("Есть еще адрес?", call.message.chat.id, call.message.message_id, reply_markup=markup7)


@bot.callback_query_handler(func=lambda call: call.data in ("yes", "no"))
def yes_or_no(call):
    if call.data == "yes":
        markup5 = types.InlineKeyboardMarkup()
        arrive_to_point_button = types.InlineKeyboardButton(text="ПРИБЫТЬ НА ТОЧКУ", callback_data="arrive_to_point")
        markup5.add(arrive_to_point_button)
        bot.edit_message_text("Вам сообщили адрес?", call.message.chat.id, call.message.message_id, reply_markup=markup5)
    else:
        markup8 = types.InlineKeyboardMarkup()
        complete_driving = types.InlineKeyboardButton(text="ЗАВЕРШИТЬ РЕЙС", callback_data="complete_driving")
        markup8.add(complete_driving)
        bot.edit_message_text("Точек больше нет", call.message.chat.id, call.message.message_id, reply_markup=markup8)


@bot.callback_query_handler(func=lambda call: call.data == "complete_driving")
def driving_completed(call):
    markup = types.InlineKeyboardMarkup()
    wake_up = types.InlineKeyboardButton(text="ПРОСНУТЬСЯ", callback_data="wake_up")
    markup.add(wake_up)
    bot.send_message(call.message.chat.id, "Рейс завершен", reply_markup=markup)


if __name__ == "__main__":
    bot.polling(none_stop=True)

