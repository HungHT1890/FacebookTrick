from requests import session
from urllib3 import disable_warnings , exceptions
from define import *
from json import loads , load
from base64 import b64decode , b64encode
disable_warnings(exceptions.InsecureRequestWarning)
ss = session()
ss.verify = ss.trust_env = False


uid = '61550836155909'
cursor = ''
id =f'app_collection:{uid}:2356318349:2'
id = (b64encode(bytes(id,'utf-8')).decode('utf-8'))
while True:
    data = {
        'av': '',
        '__user': '',
        '__a': '1',
        '__comet_req': '15',
        'fb_dtsg': 'NAcNopytwDmNcWAOcJbvnpDySzyalfh_ny3AMjqqc6YyLQ-ffjiSM-Q:38:1708076258',
        'jazoest': '25885',
        'lsd': '-W8CSypcQ-4DY07QFsEkiQ',
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'ProfileCometAppCollectionListRendererPaginationQuery',
        'variables': '{"count":8,"cursor":"'+ cursor +'","scale":1,"search":null,"id":"'+ id +'"}',
        'server_timestamps': 'true',
        'doc_id': '24973057805674571',
        }
    
    response = ss.post(url=api , headers = header , data = data).text
    with open('response.txt','w',encoding='utf-8') as f:
        f.write(response)
    response = loads(response)

    response_total = response['data']['node']['pageItems']

    def extract_info(data):
        edges = data['edges']
        for x in edges:
            node = x['node']
            uid = b64decode(node['id']).decode('utf-8').split(':')[-1]
            name = node['title']['text']
            print(uid,name)
            

    def extract_cursor(data):
        page_info = data['page_info']['end_cursor']
        return page_info



    extract_info(response_total)
    cursor =  extract_cursor(response_total)
    if cursor == None or cursor == '':
        print("GET ALL UID DONE")
        break