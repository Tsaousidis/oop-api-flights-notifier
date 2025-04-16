
# ✈️ Flight Price Alert System 📈

## Description
A system to track and notify users about low-price flights for specific destinations using the Amadeus API, Sheety for data management, and email notifications via SMTP.

## Key Features
- Get IATA codes for cities from the Amadeus API.
- Track flight prices and find the cheapest flight offers.
- Send email alerts when low-price flights are found.
- Manage destination data using the Sheety API.

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/Tsaousidis/oop-api-smtp-flights-notifier.git
   ```
2. Navigate to the project directory:
   ```bash
   cd oop-api-smtp-flights-notifier
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file and add the necessary API keys and credentials:
   ```text
   AMADEUS_API_KEY=your_amadeus_api_key
   AMADEUS_SECRET=your_amadeus_api_secret
   SHEETY_ENDPOINT=your_sheety_endpoint
   SHEETY_USERNAME=your_sheety_username
   SHEETY_PASSWORD=your_sheety_password
   EMAIL_SENDER=your_email@example.com
   EMAIL_PASSWORD=your_email_password
   EMAIL_RECIPIENT=recipient_email@example.com
   ```

## System Requirements
- Python 3.8+
- Dependencies listed in `requirements.txt`

## Technologies Used
- Python
- Amadeus API
- Sheety API
- SMTP for email notifications
- Requests for API calls
- dotenv for managing environment variables

## Usage Instructions
1. Run the script to fetch and track flight prices:
   ```bash
   python main.py
   ```

2. The system will send an email alert when a flight price lower than your current lowest price is found.

---

👨‍💻 Created by [Tsaousidis](https://github.com/Tsaousidis)  
🔄 Ready to automate your next task? Feel free to suggest updates.
