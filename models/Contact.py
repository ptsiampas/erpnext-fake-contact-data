from models.DatabaseStandard import DatabaseStandard


class Contact(DatabaseStandard):
    def __init__(self):
        super().__init__(conn=None)
        self.companyName = None
        self.emailID = None
        self.firstName = None
        self.lastName = None
        self.status = None
        self.phone = None
        self.mobile = None
        self.user = None
        self.isPrimary = False

    def insert_record(self):
        try:
            cursor = self.connection.cursor()
            sql = """ INSERT INTO tabContact
                    (`name`, `creation`, `modified`, `modified_by`, `owner`, `docstatus`, `parent`,
                    `parentfield`, `parenttype`, `idx`, `last_name`, `email_id`, `image`, `mobile_no`,
                    `salutation`, `first_name`, `_user_tags`, `unsubscribed`, `department`, `status`,
                    `_liked_by`, `_assign`, `phone`, `user`, `_comments`, `designation`, `gender`,
                    `is_primary_contact`)
                    VALUES
                    (%(name)s, %(creation)s, %(modified)s, %(modified_by)s, %(owner)s, %(docstatus)s, %(parent)s,
                    %(parentfield)s, %(parenttype)s, %(idx)s, %(last_name)s, %(email_id)s, %(image)s, %(mobile_no)s,
                    %(salutation)s, %(first_name)s, %(_user_tags)s, %(unsubscribed)s, %(department)s, %(status)s,
                    %(_liked_by)s, %(_assign)s, %(phone)s, %(user)s, %(_comments)s, %(designation)s, %(gender)s,
                    %(is_primary_contact)s)
            """

            data = {
                'name': '{}-{}-{}'.format(self.firstName, self.lastName, self.companyName),
                'creation': self.creation,
                'modified': self.modified,
                'modified_by': self.modified_by,
                'owner': self.owner,
                'docstatus': 0,
                'parent': None,
                'parentfield': None,
                'parenttype': None,
                'idx': 0,
                'last_name': self.lastName,
                'email_id': self.emailID,
                'image': None,
                'mobile_no': self.mobile,
                'salutation': None,
                'first_name': self.firstName,
                '_user_tags': None,
                'unsubscribed': 0,
                'department': None,
                'status': 'Passive',
                '_liked_by': None,
                '_assign': None,
                'phone': self.phone,
                'user': None,
                '_comments': None,
                'designation': None,
                'gender': None,
                'is_primary_contact': 1
            }
            cursor.execute(sql, data)
            self.connection.commit()

        except Exception as e:
            print('Contact:' + str(e))
