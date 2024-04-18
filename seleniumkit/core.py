from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import Select


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


def input_text(driver, by, value, text):
    """
    指定された条件の要素にテキストを入力します。

    Args:
        driver (webdriver.Chrome): WebDriverのインスタンス。
        by (By): 検索条件のタイプ。
        value (str): 検索する要素の識別子。
        text (str): 入力するテキスト。

    Raises:
        NoSuchElementException: 要素が見つからない場合。
        WebDriverException: 要素へのテキスト入力中にエラーが発生した場合。
        
    使用例:
        >>> driver = initialize_driver()
        >>> input_text(driver, By.ID, 'element_id', 'input text')
    """
    try:
        element = find_element(driver, by, value)
        element.clear()
        element.send_keys(text)
    except WebDriverException as e:
        print(
            f"An error occurred while inputting text into the element with selector ({by}, {value}): {e}"
        )
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise


def scroll_to_bottom(driver):
    """
    ブラウザでページの最下部までスクロールします。

    Args:
        driver (webdriver.Chrome): WebDriverのインスタンス。

    Returns:
        None
    """
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


def get_current_url(driver):
    """
    現在のブラウザのURLを取得します。

    Args:
        driver (webdriver.Chrome): WebDriverのインスタンス。

    Returns:
        str: 現在のURL。
    """
    return driver.current_url


def select_from_dropdown(driver, by, value, option_text):
    """
    ドロップダウンメニューから指定されたテキストを持つオプションを選択します。

    Args:
        driver (webdriver.Chrome): WebDriverのインスタンス。
        by (By): 検索条件のタイプ。
        value (str): 検索する要素の識別子。
        option_text (str): 選択するオプションのテキスト。

    Raises:
        NoSuchElementException: ドロップダウン要素またはオプションが見つからない場合。
        WebDriverException: オプションの選択中にエラーが発生した場合。
    """
    try:
        element = find_element(driver, by, value)
        select = Select(element)
        select.select_by_visible_text(option_text)
    except WebDriverException as e:
        print(
            f"An error occurred while selecting '{option_text}' from dropdown with selector ({by}, {value}): {e}"
        )
        raise
