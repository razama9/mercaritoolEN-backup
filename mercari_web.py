# %%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import chromedriver_autoinstaller
from time import sleep
import os
from random import randint, choice

# %%
# Start choromedriver
def open_chromedriver(webdriver, application_path=None, w=1600, h=1200):
    chromedriver_autoinstaller.install()
    if application_path:
        chrome_data_dir = os.path.join(application_path, 'chrome_data')
    else:
        chrome_data_dir = os.path.join(os.getcwd(), 'chrome_data')
    if not os.path.exists(chrome_data_dir):
        os.mkdir(chrome_data_dir)
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument(f"--user-data-dir={chrome_data_dir}")
    driver = webdriver.Chrome(options=options)
    sleep(1)
    driver.set_window_size(w, h)
    return driver


# Wait for any element to get loaded
# BY TAG
def wfe_by_tag(driver, el_tag):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, el_tag))
        )
        return element
    except Exception as e:
        return "element not found"


# BY NAME
def wfe_by_name(driver, el_name):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, el_name))
        )
        return element
    except Exception as e:
        return "element not found"


# BY ID
def wfe_by_id(driver, el_id):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, el_id))
        )
        return element
    except Exception as e:
        return "element not found"


# BY XPATH
def wfe_by_xpath(driver, el_xpath):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, el_xpath))
        )
        return element
    except Exception as e:
        return "element not found"


# BY CLASS
def wfe_by_class(driver, el_class):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, el_class))
        )
        return element
    except Exception as e:
        return "element not found"


# BY CSS
def wfe_by_css(driver, el_css):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, el_css))
        )
        return element
    except Exception as e:
        return "element not found"


# Bring element into view
def bring_to_view(driver, element):
    driver.execute_script("arguments[0].scrollIntoView();", element)


def get_all_listings(driver):
    go_next = False
    is_done = False
    all_items = []
    try:
        driver.get('https://jp.mercari.com/mypage/listings')
        current_listing = wfe_by_id(driver, 'currentListing')
        wfe_by_tag(current_listing, 'mer-list-item')
        # sleep(4)
        if driver.current_url.split('/')[-1] == 'listings':
            go_next = True
        if go_next:
            current_listing = wfe_by_id(driver, 'currentListing')
            wfe_by_tag(current_listing, 'mer-list-item')
            # See more
            while True:
                current_listing = wfe_by_id(driver, 'currentListing')
                wfe_by_tag(current_listing, 'button')
                see_more_btn = current_listing.find_elements(By.TAG_NAME, 'button')
                if len(see_more_btn) == 1:
                    bring_to_view(driver, see_more_btn[0])
                    sleep(1)
                    see_more_btn[0].click()
                    sleep(3)
                else:
                    break
            x = current_listing.find_elements(By.TAG_NAME, 'mer-list-item')
            for index, el in enumerate(x):
                list_item = {
                    'url': '-',
                    'img': '-',
                    'title': '-',
                    'price': '-',
                    'marked': False,
                    'status': None,
                    'action': 0,
                    'source': 'listings'
                }
                list_item['url'] = el.find_element(By.TAG_NAME, 'a').get_attribute('href')
                list_item['img'] = driver.execute_script(f"return document.querySelectorAll('mer-item-object')[{index}].shadowRoot.querySelector('mer-item-thumbnail').shadowRoot.querySelector('img').getAttribute('src')")
                li_content = driver.execute_script(f"return document.querySelectorAll('mer-item-object')[{index}].shadowRoot.querySelector('.content')")
                list_item['title'] = li_content.find_element(By.CLASS_NAME, 'item-label').text
                list_item['price'] = li_content.find_element(By.CLASS_NAME, 'item-price').text
                if len(li_content.find_elements(By.CLASS_NAME, 'information-label')) > 0:
                    list_item['source'] = 'unpublished'
                all_items.append(list_item)
            is_done = True
        else:
            is_done = False
    except Exception as e:
        print(e)
    return all_items, is_done


def get_all_drafts(driver):
    go_next = False
    is_done = False
    all_items = []
    try:
        driver.get('https://jp.mercari.com/mypage/drafts')
        draft_list = wfe_by_xpath(driver, '//mer-list[@data-testid="draft-list"]')
        # current_listing = wfe_by_id(driver, 'currentListing')
        if driver.current_url.split('/')[-1] == 'drafts':
            go_next = True
        if go_next:
            draft_list = wfe_by_xpath(driver, '//mer-list[@data-testid="draft-list"]')
            if type(draft_list) != str:
                wfe_by_tag(draft_list, 'mer-list-item')
                draft_list_items = draft_list.find_elements(By.TAG_NAME, 'mer-list-item')
                for index, el in enumerate(draft_list_items):
                    list_item = {
                        'url': '-',
                        'img': '-',
                        'title': '-',
                        'price': '-',
                        'marked': False,
                        'status': None,
                        'action': 0,
                        'source': 'drafts'
                    }
                    list_item['url'] = el.find_element(By.TAG_NAME, 'a').get_attribute('href')
                    list_item['img'] = driver.execute_script(f"return document.querySelectorAll('mer-item-object')[{index}].shadowRoot.querySelector('mer-item-thumbnail').shadowRoot.querySelector('img').getAttribute('src')")
                    li_content = driver.execute_script(f"return document.querySelectorAll('mer-item-object')[{index}].shadowRoot.querySelector('.content')")
                    list_item['title'] = li_content.find_element(By.CLASS_NAME, 'item-label').text
                    list_item['price'] = li_content.find_element(By.CLASS_NAME, 'item-price').text
                    all_items.append(list_item)
            else:
                print("draft list not found")
            is_done = True
        else:
            is_done = False
    except Exception as e:
        print(e)
    return all_items, is_done


