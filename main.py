
# An open source project by Team Chocolate - feel free to copy. Please change the API key (line 5) to the one provided to you. 

import telebot
bot = telebot.TeleBot("2103747896:AAFNQ_ZlZt6ttAysAQFCWxXzPPGPJPvM-VA")


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, """Hi, Welcome to the McDonald's chatbot, created to fulfill any McDonalds related needs. How may i help today? 😊
  
If you are unsure, please click on /commands. Alternatively, if you need help, please click on /help 😁.

For dev team: /team

❗️Disclaimer: We use URL shortners for links❗️  """)

@bot.message_handler(commands=['commands'])
def send_command(message):
  bot.send_message(message.chat.id,"""
Commands: (Please select one) 

/Menus - Discover the McDonald's Menu, with every one of our meals, snacks, drinks, and more 🍔🍟🤤

/Locations - Locate a McDonalds Near you (Currently only serving Branches in the Midlands ) 🗽🌉📍 

/Deals - View the latest offers and promotions 💸

/Contact - Require help or wish to contact us? ☎️📞

/App - Download the McDonald's App to have all the offers in the palm of your hands! 📱📲

(/start - Welcome Message. Commands are case-sensitive❕) 
  """)

@bot.message_handler(commands=['team'])
def send_team(message):
  bot.send_message(message.chat.id, """
Team Chocolate:
Manvir, Hamza, Tariq, Ayuub

Our chat bot project for 4006CEM

/start
""" )

#START OF MAIN COMMANDS ----------------------------

@bot.message_handler(commands=['Menus'])
def send_menu(message):
  bot.send_message(message.chat.id, """
McDonald's Menu:

/Burgers 🍔
/McNuggets_Dippers 
/Wraps_and_Salads 🌯
/McCafe ☕️
/Breakfast 🥞
/Vegetarian 🥙
/Vegan 🥦
/Saver 💳
/Happy_Meal 😋
/Fries_and_Sides 🍟
/Desserts 🍰🍦
/Milkshakes_and_ColdDrinks 🥤🧃

/Meals_under_400kcal 🍔👇
/Meals_under_600kcal 🍔👇
/Breakfast_under_400kcal 🥞👇

(/commands - return to Command Menu) 👈
""" )

@bot.message_handler(commands=['Locations', 'Location'])
def send_locations(message):
  bot.send_message(message.chat.id, """
Locations : 🗽🌉 (Continously being updated)

/Birmingham 📌
/Coventry 📌
/Wolverhampton 📌
/Leicester 📌
/Stock_on_Trent 📌

Get Directions from your current location! 😳
More coming soon...

(/commands - return to Command Menu) 👈
  """)

@bot.message_handler(commands=['Deals'])
def send_deals(message):
  bot.send_message(message.chat.id, """
Deals:
https://bit.ly/3mwpN4h

(/commands - return to Command Menu) 👈
  """)

@bot.message_handler(commands=['Contact'])
def send_contact(message):
  bot.send_message(message.chat.id, """
Contact:
https://bit.ly/3EzuQai

(/commands - return to Command Menu) 👈
  """)

@bot.message_handler(commands=['App'])
def send_apps(message):
  bot.send_message(message.chat.id, """
Apps:
IOS: https://apple.co/3jRsRGu 🍎
Android: https://bit.ly/2ZG7QYg 🤖

(/commands - return to Command Menu) 👈
  """) 

#END OF MAIN COMMANDS -------------------------------
 
#Start of Menu Items --------------------------------
@bot.message_handler(commands=['Burgers'])
def send_menuBurgers(message):
  bot.send_message(message.chat.id, """
Burgers🍔:
https://bit.ly/31ddv8N

(/Menus - return to the Food Menu) 👈
  """)

@bot.message_handler(commands=['McNuggets_Dippers'])
def send_menuMcNugs(message):
  bot.send_message(message.chat.id, """
McNuggets and Dippers:
https://bit.ly/3pUAKPw

(/Menus - return to the Food Menu) 👈
  """)

@bot.message_handler(commands=['Wraps_and_Salads'])
def send_menuWraps(message):
  bot.send_message(message.chat.id, """
Wraps and Salads 🌯:
https://bit.ly/3CwV2lt

(/Menus - return to the Food Menu) 👈
  """)

@bot.message_handler(commands=['McCafe'])
def send_menuMcCafe(message):
  bot.send_message(message.chat.id, """
McCafe ☕️:
https://bit.ly/3mvmavy

(/Menus - return to the Food Menu) 👈
  """)

@bot.message_handler(commands=['Breakfast'])
def send_menuBreakfast(message):
  bot.send_message(message.chat.id, """
Breakfast 🥞:
https://bit.ly/3CySy6a

(/Menus - return to the Food Menu) 👈
  """)

@bot.message_handler(commands=['Vegetarian'])
def send_menuVegetarian(message):
  bot.send_message(message.chat.id, """
Vegetarian 🥙:
https://bit.ly/3jSoriP

(/Menus - return to the Food Menu) 👈
  """)

@bot.message_handler(commands=['Vegan'])
def send_menuVegan(message):
  bot.send_message(message.chat.id, """
Vegan 🥦:
https://bit.ly/2ZJoW7T

(/Menus - return to the Food Menu) 👈
  """)

@bot.message_handler(commands=['Saver'])
def send_menuSaver(message):
  bot.send_message(message.chat.id, """
Saver 💳:
https://bit.ly/3mwoy5m

(/Menus - return to the Food Menu) 👈
  """)

