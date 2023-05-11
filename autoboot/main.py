from time import sleep

from selenium.webdriver.common.by import By

from autoboot.conf import bootpage, drivobjc, homepage, password, username


def main():
    drivobjc.get(homepage)
    sleep(10)
    drivobjc.find_element(By.CSS_SELECTOR, "input.username").send_keys(username)
    drivobjc.find_element(By.CSS_SELECTOR, "input.password").send_keys(password)
    drivobjc.find_element(By.CSS_SELECTOR, "input.btn_login").click()
    sleep(10)
    drivobjc.get(bootpage)
    sleep(10)
    drivobjc.execute_script("Reboot()")
    drivobjc.switch_to.alert.accept()
