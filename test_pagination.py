import requests
import time
import json

from collections import OrderedDict
from dotted.collection import DottedDict

import config

api_config = config.api_key

dotted_result_keys_to_column_names = OrderedDict({
    'amendment_indicator': 'amendment_indicator',
    'amendment_indicator_desc': 'amendment_indicator_desc',
    'back_reference_schedule_id': 'back_reference_schedule_id',
    'back_reference_transaction_id': 'back_reference_transaction_id',
    'beneficiary_committee_name': 'beneficiary_committee_name',
    'candidate_first_name': 'candidate_first_name',
    'candidate_id': 'candidate_id',
    'candidate_last_name': 'candidate_last_name',
    'candidate_middle_name': 'candidate_middle_name',
    'candidate_name': 'candidate_name',
    'candidate_office': 'candidate_office',
    'candidate_office_description': 'candidate_office_description',
    'candidate_office_district': 'candidate_office_district',
    'candidate_office_state': 'candidate_office_state',
    'candidate_office_state_full': 'candidate_office_state_full',
    'candidate_prefix': 'candidate_prefix',
    'candidate_suffix': 'candidate_suffix',
    'category_code': 'category_code',
    'category_code_full': 'category_code_full',
    'comm_dt': 'comm_dt',
    'committee.affiliated_committee_name': 'affiliated_committee_name',
    'committee.candidate_ids': 'candidate_ids',
    'committee.city': 'city',
    'committee.committee_id': 'committee_id',
    'committee.committee_type': 'committee_type',
    'committee.committee_type_full': 'committee_type_full',
    'committee.cycle': 'committee_cycle',
    'committee.cycles': 'committee_cycles',
    'committee.cycles_has_activity': 'cycles_has_activity',
    'committee.cycles_has_financial': 'cycles_has_financial',
    'committee.designation': 'designation',
    'committee.designation_full': 'designation_full',
    'committee.filing_frequency': 'filing_frequency',
    'committee.is_active': 'is_active',
    'committee.last_cycle_has_activity': 'last_cycle_has_activity',
    'committee.last_cycle_has_financial': 'last_cycle_has_financial',
    'committee.name': 'name',
    'committee.organization_type': 'organization_type',
    'committee.organization_type_full': 'organization_type_full',
    'committee.party': 'party',
    'committee.party_full': 'party_full',
    'committee.state': 'state',
    'committee.state_full': 'state_full',
    'committee.street_1': 'street_1',
    'committee.street_2': 'street_2',
    'committee.treasurer_name': 'treasurer_name',
    'committee.zip': 'committee.zip',
    'committee_id': 'committee_id',
    'conduit_committee_city': 'conduit_committee_city',
    'conduit_committee_name': 'conduit_committee_name',
    'conduit_committee_state': 'conduit_committee_state',
    'conduit_committee_street1': 'conduit_committee_street1',
    'conduit_committee_street2': 'conduit_committee_street2',
    'conduit_committee_zip': 'conduit_committee_zip',
    'disbursement_amount': 'disbursement_amount',
    'disbursement_date': 'disbursement_date',
    'disbursement_description': 'disbursement_description',
    'disbursement_purpose_category': 'disbursement_purpose_category',
    'disbursement_type': 'disbursement_type',
    'disbursement_type_description': 'disbursement_type_description',
    'election_type': 'election_type',
    'election_type_full': 'election_type_full',
    'entity_type': 'entity_type',
    'entity_type_desc': 'entity_type_desc',
    'fec_election_type_desc': 'fec_election_type_desc',
    'fec_election_year': 'fec_election_year',
    'file_number': 'file_number',
    'filing_form': 'filing_form',
    'image_number': 'image_number',
    'line_number': 'line_number',
    'line_number_label': 'line_number_label',
    'link_id': 'link_id',
    'load_date': 'load_date',
    'memo_code': 'memo_code',
    'memo_code_full': 'memo_code_full',
    'memo_text': 'memo_text',
    'memoed_subtotal': 'memoed_subtotal',
    'national_committee_nonfederal_account': 'national_committee_nonfederal_account',
    'original_sub_id': 'original_sub_id',
    'payee_employer': 'payee_employer',
    'payee_first_name': 'payee_first_name',
    'payee_last_name': 'payee_last_name',
    'payee_middle_name': 'payee_middle_name',
    'payee_occupation': 'payee_occupation',
    'payee_prefix': 'payee_prefix',
    'payee_suffix': 'payee_suffix',
    'pdf_url': 'pdf_url',
    'recipient_city': 'recipient_city',
    'recipient_committee.affiliated_committee_name': 'affiliated_committee_name',
    'recipient_committee.candidate_ids': 'candidate_ids',
    'recipient_committee.city': 'city',
    'recipient_committee.committee_id': 'committee_id',
    'recipient_committee.committee_type': 'committee_type',
    'recipient_committee.committee_type_full': 'committee_type_full',
    'recipient_committee.cycle': 'recipient_cycle',
    'recipient_committee.cycles': 'recipient_cycles',
    'recipient_committee.cycles_has_activity': 'cycles_has_activity',
    'recipient_committee.cycles_has_financial': 'cycles_has_financial',
    'recipient_committee.designation': 'designation',
    'recipient_committee.designation_full': 'designation_full',
    'recipient_committee.filing_frequency': 'filing_frequency',
    'recipient_committee.is_active': 'is_active',
    'recipient_committee.last_cycle_has_activity': 'last_cycle_has_activity',
    'recipient_committee.last_cycle_has_financial': 'last_cycle_has_financial',
    'recipient_committee.name': 'name',
    'recipient_committee.organization_type': 'organization_type',
    'recipient_committee.organization_type_full': 'organization_type_full',
    'recipient_committee.party': 'party',
    'recipient_committee.party_full': 'party_full',
    'recipient_committee.state': 'state',
    'recipient_committee.state_full': 'state_full',
    'recipient_committee.street_1': 'street_1',
    'recipient_committee.street_2': 'street_2',
    'recipient_committee.treasurer_name': 'treasurer_name',
    'recipient_committee.zip': 'zip',
    'recipient_committee_id': 'recipient_committee_id',
    'recipient_name': 'recipient_name',
    'recipient_state': 'recipient_state',
    'recipient_zip': 'recipient_zip',
    'ref_disp_excess_flg': 'ref_disp_excess_flg',
    'report_type': 'report_type',
    'report_year': 'report_year',
    'schedule_type': 'schedule_type',
    'schedule_type_full': 'schedule_type_full',
    'semi_annual_bundled_refund': 'semi_annual_bundled_refund',
    'spender_committee_designation': 'spender_committee_designation',
    'spender_committee_org_type': 'spender_committee_org_type',
    'spender_committee_type': 'spender_committee_type',
    'sub_id': 'sub_id',
    'transaction_id': 'transaction_id',
    'two_year_transaction_period': 'two_year_transaction_period',
    'unused_recipient_committee_id': 'unused_recipient_committee_id'
})

