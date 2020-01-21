import psycopg2 as pg
import csv

# file = r'../models/loans-historical-data.csv'
sql_insert = """INSERT INTO loans(id, End_of_Period,
    Loan_Number,
    Country_Code,
    Country,
    Borrower,
    Guarantor_Country_Code,
    Guarantor,
    Loan_Type,
    Loan_Status,
    Interest_Rate,
    Region,
    Currency_of_Commitment,
    Project_Name,
    Original_Principal_Amount,
    Cancelled_Amount,
    Undisbursed_Amount,
    Disbursed_Amount,
    Due_to_IBRD,
    Exchange_Adjustment,
    Borrower_Obligation,
    Sold_3rd_Party,
    Repaid_3rd_Party,
    Due_3rd_Party,
    Loans_Held,
    First_Repayment_Date,
    Last_Repayment_Date,
    Agreement_Signing_Date,
    Project_ID,
    Board_Approval_Date,
    Effective_Date,
    Closed_Date,
    Last_Disbursement_Date)
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s, %s, %s, %s,
                        %s, %s)"""
try:
    conn = pg.connect(user="postgres",
        password="",
        host="127.0.0.1",
        port="5432",
        database="consume")
    # print("i reach success.")
    cursor = conn.cursor()
    with open(file, 'r') as f:
        reader = csv.reader(f)
        print("i reach success.>>>>", reader)
        next(reader) # This skips the 1st row which is the header.
        # for record in reader:
        # cursor.execute(sql_insert, record)
        cursor.executemany(sql_insert, reader)
        # print("i reach success.>>>>", reader)
        conn.commit()
        print("Connection success.")
except (Exception, pg.Error) as e:
    print(e)
finally:
    if (conn):
        cursor.close()
        conn.close()
        print("Connection closed.")