def get_changed_price(old_price, by_percent, unit_amount=100, percent_amount=10, decrease=True):
    if not decrease:
        unit_amount = unit_amount * (-1)
        percent_amount = percent_amount * (-1)
    old_price1 = float(old_price)
    if by_percent:
        new_price = old_price1 * (1.0 - float(percent_amount)/100.0)
    else:
        new_price = old_price1 - unit_amount
    float_parts = str(new_price).split('.')
    if float_parts[-1] == '0':
        new_price = float_parts[0]
    else:
        if len(float_parts[1]) > 2:
            new_price = float_parts[0] + '.' + float_parts[1][:2]
        else:
            new_price = '.'.join(float_parts)
    return new_price


def change_price(driver, price):
    wfe_by_xpath(driver, '//mer-button[@data-testid="checkout-button"]').click()
    price_el = wfe_by_name(driver, 'price')
    bring_to_view(driver, price_el)
    sleep(randint(3,4))
    price_el.send_keys(Keys.CONTROL, 'A', Keys.BACKSPACE)
    price_el.send_keys(price)
    # submit changes
    wfe_by_xpath(driver, '//button[@data-testid="edit-button"]').click()


def publish_the_draft(driver, product_link):
    driver.get(product_link)
    activate_link = wfe_by_css(driver, 'mer-button[data-testid="list-draft-button"] button[type="submit"]')
    bring_to_view(driver, activate_link)
    sleep(randint(2,4))
    activate_link.click()
    listing_url = wfe_by_xpath(driver, '//a[@data-location="mypage_drafts:draft_list:link:go_item"]')
    sleep(1)
    if type(listing_url) == str:
        return None
    else:
        return listing_url.get_attribute('href')


def publish_the_unpublished(driver, product_link):
    driver.get(product_link)
    product_editing = wfe_by_xpath(driver, '//div[@data-testid="checkout-button-container"]')
    # sleep(randint(2,4))
    product_editing.click()
    sleep(randint(2,4))
    activate_link = wfe_by_css(driver, 'button[data-testid="activate-button"]')
    bring_to_view(driver, activate_link)
    sleep(randint(2,4))
    activate_link.click()
    sleep(2)


def unpublish_the_published(driver, product_link):
    driver.get(product_link)
    edit_btn = wfe_by_xpath(driver, '//mer-button[@data-testid="checkout-button"]')
    sleep(randint(2,4))
    edit_btn.click()
    deactive_link = wfe_by_css(driver, 'button[data-testid="suspend-button"]')
    bring_to_view(driver, deactive_link)
    sleep(randint(2,3))
    deactive_link.click()
    sleep(2)


def get_randomized_positions(n):
    ordered_positions = [i for i in range(n)]
    randomized_positions = []
    while len(ordered_positions) > 0:
        c_pick = choice(ordered_positions)
        randomized_positions.append(c_pick)
        ordered_positions.remove(c_pick)
    return randomized_positions


def is_logged_in(driver):
    driver.get('https://jp.mercari.com/mypage/listings')
    wfe_by_tag(driver, 'mer-navigation-top-menu-item')
    sleep(3)
    if driver.current_url.split('/')[-1] != 'listings':
        return False
    return True


if __name__ == '__main__':
    # %%
    base_url = 'https://jp.mercari.com'
    listing_url = 'https://jp.mercari.com/mypage/listings'
    mercari_username = 'ipadwatashino@gmail.com'
    mercari_password = 'GOMIBAKO24'
    wait_time_1 = 20
    wait_time_2 = 7

    # %%
    driver = open_chromedriver(webdriver)

    # %%
    input("Have you started the VPN extension?")

    # %%
    driver.get('https://jp.mercari.com')
    sleep(3)

    # %%
    # go_to_listings(driver, mercari_username, mercari_password)
    driver.get(listing_url)
    sleep(randint(3,5))
    # TODO:
    listing_links = get_all_listings(driver, mercari_username, mercari_password)

    # %%
    listing_links[3]['marked'] = True
    listing_links[5]['marked'] = True
    listing_links[6]['marked'] = True

    # %%
    def start_changing_prices(driver, listings, wait_time_1, wait_time_2):
        updated_listings = []
        for listing in listings:
            if listing['marked']:
                try:
                    driver.get(listing['url'])
                    sleep(wait_time_1 / 3 - 3)
                    price = wfe_by_xpath(driver, '//mer-price[@data-testid="price"]').get_attribute('value')
                    new_price = get_changed_price(price, False)
                    change_price(driver, new_price)
                    sleep(wait_time_1 / 3 + 3)
                    change_price(driver, price)
                    sleep(wait_time_1 / 3 - 3)
                    listing['status'] = True
                except Exception as e:
                    print(e)
                    listing['status'] = False
            updated_listings.append(listing)
        return updated_listings

    # %%
    start_changing_prices(driver, listing_links, wait_time_1, wait_time_2)

    # %%
    driver.quit()

    # %%


# %%



