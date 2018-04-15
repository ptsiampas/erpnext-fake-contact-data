from models.DatabaseStandard import DatabaseStandard


class Customer(DatabaseStandard):
    def __init__(self, customer_name):
        super().__init__(conn=None)
        self.id = 0
        self.name = customer_name.replace('  ', '-').replace(' ', '-').upper().strip()
        self.emailId = None
        self.disabled = 0
        self.mobileNo = None
        self.parent = None
        self.parentfield = None
        self.parenttype = None
        self.customer_primary_contact = None
        self.customer_details = None
        self.defaultCurrency = "AUD"
        self.namingSeries = "CUST-"
        self.language = "en"
        self.customerGroup = 'Commercial'
        self.territory = 'All Territories'
        self.customerType = 'Company'
        self.isFrozen = 0

    def insert_record(self):
        try:
            cursor = self.connection.cursor()
            sql = """
            INSERT INTO `frappe`.`tabCustomer`
            (`name`, `creation`, `modified`, `modified_by`, `owner`, `docstatus`, `parent`,
            `parentfield`, `parenttype`, `idx`, `customer_primary_contact`, `customer_details`, `email_id`,
            `image`, `disabled`, `salutation`, `mobile_no`, `lead_name`,
            `bypass_credit_limit_check_at_sales_order`, `default_currency`, `_comments`,
            `default_sales_partner`, `default_price_list`, `payment_terms`, `naming_series`, `customer_name`,
            `website`, `_liked_by`, `default_commission_rate`, `_assign`, `_user_tags`, `tax_id`,
            `credit_limit`, `language`, `gender`, `customer_group`, `territory`, `customer_type`,
            `is_frozen`, `customer_pos_id`)
            VALUES
            (%(name)s, %(creation)s, %(modified)s, %(modified_by)s, %(owner)s, %(docstatus)s, %(parent)s,
            %(parentfield)s, %(parenttype)s, %(idx)s, %(customer_primary_contact)s, %(customer_details)s, %(email_id)s,
            %(image)s, %(disabled)s, %(salutation)s, %(mobile_no)s, %(lead_name)s,
            %(bypass_credit_limit_check_at_sales_order)s, %(default_currency)s, %(_comments)s,
            %(default_sales_partner)s, %(default_price_list)s, %(payment_terms)s, %(naming_series)s, %(customer_name)s,
            %(website)s, %(_liked_by)s, %(default_commission_rate)s, %(_assign)s, %(_user_tags)s, %(tax_id)s,
            %(credit_limit)s, %(language)s, %(gender)s, %(customer_group)s, %(territory)s, %(customer_type)s,
            %(is_frozen)s, %(customer_pos_id)s);

            """
            data = {
                'name': self.name,
                'creation': self.creation,
                'modified': self.modified,
                'modified_by': self.modified_by,
                'owner': self.owner,
                'docstatus': self.docstatus,
                'parent': self.parent,
                'parentfield': self.parentfield,
                'parenttype': self.parenttype,
                'idx': self.idx,
                'customer_primary_contact': self.customer_primary_contact,
                'customer_details': self.customer_details,
                'email_id': self.emailId,
                'image': None,
                'disabled': self.disabled,
                'salutation': None,
                'mobile_no': self.mobileNo,
                'lead_name': None,
                'bypass_credit_limit_check_at_sales_order': 0,
                'default_currency': self.defaultCurrency,
                '_comments': None,
                'default_sales_partner': None,
                'default_price_list': 'Standard Selling',
                'payment_terms': None,
                'naming_series': self.namingSeries,
                'customer_name': self.name,
                'website': None,
                '_liked_by': None,
                'default_commission_rate': 0.0,
                '_assign': None,
                '_user_tags': None,
                'tax_id': None,
                'credit_limit': 0.0,
                'language': self.language,
                'gender': None,
                'customer_group': self.customerGroup,
                'territory': self.territory,
                'customer_type': self.customerType,
                'is_frozen': self.isFrozen,
                'customer_pos_id': None
            }
            cursor.execute(sql, data)
            self.connection.commit()

        except Exception as e:
            print(e)
