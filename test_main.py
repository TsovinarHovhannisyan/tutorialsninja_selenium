import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('Menu Navigation')
@allure.suite('UI Tests')
@allure.title('Test Menu Item Navigation')
@allure.description('Verifies that each menu item on the homepage navigates to the correct page and displays the correct heading.')
@allure.severity(allure.severity_level.CRITICAL)
def test_menu_item(driver):

    with allure.step("Opening the homepage"):
        driver.get("https://tutorialsninja.com/demo/")


    expected_menu_items = ["Desktops", "Laptops & Notebooks", "Components", "Tablets", "Software", "Phones & PDAs",  "Cameras", "MP3 Players"]

    with allure.step(f"Clicking on menu item: {expected_menu_items[0]}"):
        menu_item1 = driver.find_element(By.LINK_TEXT, expected_menu_items[0])
        menu_item1.click()

    with allure.step(f"Clicking on menu item: {expected_menu_items[1]}"):
        menu_item2 = driver.find_element(By.LINK_TEXT, expected_menu_items[1])
        menu_item2.click()

    with allure.step(f"Clicking on menu item: {expected_menu_items[2]}"):
        menu_item3 = driver.find_element(By.LINK_TEXT, expected_menu_items[2])
        menu_item3.click()

    with allure.step(f"Clicking on menu item: {expected_menu_items[3]}"):
        menu_item4 = driver.find_element(By.LINK_TEXT, expected_menu_items[3])
        menu_item4.click()

    with allure.step(f"Verifying the page heading for {expected_menu_items[3]}"):
        assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[3]

    with allure.step(f"Clicking on menu item: {expected_menu_items[4]}"):
       menu_item5 = driver.find_element(By.LINK_TEXT, expected_menu_items[4])
       menu_item5.click()
    with allure.step(f"Verifying the page heading for {expected_menu_items[4]}"):
       assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[4]


    with allure.step(f"Clicking on menu item: {expected_menu_items[5]}"):
       menu_item6 = driver.find_element(By.LINK_TEXT, expected_menu_items[5])
    menu_item6.click()
    with allure.step(f"Verifying the page heading for {expected_menu_items[5]}"):
       assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[5]

    with allure.step(f"Clicking on menu item: {expected_menu_items[6]}"):
        menu_item7 = driver.find_element(By.LINK_TEXT, expected_menu_items[6])
        menu_item7.click()

    with allure.step(f"Verifying the page heading for {expected_menu_items[6]}"):
        assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[6]
    with allure.step(f"Clicking on menu item: {expected_menu_items[7]}"):
        menu_item8 = driver.find_element(By.LINK_TEXT, expected_menu_items[7])
    menu_item8.click()


