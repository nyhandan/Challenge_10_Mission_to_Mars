#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Deliverable 2


# In[3]:


from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


# In[4]:


@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scraping.scrape_all()
    mars.update_one({}, {"$set":mars_data}, upsert=True)
    return redirect('/', code=302)


# In[5]:


app = Flask(__name__)


# In[6]:


# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


# In[7]:


@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)


# In[8]:


def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)
    # Run all scraping functions and store results in dictionary
    data = {
      "news_title": news_title,
      "news_paragraph": news_paragraph,
      "featured_image": featured_image(browser),
      "facts": mars_facts(),
      "last_modified": dt.datetime.now()
    }


# In[9]:


def mars_facts():
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('https://galaxyfacts-mars.com')[0]

    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html()


# In[10]:


def data_scrape():

    # 2. Create a list to hold the images and titles.
    hemisphere_image_urls = []

    # 3. Write code to retrieve the image urls and titles for each hemisphere.

    html = browser.html
    url_soup = soup(html, 'html.parser')

    links = url_soup.find_all('div', class_='item')

    url = 'https://marshemispheres.com/'

    for link in links:
        navigate = link.find('a')['href']

        browser.visit(url+navigate)



        hemisphere_pages = browser.html
        hemisphere_pages_soup = soup(hemisphere_pages, 'html.parser')

        title = hemisphere_pages_soup.find('h2', class_ = 'title').text
        image_url = hemisphere_pages_soup.find('img', class_ = 'wide-image')['src']    

        hemisphere_image_urls.append({"title": title, "img url": image_url})

    return hemisphere_image_urls


# In[9]:


# steps 4 through 8


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:


# Add try/except for error handling
try:
    slide_elem = news_soup.select_one('div.list_text')
    # Use the parent element to find the first 'a' tag and save it as 'news_title'
    news_title = slide_elem.find('div', class_='content_title').get_text()
    # Use the parent element to find the paragraph text
    news_p = slide_elem.find('div', class_='article_teaser_body').get_text()


# In[ ]:


except AttributeError:
        return None, None


# In[ ]:


def mars_news(browser):

    # Scrape Mars News
    # Visit the mars nasa news site
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    
    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find('div', class_='content_title').get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    except AttributeError:
        return None, None

    
    return news_title, news_p


# In[ ]:


try:
   # find the relative image url
   img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

except AttributeError:
    return None


# In[ ]:




