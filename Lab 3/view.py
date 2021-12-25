class view:

    def __init__(self):
        print('Program started')

    def readCommand():
        com = input("Enter command (create, update, delete): ")
        return com

    def readTable():
        tab = input("Enter table name (authors, books, subscriptions, readers): ")
        if (tab == 'authors' or tab == 'books' or tab == 'subscriptions' or tab == 'readers'):
            return tab
        return ''

    def getVal():
        val = input("Enter string: ")
        return val

    def getInt():
        val = input("Enter integer: ")
        try:
            int(val)
        except ValueError:
            print(val + " is not integer")
            return 0
        return int(val)