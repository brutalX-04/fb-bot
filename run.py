# MODULE
import os
import re
import sys
import time
import json
import requests
from bs4 import BeautifulSoup as bs
from concurrent.futures import ThreadPoolExecutor as thread


# COLOR
p  = '\33[m' 		# DEFAULT
m  = '\x1b[0;91m' 	# RED 
k  = '\033[0;93m' 	# KUNING 
h  = '\x1b[0;92m' 	# HIJAU 


# CALLING
rs = requests.Session()
loop = 1

if "linux" in sys.platform.lower():
	try:
		clear = 'clear'
	except:pass

elif "win" in sys.platform.lower():
	try:
		clear = 'cls'
	except:pass

else:
	try:
		clear = 'clear'
	except:pass


# USER AGENT
try:
	os.system(clear)
	ua = open('DATA/user-agent.txt','r').read()
	try:
		a = ua.split(';')[1].split(' ')[2]
		b = ua.split('Chrome/')[1].split('.')[0]
		c = ua.split('Chrome/')[1].split(' ')[0]
		os_ver = f'"{a}.0.0"'
		sec_ch = f'"Not:A-Brand";v="99", "Chromium";v="{b}"'
		sec_full = f'"Not.A/Brand";v="8.0.0.0", "Chromium";v="{c}", "Google Chrome";v="{c}"'
	except:
		ua = 'Mozilla/5.0 (Linux; U; Android 11; RMX3241 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36 OPR/62.4.2254.61190|"Not:A-Brand";v="99", "Chromium";v="98"|11|98.0.4758.101'
		os_ver = '"11.0.0"'
		sec_ch = '"Not:A-Brand";v="99", "Chromium";v="98"'
		sec_full = '"Not.A/Brand";v="8.0.0.0", "Chromium";v="98.0.4758.101", "Google Chrome";v="98.0.4758.101"'
except:
	os.system('mkdir DATA')
	os.system(clear)
	ua = input(' Input user agent : ')
	open('DATA/user-agent.txt','w').write(ua)
	try:
		a = ua.split(';')[1].split(' ')[2]
		b = ua.split('Chrome/')[1].split('.')[0]
		c = ua.split('Chrome/')[1].split(' ')[0]
		os_ver = f'"{a}.0.0"'
		sec_ch = f'"Not:A-Brand";v="99", "Chromium";v="{b}"'
		sec_full = f'"Not.A/Brand";v="8.0.0.0", "Chromium";v="{c}", "Google Chrome";v="{c}"'
	except:
		ua = 'Mozilla/5.0 (Linux; U; Android 11; RMX3241 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36 OPR/62.4.2254.61190|"Not:A-Brand";v="99", "Chromium";v="98"|11|98.0.4758.101'
		os_ver = '"11.0.0"'
		sec_ch = '"Not:A-Brand";v="99", "Chromium";v="98"'
		sec_full = '"Not.A/Brand";v="8.0.0.0", "Chromium";v="98.0.4758.101", "Google Chrome";v="98.0.4758.101"'


# CLASS BANNER
class banner:
	def __init__(self):
		self.banner()

	def banner(self):
		os.system(clear)
		print('┏┓┏┓┳┳┓   ┓\n ┃┃ ┃┃┃┏┓┏┫       © 2023\n┗┛┗┛┛ ┗┗┛┗┻       by%s XMod%s'%(h,p))
		print('*' * 25)


# CLASS MENU
class menu:
	def __init__(self):
		self.check()
		self.menu()

	def check(self):
		try:
			self.cookie = open('DATA/cookie.txt').read()
			self.token = open('DATA/token.txt').read()
			language(self.cookie)
			get = rs.get('https://graph.facebook.com/me?fields=id,name&access_token='+self.token,cookies={'cookie':self.cookie})
			self.nama = json.loads(get.text)['name']
			self.user_id = json.loads(get.text)['id']
		except:
			os.system(clear)
			print('%s Check Login Failled%s, Login Ulang'%(m,p))
			dtk = 3
			for i in range(3):
				print('\r - Login Ulang Dalam %s Detik   '%(dtk), end='')
				time.sleep(1)
				dtk-=1
			login.login(self)
			

	def menu(self):
		try:
			banner()
			print('Info User')
			print('Nama : %s%s%s'%(h,self.nama,p))
			print('ID   : %s%s%s'%(h,self.user_id,p))
			print('*' * 25)
			print('Home Menu\n')
			print('1. Bot Share  [ %sGraph%s ]'%(h,p))
			print('2. Bot Komen  [ %sMbasic%s ]'%(h,p))
			print('3. Bot Pesan  [ %sMbasic%s ]\n'%(h,p))
			pilih = input(' - Pilih : ')
			if pilih in ['01','1']:
				share.share(self)
				exit()

			elif pilih in ['02','2']:
				print('*' * 25)
				self.delay = input('Input Delay Comment : ')
				self.text_comment = input('Input Text comment : ')
				comment.home(self, 'https://mbasic.facebook.com/home.php?')
				exit()

			elif pilih in ['03','3']:
				print('*' * 25)
				self.delay = input('Input Delay Pesan : ')
				self.text_pesan = input('Input Text Pesan : ')
				pesan.table(self, 'https://mbasic.facebook.com/messages/?')
				exit()
		except:
			pass


