"# BONJI_store"
http://dberehovets.pythonanywhere.com/

Інтернет-магазин електроніки.
1. Магазин є динамічним з можливістю змінювати перелік категорій та товарів.
2. Можливість створювати акаунти після чого в клієнта з'являється кошик та
стає доступним замовлення товарів.
3. Автоматична зміна кількості товарів у базі даних при замовленнях. За нестачі
товару, клієнту показується повідомлення про неможливість додавання товару в
кошик.
4. Дані підписників заносяться в окрему таблицю.
5. Імплементовано пошук за назвою товару, а також за позначками, якщо товар
в розпродажі (sale), новий (new), гарячий (hot). Дані мітки для кожного товару
додаються вручну.

6. Окремим пунктом даного магазину є телеграм чатбот https://t.me/BONJI_store_bot, який дозволяє:
- переглядати товари за категоріями
- додавати товари в кошик
- робити замовленнях

Телеграм бот можна знайти клікнувши на відповідну іконку-посилання поруч з
посиланням на ЛінкедІн справа зверху, або справа внизу сторінки вебсайту.

На даний момент в розробці знаходиться REST API.
