from time import sleep

from selenium.webdriver.common.by import By

from autoboot.conf import bootpage, drivobjc, homepage, password, username


def main():
    drivobjc.get(homepage)
    sleep(5)
    drivobjc.find_element(By.CSS_SELECTOR, "input.username").send_keys(username)
    drivobjc.find_element(By.CSS_SELECTOR, "input.password").send_keys(password)
    drivobjc.find_element(By.CSS_SELECTOR, "input.btn_login").click()
    sleep(5)
    drivobjc.get(bootpage)
    sleep(5)
    drivobjc.execute_script("Reboot()")