@pytest.mark.parametrize("menu_locator, submenu_locator, result_text", [
    (
            (By.PARTIAL_LINK_TEXT, 'Desktops'),
            (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[1]/div/div/ul/li[1]/a'),
            'PC'
    ),
    (
            (By.PARTIAL_LINK_TEXT, 'Desktops'),
            (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[1]/div/div/ul/li[2]/a'),
            'Mac'
    ),
    (
            (By.PARTIAL_LINK_TEXT, 'Laptops & Notebooks'),
            (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[2]/div/div/ul/li[1]/a'),
            'Macs'
    ),
    (
            (By.PARTIAL_LINK_TEXT, 'Laptops & Notebooks'),
            (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[2]/div/div/ul/li[2]/a'),
            'Windows'
    )
])


@allure.feature('Nested Menu Navigation')
@allure.suite('UI Tests')
@allure.title('Test Nested Menu Functionality')
@allure.description('Verifies that each nested menu item navigates to the correct page.')
def test_nested_menu(driver, menu_locator, submenu_locator, result_text):
  with allure.step("Opening the homepage"):
    driver.get("https://tutorialsninja.com/demo/")

  with allure.step("Hovering over the menu and clicking submenu"):
    menu = driver.find_element(*menu_locator)
    submenu = driver.find_element(*submenu_locator)
    ActionChains(driver).move_to_element(menu).click(submenu).perform()

  with allure.step(f"Verifying the page heading is {result_text}"):
    assert driver.find_element(By.TAG_NAME, 'h2').text == result_text

@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('Search Functionality')
@allure.title('Test Search for a Product')
@allure.description('Verifies that searching for a product returns relevant results.')
def test_search_product(driver):
  with allure.step("Opening the homepage"):
    driver.get("https://tutorialsninja.com/demo/")

  with allure.step("Searching for 'MacBook'"):
    search = driver.find_element(By.NAME, 'search')
    search.send_keys('MacBook')
    button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-default.btn-lg')
    button.click()

  with allure.step("Verifying search results contain 'MacBook'"):
    products = driver.find_elements(By.TAG_NAME, 'h4')
    new_list = [ elem.text for elem in products if 'MacBook' in elem.text ]
  with allure.step("Asserting the number of relevant search results matches the total number of results"):
    assert len(products) == len(new_list)

@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('Shopping Cart')
@allure.title('Test Add Product to Cart')
@allure.description('Verifies that a product can be successfully added to the shopping cart.')
def test_add_to_cart(driver):

  with allure.step("Opening the homepage"):
    driver.get('https://tutorialsninja.com/demo/')

  with allure.step("Adding the first product to cart"):
    product = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]/button[1]')
    product.click()

  with allure.step("Verifying success message appears"):
    success_message = WebDriverWait(driver, timeout=10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert.alert-success"))
    )
    assert "Success: You have added" in success_message.text

  with allure.step("Verifying cart contains 1 item"):
    WebDriverWait(driver, timeout=10).until(
        EC.text_to_be_present_in_element((By.ID, 'cart-total'), "1 item(s)")
    )

  with allure.step("Checking cart contents"):
    cart_button = WebDriverWait(driver, timeout=10).until(
        EC.element_to_be_clickable((By.ID, "cart"))
    )
    cart_button.click()

  with allure.step("Waiting for cart contents to be visible"):
   cart_contents = WebDriverWait(driver, timeout=10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.dropdown-menu.pull-right"))
    )

   with allure.step("Scrolling to cart contents"):
    driver.execute_script("arguments[0].scrollIntoView(true);", cart_contents)

  with allure.step("Verifying the product is in the cart"):
    cart_text = cart_contents.text
    print("Cart contents text:", cart_text)

  with allure.step("Asserting the cart contains 'MacBook'"):
    assert "MacBook" in cart_text, f"Expected 'MacBook' in cart but got '{cart_text}'"


@pytest.mark.regression
@allure.feature('Homepage Slider')
@allure.suite('UI Tests')
@allure.title('Test Slider Functionality')
@allure.description('Verifies that the homepage slider works correctly, allowing navigation between slides.')
@allure.severity(allure.severity_level.NORMAL)
def test_slider_functionality(driver):
   with allure.step("Opening the homepage"):
    driver.get("https://tutorialsninja.com/demo/")

   with allure.step("Locating the slider element"):
    slider = driver.find_element(By.CLASS_NAME, 'swiper-container')
    assert slider.is_displayed(), "Slider is not visible on the page."

   with allure.step("Locating the first active slide"):
    first_slide = driver.find_element(By.CSS_SELECTOR, ".swiper-slide-active img")
    first_slide_src = first_slide.get_attribute("src")

   with allure.step("Clicking the right arrow to move to the next slide"):
    next_arrow = driver.find_element(By.CLASS_NAME, 'swiper-button-next')
    ActionChains(driver).move_to_element(slider).click(next_arrow).perform()

   with allure.step("Waiting for the slide to change"):
    WebDriverWait(driver, 10).until_not(
        EC.element_to_be_clickable(first_slide)
    )

   with allure.step("Verifying that the slider moved to a new slide"):
    new_slide = driver.find_element(By.CSS_SELECTOR, ".swiper-slide-active img")
    new_slide_src = new_slide.get_attribute("src")

   with allure.step("Ensuring that the slider has moved to a new slide"):
    assert first_slide_src != new_slide_src, "Slider did not move to the next image."

   with allure.step("Clicking the left arrow to move back to the first slide"):
    prev_arrow = driver.find_element(By.CLASS_NAME, 'swiper-button-prev')
    prev_arrow.click()

   with allure.step("Waiting for the slider to return to the first slide"):
    WebDriverWait(driver, 10).until_not(
        EC.element_to_be_clickable(new_slide)
    )
   with allure.step("Verifying that the slider returned to the first slide"):
    reverted_slide_src = driver.find_element(By.CSS_SELECTOR, ".swiper-slide-active img").get_attribute("src")
   with allure.step("Ensuring the slider returned to the first image"):
    assert reverted_slide_src == first_slide_src, "Slider did not return to the first image."


@pytest.mark.regression
@allure.feature('Wishlist Functionality')
@allure.title('Test Add Product to Wishlist')
@allure.description('Verifies that a product can be added to the wishlist.')
def test_add_to_wishlist(driver, login):
  with allure.step("Opening the homepage"):
    driver.get("https://tutorialsninja.com/demo/")

  with allure.step("Adding a product to the wishlist"):
    wishlist_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]/button[2]'))
    )

    wishlist_button.click()

  with allure.step("Verifying success message appears"):
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert.alert-success"))
    )
  with allure.step("Ensuring the success message contains 'Success: You have added'"):
    assert "Success: You have added" in success_message.text, "Wishlist add failed"

  with allure.step("Navigating to the wishlist"):
    wishlist_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="wishlist-total"]'))
    )

    wishlist_link.click()

  with allure.step("Verifying MacBook is in the wishlist"):
    wishlist_contents = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div[1]/table/tbody/tr[2]/td[2]/a'))
    )
  with allure.step("Ensuring that 'MacBook' is listed in the wishlist"):
    assert "MacBook" in wishlist_contents.text, "MacBook not found in wishlist"


