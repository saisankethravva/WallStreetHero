def close_connection(conn, cur):
    if cur is not None:
        cur.close()
        print('Cursor closed')
    if conn is not None:
        conn.close()
        print('Database connection closed.')
