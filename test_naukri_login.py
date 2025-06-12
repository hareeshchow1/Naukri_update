import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time






@pytest.fixture(scope="module")
def driver():
    # You can change to webdriver.Chrome() if you have ChromeDriver
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

def test_naukri_login(driver):
    username = 'dp121407h@gmail.com'
    password = 'code@dp3'
    Updated_Name = "panuganti deepthi"
    
    
    driver.get("https://www.naukri.com/nlogin/login")
    time.sleep(2)  # Wait for page to load

    # Find username and password fields and login button
    driver.find_element(By.ID, "usernameField").send_keys(username)
    driver.find_element(By.ID, "passwordField").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)  # Wait for login to process

    # Check if login was successful (look for a known element after login)
    assert "naukri.com" in driver.current_url

    # Navigate to the "Update Profile" or "Resume" section
    driver.get("https://www.naukri.com/mnjuser/profile")
    time.sleep(5)  # Wait for profile page to load

    # Example: Click on the "Resume Headline" edit button (update as per actual element)
    try:
        edit_button = driver.find_element(By.XPATH, '//em[@class="icon edit "]')
        edit_button.click()
        time.sleep(2)

        dialog_box = driver.find_element(By.XPATH, "//*[@id='editBasicDetailsForm']")
        assert dialog_box.is_displayed(), "Edit dialog box is not displayed."

        name_edit = driver.find_element(By.XPATH, '//*[@id="name"]')
        name_edit.clear()
        name_edit.send_keys(Updated_Name) # Update with a new name
        time.sleep(1)

        # Save changes
        save_button = driver.find_element(By.XPATH, "//button[text()='Save']")
        save_button.click()
        time.sleep(2)
    except Exception as e:
        pytest.fail(f"Failed to update resume : {e}")