@pytest.mark.parametrize("button, header, expected_text", [
    (
        (By.XPATH, '/html/body/footer/div/div/div[1]/ul/li[1]/a'),
        (By.XPATH, '//*[@id="content"]/h1'),
        "About Us"
    ),
    (
        (By.XPATH, '/html/body/footer/div/div/div[2]/ul/li[1]/a'),
        (By.XPATH, '//*[@id="content"]/h1'),
        "Contact Us"
    ),
    (
            (By.XPATH, '/html/body/footer/div/div/div[2]/ul/li[2]/a'),
            (By.XPATH, '//*[@id="content"]/h1'),
            "Product Returns"
    ),
    (
            (By.XPATH, "/html/body/footer/div/div/div[3]/ul/li[1]/a"),
            (By.XPATH, '//*[@id="content"]/h1'),
            "Find Your Favorite Brand"
    ),
    (
            (By.XPATH, '/html/body/footer/div/div/div[3]/ul/li[2]/a'),
            (By.XPATH, '//*[@id="content"]/h1'),
            "Purchase a Gift Certificate"
    )
])


@allure.feature('Footer Navigation')
@allure.title('Test Footer Links')
@allure.description('Verifies that footer links navigate to the correct pages and display the expected heading.')
@pytest.mark.regression
def test_footer(driver, button, header, expected_text):
   with allure.step("Opening the homepage"):
    driver.get("https://tutorialsninja.com/demo/")

   with allure.step(f"Clicking footer link and verifying heading: {expected_text}"):
    footer_button = driver.find_element( *button )
    footer_button.click()

    footer_header_text = driver.find_element(*header).text
   with allure.step(f"Verifying the footer heading is '{expected_text}'"):
    assert footer_header_text == expected_text, f"Expected '{expected_text}' but got '{footer_header_text}'"
