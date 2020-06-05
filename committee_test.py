from __future__ import print_function
import time
from pprint import pprint

# Rename swagger_client to something that makes sense:  fec_client
# Ideally the fec_python swagger client code would call itself this,
# but I couldn't get the codegen API to do the right thing.
import swagger_client as fec_client
from swagger_client.rest import ApiException

import config

api_key = config.api_key # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)

# Configure API key authorization: apiKey
configuration = fec_client.Configuration()
configuration.api_key['api_key'] = api_key
# Set host to use the FEC HTTP API
configuration.host = 'https://api.open.fec.gov/v1'

# create an instance of the DisbursementsApi API class
disbursements_api = fec_client.DisbursementsApi(fec_client.ApiClient(configuration))


#min_date = '2017-01-01' # date | Minimum date (optional)
committee_id = ['C00618389'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
sort = '-disbursement_date' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -disbursement_date)
two_year_transaction_period = [2018, 2020] # list[int] |  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle.  (optional)


try:
    api_response = disbursements_api.schedules_schedule_b_get(api_key, committee_id=committee_id, sort=sort, two_year_transaction_period=two_year_transaction_period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisbursementsApi->schedules_schedule_b_get: %s\n" % e)
