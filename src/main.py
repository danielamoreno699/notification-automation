   # percentage = clean_percentage(element_text)
    # print(percentage)
    # percentage = get_percentage(driver)
    # write_percentage_to_csv(percentage)
    # send_email(percentage)

from ast import Return
from selenium import webdriver

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument('disable-dev-shm-usage')
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"] )
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options)
    driver.get("https://es.investing.com/currencies/usd-cop")
    return driver


def convert_to_float(text):
    str_number = text.replace(',', '.').replace('.', '', 1)
    float_number = float(str_number)
    return float_number


def detector(number):
    percentage = 2 / 100
    number1 = percentage * number
    number2 = number - number1

    if number < number2:
        return f'Price is below 2%: {number2:.2f}'
    else:
        return f'Price is above 2%: {number2:.2f}'


def main():
    driver = get_driver()
    element = driver.find_element(by="xpath", value='//*[@id="__next"]/div[2]/div/div/div/main/div/div[1]/div[2]/div[1]/span')
    element_text = element.text
    float_element = convert_to_float(element_text)
    detector1 = detector(float_element)
    return detector1
    #print(float_element)


print(main())



