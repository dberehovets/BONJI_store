"# BONJI_store"
http://dberehovets.pythonanywhere.com/

Online electronics store.
1. The store is dynamic that allows to add and change new categories and products.
2. Possibility to create accounts, login, logout that allows user to add products to the cart
and make orders.
3. The quantity of products in the database changes automatically. If quantity = 0, the user
receives the message about a shortage of goods in stock.
4. Information about the subscribers gets into a different table.
5. Search is implemented by name, and by the product extra such as "sale", "hot", and "new". 
The extra labels are set by the admin for each product if needed.

6. The store has its own telegram bot https://t.me/BONJI_store_bot, that allows:
- view goods by categories
- add products in the cart
- make orders

You can find and check the telegram bot in the link above or clicking the telegram symbol 
in the website http://dberehovets.pythonanywhere.com/ that is located in the top rigt and bottom
right corner of the webpage.

7. REST API is made for categories and products.
