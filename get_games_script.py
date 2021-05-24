import os

from epic_games_bot import EpicGamesBot
from playwright.sync_api import sync_playwright

def Run(Playwright, username, password):
    browser = None
    print("初始化完成")
    try:
        browser = Playwright.firefox.launch()
        page = browser.new_page()
        bot = EpicGamesBot(page)
        print("正在登录。。。")
        bot.log_in(None, username, password)
        print("登录成功！")
        purchased_offer_urls = bot.purchase_free_promotional_offers()
        [print(url) for url in purchased_offer_urls]
        print("{name} 领取完成".format(name=username))
        browser.close()
    except Exception:
        if browser:
            browser.close()
            print("发生错误,领取失败")
        raise

if __name__ == '__main__':
    Email = os.environ["EPIC_EMAIL"]
    Password = os.environ["EPIC_PASSWORD"]
    QmsgToken = os.environ["QMSG_TOKEN"]
    
    CA = EpicGamesBot.list_free_promotional_offers()  # 免费游戏列表
    print(CA)
    with sync_playwright() as playwright:
        Run(playwright, Email, Password)