@bot.message_handler(commands=['Happy_Meal'])
def send_menuHappy(message):
  bot.send_message(message.chat.id, """
Happy Meal 😋:
https://bit.ly/3bqnrOj

(/Menus - return to the Food Menu) 👈
  """)

@bot.message_handler(commands=['Fries_and_Sides'])
def send_menuFries(message):
  bot.send_message(message.chat.id, """
Fries and Sides 🍟:
https://bit.ly/3w3SoBh

(/Menus - return to the Food Menu) 👈
  """)

@bot.message_handler(commands=['Desserts'])
def send_menuDesserts(message):
  bot.send_message(message.chat.id, """
Desserts 🍰🍦:
https://bit.ly/3btGl6I

(/Menus - return to the Food Menu) 👈
  """)

@bot.message_handler(commands=['Milkshakes_and_ColdDrinks'])
def send_menuMilk(message):
  bot.send_message(message.chat.id, """
Milkshakes and ColdDrinks 🥤🧃:
https://bit.ly/3pTJjKn

(/Menus - return to the Food Menu) 👈
  """)

@bot.message_handler(commands=['Meals_under_400kcal'])
def send_menu400(message):
  bot.send_message(message.chat.id, """
Meals under 400kcal 🍔👇:
https://bit.ly/3CEucYQ

(/Menus - return to the Food Menu) 👈
  """)

@bot.message_handler(commands=['Meals_under_600kcal'])
def send_menu600(message):
  bot.send_message(message.chat.id, """
Meals under 600kcal 🍔👇:
https://bit.ly/3CyTFCS

(/Menus - return to the Food Menu) 👈
  """)

@bot.message_handler(commands=['Breakfast_under_400kcal'])
def send_menub400(message):
  bot.send_message(message.chat.id, """
Breakfast under 400kcal 🥞👇:
https://bit.ly/3mvLLod

(/Menus - return to the Food Menu) 👈
  """)
#End of Menu Items --------------------------------

#Start of Location Items --------------------------------
@bot.message_handler(commands=['Birmingham'])
def send_birminghamLocations(message):
  bot.send_message(message.chat.id, """
Birmingham 📌:

Temple Row: https://bit.ly/3BrnUdD
Stephenson Place: https://bit.ly/31959Pu
Dale End: https://bit.ly/2ZGzRip
Bristol Rd: https://bit.ly/3EwPQ1t
Small Heath: https://bit.ly/3vZUNwE
Fort Shopping Park: https://bit.ly/3CtbSBE
West Bromwich: https://bit.ly/3vZUVfC
Oldbury: https://bit.ly/3GEfZ0g
Northfield: https://bit.ly/2ZPaWtb
New Oscott: https://bit.ly/3GDsAkj
Star City: https://bit.ly/3BAE0S2
Cape Hill: https://bit.ly/2ZGrCTd

The list is being continually updated... 😃

(/Locations - return to the Locations Menu) 👈
  """)

@bot.message_handler(commands=['Coventry'])
def send_coventryLocations(message):
  bot.send_message(message.chat.id, """
Coventry 📌:

Alvis Retail Park: https://bit.ly/3pUDtZg
Canley: https://bit.ly/3ENtDfZ
Binley: https://bit.ly/3w0smia
West Orchards: https://bit.ly/31kgY5F
Gallagher Retail Park: https://bit.ly/3bsBEdr
Cross Cheaping: https://bit.ly/3BDp4CY

The list is being continually updated... 😃

(/Locations - return to the Locations Menu) 👈
  """)

@bot.message_handler(commands=['Wolverhampton'])
def send_wolverhamptonLocations(message):
  bot.send_message(message.chat.id, """
Wolverhampton 📌:

Stafford Rd: https://bit.ly/3EAUtaH
Dudley Street: https://bit.ly/3brDE5w
Penn Road: https://bit.ly/3nMy2J6
Wednesfield: https://bit.ly/3bqGA2z
Wolves Fallings park: https://bit.ly/31iRYf3

The list is being continually updated... 😃

(/Locations - return to the Locations Menu) 👈
  """)

@bot.message_handler(commands=['Leicester'])
def send_LeicesterLocations(message):
  bot.send_message(message.chat.id, """
Leicester 📌:

Market Street: https://bit.ly/3EyFqi4
Fosse Park: https://bit.ly/3jVmkL8
Abbey Lane: https://bit.ly/31kzhHR
Netherhall Rd: https://bit.ly/2ZEoibW
Beaumont Leys Shopping Centre: https://bit.ly/3nJHpsP
Meridian Way: https://bit.ly/2Y61b9k
Thurmaston Shopping Centre: https://bit.ly/3msnAXI

The list is being continually updated... 😃

(/Locations - return to the Locations Menu) 👈
  """)

@bot.message_handler(commands=['Stock_on_Trent'])
def send_StockLocations(message):
  bot.send_message(message.chat.id, """
Stock on Trent 📌:

Fenton: https://bit.ly/3pUjc5V
Festival Heights Retail Park: https://bit.ly/3mul3w4
Hanley: https://bit.ly/3CwX30N
Phoenix Retail Park: https://bit.ly/3EAVkbp
Springfield Retail Park: https://bit.ly/3EoRlii
Norton Park: https://bit.ly/3w16mnr
Meir Park: https://bit.ly/3BzsGpn
Tunstall: https://bit.ly/3my5kfm

The list is being continually updated... 😃

(/Locations - return to the Locations Menu) 👈
  """)

bot.infinity_polling()