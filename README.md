# PYTHON-BDD
PYTHON-BDD PROJECT TO PERFORM API AUTOMATION

"""Virtual Enviornment (Python Libraries) Required to Run Scripts"""
Json
Json Compare - Have made some changes in library to make scripts run
json_path_rwxt
Pandas
Behave
os
configparser
allure
requests
warnings

"""Instructions to run the test"""
1. Inside the runner file there is one batch file present go ahead and run the batch file, but that would require changes to be dome in the base pat.
2. Another way is execute the below batch file command in terminal of your IDE.This will also generate allure report.

behave -i get_time_series_daily.feature -f allure_behave.formatter:AllureFormatter -o allure-results  & allure generate results/ --clean allure-results


"""Report View"""
1. Go to result folder wherever the result was stored.
2. Go to allure report and do open index.html in any of your browser.
