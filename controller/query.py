#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'controller'))
	print(os.getcwd())
except:
	pass
#%%
import psycopg2 as pg


#%%
import pandas as pd
import psycopg2
import sqlalchemy
import matplotlib as plt

get_ipython().run_line_magic('matplotlib', 'inline')


#%%
conda install psycopg2


#%%
from sqlalchemy import create_engine


#%%
# Postgres username, password, and database name
POSTGRES_PORT = '5432'
POSTGRES_USERNAME = 'postgres' 
POSTGRES_PASSWORD = ''
POSTGRES_ADDRESS = 'localhost'
POSTGRES_DBNAME  = 'consume'


#%%
# A long string that contains the necessary Postgres login information
postgres_str = ('postgresql://{username}:{password}@{ipaddress}:{port}/{dbname}'
.format(username=POSTGRES_USERNAME,
        password=POSTGRES_PASSWORD,
        ipaddress=POSTGRES_ADDRESS,
        port=POSTGRES_PORT,
        dbname=POSTGRES_DBNAME))


#%%
# Create the connection
cnx = create_engine(postgres_str)


#%%
country_data= pd.read_sql_query('''SELECT * FROM loans;''',cnx) 
country_data.head()


#%%
country_loan_status = pd.read_sql_query("""SELECT country as country, country_code as code, loan_status as status, interest_rate as interest, closed_date as date FROM loans""", cnx)
country_loan_status.head()


#%%
country_loan_status.interest.hist()


#%%
country_loan_status.interest.hist(bins=500)


#%%
country_loan_status.country.hist()


#%%
country_loan_status.country.hist(bins=500)


#%%



