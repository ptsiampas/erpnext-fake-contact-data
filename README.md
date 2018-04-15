# erpnext-fake-contact-data

This is a quick and dirty project to create fake data within the erpnext CRM.  I haven't written to much, have a look at generate.py it has a function that will create the appropriate links etc for customers.  A lot of it is customisable, I created it this way because I didn't like the way the erpnext system's import fuctions work for such simple data.

This can be expanded to pull in customers data from a single csv file, but right now it just creates dummy faker data.

Make sure you set the `connection` string to suite your db.
