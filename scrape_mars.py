
# coding: utf-8

# In[121]:
#Dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
from pprint import pprint

def scrape():
    # In[18]:
    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

    # In[19]:
    # Retrieve page with the requests module
    response = requests.get(url)

    # In[20]:
    # Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(response.text, "html.parser")

    # In[21]:
    # Examine the results, then determine element that contains sought info
    # print(soup.prettify())

    # In[22]:
    #save new title in a variable
    # news_title = soup.title.text

    # In[23]:
    soup.body.p.text

    # ## Use Splinter to navigate the site for required url(s)

    # In[24]:
    # https://splinter.readthedocs.io/en/latest/drivers/chrome.html
    # get_ipython().system('which chromedriver')

    # In[25]:
    #Use splinter to navigate the site and find the image url for the current Featured Mars Image 
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    # ## JPL Mars Space Images - Featured Image

    # In[26]:
    #Visit the url for JPL's Featured Space Image here.
    url_img = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_img)

    # In[27]:
    #Use beautiful soup to parse the html and get featured mars image
    html = browser.html
    soup = bs(html, 'html.parser')
    current_img_link = soup.find_all('article', class_="carousel_item")
    current_img_link

    # In[28]:
    #extract the url of background-image 
    current_img = current_img_link[0]['style']
    # print(current_img.find("('"))
    # print(current_img.find("')"))

    # In[29]:
    current_img_url = current_img[current_img.find("('")+len("('"):current_img.find("')")]
    # current_img_url

    # In[30]:
    #Save current featured image of mars in var featured_img_url
    featured_img_url = "https://www.jpl.nasa.gov" + current_img_url
    # featured_img_url

    # ## Mars Weather

    # In[36]:
    # URL of page with latest Mars weather tweet to be scraped
    url_weather = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url_weather)

    # In[47]:
    #Use beautiful soup to parse the html and get latest mars weather tweet
    html = browser.html
    soup = bs(html, 'html.parser')
    current_weather_info = soup.find_all('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
    # current_weather_info

    # In[48]:
    #Save latest weather info in var mars_weather
    mars_weather = current_weather_info[0].text
    # mars_weather

    # ## Mars Facts

    # In[49]:
    # URL of page with Mars facts to be scraped
    url_mars_facts = "https://space-facts.com/mars/"
    browser.visit(url_mars_facts)

    # In[54]:
    #Use the read_html function in Pandas to automatically scrape tabular data of mars facts from the page.
    table = pd.read_html(url_mars_facts)
    # table[0]

    # In[57]:
    #Create a df from table extracted from webpage
    df = table[0]
    df.columns = ['Parameter', 'Values']
    # df.head()

    # In[58]:
    #Clean the df
    df.set_index('Parameter', inplace=True)
    # df.head()

    # In[59]:
    #Generate html table from df
    html_table_marsfacts = df.to_html()
    # html_table_marsfacts

    # In[60]:
    #Strip unwanted newlines to clean up the table.
    html_table_marsfacts = html_table_marsfacts.replace('\n', '')

    # In[118]:
    #Save the table directly to a file.
    df.to_html('resources/html_table_marsfacts.html')

    # In[63]:
    # OSX Users can run this to open the file in a browser, 
    # or you can manually find the file and open it in the browser
    # get_ipython().system('open resources/html_table_marsfacts.html')

    # ## Mars Hemispheres

    # In[66]:
    # URL of page with Mars hemisphere high resolution images to be scraped
    url_hemispheres = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url_hemispheres)

    # In[68]:
    #Use beautiful soup to parse the html and get urls for all the images
    html = browser.html
    soup = bs(html, 'html.parser')
    url_hemispheres_link = soup.find_all('a', class_="itemLink product-item")
    # url_hemispheres_link

    # In[87]:
    #extract all webpages for high resolution images and store in a list
    hemisphere_img_pages = []
    for link in url_hemispheres_link:
        himg = "https://astrogeology.usgs.gov" + link['href']
        if himg not in hemisphere_img_pages:
            hemisphere_img_pages.append(himg)

    # In[110]:
    # hemisphere_img_pages

    # In[115]:
    hemisphere_image_urls = []
    for page in hemisphere_img_pages:
        temp_dict = {}
        # Create a loop to go through all the image pages and extract img link and title and store in a dictionary 
        url_hemis_img = page
        browser.visit(url_hemis_img)
        
        #Use beautiful soup to parse the webpage html and get image link and title
        html = browser.html
        soup = bs(html, 'html.parser')
        hemis_img_info = soup.find_all('div', class_="downloads")
        title = soup.title.text
        title = title[:title.find("|")-1]
        img_url = hemis_img_info[0].li.a['href']
        
        temp_dict['title'] = title
        temp_dict['img_url'] = img_url
        
        hemisphere_image_urls.append(temp_dict)

    # In[116]:
    # hemisphere_image_urls
    # ## Create one Python dictionary containing all of the scraped data.
    
    # In[119]:
    all_mars_data = {'mars_featured_image':featured_img_url, 'mars_weather':mars_weather,
                    'mars_facts':html_table_marsfacts, 'mars_hemispheres_imgs':hemisphere_image_urls}

    # In[122]:
    return all_mars_data



