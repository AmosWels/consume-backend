import psycopg2 as pg
import csv

file = r'../models/loans-historical-data.csv'
sql_insert = """INSERT INTO loans(
    id,
    end_of_period,
    loan_number,
    country_code,
    country,
    borrower,
    guarantor_country_code,
    guarantor,
    loan_status,
    currency_of_commitment,
    project_name,
    original_principal_amount,
    cancelled_amount,
    undisbursed_amount,
    disbursed_amount,
    due_to_ibrd,
    exchange_adjustment,
    borrower_obligation,
    sold_3rd_party,
    repaid_3rd_party,
    due_3rd_party,
    loans_held,
    first_repayment_date,
    last_repayment_date,
    agreement_signing_date,
    board_approval_date,
    effective_date,
    closed_date,
    last_disbursement_date,
    loan_type,
    region,
    interest_rate,
    project_id,
    repaid_to_ibrd)
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