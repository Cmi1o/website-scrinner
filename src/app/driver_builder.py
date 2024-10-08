from selenium.webdriver import ChromeOptions


def set_options() -> ChromeOptions:
    options = ChromeOptions()
    
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    
    return options


options = set_options()
