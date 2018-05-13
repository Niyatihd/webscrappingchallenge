# webscrappingchallenge

I have built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines the steps that were used to accomplish the task.

Step1: Scrapping
    Initial scraping was done using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter to acquire 
    listed information.

    Task1: Latest News Title
    Website scrapped:
    ~ NASA Mars News Site
    https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest

    Task2: JPL Mars Space Images - Featured 
    Website scrapped:
    ~ JPL's Featured Space Image
    https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars

    Task3: Mars Weather
    Website scrapped:
    ~ Mars Weather
    https://twitter.com/marswxreport?lang=en

    Task4: Mars Facts
    Website scrapped:
    ~ Mars Facts webpage
    https://space-facts.com/mars/

    Task4: Mars Hemisperes
    Website scrapped:
    ~ USGS Astrogeology site 
    https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars

Step2: MongoDB and Flask Application
    Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

    Start by converting your Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.

    Next, create a route called /scrape that will import your scrape_mars.py script and call your scrape function.

    Store the return value in Mongo as a Python dictionary.

    Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.
    Create a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.