# UBAH BAHASA - THANKS TO DAPUNTA
def language(cookie):
    try:
        with requests.Session() as xyz:
            req = xyz.get('https://mbasic.facebook.com/language/',cookies=cookie)
            pra = bs(req.content,'html.parser')
            for x in pra.find_all('form',{'method':'post'}):
                if 'Bahasa Indonesia' in str(x):
                    bahasa = {
                        "fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),
                        "jazoest" : re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),
                        "submit"  : "Bahasa Indonesia"}
                    url = 'https://mbasic.facebook.com' + x['action']
                    exec = xyz.post(url,data=bahasa,cookies=cookie)
    except Exception as e:pass


# CLASS LOGIN
class login:
	def __init__(self):
		self.login()

	# THANKS TO DAPUNTA
	def login(self):
		banner()
		cookie = input(' - Input Cookies : ')
		try:
			get = rs.get('https://business.facebook.com/business_locations', cookies={'cookie':cookie})
			token = re.search('(\["EAAG\w+)', get.text).group(1).replace('["','')
			open('DATA/token.txt','w').write(token)
			open('DATA/cookie.txt','w').write(cookie)
			print('%s Login Succes%s'%(h,p))
			time.sleep(3)
			menu()

		except:
			print('%s Login Failled%s, Silahkan Ganti Cookies'%(m,p))
			dtk = 3
			for i in range(3):
				print('\r - Login Ulang Dalam %s Detik   '%(dtk), end='')
				time.sleep(1)
				dtk-=1
			login()

# CLASS BOT SHARE
class share:
	def __init__(self):
		pass

	def share(self):
		global loop
		try:
			print('*' * 25)
			jumlah = input('Input Jumlah Share : ')
			url = input('Input Url : ')
			link = f'https://graph.facebook.com/v17.0/me/feed?link={url}&published=0&access_token={self.token}'
			awal = time.time()
			for i in range(int(jumlah)):
				post = rs.post(link, cookies={'cookie': self.cookie}).text
				if 'Kami membatasi' in post:
					print(' - Share %sFailled%s : Account Limit'%(m,p))
				elif 'spam' in post:
					print(' - Share %sFailled%s : Account Limit'%(m,p))
				elif 'id' in post:
					print(' - Succes Share Post %s%s%s X \n   Response : %s'%(h,loop,p,post))
					loop+=1

			akhir = time.time()
			total = akhir - awal
			print('\r                                               ')
			print('\n - Program Succes in %s%s%s Seccond'%(h,total,p))

		except Exception as e:
			print(e)


