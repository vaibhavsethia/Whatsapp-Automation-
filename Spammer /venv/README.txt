The project is made on Pycharm 

Make sure you have the chromedriver executable .
if Not ,
  ->Download the ChromeDriver Executable file from google
  ->place it in the projectName/venv/bin/ folder .
  
Make syre you have installed selenium which will be used 
if Not,
  ->Open terminal and write " pip install selenium " without double quotes 
  ->import selenium 
  
For msg_box ,
  ->open chrome and open whatsapp web , press cmd+shift+C to open javascript console 
  ->look for the class name of the msg box when a chat is open 
  ->read the class name and write it int the driver.find_element_by_class_name() method 
  
For xpath ,
  ->open chrome and open whatsapp web , press cmd+shift+C to open javascript console 
  ->look for the name of the chats in different divs and look for the title word 
  
For button ,
  ->open chrome and open whatsapp web , press cmd+shift+C to open javascript console 
  ->look for the class name of the send button when the message is typed 
  ->read the class name and write it int the driver.find_element_by_class_name() method 
 

