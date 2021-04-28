''' db.py
This file contains controllers to access any tables in the PostgreSQL DB.

Current Controllers:
1. AccountsController()
'''

from psycopg2.extras import RealDictCursor
import psycopg2

class AccountsController():
    '''Controller for the bank_account table'''

    def __init__(self, uri):
        self.uri = uri
        self.db_conn = None
        self.cursor = None

    def create_table(self):
        '''Conditional table creation'''

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
        '''Add row to the bank_account table based on the account_details'''

        query = ("INSERT INTO bank_account("
                 "AccountBalance, AccountType, FirstName, LastName, Address) "
                 "VALUES (%s,%s,%s,%s,%s)")
        data = (account_details["balance"],
                account_details["account_type"],
                account_details["first"],
                account_details["last"],
                account_details["address"],)
        self.run_query(query, data)

    def get_table_size(self):
        '''Query bank_account table to get number of rows'''

        query = ("SELECT COUNT(*) from bank_account")
        result = self.run_query(query)
        return result[0]["count"]

    def get_rows(self):
        '''Query bank_account to get a list of all rows'''

        query = ("SELECT * from bank_account")
        result = self.run_query(query)
        return result

    def run_query(self, query, data=None):
        '''
        General purpose query for the bank_account table.
        params:
            query: - String containing the desired query
            data:  - Optional params to be passed into the query

        returnVal:
            result: - None if query did not return anything
                    - Query result otherwise
        '''

        self.db_connect()
        result = None
        try:
            with self.db_conn:
                with self.cursor as curs:
                    curs.execute(query, data)
                    try:
                        result = curs.fetchall()
                    except psycopg2.ProgrammingError:
                        # No result to fetch
                        pass

        except psycopg2.Error as err:
            if err == psycopg2.DatabaseError:
                print("Database error while running account query: ", err)
            else:
                print("psycopg2 error: ", err)

        finally:
            self.db_disconnect()

        return result

    def db_connect(self):
        '''Establish db connection'''

        self.db_conn = psycopg2.connect(self.uri)
        self.cursor = self.db_conn.cursor(cursor_factory=RealDictCursor)

    def db_disconnect(self):
        '''Disconnect db after query is run'''

        self.cursor.close()
        self.db_conn.close()
