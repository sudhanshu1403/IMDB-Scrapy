#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jaipu
#
# Created:     06-08-2023
# Copyright:   (c) jaipu 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from wsgiref import headers
import pandas as pd
import requests

from bs4 import BeautifulSoup
import numpy as np
import soupsieve

url = "http://www.imdb.com/chart/top/?ref_=nv_mv_250"
# url = "https://www.dealshare.in/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} # This is chrome, you can set whatever browser you like

# header = {"Accept-Language":"en-US, en;q=0.5"}

results = requests.get(url, headers=headers)
soup = BeautifulSoup(results.text, 'html.parser')
# print(soup.prettify())

# initalize empty list where you will store data
titles = []
years = []
run_time = []
imdb_ratings = []

record =[]

fd = open("movies.csv","w+", encoding="utf-8")

# <li class="ipc-metadata-list-summary-item sc-bca49391-0 eypSaE cli-parent"><div class="sc-f8c44fe8-0 leyYCk cli-poster-container"><div class="ipc-poster ipc-poster--base ipc-poster--dynamic-width ipc-sub-grid-item ipc-sub-grid-item--span-2" role="group"><div class="ipc-watchlist-ribbon ipc-focusable ipc-watchlist-ribbon--s ipc-watchlist-ribbon--base ipc-watchlist-ribbon--onImage ipc-poster__watchlist-ribbon" aria-label="add to watchlist" role="button" tabindex="0"><svg class="ipc-watchlist-ribbon__bg" width="24px" height="34px" viewBox="0 0 24 34" xmlns="http://www.w3.org/2000/svg" role="presentation"><polygon class="ipc-watchlist-ribbon__bg-ribbon" fill="#000000" points="24 0 0 0 0 32 12.2436611 26.2926049 24 31.7728343"></polygon><polygon class="ipc-watchlist-ribbon__bg-hover" points="24 0 0 0 0 32 12.2436611 26.2926049 24 31.7728343"></polygon><polygon class="ipc-watchlist-ribbon__bg-shadow" points="24 31.7728343 24 33.7728343 12.2436611 28.2926049 0 34 0 32 12.2436611 26.2926049"></polygon></svg><div class="ipc-watchlist-ribbon__icon" role="presentation"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" class="ipc-icon ipc-icon--add ipc-icon--inline" viewBox="0 0 24 24" fill="currentColor" role="presentation"><path d="M18 13h-5v5c0 .55-.45 1-1 1s-1-.45-1-1v-5H6c-.55 0-1-.45-1-1s.45-1 1-1h5V6c0-.55.45-1 1-1s1 .45 1 1v5h5c.55 0 1 .45 1 1s-.45 1-1 1z"></path></svg></div></div><div class="ipc-media ipc-media--poster-27x40 ipc-image-media-ratio--poster-27x40 ipc-media--base ipc-media--poster-m ipc-poster__poster-image ipc-media__img" style="width: 100%;"><img alt="Tim Robbins in The Shawshank Redemption (1994)" class="ipc-image" loading="lazy" src="https://m.media-amazon.com/images/M/MV5BNDE3ODcxYzMtY2YzZC00NmNlLWJiNDMtZDViZWM2MzIxZDYwXkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_QL75_UX140_CR0,1,140,207_.jpg" srcset="https://m.media-amazon.com/images/M/MV5BNDE3ODcxYzMtY2YzZC00NmNlLWJiNDMtZDViZWM2MzIxZDYwXkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_QL75_UX140_CR0,1,140,207_.jpg 140w, https://m.media-amazon.com/images/M/MV5BNDE3ODcxYzMtY2YzZC00NmNlLWJiNDMtZDViZWM2MzIxZDYwXkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_QL75_UX210_CR0,2,210,311_.jpg 210w, https://m.media-amazon.com/images/M/MV5BNDE3ODcxYzMtY2YzZC00NmNlLWJiNDMtZDViZWM2MzIxZDYwXkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_QL75_UX280_CR0,3,280,414_.jpg 280w" sizes="50vw, (min-width: 480px) 34vw, (min-width: 600px) 26vw, (min-width: 1024px) 16vw, (min-width: 1280px) 16vw" width="140"></div><a class="ipc-lockup-overlay ipc-focusable" href="/title/tt0111161/?ref_=chttp_i_1" aria-label="View title page for The Shawshank Redemption"><div class="ipc-lockup-overlay__screen"></div></a></div></div><div class="ipc-metadata-list-summary-item__c"><div class="ipc-metadata-list-summary-item__tc"><span class="ipc-metadata-list-summary-item__t" aria-disabled="false"></span><div class="sc-14dd939d-0 fBusXE cli-children"><div class="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-14dd939d-7 fjdYTb cli-title"><a href="/title/tt0111161/?ref_=chttp_t_1" class="ipc-title-link-wrapper" tabindex="0"><h3 class="ipc-title__text">1. The Shawshank Redemption</h3></a></div><div class="sc-14dd939d-5 cPiUKY cli-title-metadata"><span class="sc-14dd939d-6 kHVqMR cli-title-metadata-item">1994</span><span class="sc-14dd939d-6 kHVqMR cli-title-metadata-item">2h 22m</span><span class="sc-14dd939d-6 kHVqMR cli-title-metadata-item">R</span></div><span class="sc-14dd939d-1 PnacM"><div class="sc-951b09b2-0 hDQwjv sc-14dd939d-2 fKPTOp cli-ratings-container" data-testid="ratingGroup--container"><span aria-label="IMDb rating: 9.3" class="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating"><svg width="24" height="24" xmlns="http://www.w3.org/2000/svg" class="ipc-icon ipc-icon--star-inline" viewBox="0 0 24 24" fill="currentColor" role="presentation"><path d="M12 20.1l5.82 3.682c1.066.675 2.37-.322 2.09-1.584l-1.543-6.926 5.146-4.667c.94-.85.435-2.465-.799-2.567l-6.773-.602L13.29.89a1.38 1.38 0 0 0-2.581 0l-2.65 6.53-6.774.602C.052 8.126-.453 9.74.486 10.59l5.147 4.666-1.542 6.926c-.28 1.262 1.023 2.26 2.09 1.585L12 20.099z"></path></svg>9.3</span><button aria-label="Rate The Shawshank Redemption" class="ipc-rate-button sc-951b09b2-1 bnbQXY ratingGroup--user-rating ipc-rate-button--unrated ipc-rate-button--base" data-testid="rate-button"><span class="ipc-rating-star ipc-rating-star--base ipc-rating-star--rate"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" class="ipc-icon ipc-icon--star-border-inline" viewBox="0 0 24 24" fill="currentColor" role="presentation"><path d="M22.724 8.217l-6.786-.587-2.65-6.22c-.477-1.133-2.103-1.133-2.58 0l-2.65 6.234-6.772.573c-1.234.098-1.739 1.636-.8 2.446l5.146 4.446-1.542 6.598c-.28 1.202 1.023 2.153 2.09 1.51l5.818-3.495 5.819 3.509c1.065.643 2.37-.308 2.089-1.51l-1.542-6.612 5.145-4.446c.94-.81.45-2.348-.785-2.446zm-10.726 8.89l-5.272 3.174 1.402-5.983-4.655-4.026 6.141-.531 2.384-5.634 2.398 5.648 6.14.531-4.654 4.026 1.402 5.983-5.286-3.187z"></path></svg><span class="ipc-rating-star--rate">Rate</span></span></button></div></span></div></div></div><div class="sc-bca49391-1 fYjvMO cli-post-element"><button class="ipc-icon-button cli-info-icon ipc-icon-button--base ipc-icon-button--onAccent2" title="See more information about The Shawshank Redemption" role="button" tabindex="0" aria-label="See more information about The Shawshank Redemption" aria-disabled="false"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" class="ipc-icon ipc-icon--info" viewBox="0 0 24 24" fill="currentColor" role="presentation"><path fill="none" d="M0 0h24v24H0V0z"></path><path d="M11 7h2v2h-2zm0 4h2v6h-2zm1-9C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z"></path></svg></button></div></li>
# <li class="ipc-metadata-list-summary-item sc-bca49391-0 eypSaE cli-parent"><div class="sc-f8c44fe8-0 leyYCk cli-poster-container"><div class="ipc-poster ipc-poster--base ipc-poster--dynamic-width ipc-sub-grid-item ipc-sub-grid-item--span-2" role="group"><div class="ipc-watchlist-ribbon ipc-focusable ipc-watchlist-ribbon--s ipc-watchlist-ribbon--base ipc-watchlist-ribbon--onImage ipc-poster__watchlist-ribbon" aria-label="add to watchlist" role="button" tabindex="0"><svg class="ipc-watchlist-ribbon__bg" width="24px" height="34px" viewBox="0 0 24 34" xmlns="http://www.w3.org/2000/svg" role="presentation"><polygon class="ipc-watchlist-ribbon__bg-ribbon" fill="#000000" points="24 0 0 0 0 32 12.2436611 26.2926049 24 31.7728343"></polygon><polygon class="ipc-watchlist-ribbon__bg-hover" points="24 0 0 0 0 32 12.2436611 26.2926049 24 31.7728343"></polygon><polygon class="ipc-watchlist-ribbon__bg-shadow" points="24 31.7728343 24 33.7728343 12.2436611 28.2926049 0 34 0 32 12.2436611 26.2926049"></polygon></svg><div class="ipc-watchlist-ribbon__icon" role="presentation"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" class="ipc-icon ipc-icon--add ipc-icon--inline" viewBox="0 0 24 24" fill="currentColor" role="presentation"><path d="M18 13h-5v5c0 .55-.45 1-1 1s-1-.45-1-1v-5H6c-.55 0-1-.45-1-1s.45-1 1-1h5V6c0-.55.45-1 1-1s1 .45 1 1v5h5c.55 0 1 .45 1 1s-.45 1-1 1z"></path></svg></div></div><div class="ipc-media ipc-media--poster-27x40 ipc-image-media-ratio--poster-27x40 ipc-media--base ipc-media--poster-m ipc-poster__poster-image ipc-media__img" style="width: 100%;"><img alt="Marlon Brando in The Godfather (1972)" class="ipc-image" loading="lazy" src="https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_QL75_UY207_CR3,0,140,207_.jpg" srcset="https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_QL75_UY207_CR3,0,140,207_.jpg 140w, https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_QL75_UY311_CR4,0,210,311_.jpg 210w, https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_QL75_UY414_CR6,0,280,414_.jpg 280w" sizes="50vw, (min-width: 480px) 34vw, (min-width: 600px) 26vw, (min-width: 1024px) 16vw, (min-width: 1280px) 16vw" width="140"></div><a class="ipc-lockup-overlay ipc-focusable" href="/title/tt0068646/?ref_=chttp_i_2" aria-label="View title page for The Godfather"><div class="ipc-lockup-overlay__screen"></div></a></div></div><div class="ipc-metadata-list-summary-item__c"><div class="ipc-metadata-list-summary-item__tc"><span class="ipc-metadata-list-summary-item__t" aria-disabled="false"></span><div class="sc-14dd939d-0 fBusXE cli-children"><div class="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-14dd939d-7 fjdYTb cli-title"><a href="/title/tt0068646/?ref_=chttp_t_2" class="ipc-title-link-wrapper" tabindex="0"><h3 class="ipc-title__text">2. The Godfather</h3></a></div><div class="sc-14dd939d-5 cPiUKY cli-title-metadata"><span class="sc-14dd939d-6 kHVqMR cli-title-metadata-item">1972</span><span class="sc-14dd939d-6 kHVqMR cli-title-metadata-item">2h 55m</span><span class="sc-14dd939d-6 kHVqMR cli-title-metadata-item">R</span></div><span class="sc-14dd939d-1 PnacM"><div class="sc-951b09b2-0 hDQwjv sc-14dd939d-2 fKPTOp cli-ratings-container" data-testid="ratingGroup--container"><span aria-label="IMDb rating: 9.2" class="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating"><svg width="24" height="24" xmlns="http://www.w3.org/2000/svg" class="ipc-icon ipc-icon--star-inline" viewBox="0 0 24 24" fill="currentColor" role="presentation"><path d="M12 20.1l5.82 3.682c1.066.675 2.37-.322 2.09-1.584l-1.543-6.926 5.146-4.667c.94-.85.435-2.465-.799-2.567l-6.773-.602L13.29.89a1.38 1.38 0 0 0-2.581 0l-2.65 6.53-6.774.602C.052 8.126-.453 9.74.486 10.59l5.147 4.666-1.542 6.926c-.28 1.262 1.023 2.26 2.09 1.585L12 20.099z"></path></svg>9.2</span><button aria-label="Rate The Godfather" class="ipc-rate-button sc-951b09b2-1 bnbQXY ratingGroup--user-rating ipc-rate-button--unrated ipc-rate-button--base" data-testid="rate-button"><span class="ipc-rating-star ipc-rating-star--base ipc-rating-star--rate"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" class="ipc-icon ipc-icon--star-border-inline" viewBox="0 0 24 24" fill="currentColor" role="presentation"><path d="M22.724 8.217l-6.786-.587-2.65-6.22c-.477-1.133-2.103-1.133-2.58 0l-2.65 6.234-6.772.573c-1.234.098-1.739 1.636-.8 2.446l5.146 4.446-1.542 6.598c-.28 1.202 1.023 2.153 2.09 1.51l5.818-3.495 5.819 3.509c1.065.643 2.37-.308 2.089-1.51l-1.542-6.612 5.145-4.446c.94-.81.45-2.348-.785-2.446zm-10.726 8.89l-5.272 3.174 1.402-5.983-4.655-4.026 6.141-.531 2.384-5.634 2.398 5.648 6.14.531-4.654 4.026 1.402 5.983-5.286-3.187z"></path></svg><span class="ipc-rating-star--rate">Rate</span></span></button></div></span></div></div></div><div class="sc-bca49391-1 fYjvMO cli-post-element"><button class="ipc-icon-button cli-info-icon ipc-icon-button--base ipc-icon-button--onAccent2" title="See more information about The Godfather" role="button" tabindex="0" aria-label="See more information about The Godfather" aria-disabled="false"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" class="ipc-icon ipc-icon--info" viewBox="0 0 24 24" fill="currentColor" role="presentation"><path fill="none" d="M0 0h24v24H0V0z"></path><path d="M11 7h2v2h-2zm0 4h2v6h-2zm1-9C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z"></path></svg></button></div></li>
movie_div = soup.find_all('li', class_='ipc-metadata-list-summary-item sc-bca49391-0 eypSaE cli-parent')
for container in movie_div: 
    name = container.find("h3",class_="ipc-title__text").text #container.li.a.h3.text
    name = name.strip()
    name = name.encode(encoding = 'UTF-8', errors = 'ignore').decode()
    titles.append(name)
   
    year = container.find("div",class_="sc-14dd939d-5 cPiUKY cli-title-metadata").text
    year = year.strip()
    year , time = year[0:4] , year[4:10] 
    years.append(year)
    run_time.append(time)
   
    imdb = container.find("span", class_='ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating').text
    imdb_ratings.append(imdb)

    #record.append(tuple(name,year,run_time,imdb))
    #data=(name, year, time, imdb)
    str = "{},{},{},{}\n".format(name, year, time, imdb)
    print(str)
    fd.write(str)    

    # print(data)

fd.close()
#print(titles)
#print(years) 
#print(run_time)
#print(imdb_ratings)


