import shelve
with shelve.open("scoreDB") as db:
    print(dict(db))