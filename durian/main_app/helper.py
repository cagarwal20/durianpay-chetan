import requests as req
from bs4 import BeautifulSoup
from .models import Product
import re
from .serializers import ProductPostSerializer
# walmart_url = "https://www.walmart.com/search?q={}&sort={}".format()
# nykaa_url = "https://www.nykaa.com/search/result/?q={}&root=search&searchType=Manual&sourcepage=home&sort={}".format()
# meesho_url = "https://www.meesho.com/search?q={}&searchType=manual&searchIdentifier=text_search&Sort[sort_by]=price&Sort[sort_order]=asc".format()
# myntra_url = "https://www.myntra.com/{}?sort=price_asc".format()

def create_soup_page(url):
    webpage = req.get(url)
    webpage_text = webpage.text
    soup = BeautifulSoup(webpage_text, "html.parser")
    return soup


def flipkart_scrape(search):
    """returns the item price for a sainsburys product"""
    soup = create_soup_page("https://www.flipkart.com/search?q={}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&sort={}".format(search,"price_desc"))
    
    title = soup.find("a", class_="IRpwTa").getText()
    brand = soup.find("div",class_="_2WkVRV").getText()
    price = soup.find("div",class_="_30jeq3").getText()
    price_digits = re.sub("[^0-9]", "", price)
    prod_data = Product.objects.create(
        website = "www.flipkart.com",
        url = "https://www.flipkart.com/search?q={}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&sort={}".format(search,"price_desc"),
        title = brand + " " + title,
        price = int(price_digits)
    )
    ser_data = ProductPostSerializer(data=prod_data)
    if ser_data.is_valid():
        ser_data.save()
    soup = create_soup_page("https://www.flipkart.com/search?q={}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&sort={}".format(search,"price_asc"))
    
    title = soup.find("a", class_="IRpwTa").getText()
    brand = soup.find("div",class_="_2WkVRV").getText()
    price = soup.find("div",class_="_30jeq3").getText()
    price_digits = re.sub("[^0-9]", "", price)
    prod_data = Product.objects.create(
        website = "www.flipkart.com",
        url = "https://www.flipkart.com/search?q={}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&sort={}".format(search,"price_asc"),
        title = brand + " " + title,
        price = int(price_digits)
    )
    ser_data = ProductPostSerializer(data=prod_data)
    if ser_data.is_valid():
        ser_data.save()
    
    return True


# def walmart_scrape(search):

#     """returns the item price for a sainsburys product"""
#     soup = create_soup_page("https://www.walmart.com/search?q={}&sort={}".format(search,"price_low"))
    
#     #title = soup.find("span", class_="normal dark-gray mb0 mt1 lh-title f6 f5-l lh-copy").getText()
#     brand = soup.find("div",class_="b f6 black mr1 mt2 mb1 lh-copy").getText()
#     price = soup.find("div",class_="mr1 mr2-xl b black lh-copy f5 f4-l").getText()
#     price_digits = re.sub("[^0-9]", "", price)
#     prod_data = Product.objects.create(
#         website = "www.walmart.com",
#         url = "https://www.walmart.com/search?q={}&sort={}".format(search,"price_low"),
#         title = brand + " " + title,
#         price = int(price_digits)*85
#     )
#     ser_data = ProductPostSerializer(data=prod_data)
#     if ser_data.is_valid():
#         ser_data.save()
#     soup = create_soup_page("https://www.walmart.com/search?q={}&sort={}".format(search,"price_high"))
    
#     title = soup.find("span", class_="normal dark-gray mb0 mt1 lh-title f6 f5-l lh-copy").getText()
#     brand = soup.find("div",class_="b f6 black mr1 mt2 mb1 lh-copy").getText()
#     price = soup.find("div",class_="mr1 mr2-xl b black lh-copy f5 f4-l").getText()
#     price_digits = re.sub("[^0-9]", "", price)
#     prod_data = Product.objects.create(
#         website = "www.walmart.com",
#         url = "https://www.walmart.com/search?q={}&sort={}".format(search,"price_high"),
#         title = brand + " " + title,
#         price = int(price_digits)*85
#     )
#     ser_data = ProductPostSerializer(data=prod_data)
#     if ser_data.is_valid():
#         ser_data.save()
#     return True