def get_schedule_b_results():
    results = []

    api_key = api_config
    committee_id = 'C00580100' # DJT for president
    recipient_name = 'jones%20day'
    disbursement_description = 'legal%20consulting'
    sort = '-disbursement_date'
    parameters = '?two_year_transaction_period=2020&two_year_transaction_period=2018&api_key={}&committee_id={}&recipient_name={}&disbursement_description={}&sort={}'.format(api_key, committee_id, recipient_name, disbursement_description, sort)

    last_indexes = True
    loop_count = 0

    while last_indexes is not None:
# Need to limit this to 120 calls per minute
        response = requests.get('https://api.open.fec.gov/v1/schedules/schedule_b/{}'.format(parameters))
        json_response = response.json()

        pagination = json_response['pagination']

        last_indexes = pagination.get('last_indexes')
        last_indexes_dict = DottedDict(last_indexes)

        last_index = last_indexes_dict.get('last_index')
        last_disbursement_date = last_indexes_dict.get('last_disbursement_date')

        results += json_response['results']

        if loop_count == 0:
            parameters = parameters + '&last_index={}'.format(last_index) + '&last_disbursement_date={}'.format(last_disbursement_date)
        else:
            parameters = '?two_year_transaction_period=2020&two_year_transaction_period=2018&api_key={}&committee_id={}&recipient_name={}&disbursement_description={}&sort={}&last_index={}&last_disbursement_date={}'.format(api_key, committee_id, recipient_name, disbursement_description, sort, last_index, last_disbursement_date)

        loop_count += 1
        if loop_count == 5:
            break

        time.sleep(1)

    return results

def schedule_b_results_to_rows(results):
    rows = []

    for result in results:
        result = DottedDict(result)
        row = []

        for result_key in dotted_result_keys_to_column_names.keys():
            if result_key not in result:
                normalized = None
            else:
                normalized = str(result[result_key]).strip('[]')
            row.append(normalized)
        rows.append(row)

    column_header_row = list(dotted_result_keys_to_column_names.values())
    return [column_header_row] + rows


results = get_schedule_b_results()
google_sheets_values = schedule_b_results_to_rows(results)

#print(google_sheets_values)
