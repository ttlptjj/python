
"""9-5"""

class user():

    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts = 0

    def describe_user(self):
        print("用户名为"+self.firat_name + self.last_name)
        print("登录总次数为"+str(self.login_attempts))
        print("重置后登录总量为"+str(self.login_attempts))

    def increment_login_attempts(self,number):
        self.login_attempts += number
    def reset_login_attempts(self):
	self.login_attempts = 0 
         
User=user('Li','dc')
User.increment_login_attempts(1)
User.increment_login_attempts(1)
User.increment_login_attempts(1)
User.reset_login_attempts()
User.describe_user()


