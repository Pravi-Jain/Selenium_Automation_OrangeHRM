from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

#Making a service object
serv_obj = Service("C:\Drivers\msedgedriver.exe")

ops = Options()
ops.add_experimental_option(name="detach", value=True)

# Setup the WebDriver
driver = webdriver.Edge(service=serv_obj, options=ops)


try:
    # Navigate to the OrangeHRM login page
    driver.get("https://opensource-demo.orangehrmlive.com/")

    driver.maximize_window()        # Maximize browser window

    driver.implicitly_wait(10)      # Wait for e


    ### FOR LOGIN

    # Enter username
    username_field = driver.find_element(By.NAME, "username")
    username_field.send_keys("Admin")  # Replace with valid username

    # Enter password
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("admin123")  # Replace with valid password

    # Click the login button
    login_button = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
    login_button.click()

    # Validate successful login
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "//*[@id='app']/div[1]/div[1]/aside/nav/div[1]/a/div[2]/img"))
    )
    print("Login successful!")


    ### Search user

    # custom name - can be added through excel
    uname = input("Enter the name to search")
    time.sleep(10)

    # username
    driver.find_element(By.XPATH, "//div[@class='oxd-form-row']/div/div[1]/div/div[2]/input").send_keys(uname)

    # role
    driver.find_element(By.XPATH, "//div[@class='oxd-select-wrapper']/div/div[1]").click()
    if uname == 'Admin':
        driver.find_element(By.XPATH, "//div[@role='listbox']/div[2]").click()
    else:
        driver.find_element(By.XPATH, "//div[@role='listbox']/div[3]").click()

    # status
    rolestatus = driver.find_elements(By.XPATH, "//div[@class='oxd-select-wrapper']/div/div[1]")
    rolestatus[1].click()
    driver.find_element(By.XPATH, "//div[@role='listbox']/div[2]").click()

    # driver.find_element(By.XPATH, "//div[@role='listbox']/div[3]").click()         # disabled

    # search button
    driver.find_element(By.XPATH, "//div[@class='oxd-form-actions']/button[2]").click()

    # Reset Search
    #driver.find_element(By.XPATH, "//div[@class='oxd-form-actions']/button[1]").click()


    
    ### Add user
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click()


except Exception as e:
    print(f"An error occurred: {e}")

#finally:
    # Close the browser
#    driver.quit()
