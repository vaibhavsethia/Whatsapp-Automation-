from selenium import webdriver
import os

driver = webdriver.Chrome()
driver.get('http://web.whatsapp.com')

#Scan the code before proceeding further


Flag=1
while Flag :
    name = input('Enter the name of user or group : ')
    msg = input('Enter the message : ')
    count = int(input('Enter the count : '))
    input('Enter anything after scanning QR code')


    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_class_name('_13mgZ')

    for i in range(count):
        msg_box.send_keys(msg)
        driver.find_element_by_class_name('_3M-N-').click()

    Flag=int(input("Enter Flag val : "))


