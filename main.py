import requests
from bs4 import BeautifulSoup
from business_details import business

class scraper:
    def __init__(self,city,query):
        self.city = city
        self.query = query
        self.total_page_no = 0
        self.url = 'https://www.justdial.com/'
        self.s = requests.session()
        self.s.headers['User-Agent'] = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0"


    def scrap(self):
        self.query_url = self.url+self.city+'/'+self.query
        data = self.s.get(self.query_url)
        print('scraping')

        with open('data.html', 'w', encoding='UTF-8') as f:
            f.write(data.text)
        
        return data

    def extract_all_pages_url(self):
        dic = dict()
        data = self.scrap()
        dic[1] = data.url
        soup = BeautifulSoup(data.text,'lxml')
        li = soup.findAll('div',class_ = 'jpag')
        for s in li:
            linsks = s.findAll('a')
            #print(s)
            for link in linsks:
                page_no = link.text
                try:
                    page_no = int(page_no)
                    page_link = link['href']
                    dic[page_no] = page_link
                except:pass
        self.dic = dic

    def add_to_db(self,business_name,business_link):
        pass#TODO


    def extract_business_details(self,data):
        bsns = business(data,self.city,self.query)




    def extract_data(self,data):
        soup=BeautifulSoup(data,'lxml')
        business_links = soup.findAll('h2',class_='store-name')
        for business_link in business_links:
            business = business_link.findAll('a')[0]
            business_name=business.text
            business_link = business['href']
            business_details = self.s.get(business_link)
            self.extract_business_details(business_details)


    def get_page_data(self,url):
        try:
            page_data = self.s.get(url)
            if page_data.status_code == 200:
                self.extract_data(page_data.text)
                print(' extraction for page ' + str(url))
        except Exception as e:
            print(e)

    def get_list_of_business(self):
        if len(self.dic) != 0:
            for k, v in self.dic.items():
                self.get_page_data(url=v)
                print(' extraction for page ' + str(k))
        else:
            print('dic is empty')


if __name__ == '__main__':
    # city = input('Please enter your city. :')
    # query = input('please enter your query : ')
    c = scraper('neemuch','saree store')
    c.extract_all_pages_url()
    c.get_list_of_business()