def snapdeal_scrape(search):

    """returns the item price for a sainsburys product"""
    soup = create_soup_page("https://www.snapdeal.com/search?keyword={}&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort={}".format(search,"plth"))
    
    title = soup.find("p", class_="product-title").getText()
    # brand = soup.find("div",class_="b f6 black mr1 mt2 mb1 lh-copy").getText()
    price = soup.find("span",class_="product-price").getText()
    price_digits = re.sub("[^0-9]", "", price)
    prod_data = Product.objects.create(
        website = "www.snapdeal.com",
        url = "https://www.snapdeal.com/search?keyword={}&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort={}".format(search,"plth"),
        title = title + " " + title,
        price = int(price_digits)
    )
    ser_data = ProductPostSerializer(data=prod_data)
    if ser_data.is_valid():
        ser_data.save()
    soup = create_soup_page("https://www.snapdeal.com/search?keyword={}&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort={}".format(search,"phtl"))
    
    title = soup.find("p", class_="product-title").getText()
    # brand = soup.find("div",class_="b f6 black mr1 mt2 mb1 lh-copy").getText()
    price = soup.find("span",class_="product-price").getText()
    price_digits = re.sub("[^0-9]", "", price)
    prod_data = Product.objects.create(
        website = "www.snapdeal.com",
        url = "https://www.snapdeal.com/search?keyword={}&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort={}".format(search,"phtl"),
        title = title + " " + title,
        price = int(price_digits)
    )
    ser_data = ProductPostSerializer(data=prod_data)
    if ser_data.is_valid():
        ser_data.save()

def paytmmall_scrape(search):

    """returns the item price for a sainsburys product"""
    soup = create_soup_page("https://paytmmall.com/shop/search?q={}&from=organic&child_site_id=6&site_id=2&sort_price=0&page=1".format(search))
    title = soup.find("div", class_="UGUy").getText()
    try:
        brand = soup.find("div",class_="_3s55").getText()
    except:
        brand=""
    price = soup.find("div",class_="_1kMS").getText()
    price_digits = re.sub("[^0-9]", "", price)
    prod_data = Product.objects.create(
        website = "www.paytmmall.com",
        url = "https://paytmmall.com/shop/search?q={}&from=organic&child_site_id=6&site_id=2&sort_price=0&page=1".format(search),
        
        price = int(price_digits)
    )
    ser_data = ProductPostSerializer(data=prod_data)
    if ser_data.is_valid():
        ser_data.save()
    soup = create_soup_page("https://paytmmall.com/shop/search?q={}&from=organic&child_site_id=6&site_id=2&sort_price=1&page=1".format(search))
    
    title = soup.find("div", class_="UGUy").getText()
    try:
        brand = soup.find("div",class_="_3s55").getText()
    except:
        brand=""
    price = soup.find("div",class_="_1kMS").getText()
    price_digits = re.sub("[^0-9]", "", price)
    prod_data = Product.objects.create(
        website = "www.paytmmall.com",
        url = "https://paytmmall.com/shop/search?q={}&from=organic&child_site_id=6&site_id=2&sort_price=1&page=1".format(search),
        title = brand + " " + title,
        price = int(price_digits)
    )
    ser_data = ProductPostSerializer(data=prod_data)
    if ser_data.is_valid():
        ser_data.save()

    return True

