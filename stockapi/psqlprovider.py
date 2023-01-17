from stockapi.psqlhelper import close_connection
from psycopg2.extras import RealDictCursor
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash
from stockapi.user_model import user_model
from stockapi.config import Config


def add_user(user: user_model):
    try:
        conn = psycopg2.connect(
            host=Config.db_host,
            database=Config.db_database,
            user=Config.db_username,
            password=Config.db_password)

        # create a cursor
        cur = conn.cursor()
        hash_password = generate_password_hash(user['password'])
        cur.execute('CALL sp_add_new_user(%s, %s, %s, %s, %s)',
                    (hash_password, user['first_name'], user['last_name'], user['phone_number'], user['email']))

        # commit the transaction
        conn.commit()
        return "Success"
    except (Exception, psycopg2.DatabaseError) as error:

        return error;
    finally:
        close_connection(conn, cur)


def get_user(email_id):
    try:
        conn = psycopg2.connect(
            host=Config.db_host,
            database=Config.db_database,
            user=Config.db_username,
            password=Config.db_password)

        # create a cursor
        cur = conn.cursor(cursor_factory=RealDictCursor)
        sql = "SELECT u.user_id, u.email, u.fn ,u.ln, u.phone_no, r.role_id FROM users u  LEFT JOIN users_roles r ON u.user_id= r.user_id where email = '{0}'".format(
            email_id)

        cur.execute(sql)
        row = cur.fetchone()
        return row
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return "Failed"
    finally:
        close_connection(conn, cur)


def verify_user(email_id, password):
    try:
        conn = psycopg2.connect(
            host=Config.db_host,
            database=Config.db_database,
            user=Config.db_username,
            password=Config.db_password)

        # create a cursor
        cur = conn.cursor(cursor_factory=RealDictCursor)
        sql = "SELECT u.user_id, u.email, u.password, u.fn ,u.ln, u.phone_no, r.role_id FROM users u  LEFT JOIN users_roles r ON u.user_id= r.user_id where email = '{0}'".format(
            email_id)
        cur.execute(sql)
        row = cur.fetchone()
        if (check_password_hash(row['password'], password)):
            return row
        else:
            return None
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return "Failed"
    finally:
        close_connection(conn, cur)


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
            host=Config.db_host,
            database=Config.db_database,
            user=Config.db_username,
            password=Config.db_password)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        close_connection(conn, cur)
