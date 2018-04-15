import mysql.connector
from auspost_pac.pac import PAC
from faker import Faker

from models.Address import Address
from models.Contact import Contact
from models.Customer import Customer
from models.DynamicLink import DynamicLink

fake = Faker('en_AU')

API_KEY = '69470f91-3b90-464b-82bd-6938683ed7cd'
codesearch = PAC(API_KEY)

# Change this line to suite your environment.
connection = mysql.connector.connect(user='root', password='1234',
                                     host='127.0.0.1', port=3307,
                                     database='frappe')


def create_fake_names(no_to_create=1):
    for _ in range(no_to_create):
        company_name = fake.company()
        email_id = fake.email()
        phone = fake.phone_number()
        mobile = fake.numerify(text="04## ### ###")

        cust = Customer(company_name)
        cust.connection = connection
        cust.emailId = email_id
        cust.mobileNo = phone
        cust.insert_record()

        address = Address()
        address.connection = connection
        address.name = cust.name
        address.email_id = cust.emailId
        address.phone = fake.phone_number()
        address.addressLine1 = fake.numerify(text="###") + ' ' + fake.street_name() + ' ' + fake.street_suffix()
        address.suburb = fake.city()
        address.postCode = fake.postcode()
        address.state = fake.state()
        address.insert_record()

        link = DynamicLink(cust.name, address.name + '-' + address.addressType, 'Address', 'Customer')
        link.connection = connection
        link.insert_record()

        contact = Contact()
        contact.companyName = cust.name
        contact.connection = connection
        contact.firstName = fake.first_name()
        contact.lastName = fake.last_name()
        contact.phone = fake.phone_number()
        contact.mobile = mobile
        contact.emailID = fake.email()
        contact.insert_record()

        link = DynamicLink(cust.name, contact.firstName + '-' + contact.lastName + '-' + cust.name, 'Contact',
                           'Customer')
        link.connection = connection
        link.insert_record()

    connection.close()


create_fake_names(100)
