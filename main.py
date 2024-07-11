from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

# Configuração do driver para Appium
desired_caps = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "emulator-5554",  # ou o nome do seu dispositivo real
    "appPackage": "com.example.myapp",  # pacote do seu aplicativo
    "appActivity": ".MainActivity",  # atividade principal do seu aplicativo
    "automationName": "UiAutomator2"  # ou "Espresso" para testes em Android nativo
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

# Exemplo de interação com elementos na tela
element = driver.find_element_by_id("com.example.myapp:id/button")
element.click()

time.sleep(2)

# Exemplo de uso de TouchAction para gestos
action = TouchAction(driver)
action.press(x=100, y=500).move_to(x=100, y=200).release().perform()

time.sleep(2)

# Fechando o driver
driver.quit()
