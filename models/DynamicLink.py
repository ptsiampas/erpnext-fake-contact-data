import hashlib

from models.DatabaseStandard import DatabaseStandard


class DynamicLink(DatabaseStandard):
    def __init__(self, company_name, parent, parent_type, link_doc_type):
        """ Adds a link that connects company to the child document.
        :type link_doc_type: stuff
        """
        super().__init__(conn=None)
        self.parent = parent
        self.parentField = "links"
        self.parentType = parent_type
        self.linkTitle = 'Customer'
        self.linkDocType = link_doc_type
        self.linkName = company_name

    def insert_record(self):
        try:
            cursor = self.connection.cursor()
            sql = "insert into `tabDynamic Link` " \
                  "(" \
                  "name, creation,modified, modified_by, owner, parent, parentfield, " \
                  "parenttype, link_doctype, link_name, idx" \
                  ")" \
                  " VALUES " \
                  "(" \
                  "%(name)s, %(creation)s, %(modified)s, %(modified_by)s, %(owner)s, %(parent)s, %(parentfield)s, " \
                  "%(parenttype)s, %(link_doctype)s, %(link_name)s, %(idx)s" \
                  ")"
            data = {
                'name': hashlib.md5((self.parent + str(self.creation)).encode('utf-8')).hexdigest(),
                'creation': self.creation,
                'modified': self.modified,
                'modified_by': self.owner,
                'owner': self.owner,
                'parent': self.parent,
                'parentfield': self.parentField,
                'parenttype': self.parentType,
                'link_doctype': self.linkDocType,
                'link_name': self.linkName,
                'idx': 1
            }
            cursor.execute(sql, data)

            self.connection.commit()

        except Exception as e:
            print("FAILED DynamicLink: {}".format(str(e)))
