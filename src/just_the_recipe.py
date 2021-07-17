from bs4 import BeautifulSoup
import re
from urllib.request import urlopen

def get_url():
    url = input('Enter url for recipe blog: ')
    print("Searching " + url + "...")
    # TO DO: add error handling for url type
    return url

def get_html(url):
    html=""
    BAD_PAGE_MESSAGE = 'Sorry we could not open this page.'
    BAD_CONTENT_MESSAGE = 'Sorry this page contains content we cannot parse.'
    TRY_AGAIN_MESSAGE =  'Try searching another website.'
    try:
        recipe_page = urlopen(url)
    except:
        print(BAD_PAGE_MESSAGE + TRY_AGAIN_MESSAGE)
        return html
    try:
        html_bytes = recipe_page.read()
    except:
        print(BAD_PAGE_MESSAGE + TRY_AGAIN_MESSAGE)
        return html
    try:
        html = html_bytes.decode("utf-8")
    except:
        print(BAD_CONTENT_MESSAGE + TRY_AGAIN_MESSAGE)
        return html
    return html

def get_tag_content(html,tag):
    start_tag="<"+tag+">"
    end_tag="</"+tag+">"
    tag_start = html.find(start_tag)
    tag_content_start = tag_start+len(start_tag)
    tag_content_end = html.find(end_tag)
    tag_content_raw = html[tag_content_start:tag_content_end]
    tag_content = re.sub("<.*>", "", tag_content_raw)
    return tag_content

def get_recipe_title(html):
    title_content = get_tag_content(html,'title')
    print(title_content)

def get_page_text(html):
    soup_html = BeautifulSoup(html, "html.parser")
    page_text = soup_html.get_text()
    return page_text

def get_ingredient_list(page_text):
    ingredients_start = page_text.find('Ingredients') # multiple or none case needs to be handled
    directions_start = page_text.find('Directions')
    if(directions_start == -1):
        directions_start= page_text.find('Steps')
    ingredients_content_raw =  page_text[ingredients_start:directions_start]
    ingredients_content =  re.sub("   *", "\n", ingredients_content_raw)
    print(ingredients_content)

def get_directions(page_text):
    directions_start= page_text.find('Directions')
    directions_text = page_text[directions_start:]
    comments_start = directions_text.find('Comments')
    reviews_start = directions_text.find('Reviews')
    if (comments_start != -1):
        directions_text = directions_text[:comments_start]
    elif (reviews_start != -1):
        directions_text = directions_text[:reviews_start]
    directions_content = re.sub("   *", "\n", directions_text)
    print(directions_content)

url = get_url()
html = get_html(url)
if(html != ""):
    get_recipe_title(html)
    page_text = get_page_text(html)
    get_ingredient_list(page_text)
    get_directions(page_text)