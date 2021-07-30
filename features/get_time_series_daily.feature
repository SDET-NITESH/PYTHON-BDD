# Created by Nitesh.Agarwal at 7/30/2021
#  Functional and Negative scenarios for Time Series Daily API
Feature: Validate Get Time Series Daily API with valid and invalid combination of data.
  # Enter feature description here

  @functional-Scenarios
  Scenario Outline: Validate Get time series resource for given "<test_type>" and "<test_case_id>"
        Given end point of get time resource along with query param as "<query_param>" and query value as "<query_value>"
        When send request to the server for the time series endpoint along with query data
        Then validate server response code "<response_code>"
      Examples:
        |test_type                                                                                   |response_code  |test_case_id                    |query_param                                       |query_value|
        |Demonstrate that Get time Resource api returns data for given valid set of required data    |200            |API_GTS_Valid_001               |["function","symbol","apikey"]                    |["TIME_SERIES_DAILY","IBM","LVDWZYDOWUB07C36"]|
        |Demonstrate that Get time Resource api returns data for required and optional data          |200            |API_GTS_Valid_002               |["function","symbol","apikey","outputsize"]       |["TIME_SERIES_DAILY","IBM","LVDWZYDOWUB07C36","full"]|



  @negative-Scenarios
  Scenario Outline: Validate Get time series resource for given "<test_type>" and "<test_case_id>"
        Given end point of get time resource along with query param as "<query_param>" and query value as "<query_value>"
        When send request to the server for the time series endpoint along with query data
        Then validate server response code "<response_code>"
        Then Validate server response error messages for "<test_case_id>"
      Examples:
        |test_type                                                                                   |response_code  |test_case_id                    |query_param                          |query_value|
        |Validate get time series api returns error for invalid function value                       |200            |API_GTS_InValid_001             |["function","symbol","apikey"]       |["TIME_SERIES","IBM","LVDWZYDOWUB07C36"]|
        |Validate get time series api returns error for invalid function key                         |200            |API_GTS_InValid_002             |["functi","symbol","apikey"]       |["TIME_SERIES_DAILY","IBM","LVDWZYDOWUB07C36"]|
        |Validate get time series api returns error for invalid symbol key                           |200            |API_GTS_InValid_003             |["function","symb","apikey"]       |["TIME_SERIES_DAILY","IBM","LVDWZYDOWUB07C36"]|
        |Validate get time series api returns error for invalid apiKey key                           |200            |API_GTS_InValid_004             |["function","symbol","apik"]       |["TIME_SERIES_DAILY","IBM","LVDWZYDOWUB07C36"]|