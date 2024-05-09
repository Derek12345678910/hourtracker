# Used to grab the sheets API using Python

import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope and credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

# Authorize the client
client = gspread.authorize(creds)

# Open the Google Sheet by its title
sheet = client.open('Your Google Sheet Title').sheet1

# Example: Reading data from the spreadsheet
data = sheet.get_all_records()
print("Data from the Google Sheet:")
print(data)

# Example: Writing data to the spreadsheet
new_row = ["New Data 1", "New Data 2", "New Data 3"]
sheet.append_row(new_row)
print("New row appended to the Google Sheet.")

# Example: Updating data in the spreadsheet
cell_to_update = 'A1'
new_value = "Updated Value"
sheet.update(cell_to_update, new_value)
print("Cell A1 updated in the Google Sheet.")

