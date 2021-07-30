@echo off
cmd /k "cd /d C:\regress_venv\Scripts & activate &  cd /d  C:\Users\nitesh.agarwal\PycharmProjects\centime_bdd_framework\results &  behave -i get_time_series_daily.feature -f allure_behave.formatter:AllureFormatter -o allure-results  & allure generate results/ --clean allure-results
pause