# CLASS BOT KOMEN
class comment:
	def __init__(self):
		pass

	def home(self, url):
		try:
			awal = time.time()
			get = bs(rs.get(url, cookies={'cookie': self.cookie}).text, 'html.parser')
			clas = re.search('div id="m-top-of-feed"></div><div class=".. .. .."><div class="(.*?)" data-ft=', str(get)).group(1)
			all_story = get.find_all('div', class_='%s'%(clas))
			for story in all_story:
				clas = re.search('Tanggapi</a></span><span> · </span><a class="(.*?)" href', str(story)).group(1)
				url = story.find('a', class_='%s'%(clas)).get('href')
				if 'https://mbasic.facebook.com' in url:
					pass
				else:
					url = 'https://mbasic.facebook.com'+url

				comment.comment(self, url)
				io = int(self.delay)
				for i in range(int(self.delay)):
					print('\r - Lanjut Dalam %s Detik  '%(io), end='')
					io-=1
					time.sleep(1)

			if 'Lihat Berita Lain' in str(get):
				try:
					clas = re.search('Lainnya</a></div></div></div></div><a class="(.*?)" href=', str(get)).group(1)
					url = get.find('a', class_='%s'%(clas)).get('href')
					if 'https://mbasic.facebook.com' in url:
						pass
					else:
						url = 'https://mbasic.facebook.com'+url
					comment.home(self, url)
				except:
					print('\n - Failled Get More Post')
			else:
				pass

			akhir = time.time()
			total = akhir - awal
			print('\r                                                 ')
			print('\n - Program Succes in %s%s%s Seccond'%(h,total,p))

		except Exception as e:
			print(e)
			exit()

	def comment(self, url):
		global loop
		try:
			get = bs(rs.get(url, cookies={'cookie': self.cookie}).text, 'html.parser')
			form = get.find('form', {'method': 'post'})
			headers = {
			    'authority': 'mbasic.facebook.com',
			    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
			    'accept-language': 'en-US,en;q=0.9,id;q=0.8',
			    'cache-control': 'no-cache',
			    'content-type': 'application/x-www-form-urlencoded',
			    'dpr': '1',
			    'origin': 'https://mbasic.facebook.com',
			    'pragma': 'no-cache',
			    'referer': url,
			    'sec-ch-prefers-color-scheme': 'light',
			    'sec-ch-ua': sec_ch,
			    'sec-ch-ua-full-version-list': sec_full,
			    'sec-ch-ua-mobile': '?1',
			    'sec-ch-ua-model': '""',
			    'sec-ch-ua-platform': '"Android"',
			    'sec-ch-ua-platform-version': os_ver,
			    'sec-fetch-dest': 'document',
			    'sec-fetch-mode': 'navigate',
			    'sec-fetch-site': 'same-origin',
			    'sec-fetch-user': '?1',
			    'upgrade-insecure-requests': '1',
			    'user-agent': ua
			}
			data = {
				'fb_dtsg':	re.search('name="fb_dtsg" type="hidden" value="(.*?)"', str(form)).group(1),
				'jazoest':	re.search('name="jazoest" type="hidden" value="(.*?)"', str(form)).group(1),
				'comment_text':	self.text_comment
			}
			nama = get.find('title').text
			try:
				nama = nama.split(' ')[0]
			except:
				pass
			url = form.get('action')
			if 'https://mbasic.facebook.com' in url:
				pass
			else:
				url = 'https://mbasic.facebook.com'+url
			
			post = rs.post(url, headers=headers, data= data, cookies={'cookie': self.cookie})
			if '<Response [200]>' in str(post):
				print('\r - [ %s ] Succes Comment In Post : %s%s%s'%(loop,h,nama,p))
				loop+=1
			else:
				print('\r - Failled Comment In Post : %s%s%s'%(h,nama,p))

		except Exception as e:
			print('\r - Failled : '+str(e))


# CLASS BOT PESAN
class pesan:
	def __init__(self):
		pass

	def table(self, url):
		try:
			awal = time.time()
			get = bs(rs.get(url, cookies={'cookie': self.cookie}).text, 'html.parser')
			clas = re.search('Cari pesan</a></div><div><div><table class="(.*?)"><tr>', str(get)).group(1)
			all_table = get.find_all('table', class_='%s'%(clas))
			for table in all_table:
				url = table.find('a').get('href')
				if 'https://mbasic.facebook.com' in url:
					pass
				else:
					url = 'https://mbasic.facebook.com'+url
				pesan.pesan(self, url)
				io = int(self.delay)
				for i in range(int(self.delay)):
					print('\r - Lanjut Dalam %s Detik  '%(io), end='')
					io-=1
					time.sleep(1)

			akhir = time.time()
			total = akhir - awal
			print('\r                                               ')
			print(' - Program Succes in %s%s%s Seccond'%(h,total,p))

		except Exception as e:
			print(e)

	def pesan(self, url):
		try:
			global loop
			get = bs(rs.get(url, cookies={'cookie': self.cookie}).text, 'html.parser')
			form = get.find('form', {'method': 'post'})
			open('pesan.txt', 'w', encoding='utf-8').write(str(form))
			ids = re.search('name="ids(.*?)" type="hidden" value="(.*?)"', str(form)).group(2)
			data = {
			    'fb_dtsg':	re.search('name="fb_dtsg" type="hidden" value="(.*?)"', str(form)).group(1),
				'jazoest':	re.search('name="jazoest" type="hidden" value="(.*?)"', str(form)).group(1),
			    'body': self.text_pesan,
			    'send': 'Kirim',
			    'tids': re.search('name="tids" type="hidden" value="(.*?)"', str(form)).group(1),
			    'wwwupp': 'C3',
			    f'ids[{ids}]': f'{ids}',
			    'platform_xmd': '',
			    'referrer': '',
			    'ctype': '',
			    'cver': 'legacy',
			    'csid': re.search('name="csid" type="hidden" value="(.*?)"', str(form)).group(1)
			}
			nama = get.find('title').text
			url = form.get('action')
			if 'https://mbasic.facebook.com' in url:
				pass
			else:
				url = 'https://mbasic.facebook.com'+url

			post = rs.post(url, data= data, cookies={'cookie': self.cookie})
			if '<Response [200]>' in str(post):
				print('\r - [ %s ] Succes Comment In Post : %s%s%s'%(loop,h,nama,p))
				loop+=1
			else:
				print('\r - Failled Comment In Post : %s%s%s'%(h,nama,p))

		except Exception as e:
			print(e)



# RUNNING
if __name__=='__main__':
	try:
		os.system('mkdir DATA')
	except:
		pass
	menu()