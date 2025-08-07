# ✈️ Automation Flight Booking System

This is a Python automation project using **Selenium WebDriver** to simulate a flight booking system.

---

## 🛠️ Features

- Automates flight search and booking on a sample website.
- Uses ChromeDriver for browser automation.
- Includes form filling, submission, and confirmation.

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Durgarao3/Automation-FlightBooking-System.git
cd Automation-FlightBooking-System

### 2.Install dependencies
Make sure you have Python installed, then run:
pip install selenium

###3.Run the automation script
python flightbookings.py

git add README.md
git commit -m "Add project README"
git push

---

## 🧪 Notes

- Ensure **Google Chrome** is installed.
- Download the matching **ChromeDriver** version from:  
  👉 [https://sites.google.com/chromium.org/driver/](https://sites.google.com/chromium.org/driver/)

### ➕ Add ChromeDriver to Environment Path (Windows)

1. Extract the downloaded `chromedriver.exe`.
2. Move it to a folder like `C:\WebDriver\bin\` or your project directory.
3. Add the folder path to **Environment Variables**:
   - Search **"Environment Variables"** in Windows Search.
   - Click **Environment Variables...**
   - Under **System variables**, select `Path` → **Edit** → **New** → paste the folder path.
   - Click OK and restart your terminal.

🔄 Alternatively, in your script you can specify the path manually:

```python
driver = webdriver.Chrome(executable_path="C:/path/to/chromedriver.exe")

## 🔗 Related Project

This automation script was built to test the frontend built in the following project:

✈️ [Airline Booking System (HTML/CSS UI)](https://github.com/Durgarao3/AirlineBookingSystem)

You can view the live demo of the booking system here:  
🌐 [Live Demo](https://durgarao3.github.io/AirlineBookingSystem/)
