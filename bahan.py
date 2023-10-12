# --> Class Login
class auth:
    def __init__(self):
        pass
    
    # --> Get Data Login Account
    def login(self):
		try:
			banner('Login')
			cook = input('Input Cookies : ')
			cookie = {'cookie': cook}
			open('DATA/account/.cookie.txt', 'w').write(cook)
			with requests.Session() as rsn:
				# --> Get Token Eaat
				try:
					data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038', 'scope': ''}
					post = rsn.post('https://graph.facebook.com/v18.0/device/login/',data=data).json()
					code, user_code = post['code'], post['user_code']
					url = 'https://graph.facebook.com/v18.0/device/login_status?method=post&code=%s&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038'%(code)
					get = bs(rsn.get('https://mbasic.facebook.com/device',cookies=cookie).content,'html.parser')
					form = get.find('form',{'method':'post'})
					data1 = {'jazoest'   : re.search('name="jazoest" type="hidden" value="(.*?)"',str(form)).group(1),'fb_dtsg'   : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(form)).group(1),'qr'        : '0','user_code' : user_code}
					url1 = 'https://mbasic.facebook.com' + form['action']
					post1 = bs(rsn.post(url1,data=data1,cookies=cookie).content,'html.parser')
					data2 = {}
					form1 = post1.find('form',{'method':'post'})
					for x in form1('input',{'value':True}):
						try:
							if x['name'] == '__CANCEL__' :
								pass
							else:
								data2.update({x['name']:x['value']})
						except Exception as e:
							pass
					url2 = 'https://mbasic.facebook.com' + form1['action']
					pos = bs(rsn.post(url2,data=data2,cookies=cookie).content,'html.parser')
					get_token = rsn.get(url,cookies=cookie).json()
					token = get_token['access_token']
					open('DATA/account/.token-eaat.txt', 'w').write(token)
				except:
					printer().failled('Failled Get Token EAAT')

				# --> Get Token Eaag
				try:
					get_token_eaag = rsn.get('https://business.facebook.com/business_locations',cookies=cookie)
					token_eaag = re.search('(\["EAAG\w+)', get_token_eaag.text).group(1).replace('["','')
					open('DATA/account/.token-eaag.txt', 'w').write(token_eaag)
					printer().succes('Login Succes')
				except:
					printer().failled('Failled Get Token EAAG')
				exit()

		except Exception as e:
			printer().failled('Login Failled')
			exit()


# --> Dump Id
def dump():
    # --> Get Publick Friends
    get = requests.get('https://graph.facebook.com/%s?fields=friends&access_token=%s'%(target_id, token_eaat), cookies=cookie).json()

    # --> Get Publick Followers
    get = requests.get('https://graph.facebook.com/%s/subscribers?limit=10000&access_token=%s'%(target_id, token_eaag), cookies=cookie).json()
