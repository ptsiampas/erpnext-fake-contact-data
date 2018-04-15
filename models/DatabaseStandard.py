from datetime import datetime
import pymysql

class DatabaseStandard(object):
    def __init__(self, conn):
        self.creation = datetime.now()
        self.modified = datetime.now()
        self.modified_by = "Administrator"
        self.owner = "Administrator"
        self.docstatus = 0
        self.idx = 0
        self.connection = conn

    # Start of user code -> properties/constructors for DatabaseStandard class

    # End of user code
    def insert_record(self):
        # Start of user code protected zone for insertRecord function body
        raise NotImplementedError
        # End of user code
    # Start of user code -> methods for DatabaseStandard class

    # End of user code