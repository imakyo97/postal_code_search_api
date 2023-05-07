import sqlite3


class PostalCodeRepository(object):

    def fetch_address(self, code: str) -> str:
        conn = sqlite3.connect('postal_code_db/postal_code.db')
        curs = conn.cursor()
        curs.execute(
            'SELECT address FROM "postal_code" WHERE code = ?;',
            (code,)
        )
        address = curs.fetchone()
        curs.close()
        conn.close()
        return address
