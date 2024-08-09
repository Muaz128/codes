import requests
from selenium import webdriver

# Path to your WebDriver executable
driver_path = 'path/to/chromedriver'

# Initialize the WebDriver (e.g., for Chrome)
driver = webdriver.Chrome(executable_path=driver_path)

# Open the target website
driver.get('https://example.com')

# Extract cookies
cookies = driver.get_cookies()

# Prepare the data to send to the Discord webhook
webhook_url = 'https://discord.com/api/webhooks/your_webhook_id/your_webhook_token'
content = 'Extracted cookies:'
embeds = [
    {
        'title': 'Cookies Extracted',
        'description': content,
        'fields': [{'name': cookie['name'], 'value': cookie['value']} for cookie in cookies]
    }
]

# Send the data to the Discord webhook
data = {
    'content': 'Here is the extracted data:',
    'embeds': embeds
}
response = requests.post(webhook_url, json=data)

# Check if the request was successful
if response.status_code == 204:
    print('Data sent successfully!')
else:
    print(f'Failed to send data. Status code: {response.status_code}')

# Close the browser
driver.quit()
