import requests
import pandas as pd 

# output container
result = []

for page_num in range(1,50):

    # base URL
    url = "https://jiji.ng/api_web/v1/listing"

    # prefrences
    querystring = {"po":"6.2","lsmid":"1644252189240","webp":"false","slug":"cars","page":f"{page_num}"}
    payload = ""
    headers = {
        "cookie": "app=e47ca390800b4f13a0c06676c9290d94; uid=d9bc1c8f45e13e3879f325d076ea4db27bad5347",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://jiji.ng/cars",
        "X-Requested-With": "XMLHttpRequest",
        "X-Window-ID": "1644252188065",
        "x-listing-id": "cxqlCtNhoNmYEE3G",
        "Connection": "keep-alive",
        "Cookie": "first_visit=1638532331; app=e47ca390800b4f13a0c06676c9290d94; uid=d9bc1c8f45e13e3879f325d076ea4db27bad5347; g_state={'i_l':0}; _ga_V7SNPVJK6G=GS1.1.1641383030.1.1.1641384838.0; _ga=GA1.2.1006118835.1641383035; _gcl_au=1.1.78002763.1641383035; _fbp=fb.1.1641383049724.950543836; __gads=ID=ff4325c47d4248f9-2282744de1ce0099:T=1641384108:S=ALNI_MYASFQ6vXJRqrgLo9qgsx9he8MJKQ; rid=direct; _js2=2F5Ewfb9rBY2L8bxiepuLaREkFIlA0EXHU6TiFBzQlU=; app_sid=1644252188357",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers"
    }

    try:
        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

        data = response.json()

        # extract root dir
        products = data['adverts_list']['adverts']
        for p in products:
            result.append(p)
        
        print(f'page {page_num} done... ')
    except:
        print(f'requests response {response.status_code}')
        break

# structure data sith JSON
df = pd.json_normalize(result)

# clean data
col_drop = ['apply_url','apply_url','attributes','can_view_contacts','category_name','category_slug','id',
            'images_count','is_boost','as_top','can_view_contacts_auth_url','is_cv','is_job','is_owner','is_top',
            'message_url','region_item_text','region_slug','title_labels','tops_count','user_id','user_phone','booster_info.count',
           'booster_info.type','fb_view_content_data.content_category','fb_view_content_data.content_ids',	
           'fb_view_content_data.content_type',	'fb_view_content_data.currency','fb_view_content_data.value','image_obj.center', 
           'image_obj.url',	'paid_info.text','price_obj.period','badge_info.aside_color','badge_info.bg_color',	'badge_info.label',	
           'badge_info.service_type','badge_info.slug','badge_info.text_color','paid_info']

df = df.drop(col_drop, axis=1)
df1 = df.copy()
df1.to_csv('crawled_data/jiji_cars_trimmed_multi.csv')
    