def nykaa_scrape(search):

    """returns the item price for a sainsburys product"""
    soup = create_soup_page("https://www.nykaa.com/search/result/?q={}&root=search&searchType=Manual&sourcepage=home&sort=price_asc".format(search))
    
    title = soup.find("div", class_="css-1rd7vky").getText()
    # brand = soup.find("div",class_="_3s55").getText()
    price = soup.find("span",class_="css-111z9ua").getText()
    price_digits = re.sub("[^0-9]", "", price)
    prod_data = Product.objects.create(
        website = "www.nykaa.com",
        url = "https://www.nykaa.com/search/result/?q={}&root=search&searchType=Manual&sourcepage=home&sort=price_asc".format(search),
        title = title + " " + title,
        price = int(price_digits)
    )
    ser_data = ProductPostSerializer(data=prod_data)
    if ser_data.is_valid():
        ser_data.save()
    
    """returns the item price for a sainsburys product"""
    soup = create_soup_page("https://www.nykaa.com/search/result/?q={}&root=search&searchType=Manual&sourcepage=home&sort=price_desc".format(search))
    
    title = soup.find("div", class_="css-1rd7vky").getText()
    # brand = soup.find("div",class_="_3s55").getText()
    price = soup.find("span",class_="css-111z9ua").getText()
    price_digits = re.sub("[^0-9]", "", price)
    prod_data = Product.objects.create(
        website = "www.nykaa.com",
        url = "https://www.nykaa.com/search/result/?q={}&root=search&searchType=Manual&sourcepage=home&sort=price_desc".format(search),
        title = title + " " + title,
        price = int(price_digits)
    )
    ser_data = ProductPostSerializer(data=prod_data)
    if ser_data.is_valid():
        ser_data.save()
    return True

def westside_scrape(search):

    """returns the item price for a sainsburys product"""
    
    soup = create_soup_page("https://www.westside.com/pages/search?attributeFacetValuesLimit=20&currency=USD&inStock[]=true&inStock[]=false&page=1&productsCount=24&q={}&searchedKey=VU05NGUza2pzYkFYR1ZXdXpOMFd2Ull3MFJxM0FmT0J0a25vMndqZW5Bdz0%3D&sort_field[]=sellingPrice&sort_order[]=asc".format(search))
    try:
        title = soup.find("p", class_="product-item-title").getText()
    except:
        title = ""
    try:
        price = soup.find("div",class_="wizzy-product-item-price  ").getText()
    except:
        price = "-1"
    price_digits = re.sub("[^0-9]", "", price)
    prod_data = Product.objects.create(
        website = "www.westside.com",
        url = "https://www.westside.com/pages/search?attributeFacetValuesLimit=20&currency=USD&inStock[]=true&inStock[]=false&page=1&productsCount=24&q={}&searchedKey=VU05NGUza2pzYkFYR1ZXdXpOMFd2Ull3MFJxM0FmT0J0a25vMndqZW5Bdz0%3D&sort_field[]=sellingPrice&sort_order[]=asc".format(search),
        title = title + " " + title,
        price = int(price_digits)
    )
    ser_data = ProductPostSerializer(data=prod_data)
    if ser_data.is_valid():
        ser_data.save()
    
    """returns the item price for a sainsburys product"""
    soup = create_soup_page("https://www.westside.com/pages/search?attributeFacetValuesLimit=20&currency=USD&inStock[]=true&inStock[]=false&page=1&productsCount=24&q={}&searchedKey=VU05NGUza2pzYkFYR1ZXdXpOMFd2Ull3MFJxM0FmT0J0a25vMndqZW5Bdz0%3D&sort_field[]=sellingPrice&sort_order[]=desc".format(search))
    try:
        title = soup.find("p", class_="product-item-title").getText()
    except:
        title = ""
    try:
        price = soup.find("div",class_="wizzy-product-item-price  ").getText()
    except:
        price = "-1"
    price_digits = re.sub("[^0-9]", "", price)
    prod_data = Product.objects.create(
        website = "www.westside.com",
        url = "https://www.westside.com/pages/search?attributeFacetValuesLimit=20&currency=USD&inStock[]=true&inStock[]=false&page=1&productsCount=24&q={}&searchedKey=VU05NGUza2pzYkFYR1ZXdXpOMFd2Ull3MFJxM0FmT0J0a25vMndqZW5Bdz0%3D&sort_field[]=sellingPrice&sort_order[]=desc".format(search),
        title = title + " " + title,
        price = int(price_digits)
    )
    ser_data = ProductPostSerializer(data=prod_data)
    if ser_data.is_valid():
        ser_data.save()
    return True