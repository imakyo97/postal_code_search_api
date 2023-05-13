import sqlite3
from typing import Optional
from functools import lru_cache


class PostalCodeRepository(object):
    def __init__(self):
        self.postal_codes = {}

    @lru_cache(maxsize=128)
    def fetch_address(self, code: str) -> Optional[str]:
        if code not in self.postal_codes:
            conn = sqlite3.connect("postal_code_db/postal_code.db")
            curs = conn.cursor()
            curs.execute('SELECT address FROM "postal_code" WHERE code = ?;', (code,))
            tuple_address = curs.fetchone()
            curs.close()
            conn.close()
            if tuple_address is None:
                return None
            (address,) = tuple_address
            self.postal_codes[code] = address
            return address
        return self.postal_codes[code]
