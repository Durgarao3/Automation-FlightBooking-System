from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


# Setup Chrome driver
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service = Service(r"C:\Users\LENOVO\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get("https://durgarao3.github.io/AirlineBookingSystem/")  # Load the main page

driver.find_element(By.ID, "from").send_keys("Hyderabad")
time.sleep(1)  # wait for suggestions to load
driver.find_element(By.ID, "to").send_keys("Bangalore")
time.sleep(1)  # wait for suggestions to load
driver.find_element(By.ID, "date").send_keys("15-07-2025")
time.sleep(1)  # wait for date picker to load
driver.find_element(By.XPATH, "//button[text()='Search Flights']").click()
time.sleep(3)

# Step 2: Simulate flight selection (static page)
driver.get("https://durgarao3.github.io/AirlineBookingSystem/booking.html?")  # simulate clicking flight card
flight_cards = driver.find_elements(By.CLASS_NAME, "flight-card")
time.sleep(2)
# Step 3: Fill passenger booking form

driver.find_element(By.ID, "fullname").send_keys("DurgaRao Patnala")
time.sleep(1)
driver.find_element(By.ID, "email").send_keys("patnaladurgarao3@gmail.com")
time.sleep(1)
driver.find_element(By.ID, "phone").send_keys("7337403364")
time.sleep(1)
driver.find_element(By.XPATH, "//button[text()='Confirm Booking']").click()
time.sleep(3)

# Step 4: Verify confirmation
current_url = driver.current_url
if "confirmation.html" in current_url:
    print("Booking confirmed successfully!")
else:
    print("Booking failed!")

# Optional: Close browser after some time
time.sleep(3)
driver.quit()