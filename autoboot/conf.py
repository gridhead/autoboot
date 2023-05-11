from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

optnobjc = webdriver.ChromeOptions()
optnobjc.add_experimental_option("detach", True)
optnobjc.set_capability("acceptInsecureCerts", True)
drivobjc = webdriver.Chrome(options=optnobjc, service=Service(ChromeDriverManager().install()))

username = "admin"
password = "admin"

hostname = "192.168.0.1"
homepage = "https://%s/" % hostname
bootpage = "https://%s/pages.html#stat.stat5.stat54" % hostname
