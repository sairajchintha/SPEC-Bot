from flask import Flask, request, jsonify
from telegram_bot import TelegramBot
from config import TELEGRAM_INIT_WEBHOOK_URL
import requests,json,urllib.parse
import selenium.webdriver as webdriver
from bs4 import BeautifulSoup as bs


app = Flask(__name__)
TelegramBot.init_webhook(TELEGRAM_INIT_WEBHOOK_URL)


@app.route('/')
def home():
    return "<h1>Hello SPEC Toxic World</h1>"


@app.route('/webhook', methods=['POST'])
def index():
    req = request.get_json() 
    bot = TelegramBot()
    bot.parse_webhook_data(req)

    if bot.incoming_message_text == '/start':
            message = '🤙Enter Your Roll No /search "roll_no"🤙'
            success=bot.send_msg(bot.chat_id,message)
            return jsonify(success=success)

    elif bot.incoming_message_text[0:7]=="/search":
            if bot.incoming_message_text[8:].strip(" ")==False:
                success=bot.send_msg(bot.chat_id,"please enter valid roll no")
                return jsonify(success=success)
            searching_text=bot.incoming_message_text[8:]
            print(searching_text)
            message=""
            url='https://specexams.com/BeesErp/Login.aspx'
            driver = webdriver.Chrome()
            driver.get(url)
            username=bot.incoming_message_text[8:].upper()
            password=bot.incoming_message_text[8:].upper()
            email_element = driver.find_element_by_id('txtUserName')
            email_element.send_keys(username) 

            login_button = driver.find_element_by_id('btnNext')
            login_button.click()

            password_element = driver.find_element_by_id('txtPassword')
            password_element.send_keys(password) 

            login_button = driver.find_element_by_id('btnSubmit')
            login_button.click()

            urls=requests.get(url)
            soup=bs(driver.page_source,"html.parser")

            name=soup.find(id="ctl00_cpHeader_ucStud_lblStudentName")
            attendance=soup.find(id="ctl00_cpStud_lblTotalPercentage")
            warning_msg=soup.find(id="ctl00_cpStud_lblAttComment")

            message="Hello"+name.text[11:]+"\n Your attendance is "+attendance.text+" "+warning_msg.text[:-1]

            #print(attendance.text)
            #print(warning_msg.text)
            print(str(message))
            success=bot.send_msg(bot.chat_id,urllib.parse.quote(message))
            driver.quit()
            return jsonify(success=success)
    else:
            message = "invalid command or you changed password given by college"
            success=bot.send_msg(bot.chat_id,"Invalid Command")
            driver.quit()
            return jsonify(success=success)


if __name__ == '__main__':
    app.run(host ='0.0.0.0',port=80)


# https://telegram.me

# check bot initialization: https://api.telegram.org/bot<secret key>/getme
# check webhook url: https://api.telegram.org/secret key/getWebhookInfo
