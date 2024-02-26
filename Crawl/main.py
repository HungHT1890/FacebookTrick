from json import loads , load
from requests import session
from re import findall
from urllib3  import disable_warnings , exceptions
from base64 import b64decode , b64encode
from define import *

disable_warnings(exceptions.InsecureRequestWarning)
ss = session()
ss.verify = ss.trust_env = False

uid = '100094606110131'
id = f'app_collection:{uid}:2356318349:2'
# id = b64encode(bytes(str(id),'utf-8').decode('utf-8'))
id =    b64encode(bytes(id,'utf-8')).decode('utf-8')

        
if __name__ == '__main__':
    # while True:
    cursor = ''
    while True:
        # print(f'{x}: {cursor}')
        playload = {
                    'av': '0',
                    '__aaid': '0',
                    '__user': '0',
                    '__a': '1',
                    '__req': 'w',
                    '__hs': '19779.HYP:comet_pkg.2.1..2.1',
                    'dpr': '1',
                    '__ccg': 'EXCELLENT',
                    '__rev': '1011644928',
                    '__s': 'jsqhn7:hamgvq:zl3xw1',
                    '__hsi': '7339775033255733762',
                    '__dyn': '7AzHK4HwkEng5K8G6EjBAg2owIxu13wFwnUW3q2ibwNwnof8boG0x8bo6u3y4o2Gwfi0LVEtwMw65xO2OU7m221FwgolzUO0-E7m4oaEnxO0Bo7O2l2Utwwwi831wiE567Udo5qfK0zEkxe2GewyDwkUtxGm2SUbElxm3y11xfxmu3W3y261eBx_wHwdG7FoarCwLyESE6C14wwwOg2cwMwrUK2K364UrwFg2fwxyo566k1FwgU4q3G1eKufxa3m',
                    '__csr': 'gT5tPlbONcj9Yz8x5PhZOTOihlhcJOjTSG5qkp6EPeGFbiHmBIhBldOtp97F2uuiDKmVl_bRZbyrBxJ2kb_yaGFTyayQ-8ylQAbyogmt5GeATxm4UN2ogDV9HxO2C8x2fxKXmUuxe9Cixqieyo8ogqyEjwwDyU8rK7889Uy2el08e15G32u9xmuu0BU4K78-1gwIw_wBwCxy2m1fxy2udwqoaU4O12xW0mZ06hwe23S0ji046Q087w0sWo03rWg6y5U510kUmo15Ow82q1Hg33w6Ozki0H80kAw16m0jeq0q204ao8U0mgw5qw11O0h20c5zS04ik01lBBgfUkBo36w45w12i',
                    '__comet_req': '15',
                    'fb_dtsg': 'NAcNsApo3JqOBuKOfy4XYzIVoT8Q-5JPLzTScnR_kRT2504CuAEQwUQ:38:1708076258',
                    'jazoest': '25352',
                    'lsd': 'iLcfw4DDEXHv6uqlzWs17O',
                    '__spin_r': '1011644928',
                    '__spin_b': 'trunk',
                    '__spin_t': '1708924545',
                    'fb_api_caller_class': 'RelayModern',
                    'fb_api_req_friendly_name': 'ProfileCometAppCollectionListRendererPaginationQuery',
                    'variables': '{"count":8,"cursor":"'+ cursor + '","scale":1,"search":null,"id":"' + id +'"}',
                    'server_timestamps': 'true',
                    'doc_id': '24973057805674571',
                        }
        response = ss.post(url=api , headers= header , data= playload).text
        json_test = loads(response)['data']['node']['pageItems']
        def extract_info(data):
            edges = data['edges']
            for data in edges:
                data_extract_total = data['node']
                uid = b64decode(data_extract_total['id']).decode('utf-8').split(':')[-1]
                name = data_extract_total['title']['text']
                print(uid,name)


        def get_curson(data):
            page_info = data['page_info']
            end_cursor = page_info['end_cursor']
            return end_cursor
            
        data = json_test
        extract_info(data)
        cursor = get_curson(data)
        if cursor == None:
            print('DA GET HET UID')
            break
        
    # 100094606110131
    
    