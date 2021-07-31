from behave import  given, when, then
from proboscis import  asserts
import json
import jsonpath_rw_ext as jp
from jsoncompare import jsoncompare as json_comp
from util.util import get_request, get_config_value,generate_query_data,generate_url_with_query_data, capture_log, capture_log_pretty_json, convert_excel_dict,pick_required_data
from util.get_time_series_util import get_time_series_util as gtsu

"""URL for application"""
TIME_SERIES_DAILY_ENDPOINT = get_config_value('get_time_series_endpoint')


"""Test Data for application"""
TIME_SERIES_ERROR_MESSAGE = convert_excel_dict(gtsu.time_series_test_data_sheet, gtsu.TIME_SERIES_ERROR_MESSAGE_SHEET_NAME)


@given('end point of get time resource along with query param as "{query_param}" and query value as "{query_value}"')
def end_point_of_time_resource_with_query_data(context, query_param, query_value):
    """
    :param context:behave.runner.Context
     :type context: behave.runner.Context
    :param query_param: query parameter to pass query fields
    :type query_param: str
    :param query_value: filed values to be passed as query value
    :type query_value: str

    """
    context.end_point = TIME_SERIES_DAILY_ENDPOINT
    context.query_param = query_param
    context.query_value = query_value
    context.log_endpoint = context.end_point + generate_url_with_query_data(query_param, query_value)
    capture_log(context.log_endpoint, "End point of the time series api with query data is")


@when(u'send request to the server for the time series endpoint along with query data')
def send_request_for_time_series(context):
    """
    method for sending request to server for customer based on Part Number


    """
    query_data = generate_query_data(context.query_param, context.query_value)
    try:
        context.response = get_request(context.end_point, **query_data)
    except Exception as e:
        print("Exception Occured ",e)
    capture_log_pretty_json(context.response.text, "Response messages of the request for " )


@then(u'Validate server response code "{response_code}"')
def validate_response_code(context, response_code):
    """
    :param context:
    :param response_code: actual response code
    :type context:behave.runner.Context
    :type response_code: str

    """

    capture_log(context.response.status_code, "Expected response code " +  str(response_code)  + " and actual response code " + str(context.response.status_code))
    asserts.assert_equal(context.response.status_code, int(response_code), "Expected and actual code should match")


@then('Validate server response error messages for "{test_case_id}"')
def validate_error_message(context, test_case_id):
    """
    :type context: behave.runner.Context
    :type test_case_id: str
    """
    context.response = json.loads(context.response.text)
    actual_error_message = jp.match(gtsu.actual_error_message_json_path, context.response)
    context.expected_data = json.loads(pick_required_data(TIME_SERIES_ERROR_MESSAGE, test_case_id, "Test_Data_Reference"))
    context.expected_error_message = jp.match(gtsu.expected_error_message_json_path, context.expected_data)
    comp_result_error_message = json_comp._is_list_same(actual_error_message, context.expected_error_message, True)
    if comp_result_error_message is False:
        capture_log(comp_result_error_message, "Compare the Error message ")
        assert False