# Used to grab the sheets API using Python

#source .venv/bin/activate to activate python enviorement

from googleapiclient.discovery import build
from google.oauth2 import service_account

# Define the necessary scopes and credentials
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'credentials.json'  # Replace with the path to your service account credentials JSON file
SPREADSHEET_ID = 'your_spreadsheet_id'  # Replace with your actual spreadsheet ID

# Authenticate and create the service
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('sheets', 'v4', credentials=credentials)

# Example: Reading data from the spreadsheet
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range='Sheet1').execute()
values = result.get('values', [])
if not values:
    print('No data found.')
else:
    print('Data from the Google Sheet:')
    for row in values:
        print(row)

# Example: Writing data to the spreadsheet
new_values = [
    ["New Data 1", "New Data 2", "New Data 3"],
    ["Another New Data 1", "Another New Data 2", "Another New Data 3"]
]
body = {'values': new_values}
result = sheet.values().append(spreadsheetId=SPREADSHEET_ID, range='Sheet1', valueInputOption='RAW', body=body).execute()
print('{0} cells updated.'.format(result.get('updatedCells')))

# Example: Updating data in the spreadsheet
new_value = "Updated Value"
update_body = {'values': [[new_value]]}
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID, range='A1', valueInputOption='RAW', body=update_body).execute()
print('{0} cells updated.'.format(result.get('updatedCells')))
