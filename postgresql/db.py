from psycopg2.extras import RealDictCursor
import psycopg2

class AccountsController():
    def __init__(self, uri):
        self.uri = uri

    def create_table(self):
        query = ("CREATE TABLE IF NOT EXISTS bank_account("
                 "AccountID serial PRIMARY KEY,"
                 "AccountBalance NUMERIC(10,2) NOT NULL,"
                 "AccountType VARCHAR(20) NOT NULL,"
                 "FirstName VARCHAR(50) NOT NULL,"
                 "LastName VARCHAR(50) NOT NULL,"
                 "Address VARCHAR(100) NOT NULL"
                 ");")
        self.run_query(query)

    def add_account(self, account_details):
        query = ("INSERT INTO bank_account("
                 "AccountBalance, AccountType, FirstName, LastName, Address) "
                 "VALUES (%s,%s,%s,%s,%s)")
        data = (account_details["balance"],
                account_details["account_type"],
                account_details["first"],
                account_details["last"],
                account_details["address"],)
        self.run_query(query, data)

    def run_query(self, query, data=[]):
        self.db_connect()
        try:
            with self.db_conn:
                with self.cursor as curs:
                    curs.execute(query, data)
        except psycopg2.Error as e:
            print("Error while running account query: ", e)
        except psycopg2.Warning as w:
            print("Warning while running account query: ", w)
        finally:
            self.db_disconnect()

    def db_connect(self):
        self.db_conn = psycopg2.connect(self.uri)
        self.cursor = self.db_conn.cursor(cursor_factory=RealDictCursor)

    def db_disconnect(self):
        self.cursor.close()
        self.db_conn.close()
