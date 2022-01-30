ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
headers = {'User-Agent': ua}

import requests
from bs4 import BeautifulSoup
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def catch_param(T_url):
    r = requests.get(T_url, headers=headers)
    html = r.content
    bsObj = BeautifulSoup(html, "html.parser")

    ## catch params
    rest_name = bsObj.findAll('meta',property='og:title')[0]['content']

    fig_url_t = bsObj.findAll('img',class_='p-main-photos__slider-image')
    fig_url_p = bsObj.findAll('p', class_='rstdtl-top-postphoto__photo')
    if len(fig_url_t)>0:
        fig_url = fig_url_t[0]['src']
    elif len(fig_url_t)==0 and len(fig_url_p)>0:
        fig_url_p = bsObj.findAll('p', class_='rstdtl-top-postphoto__photo')[0]
        fig_url = fig_url_p.findAll('a')[0]['href']
    else:
        fig_url = 'https://miro.medium.com/max/400/1*UL9RWkTUtJlyHW7kGm20hQ.png'

    address = bsObj.findAll('p', class_='rstinfo-table__address')[0].get_text()

    station = [{'name':bsObj.findAll('span', class_='linktree__parent-target-text')[0].get_text()}]

    good_t = bsObj.findAll('span', class_='linktree__parent-target-text')
    good = [{'name':good_t[2].get_text()}]
    if len(good_t)==4:
        good.append({'name':good_t[3].get_text()})
    elif len(good_t)==5:
        good.append({'name':good_t[4].get_text()})

    cost = bsObj.findAll('a', class_='rdheader-budget__price-target')
    dinner_cost = cost[0].get_text()
    lunch_cost = cost[1].get_text()

    business_hours = bsObj.findAll('p', class_='rstinfo-table__subject-text')[0].get_text()

    return {
        'rest_name':rest_name, 
        'fig_url':fig_url, 
        'address':address, 
        'station':station, 
        'good':good, 
        'dinner_cost':dinner_cost, 
        'lunch_cost':lunch_cost, 
        'business_hours':business_hours
    }
