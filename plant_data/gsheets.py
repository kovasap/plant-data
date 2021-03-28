import os.path

from googleapiclient.discovery import build
from google.oauth2 import service_account


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1GBeSWGv5R-BQbKymKNVWs17HTEuIsa1XquMWWbnyiE8'

class GSheets:
    def __init__(self):
        creds = service_account.Credentials.from_service_account_file(
            os.path.join(os.path.dirname(__file__), 'client_secret.json'),
            scopes=['https://www.googleapis.com/auth/spreadsheets'])

        self.service = build('sheets', 'v4', credentials=creds)

    def append_row(self, data):
        sheet = self.service.spreadsheets()
        result = sheet.values().append(
            spreadsheetId=SAMPLE_SPREADSHEET_ID,
            body={'values': data},
            range='Sheet1!A1:D',
            valueInputOption='RAW',
        ).execute()
