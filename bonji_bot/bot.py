from telebot import TeleBot, types
from django.shortcuts import get_object_or_404

from categories.models import Category
from products.models import Product
from bonji_bot.models import TelegramCart, TelegramCartItem, TelegramCustomer
from django.conf import settings

class TGBot(TeleBot):

    def send_categories(self, message):

        """Sends categoriy list to the user"""

        kb = types.InlineKeyboardMarkup(row_width=2)
        categories = Category.objects.all()

        buttons = [types.InlineKeyboardButton(switch_inline_query_current_chat=cat.id,
                                        text=cat.title) for cat in categories]
        kb.add(*buttons)

        self.send_message(message.chat.id, "Choose category", reply_markup=kb)


    def send_products(self, query, category_id):
        """Sends product of a particular category to the chat that was requested"""

        results = []
        category = Category.objects.get(id=category_id)
        products = Product.objects.filter(category=category)
        for product in products:
            kb = types.InlineKeyboardMarkup()
            button = types.InlineKeyboardButton(text="Add to Cart", callback_data="product_" + str(product.id))
            kb.add(button)
            result = types.InlineQueryResultArticle(
                id=product.id,
                title=product.name,
                description=f"${product.new_price}",
                input_message_content=types.InputTextMessageContent(parse_mode="HTML",
                                                                    disable_web_page_preview=False,
                                                                    message_text=f"{product.name} - ${product.new_price}\n\n{product.characteristics} "
                                                                                 f"<a href='{settings.BASE_URL}{product.main_image.url}'>&#8204</a>"
                                                                    ),
                thumb_url=settings.BASE_URL + product.main_image.url,
                reply_markup=kb
            )
            results.append(result)
        self.answer_inline_query(query.id, results, cache_time=0)


    def add_to_cart(self, call, product_id):
        """ Using call find user in the database. Get or create it's cart.
        if product is already in the cart, add 1 to it's quantity. Else create
        cartItem and add it to the cart """

        product = Product.objects.get(pk=product_id)
        if product.quantity >= 1:
            user = TelegramCustomer.objects.get(telegram_id=call.from_user.id)
            cart, cr = TelegramCart.objects.get_or_create(user=user, ordered=False)
            cart_item, created = TelegramCartItem.objects.get_or_create(product=product, cart=cart)
            if not created:
                cart_item.quantity += 1
                cart_item.save()
            cart_item.product.quantity -= 1
            cart_item.product.save()

            cart.clean()
            self.send_message(call.from_user.id, "Product has been added to cart!")
        else:
            self.send_message(call.from_user.id, "Shortage of products in stock. Cannot add product to cart(")


    def remove_from_cart(self, call, item_id):
        """ When have callback and item id remove the item from the cart of
            particular user"""

        user = get_object_or_404(TelegramCustomer, telegram_id=call.from_user.id)
        cart_item = TelegramCartItem.objects.get(pk=item_id)
        cart_item.product.quantity += cart_item.quantity
        cart_item.product.save()
        cart_item.delete()
        self.edit_message_caption(caption="Product deleted!",  chat_id=call.message.chat.id, message_id=call.message.message_id)


    def send_cart(self, user_id):
        """Having user_id send cart of the user"""

        user = get_object_or_404(TelegramCustomer, telegram_id=user_id)
        cart, created = TelegramCart.objects.get_or_create(user=user, ordered=False)
        cart_items = cart.items.all()

        if cart_items:
            for item in cart_items:
                kb = types.InlineKeyboardMarkup()
                button = types.InlineKeyboardButton(text=f"Delete {item.product.name} from cart", callback_data="delete_" + str(item.id))
                kb.add(button)
                self.send_photo(user_id, photo=f"{settings.BASE_URL}{item.product.main_image.url}",
                caption=f"{item.product.name} - ${item.product.new_price}\nAmount in cart: {item.quantity}\n\n{item.product.characteristics[:700]}", reply_markup=kb)

            kb = types.InlineKeyboardMarkup()
            button = types.InlineKeyboardButton(text="Order!", callback_data="order_" + str(user_id))
            kb.add(button)
            one_or_many = "product" if cart.product_quantity == 1 else "products"
            self.send_message(user_id, f"{cart.product_quantity} {one_or_many} for ${cart.total_price}", reply_markup=kb)
        else:
            self.send_message(user_id, "Cart is empty!")


    def complete_order(self, user):
        cart = TelegramCart.objects.get(user=user, ordered=False)
        self.send_message(user.telegram_id,
                            f"Thank you, {user.first_name}! Our manager will contact you for order confirmation.")
        self.send_message(chat_id=438422378, text=f"{user.first_name} {user.last_name} phone number {user.phone_number} made order:")
        for item in cart.items.all():
            self.send_message(chat_id=438422378, text=item.product.name)
        cart.ordered = True
        cart.save()
