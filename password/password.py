password = 'a123456'
x = 3
while x > 0:
	x = x - 1
	login = input('請輸入密碼: ')
	if login == password:
		print('登入成功')
		break
	else:
		print('密碼錯誤!')
		print('還有', x ,'次機會!')
		if x == 0: 
			print('密碼錯誤!帳號已凍結!')