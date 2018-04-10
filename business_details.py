import requests
from bs4 import BeautifulSoup
from database import create_database,add_data_to_database,add_address

class business:
    def __init__(self,data,city):
        self.business_data = data
        self.city = city

        self.soup = BeautifulSoup(self.business_data.text, 'lxml')
        self.address = self.get_business_adrs()
        self.mode_of_payment = self.get_mod_of_payment()
        self.business_name = self.get_business_name()
        self.rating = self.get_rating()

        self.phone_number = ''
        self.web_url = data.url
        self.total_votes = self.get_vote()
        # self.service_aminities()

        create_database(self.city)
        add_data_to_database(self)




    def get_business_adrs(self):
        # soup = BeautifulSoup(self.business_data.text, 'lxml')
        detail = self.soup.findAll('span', class_='adrstxtr')
        for d in detail:
            data = str(d.text).replace('(Map)','').replace('\n',' ')
            # print(data)
            return data

    def get_business_name(self):
        detail = self.soup.findAll('span', class_='fn')
        for d in detail:
            data = str(d.text)

            return (data)

    def get_vote(self):
        detail = self.soup.findAll('span', class_='votes')
        for d in detail:
            data = str(d.text)

            return (data)

    def get_rating(self):
        detail = self.soup.findAll('span', class_='value-title')
        for d in detail:
            data = str(d['title'])
            # print(data)
            return (data)



    def get_mod_of_payment(self):
        detail = self.soup.findAll('span', class_='lng_mdpay')
        li = list()
        for d in detail:
            # data = d.finadAll('ul')
            li.append(d.text)
        data = ','.join(li)
        print(data)
        return data
        # print('='*25)
