# Import dependencies
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt



# Define scraping function
def scrape():

    # Part 1.1 NASA Mars News Scraping
    # Driver is headless to avoid windows popping up
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    # Visit website
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    # Convert browser html to a soup object
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    lists = soup.select_one('div.list_text')

    content_title = lists.find(class_ = 'content_title').text
    teaser = lists.find(class_ = 'article_teaser_body').text

    # Quit first browser
    browser.quit()

    # ---------------------------------------------------------------------------------------------

    # Part 1.2 JPL Mars Featured Image Scraping
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    # Visit website
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url)

    # Code for clicking the image
    full_image = browser.find_by_tag('button')[1]
    full_image.click()

    # Parse resulting html to a soup object
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    fancy_box = soup.select_one('div.fancybox-inner')
    featured_image = fancy_box.find(class_ = 'fancybox-image')
    featured_image_url = featured_image['src']

    # Quit second browser
    browser.quit()

    # ---------------------------------------------------------------------------------------------

    # Part 1.3 Mars Facts Scraping
    # executable_path = {'executable_path': ChromeDriverManager().install()}
    # browser = Browser('chrome', **executable_path, headless=True)

    # Visit website
    url = 'https://space-facts.com/mars/'
    # browser.visit(url)

    fact_table = pd.read_html(url)
    fact_table

    df = fact_table[2].rename(columns={0:"",1: "Mars"})

    df.set_index("", inplace=True)

    html_fact_table = df.to_html(classes="table table-striped")
    # Here used with 'classes' as argument, and then given bootstrap classes, which will give you the striped table format
    # Classes are modified
    
    # Quit third browser
    # browser.quit()

    # ---------------------------------------------------------------------------------------------

    # Part 1.4 Mars Hemispheres Scraping
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    # Cerberus
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url)


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # -----

    meta_section = soup.select_one('section.block')

    hem_cerb_title = meta_section.find('h2', class_ = 'title').text
    hem_cerb_title1 = hem_cerb_title.replace('Enhanced','')
    # print(hem_cerb_title1)

    # -----

    downloads_cerb = soup.select_one('div.downloads')

    original_download_cerb = downloads_cerb.find('a')
    original_download_url_cerb = original_download_cerb['href']
    # print(original_download_url_cerb)


    # Cerberus dictionary
    cerb_dict = {"title": hem_cerb_title1,"img_url": original_download_url_cerb}
    # cerb_dict

    browser.quit()

    # *******************************

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    # Schiaparelli
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(url)


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # -----

    meta_section = soup.select_one('section.block')

    hem_schiap_title = meta_section.find('h2', class_ = 'title').text
    hem_schiap_title1 = hem_schiap_title.replace('Enhanced','')
    # print(hem_schiap_title1)

    # -----

    downloads_schiap = soup.select_one('div.downloads')

    original_download_schiap = downloads_schiap.find('a')
    original_download_url_schiap = original_download_schiap['href']
    # print(original_download_url_schiap)


    # Sciaparelli dictionary
    schiap_dict = {"title": hem_schiap_title1,"img_url": original_download_url_schiap}
    # schiap_dict

    browser.quit()

    # *******************************

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    # Syrtis Major
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(url)


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # -----

    meta_section = soup.select_one('section.block')

    hem_syrtis_title = meta_section.find('h2', class_ = 'title').text
    hem_syrtis_title1 = hem_syrtis_title.replace('Enhanced','')
    # print(hem_syrtis_title1)

    # -----

    downloads_syrtis = soup.select_one('div.downloads')

    original_download_syrtis = downloads_syrtis.find('a')
    original_download_url_syrtis = original_download_syrtis['href']
    # print(original_download_url_syrtis)


    # Syrtis Major dictionary
    syrtis_dict = {"title": hem_syrtis_title1,"img_url": original_download_url_syrtis}
    # syrtis_dict

    browser.quit()

    # *******************************

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    # Valles Marineris
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(url)


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # -----

    meta_section = soup.select_one('section.block')

    hem_valles_title = meta_section.find('h2', class_ = 'title').text
    hem_valles_title1 = hem_valles_title.replace('Enhanced','')
    # print(hem_valles_title1)

    # -----

    downloads_valles = soup.select_one('div.downloads')

    original_download_valles = downloads_valles.find('a')
    original_download_url_valles = original_download_valles['href']
    # print(original_download_url_valles)


    # Valles Marineris dictionary
    valles_dict = {"title": hem_valles_title1,"img_url": original_download_url_valles}
    # valles_dict

    browser.quit()

    # *******************************

    # Append all dictionaries to a list
    hemisphere_image_urls = []

    hemisphere_image_urls.append(cerb_dict.copy())
    hemisphere_image_urls.append(schiap_dict.copy())
    hemisphere_image_urls.append(syrtis_dict.copy())
    hemisphere_image_urls.append(valles_dict.copy())

    # ---------------------------------------------------------------------------------------------


    # content_title,teaser = mars_news(browser)

    # Run all scraping functions and store in dictionary
    data = {
        "content_title": content_title,
        "teaser": teaser,
        "featured_image_url": featured_image_url,
        "mars_facts": html_fact_table,
        "hemispheres": hemisphere_image_urls,
        "last modified": dt.datetime.now()
    }

    # # Stop web-driver and return data
    # browser.quit()
    
    # Return results
    return data



# # Part 1.1 NASA Mars News Scraping
# # Mars news browser
# def mars_news(browser):

#     # Scrape mars news
#     # Visit website
#     url = 'https://mars.nasa.gov/news/'
#     browser.visit(url)

#     # Convert browser html to a soup object
#     html = browser.html
#     soup = BeautifulSoup(html, 'html.parser')

