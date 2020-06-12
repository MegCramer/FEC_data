from __future__ import print_function
import pickle
import json
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import get_schedule_a

# If modifying these scopes, delete the file token.pickle.
# MC - Still not sure what this does
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
spreadsheetId = '1fkGZ7-2mGxRMe8Opzuf5O2WoiWDswgd-cLt3ozhD1ck'
range = 'schedule_a'
value_input_option = 'USER_ENTERED'

value_range_body = {
    'majorDimension': 'ROWS',
    'values': get_schedule_a.google_sheets_values
}

def main():

    token = open('token.pickle', 'rb')
    creds = pickle.load(token)

    service = build('sheets', 'v4', credentials=creds)

    #Call the Sheets API
    sheet = service.spreadsheets()
    write = sheet.values().update(spreadsheetId=spreadsheetId, range=range, valueInputOption=value_input_option, body=value_range_body)
    response = write.execute()
    result = sheet.values().get(spreadsheetId=spreadsheetId,
                             range=range).execute()

    print(response)

if __name__ == '__main__':
    main()
