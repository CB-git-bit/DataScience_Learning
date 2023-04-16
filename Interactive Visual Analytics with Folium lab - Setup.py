# install python packages required to run application:
python3.8 -m pip install pandas dash
# collect the dataset of spacex_launch_dash.csv:
wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv"
#Download a skeleton Dash app to work off of: 
wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_3/spacex_dash_app.py"
#Test the skeleton app in terminal:
python3.8 spacex_dash_app.py
