from bonji_bot.bot import TGBot, types
from rest_framework.response import Response
from rest_framework.views import APIView
from BONJI_store.settings import TOKEN
from bonji_bot.models import TelegramCustomer, TelegramCart

bot = TGBot(TOKEN)


class BotView(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Bot works!")

    def post(self, request, *args, **kwargs):
        json_str = request.body.decode('UTF-8')
        update = types.Update.de_json(json_str)
        bot.process_new_updates([update])

        return Response({'code': 200})


### Checking if user started conversation. Showing Keyboard.
@bot.message_handler(commands=['start'])
def start_message(message):
    user, created = TelegramCustomer.objects.get_or_create(
        telegram_id = message.from_user.id,
        username = message.from_user.username,
        first_name = message.from_user.first_name,
        last_name = message.from_user.last_name,
    )
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [types.KeyboardButton("Catalog"), types.KeyboardButton("Cart"),]
    kb.add(*buttons)

    bot.send_message(message.chat.id, "Hello! What would you like to buy today?",
                        reply_markup=kb)


# Checking if user clicked "Catalog". Showing list of categories.
@bot.message_handler(func=lambda message: message.text == "Catalog")
def show_catalog(message):
    bot.send_categories(message)


# Checking if user clicked "Cart". Showing cart content.
@bot.message_handler(func=lambda message: message.text == "Cart")
def show_cart(message):
    bot.send_cart(message.from_user.id)


# When user clicks on some category. Showing products of the category.
@bot.inline_handler(func=lambda query: True)
def show_products(query):
    category_id = query.query
    bot.send_products(query, category_id)


# Checking if user clicked "Add to cart". Adding product to the cart.
@bot.callback_query_handler(func=lambda call: True if "product" in call.data else False)
def add_to_cart(call):
    product_id = call.data.split("_")[1]
    bot.add_to_cart(call, product_id)


# Checking if user clicked "Delete from cart". Removing item the cart.
@bot.callback_query_handler(func=lambda call: True if "delete" in call.data else False)
def remove_from_cart(call):
    item_id = call.data.split("_")[1]
    bot.remove_from_cart(call, item_id)


# When customer made an oder, send information to admin
@bot.callback_query_handler(func=lambda call: True if "order" in call.data else False)
def make_order(call):
    user = TelegramCustomer.objects.get(telegram_id=call.from_user.id)
    cart = TelegramCart.objects.get(user=user, ordered=False)
    if cart.items.exists():
        if user.phone_number:
            buttons = [types.InlineKeyboardButton(text="Yes", callback_data="yes"),
                    types.InlineKeyboardButton(text="No", callback_data="no"),
            ]
            kb = types.InlineKeyboardMarkup(row_width=2)
            kb.add(*buttons)
            bot.send_message(call.from_user.id, f"Is it your phone number {user.phone_number}?", reply_markup=kb)

        else:
            kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
            phone_button = types.KeyboardButton("Share phone number", request_contact=True)
            kb.add(phone_button)
            bot.send_message(call.from_user.id, "Please share your phone number so we could contact you.", reply_markup=kb)
    else:
        bot.send_message(call.message.chat.id, "Cart is empty!")


# Adding customer's phone number to the database
@bot.message_handler(content_types=['contact'])
def add_phone(message):
    phone = message.contact.phone_number
    user = TelegramCustomer.objects.get(telegram_id=message.from_user.id)
    user.phone_number = phone
    user.save()
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [types.KeyboardButton("Catalog"), types.KeyboardButton("Cart"),]
    kb.add(*buttons)
    bot.send_message(message.chat.id, "Thank you!", reply_markup=kb)
    bot.complete_order(user)


@bot.callback_query_handler(func=lambda call: True if call.data == "yes" else False)
def phone_confirmed(call):
    user = TelegramCustomer.objects.get(telegram_id=call.from_user.id)
    bot.complete_order(user)


@bot.callback_query_handler(func=lambda call: True if call.data == "no" else False)
def phone_not_confirmed(call):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    phone_button = types.KeyboardButton("Share phone number", request_contact=True)
    kb.add(phone_button)
    bot.send_message(call.from_user.id, "Please share your phone number so we could contact you.", reply_markup=kb)
