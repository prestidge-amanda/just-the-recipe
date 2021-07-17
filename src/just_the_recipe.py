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
    return html[tag_content_start:tag_content_end]
    
def get_ingredient_list(url):
    recipe_page = urlopen(url)
    html_bytes = recipe_page.read()
    html = html_bytes.decode("utf-8")
   # print(html)
    # title_index = html.find('<title>')
    # title_start = title_index + len('<title>')
    # title_end = html.find('</title>')
    # print(html[title_start:title_end])
    title_content = get_tag_content(html,'title')
    print(title_content)

url = get_url()
get_ingredient_list(url)