from model import authors
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
        print('Enter title, price, author_id, subscription_id')
        title = view.getVal()
        price = view.getInt()
        author_id = view.getInt()
        subscription_id = view.getInt()
        b.create(title, price, author_id, subscription_id)
    elif (table == 'readers'):
        print('Enter name, subscription_id')
        name = view.getVal()
        subscription_id = view.getInt()
        r.create(name, subscription_id)
    elif (table == 'subscriptions'):
        print('Enter price')
        price = view.getInt()
        ab.create(price)
    else:
        print('Invalid table name')

elif (command == 'read'):
    table = view.readTable()

    if (table == 'authors'):
        print('Enter id')
        id = view.getInt()
        au.read(id)
    elif (table == 'books'):
        print('Enter id')
        id = view.getInt()
        b.read(id)
    elif (table == 'readers'):
        print('Enter id')
        id = view.getInt()
        r.read(id)
    elif (table == 'subscriptions'):
        print('Enter id')
        id = view.getInt()
        ab.read(id)
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
        print('Enter id, new name, new subscription_id')
        id = view.getInt()
        name = view.getVal()
        read_count = view.getInt()
        subscription_id = view.getInt()
        r.update(id, name, read_count, subscription_id)
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

elif (command == 'generate'):

    table = view.readTable()

    if (table == 'authors'):
        print('Enter numeber to generate')
        gen_num = view.getInt()
        au.generate(gen_num)
    elif (table == 'books'):
        print('Enter numeber to generate')
        gen_num = view.getInt()
        b.generate(gen_num)
    elif (table == 'readers'):
        print('Enter numeber to generate')
        gen_num = view.getInt()
        r.generate(gen_num)
    elif (table == 'subscriptions'):
        print('Enter numeber to generate')
        gen_num = view.getInt()
        ab.generate(gen_num)
    else:
        print('Invalid table name')

elif (command == 'search'):
    print('Enter year, name')
    year = view.getInt()
    name = view.getVal()

    au.searchAuthorsBooks(name, year)

else:
    print('Invalid command')