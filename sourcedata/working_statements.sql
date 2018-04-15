select name, email_id, customer_type
from tabCustomer;

select name, email_id from tabCustomer;
select name, email_id, address_line1, city, state, pincode, country from tabAddress;
select name, email_id, first_name, last_name, status, mobile_no, user, is_primary_contact from tabContact;
select parent, parentfield, parenttype, link_doctype, link_name from `tabDynamic Link`;

delete from tabCustomer
where name not like '%Dummy%';

delete from tabAddress
where name not like '%Dummy%';

delete from tabContact
where name not like '%Dummy%';

delete from `tabDynamic Link`
where link_name not like '%Dummy%';

select *
from tabCustomer;

select name, parent, parentfield, parenttype, link_doctype, link_name from `tabDynamic Link`;

select * from tabAddress;

SHOW columns FROM tabContact;

select *
from `tabDynamic Link`;
