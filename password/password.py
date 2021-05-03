password = 'a123456'
x = 0
while True:
    login = input('請輸入密碼: ')
    x = x + 1
    if login != password and x < 2:
	    print('密碼錯誤!還有2次機會!')
    elif login != password and x < 3:
	    print('密碼錯誤!還有1次機會!')
    elif login != password and x < 4:
	    print('密碼錯誤!退出系統!')
	    break
    elif login == password:
	    print('登入成功')
	    break