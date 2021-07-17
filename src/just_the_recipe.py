from bs4 import BeautifulSoup
import re
from urllib.request import urlopen

def get_url():
    url = input('Enter url for recipe blog: ')
    print("Searching " + url + "...")
    # TO DO: add error handling for url type
    return url

def get_tag_content(html,tag):
    start_tag="<"+tag+">"
    end_tag="</"+tag+">"
    tag_start = html.find(start_tag)
    tag_content_start = tag_start+len(start_tag)
    tag_content_end = html.find(end_tag)
    tag_content_raw = html[tag_content_start:tag_content_end]
    tag_content = re.sub("<.*>", "", tag_content_raw)
    return tag_content
    
def get_ingredient_list(url):
    recipe_page = urlopen(url)
    html_bytes = recipe_page.read()
    html = html_bytes.decode("utf-8")
    title_content = get_tag_content(html,'title')
    ingredients_start = html.find('Ingredients')
    directions_start = html.find('Directions')
    ingredients_content_raw =  html[ingredients_start:directions_start]
    #ingredients_content = re.sub("<.*>", "", ingredients_content_raw)
    print(ingredients_content_raw)

def get_ingredient_list_with_soup(url):
    recipe_page = urlopen(url)
    html_bytes = recipe_page.read()
    html = html_bytes.decode("utf-8")
    soup_html = BeautifulSoup(html, "html.parser")
    page_text = soup_html.get_text()
    ingredients_start = page_text.find('Ingredients')
    directions_start = page_text.find('Directions')
    ingredients_content_raw =  page_text[ingredients_start:directions_start]
    print(ingredients_content_raw)

url = get_url()
#get_ingredient_list(url)
get_ingredient_list_with_soup(url)