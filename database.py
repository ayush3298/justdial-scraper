import sqlite3

conn = sqlite3.connect('business.sqlite')
cur = conn.cursor()

def create_database(city):
    query = """CREATE TABLE IF NOT EXISTS {} (
	name	TEXT UNIQUE,
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	phone_number	TEXT,
	address	TEXT,
	mode_of_payment	TEXT,
	rating	TEXT,
	web_url TEXT
);""".format(city)
    cur.execute(query)
    conn.commit()



def add_data_to_database(self):
    try:
        print('adding to db for ' + self.business_name)
        # print(self.mode_of_payment)
        cur.execute('INSERT INTO {}(name,phone_number,address,mode_of_payment,rating,web_url)VALUES (?,?,?,?,?,?)'.format(self.city),(self.business_name,self.phone_number,self.address,self.mode_of_payment,self.rating,self.web_url))
        # self.add_adress()
        conn.commit()
    except Exception as e:
        print(e)


def add_address(self):
    try:
        cur.execute('UPDATE {} set address = ? '.format(self.city),(self.address,))
    except Exception as e:
        print(e)






