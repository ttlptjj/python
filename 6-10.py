"""6-10"""
favorite_number={'dc':['2','6'],'zj':['8','7'],'jr':['4','3']}
for key,values in favorite_number.items():
    print(key+"最喜欢的数字是：")
    for value in values:
        print(value+' ')
