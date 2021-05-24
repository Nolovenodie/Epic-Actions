import os

from epic_games_bot import EpicGamesBot
from playwright.sync_api import sync_playwright

def Run(Playwright, username, password):
    browser = None
    print(username+" 开始领取") 
    
    try:
        browser = playwright.firefox.launch()
        page = browser.new_page()
        
        bot = EpicGamesBot(page)
        print("开始登录")
            
        bot.log_in(None, username, password)
        print("登录成功")

        purchased_offer_urls = bot.purchase_free_promotional_offers()
        print("领取完毕")
        
        [print(url) for url in purchased_offer_urls]

        browser.close()
    except Exception:
        if browser:
            browser.close()

        raise

if __name__ == '__main__':
    Email = os.environ["EPIC_EMAIL"]
    Password = os.environ["EPIC_PASSWORD"]
    QmsgToken = os.environ["QMSG_TOKEN"]
    
    Games = EpicGamesBot.list_free_promotional_offers()  # 游戏列表
    print(Games)
    
    with sync_playwright() as playwright:
        Run(playwright, Email, Password)
