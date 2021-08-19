"""9-7"""
class User():
    def __init__(self, first_name,last_name):
	self.first_name = first_name
	self.last_name = last_name
    def describe_user(self):
	print('用户名称为：' + self.first_name + self.last_name)
    def greet_user(self):
	print('你好！ ' + self.first_name + self.last_name)

class Admin(User):
    def __init__(self,first_name,last_name):
	super().__init__(first_name,last_name)
	self.privileges = ['can add post','can del post','can ban user']
    def show_privileges(self):
		
	for i in self.privileges:
	    print("管理员权限有：" + i)
Admin1 = Admin('Li','dc')
Admin1.show_privileges()

