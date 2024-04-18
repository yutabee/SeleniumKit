from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


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


def find_element(driver, by, value, timeout=10):
    """
    指定された条件で要素を検索し、指定された時間内に要素が見つかるのを待ちます。

    Args:
        driver (webdriver.Chrome): WebDriverのインスタンス。
        by (By): 検索条件のタイプ（By.ID, By.XPATHなど）。
        value (str): 検索する要素の識別子。
        timeout (int): 最大待機時間（デフォルトは10秒）。

    Returns:
        WebElement: 検索された要素。

    Raises:
        NoSuchElementException: 指定されたセレクタで要素が見つからない場合。
        TimeoutException: 指定された時間内に要素が見つからない場合。
        
    使用例:
        >>> driver = initialize_driver()
        >>> element = find_element(driver, By.ID, 'element_id')
    """
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((by, value))
        )
        return element
    except TimeoutException as e:
        error_msg = f"Timeout: Element not visible after {timeout} seconds for selector ({by}, {value})"
        print(error_msg)
        raise TimeoutException(error_msg) from e
    except NoSuchElementException as e:
        error_msg = f"Element not found for selector ({by}, {value})"
        print(error_msg)
        raise NoSuchElementException(error_msg) from e
