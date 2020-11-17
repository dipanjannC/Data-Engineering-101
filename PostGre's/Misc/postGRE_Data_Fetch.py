import psycopg2
from io import StringIO
import pandas as pd
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# connection info and credentials 

host = "covid19postgres.postgres.database.azure.com"
dbname = "stock_db"
user = "bridgei2i@covid19postgres.postgres.database.azure.com"
password = "Bridge@1234"
sslmode = "require"



conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string) 
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
#cursor = conn.cursor()

table = "nifty500"

#checking number of records inserted in the table this will return the table as dataframe
df = pd.read_sql_query('select * from %s'%table, conn)
records = len(df)

#cursor.close()
conn.close()