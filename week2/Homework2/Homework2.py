from selenium import webdriver
from bs4 import BeautifulSoup
from tqdm import tqdm
import pandas as pd


#Configuraiton of  webdirivers chrome options section:
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--log-level=3")
options.add_argument('headless=True')

driver = webdriver.Chrome(executable_path="week2\chromedriver.exe",
                            chrome_options=options)
driver.set_window_size(1920,1080)



def collect_news_link(page_number):
    collect_news_link=list()
    for number in tqdm(range(1,page_number+1),desc='Collecting Links'):
        url = f'https://www.webtekno.com/haber?s={number}'
        driver.get(url)
        links = driver.find_elements_by_xpath("//a[@href]")
        
        for link in (links):
            new_link = link.get_attribute("href")
            if not new_link in collect_news_link and new_link.endswith('html'):
                collect_news_link.append(link.get_attribute("href"))
    
    return (collect_news_link)


def create_data(link_lst):
    data_set = list()
    for link in link_lst:
        print(link)
        driver.get(link)
        bs = BeautifulSoup(driver.page_source,'html.parser')
        title = bs.find('h1',{'itemprop':'headline'}).text
        content =bs.find('div',{'class':"content-body__description"}).text
        emoloji_lst = dict()
        for emoloji in ['sad','angry','shy','laugh','amazing']:
            smile_item = bs.find('div',{'data-smile-type':emoloji})
            count = smile_item.find('span',{'class':'content-smile__count'}).text
            emoloji_lst[emoloji] = count
        data1={
                'Title':title,
                'Content':content,
                'Link' : link
            }
        data_set.append({**data1,**emoloji_lst})
    return data_set


news_link = collect_news_link(100)
dataset = create_data(news_link)


#create dataframe with pandas and export to CSV file
dataframe = pd.DataFrame(dataset)
dataframe.to_csv('week2/news_reactions_result.csv')

