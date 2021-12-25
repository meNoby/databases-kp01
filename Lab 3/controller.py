from model import authors, Trigger
from model import books
from model import readers
from model import subscriptions
from view import view

v = view()
au = authors()
b = books()
r = readers()
ab = subscriptions()

command = view.readCommand()

if (command == 'create'):

    table = view.readTable()

    if (table == 'authors'):
        print('Enter name, country')
        name = view.getVal()
        country = view.getVal()
        au.create(name, country)
    elif (table == 'books'):
        print('Enter title, year, author_id, subscription_id')
        title = view.getVal()
        price = view.getInt()
        author_id = view.getInt()
        subscription_id = view.getInt()
        b.create(title, price, author_id, subscription_id)

    elif (table == 'readers'):
        print('Enter username, subscription_id')
        username = view.getVal()
        subscription_id = view.getInt()
        r.create(username, subscription_id)
    elif (table == 'subscriptions'):
        print('Enter price')
        price = view.getInt()
        ab.create(price)
    else:
        print('Invalid table name')

elif (command == 'update'):

    table = view.readTable()

    if (table == 'authors'):
        print('Enter id, new name, new country')
        id = view.getInt()
        name = view.getVal()
        country = view.getVal()
        au.update(id, name, country)
    elif (table == 'books'):
        print('Enter id, new title, new year, new author_id, new subscription_id')
        id = view.getInt()
        title = view.getVal()
        year = view.getInt()
        author_id = view.getInt()
        subscription_id = view.getInt()
        b.update(id, title, year, author_id, subscription_id)
    elif (table == 'readers'):
        print('Enter id, new username, new subscription_id')
        id = view.getInt()
        username = view.getVal()
        subscription_id = view.getInt()
        r.update(id, username, subscription_id)
    elif (table == 'subscriptions'):
        print('Enter id, new price')
        id = view.getInt()
        price = view.getInt()
        ab.update(id, price)
    else:
        print('Invalid table name')

elif (command == 'delete'):

    table = view.readTable()

    if (table == 'authors'):
        print('Enter id')
        id = view.getInt()
        au.delete(id)
    elif (table == 'books'):
        print('Enter id')
        id = view.getInt()
        b.delete(id)
    elif (table == 'readers'):
        print('Enter id')
        id = view.getInt()
        r.delete(id)
    elif (table == 'subscriptions'):
        print('Enter id')
        id = view.getInt()
        ab.delete(id)
    else:
        print('Invalid table name')

else:
    print('Invalid command')