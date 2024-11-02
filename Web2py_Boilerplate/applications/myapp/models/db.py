# Database connection
if not request.env.web2py_runtime_gae:
    db = DAL('sqlite://storage.sqlite')  # use SQLite for local development
else:
    db = DAL('google:datastore')  # use Google App Engine for deployment

# Define a sample table
db.define_table('example',
                Field('name'),
                Field('description', 'text'))
