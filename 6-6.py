"""6-6"""
favorite_languages = {
	'amada':'C',
	'jacky':'java',
	'frank':'c++',
	'polly':'php',
	'maily':'.net'
	}
lists = ['amada','jacky','mayun','admin']
surveied=[]
for person in favorite_languages.keys():
    surveied.append(person)
print(surveied)

for person in lists:
    if person in surveied:
        print("Thank you for your support")
    else:
        print("Please cooperate with us")

