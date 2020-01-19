import os
path = os.path.join('C:\\','Users','user','Desktop')
dirname = '不存在的資料夾'
path = os.path.join(path , dirname)

print(path , os.path.exists(path))
if not os.path.exists(path):
	print('os.makedir:',path)
	os.makedirs(path)
else:
	print("存在:",path)