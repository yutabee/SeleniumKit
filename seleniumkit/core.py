from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options


def initialize_driver(headless: bool = True) -> webdriver.Chrome:
    """
    Selenium WebDriverを初期化する関数

    Args:
        headless (bool): ブラウザをヘッドレスモードで起動するかどうか。
    
    Returns:
        webdriver.Chrome: 初期化されたWebDriverインスタンス
        
    Raises:
        WebDriverException: WebDriverの初期化またはURLのオープン中にエラーが発生した場合
        
    使用例:
        >>> driver = initialize_driver(headless=True)
        >>> driver.get('https://www.google.com')
        >>> driver.quit()
    """
    try:
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-software-rasterizer")
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36")

        driver = webdriver.Chrome(options=chrome_options)

        print('initialize driver success')
        return driver

    except WebDriverException as e:
        print(f"An error occurred while initializing the WebDriver or opening the URL: {e}")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise

  
