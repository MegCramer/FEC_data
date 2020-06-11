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
    'back_reference_schedule_name': 'back_reference_schedule_name',
    'back_reference_transaction_id': 'back_reference_transaction_id',
    'candidate_first_name': 'candidate_first_name',
    'candidate_id': 'candidate_id',
    'candidate_last_name': 'candidate_last_name',
    'candidate_middle_name': 'candidate_middle_name',
    'candidate_name': 'candidate_name',
    'candidate_office': 'candidate_office',
    'candidate_office_district': 'candidate_office_district',
    'candidate_office_full': 'candidate_office_full',
    'candidate_office_state': 'candidate_office_state',
    'candidate_office_state_full': 'candidate_office_state_full',
    'candidate_prefix': 'candidate_prefix',
    'candidate_suffix': 'candidate_suffix',
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
    'conduit_committee_id': 'conduit_committee_id',
    'conduit_committee_name': 'conduit_committee_name',
    'conduit_committee_state': 'conduit_committee_state',
    'conduit_committee_street1': 'conduit_committee_street1',
    'conduit_committee_street2': 'conduit_committee_street2',
    'conduit_committee_zip': 'conduit_committee_zip',
    'contribution_receipt_amount': 'contribution_receipt_amount',
    'contribution_receipt_date': 'contribution_receipt_date',
    'contributor.affiliated_committee_name': 'contributor.affiliated_committee_name',
    'contributor.candidate_ids': 'contributor.candidate_ids',
    'contributor.city': 'contributor.city',
    'contributor.committee_id': 'contributor.committee_id',
    'contributor.committee_type': 'contributor.committee_type',
    'contributor.committee_type_full': 'contributor.committee_type_full',
    'contributor.cycle': 'contributor.cycle',
    'contributor.cycles': 'contributor.cycles',
    'contributor.cycles_has_activity': 'contributor.cycles_has_activity',
    'contributor.cycles_has_financial': 'contributor.cycles_has_financial',
    'contributor.designation': 'contributor.designation',
    'contributor.designation_full': 'contributor.designation_full',
    'contributor.filing_frequency': 'contributor.filing_frequency',
    'contributor.is_active': 'contributor.is_active',
    'contributor.last_cycle_has_activity': 'contributor.last_cycle_has_activity',
    'contributor.last_cycle_has_financial': 'contributor.last_cycle_has_financial',
    'contributor.name': 'contributor.name',
    'contributor.organization_type': 'contributor.organization_type',
    'contributor.organization_type_full': 'contributor.organization_type_full',
    'contributor.party': 'contributor.party',
    'contributor.party_full': 'contributor.party_full',
    'contributor.state': 'contributor.state',
    'contributor.state_full': 'contributor.state_full',
    'contributor.street_1': 'contributor.street_1',
    'contributor.street_2': 'contributor.street_2',
    'contributor.treasurer_name': 'contributor.treasurer_name',
    'contributor.zip': 'contributor.zip',
    'contributor_aggregate_ytd': 'contributor_aggregate_ytd',
    'contributor_city': 'contributor_city',
    'contributor_employer': 'contributor_employer',
    'contributor_first_name': 'contributor_first_name',
    'contributor_id': 'contributor_id',
    'contributor_last_name': 'contributor_last_name',
    'contributor_middle_name': 'contributor_middle_name',
    'contributor_name': 'contributor_name',
    'contributor_occupation': 'contributor_occupation',
    'contributor_prefix': 'contributor_prefix',
    'contributor_state': 'contributor_state',
    'contributor_street_1': 'contributor_street_1',
    'contributor_street_2': 'contributor_street_2',
    'contributor_suffix': 'contributor_suffix',
    'contributor_zip': 'contributor_zip',
    'donor_committee_name': 'donor_committee_name',
    'election_type': 'election_type',
    'election_type_full': 'election_type_full',
    'entity_type': 'entity_type',
    'entity_type_desc': 'entity_type_desc',
    'fec_election_type_desc': 'fec_election_type_desc',
    'fec_election_year': 'fec_election_year',
    'file_number': 'file_number',
    'filing_form': 'filing_form',
    'image_number': 'image_number',
    'increased_limit': 'increased_limit',
    'is_individual': 'is_individual',
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
    'pdf_url': 'pdf_url',
    'receipt_type': 'receipt_type',
    'receipt_type_desc': 'receipt_type_desc',
    'receipt_type_full': 'receipt_type_full',
    'recipient_committee_designation': 'recipient_committee_designation',
    'recipient_committee_org_type': 'recipient_committee_org_type',
    'recipient_committee_type': 'recipient_committee_type',
    'report_type': 'report_type',
    'report_year': 'report_year',
    'schedule_type': 'schedule_type',
    'schedule_type_full': 'schedule_type_full',
    'sub_id': 'sub_id',
    'transaction_id': 'transaction_id',
    'two_year_transaction_period': 'two_year_transaction_period',
    'unused_contbr_id': 'unused_contbr_id'
})

def get_schedule_a_results():
    results = []

    api_key = api_config
    per_page = 100
    committee_id = 'C00580100' # DJT for president
    sort = '-contribution_receipt_date'
    parameters = '?two_year_transaction_period=2020&two_year_transaction_period=2018&api_key={}&per_page={}&committee_id={}&sort={}'.format(api_key, per_page, committee_id, sort)

    last_indexes = True
    loop_count = 0

    while last_indexes is not None:
# Need to limit this to 120 calls per minute
        response = requests.get('https://api.open.fec.gov/v1/schedules/schedule_a/{}'.format(parameters))
        json_response = response.json()

        pagination = json_response['pagination']

        last_indexes = pagination.get('last_indexes')
        last_indexes_dict = DottedDict(last_indexes)

        last_index = last_indexes_dict.get('last_index')
        last_contribution_receipt_date = last_indexes_dict.get('last_contribution_receipt_date')

        results += json_response['results']

        if loop_count == 0:
            parameters = parameters + '&last_index={}'.format(last_index) + '&last_contribution_receipt_date={}'.format(last_contribution_receipt_date)
        else:
            parameters = '?two_year_transaction_period=2020&two_year_transaction_period=2018&api_key={}&per_page={}&committee_id={}&sort={}&last_index={}&last_contribution_receipt_date={}'.format(api_key, per_page, committee_id, sort, last_index, last_contribution_receipt_date)

        loop_count += 1
        if loop_count == 2:
            break
        print(loop_count)
        print(pagination)
        time.sleep(1)

    return results

def schedule_a_results_to_rows(results):
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


results = get_schedule_a_results()
google_sheets_values = schedule_a_results_to_rows(results)
print(results)
print(google_sheets_values)

#print(google_sheets_values)
