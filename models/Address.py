from models.DatabaseStandard import DatabaseStandard


class Address(DatabaseStandard):
    def __init__(self):
        super().__init__(conn=None)
        self.name = None
        self.email_id = None
        self.country = "Australia"
        self.addressLine1 = None
        self.addressLine2 = None
        self.suburb = None
        self.state = None
        self.postCode = None
        self.phone = None
        self.addressType = "Billing"
        self.isShipping = 1
        self.isPrimary = 1

    def insert_record(self):
        try:
            cursor = self.connection.cursor()
            sql = """ INSERT INTO `frappe`.`tabAddress`
                (`name`, `creation`, `modified`, `modified_by`, `owner`, `docstatus`, `parent`,
                `parentfield`, `parenttype`, `idx`, `email_id`, `pincode`, `county`,
                `is_your_company_address`, `address_line2`, `city`, `address_line1`, `_comments`,
                `is_primary_address`, `state`, `address_type`, `fax`, `_liked_by`, `address_title`,
                `_assign`, `phone`, `_user_tags`, `country`, `is_shipping_address`)
                VALUES
                (%(name)s, %(creation)s, %(modified)s, %(modified_by)s, %(owner)s, %(docstatus)s, %(parent)s,
                %(parentfield)s, %(parenttype)s, %(idx)s, %(email_id)s, %(pincode)s, %(county)s,
                %(is_your_company_address)s, %(address_line2)s, %(city)s, %(address_line1)s, %(_comments)s,
                %(is_primary_address)s, %(state)s, %(address_type)s, %(fax)s, %(_liked_by)s, %(address_title)s,
                %(_assign)s, %(phone)s, %(_user_tags)s, %(country)s, %(is_shipping_address)s); """

            data = {
                'name': self.name + '-' + self.addressType,
                'creation': self.creation,
                'modified': self.modified,
                'modified_by': self.modified_by,
                'owner': self.owner,
                'docstatus': self.docstatus,
                'parent': None,
                'parentfield': None,
                'parenttype': None,
                'idx': self.idx,
                'email_id': self.email_id,
                'pincode': self.postCode,
                'county': None,
                'is_your_company_address': 0,
                'address_line2': self.addressLine2,
                'city': self.suburb,
                'address_line1': self.addressLine1,
                '_comments': None,
                'is_primary_address': True,
                'state': self.state,
                'address_type': self.addressType,
                'fax': None,
                '_liked_by': None,
                'address_title': self.name + '-' + self.suburb,
                '_assign': None,
                'phone': self.phone,
                '_user_tags': None,
                'country': self.country,
                'is_shipping_address': True
            }
            cursor.execute(sql, data)
            self.connection.commit()

        except Exception as e:
            print('Address:' + str(e))
