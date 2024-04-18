from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options


def initialize_driver(headless: bool = True) -> webdriver.Chrome:
    """
    WebDriverを初期化する関数
    """
    try:
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
        # ログの出力レベルを設定
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        # メモリの使用量を抑えるために必要なオプション
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-software-rasterizer")
        # ユーザーエージェントを指定
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36")
        # ドライバーの初期化
        driver = webdriver.Chrome(options=chrome_options)

        print('initialize driver success')
        return driver

    except WebDriverException as e:
        print(f"An error occurred while initializing the WebDriver or opening the URL: {e}")
        raise
