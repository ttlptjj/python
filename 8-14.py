"""8-14"""
def car_message(factory,model,**elseinfor):
    car={}
    car['factory']=factory
    car['model']=model
    for key,value in elseinfor.items():
        car[key]=value

    return car

car=car_message('benchi','4s',color='black',tow_package=True)
print(car)
