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
        edit_button = driver.find_element(By.XPATH, "//span[text()='Resume Headline']/following-sibling::span[contains(@class, 'edit')]")
        edit_button.click()
        time.sleep(2)

        # Update the resume headline (example text)
        headline_box = driver.find_element(By.XPATH, "//textarea[@name='resumeHeadline']")
        headline_box.clear()
        headline_box.send_keys("Experienced Python Developer with expertise in automation and web scraping.")

        # Save changes
        save_button = driver.find_element(By.XPATH, "//button[text()='Save']")
        save_button.click()
        time.sleep(2)
    except Exception as e:
        pytest.fail(f"Failed to update resume headline: {e}")

    # Optionally, assert that the update was successful
    updated_headline = driver.find_element(By.XPATH, "//span[text()='Resume Headline']/following-sibling::span[1]").text
    assert "Experienced Python Developer" in updated_headline
