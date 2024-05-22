from requests import session
from re import findall
ss = session()
def check_create(cookie,uid=4):
    api = 'https://www.facebook.com/api/graphql/'
    headers = {
        'Accept-Language':'en,vi;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5,nl;q=0.4',
        'Content-Length':'1868',
        'Content-Type':'application/x-www-form-urlencoded',
        'Cookie': cookie.strip(),
        'Dpr':'1',
        'Origin':'https://www.facebook.com',
        'Sec-Ch-Prefers-Color-Scheme':'dark',
        'Sec-Ch-Ua':'"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'Sec-Ch-Ua-Full-Version-List':'"Chromium";v="122.0.6261.129", "Not(A:Brand";v="24.0.0.0", "Google Chrome";v="122.0.6261.129"',
        'Sec-Ch-Ua-Mobile':'?0',
        'Sec-Ch-Ua-Model':'""',
        'Sec-Ch-Ua-Platform':'"Windows"',
        'Sec-Ch-Ua-Platform-Version':'"10.0.0"',
        'Sec-Fetch-Dest':'empty',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-origin',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Viewport-Width':'908',
        'X-Asbd-Id':'129477',
        'X-Fb-Friendly-Name':'MarketplaceSellerProfileDialogQuery',
        'X-Fb-Lsd':'y0qrNgEQAPqPE3jyQfjc6e',
                }
    av_id = findall(r'c_user=(\d+)',cookie)[0]
    # nếu requests qua api này lỗi ae liên hệ t.me/hunght1890 - hoặc tự thay phần fb_dtsg hoặc jazoest hoặc lsd
    data = {
            'av': av_id,
            'dpr': '1',
            '__comet_req': '15',
            'fb_dtsg': 'NAcOpWt344j4V4wWIuCrOec5SEdNB0WZyflfHUBzp5ZuCrMmUK4HamQ:21:1705050718',
            'jazoest': '25434',
            'lsd': 'MYUfqYvL5ZHWFfdPQ1kktF',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'MarketplaceSellerProfileDialogQuery',
            'variables': '{"isCOBMOB":false,"isSelfProfile":false,"productID":"944605867143682","scale":1,"sellerId":"'+ uid +'","useContextualViewHeader":true}',
            'server_timestamps': 'true',
            'doc_id': '7089290281172095'
                }
    
    try:
        response = ss.post(url=api , headers= headers , data = data)
        if __name__ == '__main__':
            # in ra thử xem có lỗi gì
            print(response.text)
            
        response_js = response.json()
        data = response_js['data']
        user = data['user']
        items = user['items']
        node = items['nodes']
        for x in node:
            text = x['title']['text']
            print(text)
    except Exception as f:
        print(f)
        pass

if __name__ == '__main__':
    test_id = '4'
    cookie = ''
    check_create(cookie,test_id)