#     lists = soup.select_one('div.list_text')

#     content_title = lists.find(class_ = 'content_title').text
#     teaser = lists.find(class_ = 'article_teaser_body').text

#     return content_title, teaser


# # Part 1.2 JPL Mars Featured Image Scraping
# def featured_image(browser):
#     # executable_path = {'executable_path': ChromeDriverManager().install()}
#     # browser = Browser('chrome', **executable_path, headless=True)

#     # Visit website
#     url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
#     browser.visit(url)

#     # Code for clicking the image
#     full_image = browser.find_by_tag('button')[1]
#     full_image.click()

#     # Parse resulting html to a soup object
#     html = browser.html
#     soup = BeautifulSoup(html, 'html.parser')

#     fancy_box = soup.select_one('div.fancybox-inner')
#     featured_image = fancy_box.find(class_ = 'fancybox-image')
#     featured_image_url = featured_image['src']

#     return featured_image_url


# # Part 1.3 Mars Facts Scraping
# def mars_facts():

#     url = 'https://space-facts.com/mars/'
#     # browser.visit(url)

#     fact_table = pd.read_html(url)
#     fact_table

#     df = fact_table[2]

#     # df.columns = []
#     # df.head()

#     df.set_index(0, inplace=True)
#     df

#     html_fact_table = df.to_html()
#     return html_fact_table


# # Part 1.4 Mars Hemispheres Scraping
# def hemispheres(browser):
#     # executable_path = {'executable_path': ChromeDriverManager().install()}
#     # browser = Browser('chrome', **executable_path, headless=True)

#     # Cerberus
#     url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
#     browser.visit(url)

#     html = browser.html
#     soup = BeautifulSoup(html, 'html.parser')

#     # -----

#     meta_section = soup.select_one('section.block')

#     hem_cerb_title = meta_section.find('h2', class_ = 'title').text
#     hem_cerb_title1 = hem_cerb_title.replace('Enhanced','')
#     # print(hem_cerb_title1)

#     # -----

#     downloads_cerb = soup.select_one('div.downloads')

#     original_download_cerb = downloads_cerb.find('a')
#     original_download_url_cerb = original_download_cerb['href']
#     # print(original_download_url_cerb)


#     # Cerberus dictionary
#     cerb_dict = {"title": hem_cerb_title1,"img_url": original_download_url_cerb}
#     # cerb_dict


#     # executable_path = {'executable_path': ChromeDriverManager().install()}
#     # browser = Browser('chrome', **executable_path, headless=True)


#     # Schiaparelli
#     url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
#     browser.visit(url)


#     html = browser.html
#     soup = BeautifulSoup(html, 'html.parser')

#     # -----

#     meta_section = soup.select_one('section.block')

#     hem_schiap_title = meta_section.find('h2', class_ = 'title').text
#     hem_schiap_title1 = hem_schiap_title.replace('Enhanced','')
#     # print(hem_schiap_title1)

#     # -----

#     downloads_schiap = soup.select_one('div.downloads')

#     original_download_schiap = downloads_schiap.find('a')
#     original_download_url_schiap = original_download_schiap['href']
#     # print(original_download_url_schiap)


#     # Sciaparelli dictionary
#     schiap_dict = {"title": hem_schiap_title1,"img_url": original_download_url_schiap}
#     # schiap_dict


#     # executable_path = {'executable_path': ChromeDriverManager().install()}
#     # browser = Browser('chrome', **executable_path, headless=True)


#     # Syrtis Major
#     url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
#     browser.visit(url)


#     html = browser.html
#     soup = BeautifulSoup(html, 'html.parser')

#     # -----

#     meta_section = soup.select_one('section.block')

#     hem_syrtis_title = meta_section.find('h2', class_ = 'title').text
#     hem_syrtis_title1 = hem_syrtis_title.replace('Enhanced','')
#     # print(hem_syrtis_title1)

#     # -----

#     downloads_syrtis = soup.select_one('div.downloads')

#     original_download_syrtis = downloads_syrtis.find('a')
#     original_download_url_syrtis = original_download_syrtis['href']
#     # print(original_download_url_syrtis)



#     # Syrtis Major dictionary
#     syrtis_dict = {"title": hem_syrtis_title1,"img_url": original_download_url_syrtis}
#     # syrtis_dict



#     # executable_path = {'executable_path': ChromeDriverManager().install()}
#     # browser = Browser('chrome', **executable_path, headless=True)


#     # Valles Marineris
#     url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
#     browser.visit(url)


#     html = browser.html
#     soup = BeautifulSoup(html, 'html.parser')

#     # -----

#     meta_section = soup.select_one('section.block')

#     hem_valles_title = meta_section.find('h2', class_ = 'title').text
#     hem_valles_title1 = hem_valles_title.replace('Enhanced','')
#     # print(hem_valles_title1)

#     # -----

#     downloads_valles = soup.select_one('div.downloads')

#     original_download_valles = downloads_valles.find('a')
#     original_download_url_valles = original_download_valles['href']
#     # print(original_download_url_valles)



#     # Valles Marineris dictionary
#     valles_dict = {"title": hem_valles_title1,"img_url": original_download_url_valles}
#     # valles_dict



    # # Append all dictionaries to a list
    # hemisphere_image_urls = []

    # hemisphere_image_urls.append(cerb_dict.copy())
    # hemisphere_image_urls.append(schiap_dict.copy())
    # hemisphere_image_urls.append(syrtis_dict.copy())
    # hemisphere_image_urls.append(valles_dict.copy())

    # return hemisphere_image_urls


# if __name__ == "__main__":
#     print(scrape())