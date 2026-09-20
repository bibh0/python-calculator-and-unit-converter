#calculator v2 retry
#length
def to_meter(x):
	if from_unit == 'centimeter':
		meter=0.01*x
	elif from_unit == 'km':
		meter=1000*x
	elif from_unit == 'foot':
		meter=.3048*x
	elif from_unit == 'mile':
		meter= 1609.34*x
	elif from_unit == 'inch' :
		meter= 39.37*x
	elif from_unit == 'meter' :
		meter= x
	elif from_unit == 'micrometer':
		meter= 0.000001*x
	elif from_unit == 'nautical_mile':
		meter= 1852*x
	elif from_unit == 'yard':
		meter= 0.9144*x
	else:
		print("invalid input")
	return(meter)
imperial_length=['foot','miles','inch','yard']
metric_length=['centimeter','km','meter','micrometer','nautical_mile']

def from_meter(x):
	if to_unit=='centimeter':
		final_value = 100*x
	elif to_unit=='mile':
		final_value=0.0006214*x
	elif to_unit=='km':
		final_value=.001*x
	elif to_unit== 'foot':
		final_value=3.28*x
	elif to_unit=='inch':
		final_value=39.37*x
	elif to_unit=='meter':
		final_value=x
	elif to_unit=='micrometer':
		final_value=1000000*x
	elif to_unit=='nautical_mile':
		final_value=5.34*x
	elif to_unit=='yard':
		final_value=1.09*x
	else:
		print("Invalid input")
	return(final_value)

def to_inch(x):
	if from_unit=='foot':
		inch=12*x
	elif from_unit=='yard':
		inch=36*x
	elif from_unit=='inch':
		inch=x
	else:
		print("invalid input")
	return(inch)


def from_inch(x):
	if to_unit=='inch':
		final_value=x
	elif to_unit=='yard':
		final_value=x/36
	elif to_unit=='foot':
		final_value=x/12
	else:
		print("Invalid input")
	return(final_value)


#area

def to_sqmeter(x):
	if from_unit=='acre':
		metersq=x*4046.85
	elif from_unit=='sqmeter':
                metersq=x
	elif from_unit=='sqkm':
		metersq=x*1000000
	elif from_unit=='sqcm':
                metersq=x/10000
	elif from_unit=='sqmm':
                metersq=x/1000000
	elif from_unit=='hectre':
                metersq=10000*x
	elif from_unit=='sqft':
                metersq=0.093*x
	elif from_unit=='sqinch':
                metersq=x/1550
	elif from_unit=='sqyd':
                metersq=0.863*x
	else:
		print("invalid input")
	return(metersq)

imperial_area= ['acre','sqft','sqinch','sqyd']
metric_area= ['sqmeter','sqkm','sqcm','sqmm','hectre']


def from_sqmeter(x):
	if to_unit=='sqmeter':
		final_value=x
	elif to_unit=='acre':
		final_value=x/4046.85
	elif to_unit=='sqkm':
                final_value=x/1000000
	elif to_unit=='sqcm':
                final_value=x*10000
	elif to_unit=='sqmm':
                final_value=x*1000000
	elif to_unit=='hectre':
                final_value=x/10000
	elif to_unit=='sqft':
                final_value=x/0.093
	elif to_unit=='sqinch':
                final_value=x*1550
	elif to_unit=='sqyd':
                final_value=x/0.863
	else:
		print("invalid_input")
	return(final_value)

def to_sqinch(x):
	if from_unit=='sqinch':
		sqinch=x
	elif from_unit=='sqft':
		sqinch=144*x
	elif from_unit=='acre':
		sqinch=6272640*x
	elif from_unit=='sqyd':
		sqinch=1296*x
	else:
		print("Invalid input")
	return(sqinch)

def from_sqinch(x):
        if to_unit=='sqinch':
                final_value=x
        elif to_unit=='sqft':
                final_value=x/144
        elif to_unit=='acre':
                final_value=x/6272640
        elif to_unit=='sqyd':
                final_value=x/1296
        else:
                print("Invalid input")
        return(final_value)



#volume
def to_cubicmeter(x):
	if from_unit=='litre':
		cubicmeter=x/1000
	elif from_unit=='USgallon':
		cubicmeter=x/264.172
	elif from_unit=='UKgallon':
                cubicmeter=x/219.97
	elif from_unit=='ml':
                cubicmeter=x/1000000
	elif from_unit=='cubiccm':
                cubicmeter=x/1000000
	elif from_unit=='cubicinch':
                cubicmeter=x/61023.744
	elif from_unit=='cubicft':
                cubicmeter=x/35.31467
	elif from_unit=='cubicmeter':
                cubicmeter=x
	else:
		print("Invalid input")
	return(cubicmeter)


imperial_volume=['USgallon','cubicinch','cubicft']
metric_volume=['litre','UKgallon','ml','cubiccm','cubicmeter']


def from_cubicmeter(x):
	if to_unit=='litre':
                final_value=x*1000
	elif to_unit=='USgallon':
                final_value=x*264.172
	elif to_unit=='UKgallon':
                final_value=x*219.97
	elif to_unit=='ml':
                final_value=x*1000000
	elif to_unit=='cubiccm':
                final_value=x*1000000
	elif to_unit=='cubicinch':
                final_value=x*61023.744
	elif to_unit=='cubicft':
                final_value=x*35.31467
	elif to_unit=='cubicmeter':
                final_value=x
	else:
                print("Invalid input")
	return(final_value)


def to_cubicinch(x):
	if from_unit=='USgallon':
		cbinch=231*x
	elif from_unit=='cubicft':
		cbinch=1728*x
	elif from_unit=='cubicinch':
		cbinch=x
	else:
                print("Invalid input")
	return(cbinch)

def from_cubicinch(x):
	if to_unit=='USgallon':
                final_value=x/231
	elif to_unit=='cubicft':
                final_value=x/1728
	elif to_unit=='cubicinch':
                final_value=x
	else:
             	print("Invalid input")
	return(final_value)

#time month is taken 30days and year is taken 365
def to_sec(x):
	if from_unit=='sec':
		sec=x
	elif from_unit=='hour':
		sec=3600*x
	elif from_unit=='minute':
                sec=60*x
	elif from_unit=='millisecond':
                sec=0.001*x
	elif from_unit=='day':
                sec=86400*x
	elif from_unit=='week':
                sec=604800*x
	elif from_unit=='month':
                sec=86400*30*x
	elif from_unit=='year':
                sec=86400*365*x
	else:
		print("Invalid input")
	return(sec)

def from_sec(x):
	if to_unit=='sec':
		final_value=x
	elif to_unit=='hour':
                final_value=x/3600
	elif to_unit=='minute':
                final_value=x/60
	elif to_unit=='millisecond':
                final_value=x*1000
	elif to_unit=='day':
                final_value=x/86400
	elif to_unit=='week':
                final_value=x/604800
	elif to_unit=='month':
                final_value=x/2592000
	elif to_unit=='year':
                final_value=x/31536000
	else:
		print("Invalid input")
	return(final_value)

time=['sec','hour','minute','millisecond','day','week','month','year']
#temprature

def to_celcius(x):
	if from_unit=='celcius':
               cel=x
	elif from_unit=='farenhit':
                cel=((x-32)*9)/5
	elif from_unit=='kelvin':
                cel=x-273.15
	else:
                print("Invalid input")
	return(cel)

def from_celcius(x):
	if to_unit=='celcius':
                final_value=x
	elif to_unit=='farenhit':
                final_value=(1.8*x)+32
	elif to_unit=='kelvin':
                final_value=x+273.15
	else:
                print("Invalid input")
	return(final_value)

temprature=['celcius','farenhit','kelvin']
#weight

def to_kg(x):
	if from_unit=='kg':
                kg=x
	elif from_unit=='pound':
               kg =x/2.2046
	elif from_unit=='ounce':
                kg=x/35.274
	elif from_unit=='tonne':
                kg=x/0.001
	elif from_unit=='gram':
                kg=x/1000
	elif from_unit=='milligram':
                kg=x/1000000
	elif from_unit=='quintal':
                kg=x/0.01
	else:
                print("Invalid input")
	return(kg)


imperial_weight=['pound','ounce']
metric_weight=['kg','tonne','milligram','quintal']


def from_kg(x):
	if to_unit=='kg':
                final_value=x
	elif to_unit=='pound':
                final_value=x*2.2046
	elif to_unit=='ounce':
                final_value=x*35.274
	elif to_unit=='tonne':
                final_value=x*0.001
	elif to_unit=='quintal':
                final_value=x*0.01
	elif to_unit=='gram':
                final_value=x*1000
	elif to_unit=='milligram':
                final_value=x*1000000
	else:
                print("Invalid input")
	return(final_value)

def to_oz(x):
	if from_unit=='ounce':
		oz=x
	elif from_unit=='pound':
		oz=16*x
	else:
                print("Invalid input")
	return(oz)

def from_oz(x):
	if to_unit=='ounce':
		final_value=x
	elif to_unit=='pound':
		final_value=x/16
	else:
                print("Invalid input")
	return(final_value)

#general calculations
def addition(x,y):
	ans = x+y
	return(ans)

def subtraction(x,y):
	ans=x-y
	return(ans)

def multiplication(x,y):
	ans=x*y
	return(ans)

def division(x,y):
    list1=[]
    q=x//y
    remainder=(x%y)
    ans=x/y
    list1 = list1 + [q] +[remainder] + [ans]
    return(list1)
def factorial(x):
    if x<=1:
        ans=1
        return(ans)
    else:
        ans= x*factorial(x-1)
        return(ans)

def sqof(x):
    ans=x**2
    return(ans)

def cubeof(x):
    ans=x**3
    return(ans)
    
def xtothepowery(x,y):
    ans=x**y
    return(ans)

def ypercentofx(x,y):
    ans=x*0.01*y
    return(ans)




history=[]
user_calculation_or_conversion=input("calculation(1) or conversion(2)? :")
#calculations
if user_calculation_or_conversion=='calculation' or user_calculation_or_conversion=='1':
    user_calculation_need=input("Choose operation\nsum,minus,multiply,divide,percentage\nsquare,cube,x to the power y, factorial:")
    if user_calculation_need=='sum':
        print("sum of x and y.")
        a=float(input("Enter x:"))
        b=float(input("Enter y:"))
        ans=addition(a,b)
        history.append(str(a)+" + "+str(b)+" = "+str(ans))
        print(str(a)+" + "+str(b)+" = "+str(ans))
    elif user_calculation_need=='minus':
        print("subtract y from x.")
        b=float(input("Enter y:"))
        a=float(input("Enter x:"))
        ans=subtraction(a,b)
        history.append(str(a)+" - "+str(b)+" = "+str(ans))
        print(str(a)+" - "+str(b)+" = "+str(ans))
    elif user_calculation_need=='multiply':
        print("multiply x with y.")
        a=float(input("Enter x:"))
        b=float(input("Enter y:"))
        ans=multiplication(a,b)
        history.append(str(a)+" x "+str(b)+" = "+str(ans))
        print(str(a)+" x "+str(b)+" = "+str(ans))
    elif user_calculation_need=='divide':
        while True:
            print("Divide x by y.")
            a=float(input("Enter x:"))
            b=float(input("Enter y:"))
            if b==0:
                print("Invalid operation")
            else:
                ans=division(a,b)
                history.append(str(a)+"/"+str(b)+" results in quotient,remainder and answer as "+str(ans))
            print(str(a)+"/"+str(b)+" results in quotient,remainder and answer as "+str(ans))
            break
    elif user_calculation_need=='factorial':
        print("Factorial of x.")
        a=int(input("Enter x:"))
        ans=factorial(a)
        history.append(str(a)+" + "+str(b)+" = "+str(ans))
        print(str(a)+" + "+str(b)+" = "+str(ans))
    elif user_calculation_need=='percentage':
        print("y percent of x.")
        b=float(input("Enter y:"))
        a=float(input("Enter x:"))
        ans=ypercentofx(a,b)
        history.append(str(a)+" x "+str(b)+"% = "+str(ans))
        print(str(a)+" x "+str(b)+"% = "+str(ans))
    elif user_calculation_need=='square':
        print("Square of x.")
        a=float(input("Enter x:"))
        ans=sqof(a)
        history.append(str(a)+"^2 = "+str(ans))
        print(str(a)+"^2 = "+str(ans))
    elif user_calculation_need=='cube':
        print("Cube of x.")
        a=float(input("Enter x:"))
        ans=cubeof(a)
        history.append(str(a)+"^3 = "+str(ans))
        print(str(a)+"^3 = "+str(ans))
    elif user_calculation_need=='x to the power y':
        a=float(input("Enter x:"))
        b=float(input("Enter y:"))
        ans=xtothepowery(a,b)
        history.append(str(a)+"^"+str(b)+" = "+str(ans))
        print(str(a)+"^"+str(b)+" = "+str(ans))
    else:
        print("Invalid Input")
elif user_calculation_or_conversion=='conversion' or user_calculation_or_conversion=='2':
    conv=input("Choose Data type\n(length,area,volume,time,temprature,weight):")
    if conv=='length':
        from_unit=input("please enter your from unit "+str(imperial_length)+str(metric_length)+":")
        value= float(input("Please enter your value:"))
        to_unit=input("please enter your to unit "+str(imperial_length)+str(metric_length)+":")
        if from_unit in imperial_length and to_unit in imperial_length:
            ans=from_inch(to_inch(value))
        else:
            ans=from_meter(to_meter(value))
    elif conv=='volume':
        from_unit=input("please enter your from unit "+str(imperial_volume)+str(metric_volume)+":")
        value= float(input("Please enter your value:"))
        to_unit=input("please enter your to unit "+str(imperial_volume)+str(metric_volume)+":")
        if from_unit in imperial_volume and to_unit in imperial_volume:
            ans=from_cubicinch(to_cubicinch(value,from_unit),to_unit)
        else:
            ans=from_cubicmeter(to_cubicmeter(value,from_unit),to_unit)
    elif conv=='area':
        from_unit=input("please enter your from unit "+str(imperial_area)+str(metric_area)+":")
        value= float(input("Please enter your value:"))
        to_unit=input("please enter your to unit "+str(imperial_area)+str(metric_area)+":")
        if from_unit in imperial_volume and to_unit in imperial_volume:
            ans=from_sqinchinch(to_sqinch(value))
        else:
            ans=from_sqmeter(to_sqmeter(value))
    elif conv=='time':
        from_unit=input("please enter your from unit "+str(time)+":")
        value= float(input("Please enter your value:"))
        to_unit=input("please enter your to unit "+str(time)+":")
        ans=from_sec(to_sec(value))
    elif conv=='temprature':
        from_unit=input("please enter your from unit "+str(temprature)+":")
        value= float(input("Please enter your value:"))
        to_unit=input("please enter your to unit "+str(temprature)+":")
        ans=from_celcius(to_celcius(value,from_unit),to_unit)
    elif conv=='weight':
        from_unit=input("please enter your from unit "+str(imperial_weight)+str(metric_weight)+":")
        value= float(input("Please enter your value:"))
        to_unit=input("please enter your to unit "+str(imperial_weight)+str(metric_weight)+":")
        if from_unit in imperial_weight and to_unit in imperial_weight:
            ans=from_oz(to_oz(value,from_unit),to_unit)
        else:
            ans=from_kg(to_kg(value,from_unit),to_unit)
    else:
        print("Invalid input")
    history.append(str(value)+" "+str(from_unit)+" = "+str(ans) +" "+str(to_unit))
    print(str(value)+" "+str(from_unit)+" = "+str(ans) +" "+str(to_unit))
else:
    print("Invalid input")
while True:
    next1=input("what next ?\n[continue and ask every time(1), end(2), calculation only(3), conversion only(4), print history(5)]:")
    if next1=='end' or next1=='2':
        print("Thank you for using calculator")
        break
    elif next1=='continue and ask every time' or next1=='1':
        while True:
            next2=input("what next ?\n[calculation (1), conversion (2), end (3), print history(4)]:")
            if next2=='calculation' or next2=='1':
                from_or_fresh=input("fresh (1) or from ((continue from last)) (2)or print history(3):")
                if from_or_fresh=='from' or from_or_fresh=='2':
                    user_calculation_need=input("Choose operation\nsum,minus,multiply,divide,percentage\nsquare,cube,x to the power y, factorial:")
                    if user_calculation_need=='sum':
                        print("sum of x and y.")
                        a=ans
                        b=float(input("Enter y:"))
                        ans=addition(a,b)
                        history.append(str(a)+" + "+str(b)+" = "+str(ans))
                        print(str(a)+" + "+str(b)+" = "+str(ans))
                    elif user_calculation_need=='minus':
                        print("subtract y from x.")
                        b=float(input("Enter y:"))
                        a=ans
                        ans=subtraction(a,b)
                        history.append(str(a)+" - "+str(b)+" = "+str(ans))
                        print(str(a)+" - "+str(b)+" = "+str(ans))
                    elif user_calculation_need=='multiply':
                        print("multiply x with y.")
                        a=ans
                        b=float(input("Enter y:"))
                        ans=multiplication(a,b)
                        history.append(str(a)+" x "+str(b)+" = "+str(ans))
                        print(str(a)+" x "+str(b)+" = "+str(ans))
                    elif user_calculation_need=='divide':
                        while True:
                            print("Divide x by y.")
                            a=ans
                            b=float(input("Enter y:"))
                            if b==0:
                                print("Invalid operation")
                            else:
                                ans=division(a,b)
                                history.append(str(a)+"/"+str(b)+" results in quotient,remainder and answer as "+str(ans))
                            print(str(a)+"/"+str(b)+" results in quotient,remainder and answer as "+str(ans))
                            break
                    elif user_calculation_need=='factorial':
                        print("Factorial of x.")
                        a=int(ans)
                        ans=factorial(a)
                        history.append(str(int(a))+" + "+str(b)+" = "+str(ans))
                        print(str(a)+" + "+str(b)+" = "+str(ans))
                    elif user_calculation_need=='percentage':
                        print("y percent of x.")
                        b=float(input("Enter y:"))
                        a=ans
                        ans=ypercentofx(a,b)
                        history.append(str(a)+" x "+str(b)+"% = "+str(ans))
                        print(str(a)+" x "+str(b)+"% = "+str(ans))
                    elif user_calculation_need=='square':
                        print("Square of x.")
                        a=ans
                        ans=sqof(a)
                        history.append(str(a)+"^2 = "+str(ans))
                        print(str(a)+"^2 = "+str(ans))
                    elif user_calculation_need=='cube':
                        print("Cube of x.")
                        a=ans
                        ans=cubeof(a)
                        history.append(str(a)+"^3 = "+str(ans))
                        print(str(a)+"^3 = "+str(ans))
                    elif user_calculation_need=='x to the power y':
                        a=ans
                        b=float(input("Enter y:"))
                        ans=xtothepowery(a,b)
                        history.append(str(a)+"^"+str(b)+" = "+str(ans))
                        print(str(a)+"^"+str(b)+" = "+str(ans))
                    else:
                        print("Invalid Input")
                elif from_or_fresh=='fresh' or from_or_fresh=='1':
                    user_calculation_need=input("Choose operation\nsum,minus,multiply,divide,percentage\nsquare,cube,x to the power y, factorial:")
                    if user_calculation_need=='sum':
                        print("sum of x and y.")
                        a=float(input("Enter x:"))
                        b=float(input("Enter y:"))
                        ans=addition(a,b)
                        history.append(str(a)+" + "+str(b)+" = "+str(ans))
                        print(str(a)+" + "+str(b)+" = "+str(ans))
                    elif user_calculation_need=='minus':
                        print("subtract y from x.")
                        b=float(input("Enter y:"))
                        a=float(input("Enter x:"))
                        ans=subtraction(a,b)
                        history.append(str(a)+" - "+str(b)+" = "+str(ans))
                        print(str(a)+" - "+str(b)+" = "+str(ans))
                    elif user_calculation_need=='multiply':
                        print("multiply x with y.")
                        a=float(input("Enter x:"))
                        b=float(input("Enter y:"))
                        ans=multiplication(a,b)
                        history.append(str(a)+" x "+str(b)+" = "+str(ans))
                        print(str(a)+" x "+str(b)+" = "+str(ans))
                    elif user_calculation_need=='divide':
                        while True:
                            print("Divide x by y.")
                            a=float(input("Enter x:"))
                            b=float(input("Enter y:"))
                            if b==0:
                                print("Invalid operation")
                            else:
                                ans=division(a,b)
                                history.append(str(a)+"/"+str(b)+" results in quotient,remainder and answer as "+str(ans))
                            print(str(a)+"/"+str(b)+" results in quotient,remainder and answer as "+str(ans))
                            break
                    elif user_calculation_need=='factorial':
                        print("Factorial of x.")
                        a=int(input("Enter x:"))
                        ans=factorial(a)
                        history.append(str(a)+" + "+str(b)+" = "+str(ans))
                        print(str(a)+" + "+str(b)+" = "+str(ans))
                    elif user_calculation_need=='percentage':
                        print("y percent of x.")
                        b=float(input("Enter y:"))
                        a=float(input("Enter x:"))
                        ans=ypercentofx(a,b)
                        history.append(str(a)+" x "+str(b)+"% = "+str(ans))
                        print(str(a)+" x "+str(b)+"% = "+str(ans))
                    elif user_calculation_need=='square':
                        print("Square of x.")
                        a=float(input("Enter x:"))
                        ans=sqof(a)
                        history.append(str(a)+"^2 = "+str(ans))
                        print(str(a)+"^2 = "+str(ans))
                    elif user_calculation_need=='cube':
                        print("Cube of x.")
                        a=float(input("Enter x:"))
                        ans=cubeof(a)
                        history.append(str(a)+"^3 = "+str(ans))
                        print(str(a)+"^3 = "+str(ans))
                    elif user_calculation_need=='x to the power y':
                        a=float(input("Enter x:"))
                        b=float(input("Enter y:"))
                        ans=xtothepowery(a,b)
                        history.append(str(a)+"^"+str(b)+" = "+str(ans))
                        print(str(a)+"^"+str(b)+" = "+str(ans))
                    else:
                        print("Invalid Input")
                elif from_or_fresh=='print history' or from_or_fresh=='3':
                    for x in history:
                        print(x)
                else:
                    print("Invalid Input")
            elif next2=='conversion' or next2=='2':
                from_or_fresh=input("fresh (1) or from ((continue from last)) (2) or print history (3):")
                if from_or_fresh=='from' or from_or_fresh=='2':
                    conv=input("Choose Data type\n(length,area,volume,time,temprature,weight):")
                    if conv=='length':
                        from_unit=input("please enter your from unit "+str(imperial_length)+str(metric_length)+":")
                        value=ans
                        to_unit=input("please enter your to unit "+str(imperial_length)+str(metric_length)+":")
                        if from_unit in imperial_length and to_unit in imperial_length:
                            ans=from_inch(to_inch(value))
                        else:
                            ans=from_meter(to_meter(value))
                    elif conv=='volume':
                        from_unit=input("please enter your from unit "+str(imperial_volume)+str(metric_volume)+":")
                        value=ans
                        to_unit=input("please enter your to unit "+str(imperial_volume)+str(metric_volume)+":")
                        if from_unit in imperial_volume and to_unit in imperial_volume:
                            ans=from_cubicinch(to_cubicinch(value,from_unit),to_unit)
                        else:
                            ans=from_cubicmeter(to_cubicmeter(value,from_unit),to_unit)
                    elif conv=='area':
                        from_unit=input("please enter your from unit "+str(imperial_area)+str(metric_area)+":")
                        value=ans
                        to_unit=input("please enter your to unit "+str(imperial_area)+str(metric_area)+":")
                        if from_unit in imperial_area and to_unit in imperial_area:
                            ans=from_sqinchinch(to_sqinch(value))
                        else:
                            ans=from_sqmeter(to_sqmeter(value))
                    elif conv=='time':
                        from_unit=input("please enter your from unit "+str(time)+":")
                        value=ans
                        to_unit=input("please enter your to unit "+str(time)+":")
                        ans=from_sec(to_sec(value))
                    elif conv=='temprature':
                        from_unit=input("please enter your from unit "+str(temprature)+":")
                        value=ans
                        to_unit=input("please enter your to unit "+str(temprature)+":")
                        ans=from_celcius(to_celcius(value,from_unit),to_unit)
                    elif conv=='weight':
                        from_unit=input("please enter your from unit "+str(imperial_weight)+str(metric_weight)+":")
                        value=ans
                        to_unit=input("please enter your to unit "+str(imperial_weight)+str(metric_weight)+":")
                        if from_unit in imperial_weight and to_unit in imperial_weight:
                            ans=from_oz(to_oz(value,from_unit),to_unit)
                        else:
                            ans=from_kg(to_kg(value,from_unit),to_unit)
                    else:
                        print("Invalid input")
                    history.append(str(value)+" "+str(from_unit)+" = "+str(ans) +" "+str(to_unit))
                    print(str(value)+" "+str(from_unit)+" = "+str(ans) +" "+str(to_unit))
                elif from_or_fresh=='fresh' or from_or_fresh=='1':
                    conv=input("Choose Data type\n(length,area,volume,time,temprature,weight):")
                    if conv=='length':
                        from_unit=input("please enter your from unit "+str(imperial_length)+str(metric_length)+":")
                        value= float(input("Please enter your value:"))
                        to_unit=input("please enter your to unit "+str(imperial_length)+str(metric_length)+":")
                        if from_unit in imperial_length and to_unit in imperial_length:
                            ans=from_inch(to_inch(value))
                        else:
                            ans=from_meter(to_meter(value))
                    elif conv=='volume':
                        from_unit=input("please enter your from unit "+str(imperial_volume)+str(metric_volume)+":")
                        value= float(input("Please enter your value:"))
                        to_unit=input("please enter your to unit "+str(imperial_volume)+str(metric_volume)+":")
                        if from_unit in imperial_volume and to_unit in imperial_volume:
                            ans=from_cubicinch(to_cubicinch(value,from_unit),to_unit)
                        else:
                            ans=from_cubicmeter(to_cubicmeter(value,from_unit),to_unit)
                    elif conv=='area':
                        from_unit=input("please enter your from unit "+str(imperial_area)+str(metric_area)+":")
                        value= float(input("Please enter your value:"))
                        to_unit=input("please enter your to unit "+str(imperial_area)+str(metric_area)+":")
                        if from_unit in imperial_volume and to_unit in imperial_volume:
                            ans=from_sqinchinch(to_sqinch(value))
                        else:
                            ans=from_sqmeter(to_sqmeter(value))
                    elif conv=='time':
                        from_unit=input("please enter your from unit "+str(time)+":")
                        value= float(input("Please enter your value:"))
                        to_unit=input("please enter your to unit "+str(time)+":")
                        ans=from_sec(to_sec(value))
                    elif conv=='temprature':
                        from_unit=input("please enter your from unit "+str(temprature)+":")
                        value= float(input("Please enter your value:"))
                        to_unit=input("please enter your to unit "+str(temprature)+":")
                        ans=from_celcius(to_celcius(value,from_unit),to_unit)
                    elif conv=='weight':
                        from_unit=input("please enter your from unit "+str(imperial_weight)+str(metric_weight)+":")
                        value= float(input("Please enter your value:"))
                        to_unit=input("please enter your to unit "+str(imperial_weight)+str(metric_weight)+":")
                        if from_unit in imperial_weight and to_unit in imperial_weight:
                            ans=from_oz(to_oz(value,from_unit),to_unit)
                        else:
                            ans=from_kg(to_kg(value,from_unit),to_unit)
                    else:
                        print("Invalid input")
                    history.append(str(value)+" "+str(from_unit)+" = "+str(ans) +" "+str(to_unit))
                    print(str(value)+" "+str(from_unit)+" = "+str(ans) +" "+str(to_unit))
                elif from_or_fresh=='print history' or from_or_fresh=='3':
                    for x in history:
                        print(x)
                else:
                        print("Invalid Input")
            elif next2== 'end' or next2=='3':
                print("Thank you for using calculator")
                break
            elif next2=='print history' or next2=='4':
                for x in history:
                    print(x)
            else:
                print("Invalid Input")
    elif next1=='print history' or next1=='5':
        for x in history:
            print(x)
    elif next1=='calculation only' or next1=='3':
        next2=input("How would you like your calculations to proceed?\n[ask every time (1), fresh only (2), from only (3), print history(4)]:")
        if next2=='ask every time'  or next2=='1':
            while True:
                from_or_fresh=input("from (1)//continue from last// or fresh (2) or end (3) or print history (4):")
                if from_or_fresh=='fresh' or from_or_fresh=='2':
                    user_calculation_need=input("Choose operation\nsum,minus,multiply,divide,percentage\nsquare,cube,x to the power y, factorial:")
                    if user_calculation_need=='sum':
                        print("sum of x and y.")
                        a=float(input("Enter x:"))
                        b=float(input("Enter y:"))
                        ans=addition(a,b)
                        history.append(str(a)+" + "+str(b)+" = "+str(ans))
                        print(str(a)+" + "+str(b)+" = "+str(ans))
                    elif user_calculation_need=='minus':
                        print("subtract y from x.")
                        b=float(input("Enter y:"))
                        a=float(input("Enter x:"))
                        ans=subtraction(a,b)
                        history.append(str(a)+" - "+str(b)+" = "+str(ans))
                        print(str(a)+" - "+str(b)+" = "+str(ans))
                    elif user_calculation_need=='multiply':
                        print("multiply x with y.")
                        a=float(input("Enter x:"))
                        b=float(input("Enter y:"))
                        ans=multiplication(a,b)
                        history.append(str(a)+" x "+str(b)+" = "+str(ans))
                        print(str(a)+" x "+str(b)+" = "+str(ans))
                    elif user_calculation_need=='divide':
                        while True:
                            print("Divide x by y.")
                            a=float(input("Enter x:"))
                            b=float(input("Enter y:"))
                            if b==0:
                                print("Invalid operation")
                            else:
                                ans=division(a,b)
                                history.append(str(a)+"/"+str(b)+" results in quotient,remainder and answer as "+str(ans))
                            print(str(a)+"/"+str(b)+" results in quotient,remainder and answer as "+str(ans))
                            break
                    elif user_calculation_need=='factorial':
                        print("Factorial of x.")
                        a=int(input("Enter x:"))
                        ans=factorial(a)
                        history.append(str(a)+" + "+str(b)+" = "+str(ans))
                        print(str(a)+" + "+str(b)+" = "+str(ans))
                    elif user_calculation_need=='percentage':
                        print("y percent of x.")
                        b=float(input("Enter y:"))
                        a=float(input("Enter x:"))
                        ans=ypercentofx(a,b)
                        history.append(str(a)+" x "+str(b)+"% = "+str(ans))
                        print(str(a)+" x "+str(b)+"% = "+str(ans))
                    elif user_calculation_need=='square':
                        print("Square of x.")
                        a=float(input("Enter x:"))
                        ans=sqof(a)
                        history.append(str(a)+"^2 = "+str(ans))
                        print(str(a)+"^2 = "+str(ans))
                    elif user_calculation_need=='cube':
                        print("Cube of x.")
                        a=float(input("Enter x:"))
                        ans=cubeof(a)
                        history.append(str(a)+"^3 = "+str(ans))
                        print(str(a)+"^3 = "+str(ans))
                    elif user_calculation_need=='x to the power y':
                        a=float(input("Enter x:"))
                        b=float(input("Enter y:"))
                        ans=xtothepowery(a,b)
                        history.append(str(a)+"^"+str(b)+" = "+str(ans))
                        print(str(a)+"^"+str(b)+" = "+str(ans))
                    else:
                        print("Invalid Input")
                elif from_or_fresh=='from' or from_or_fresh=='1':
                    user_calculation_need=input("Choose operation\nsum,minus,multiply,divide,percentage\nsquare,cube,x to the power y, factorial:")
                    if user_calculation_need=='sum':
                        print("sum of x and y.")
                        a=ans
                        b=float(input("Enter y:"))
                        ans=addition(a,b)
                        history.append(str(a)+" + "+str(b)+" = "+str(ans))
                        print(str(a)+" + "+str(b)+" = "+str(ans))
                    elif user_calculation_need=='minus':
                        print("subtract y from x.")
                        b=float(input("Enter y:"))
                        a=ans
                        ans=subtraction(a,b)
                        history.append(str(a)+" - "+str(b)+" = "+str(ans))
                        print(str(a)+" - "+str(b)+" = "+str(ans))
                    elif user_calculation_need=='multiply':
                        print("multiply x with y.")
                        a=ans
                        b=float(input("Enter y:"))
                        ans=multiplication(a,b)
                        history.append(str(a)+" x "+str(b)+" = "+str(ans))
                        print(str(a)+" x "+str(b)+" = "+str(ans))
                    elif user_calculation_need=='divide':
                        while True:
                            print("Divide x by y.")
                            a=ans
                            b=float(input("Enter y:"))
                            if b==0:
                                print("Invalid operation")
                            else:
                                ans=division(a,b)
                                history.append(str(a)+"/"+str(b)+" results in quotient,remainder and answer as "+str(ans))
                            print(str(a)+"/"+str(b)+" results in quotient,remainder and answer as "+str(ans))
                            break
                    elif user_calculation_need=='factorial':
                        print("Factorial of x.")
                        a=int(ans)
                        ans=factorial(a)
                        history.append(str(int(a))+" + "+str(b)+" = "+str(ans))
                        print(str(a)+" + "+str(b)+" = "+str(ans))
                    elif user_calculation_need=='percentage':
                        print("y percent of x.")
                        b=float(input("Enter y:"))
                        a=ans
                        ans=ypercentofx(a,b)
                        history.append(str(a)+" x "+str(b)+"% = "+str(ans))
                        print(str(a)+" x "+str(b)+"% = "+str(ans))
                    elif user_calculation_need=='square':
                        print("Square of x.")
                        a=ans
                        ans=sqof(a)
                        history.append(str(a)+"^2 = "+str(ans))
                        print(str(a)+"^2 = "+str(ans))
                    elif user_calculation_need=='cube':
                        print("Cube of x.")
                        a=ans
                        ans=cubeof(a)
                        history.append(str(a)+"^3 = "+str(ans))
                        print(str(a)+"^3 = "+str(ans))
                    elif user_calculation_need=='x to the power y':
                        a=ans
                        b=float(input("Enter y:"))
                        ans=xtothepowery(a,b)
                        history.append(str(a)+"^"+str(b)+" = "+str(ans))
                        print(str(a)+"^"+str(b)+" = "+str(ans))
                    else:
                        print("Invalid Input")
                elif from_or_fresh=='print history' or from_or_fresh=='4':
                    for x in history:
                        print(x)
                elif from_or_fresh=='end' or from_or_fresh=='3':
                    print("Thank you for using calculator")
                    break
                else:
                    print("Invalid Input")
        elif next1=='print history' or next1=='4':
            for x in history:
                print(x)
        elif next2== 'fresh only' or next2=='2':
            while True:
                end_or_continue=input("continue (1) or end (2) or print history (3):")
                if end_or_continue=='continue' or end_or_continue=='1':
                    user_calculation_need=input("Choose operation\nsum,minus,multiply,divide,percentage\nsquare,cube,x to the power y, factorial:")
                    if user_calculation_need=='sum':
                        print("sum of x and y.")
                        a=float(input("Enter x:"))
                        b=float(input("Enter y:"))
                        ans=addition(a,b)
                        history.append(str(a)+" + "+str(b)+" = "+str(ans))
                        print(str(a)+" + "+str(b)+" = "+str(ans))
                    elif user_calculation_need=='minus':
                        print("subtract y from x.")
                        b=float(input("Enter y:"))
                        a=float(input("Enter x:"))
                        ans=subtraction(a,b)
                        history.append(str(a)+" - "+str(b)+" = "+str(ans))
                        print(str(a)+" - "+str(b)+" = "+str(ans))
                    elif user_calculation_need=='multiply':
                        print("multiply x with y.")
                        a=float(input("Enter x:"))
                        b=float(input("Enter y:"))
                        ans=multiplication(a,b)
                        history.append(str(a)+" x "+str(b)+" = "+str(ans))
                        print(str(a)+" x "+str(b)+" = "+str(ans))
                    elif user_calculation_need=='divide':
                        while True:
                            print("Divide x by y.")
                            a=float(input("Enter x:"))
                            b=float(input("Enter y:"))
                            if b==0:
                                print("Invalid operation")
                            else:
                                ans=division(a,b)
                                history.append(str(a)+"/"+str(b)+" results in quotient,remainder and answer as "+str(ans))
                            print(str(a)+"/"+str(b)+" results in quotient,remainder and answer as "+str(ans))
                            break
                    elif user_calculation_need=='factorial':
                        print("Factorial of x.")
                        a=int(input("Enter x:"))
                        ans=factorial(a)
                        history.append(str(a)+" + "+str(b)+" = "+str(ans))
                        print(str(a)+" + "+str(b)+" = "+str(ans))
                    elif user_calculation_need=='percentage':
                        print("y percent of x.")
                        b=float(input("Enter y:"))
                        a=float(input("Enter x:"))
                        ans=ypercentofx(a,b)
                        history.append(str(a)+" x "+str(b)+"% = "+str(ans))
                        print(str(a)+" x "+str(b)+"% = "+str(ans))
                    elif user_calculation_need=='square':
                        print("Square of x.")
                        a=float(input("Enter x:"))
                        ans=sqof(a)
                        history.append(str(a)+"^2 = "+str(ans))
                        print(str(a)+"^2 = "+str(ans))
                    elif user_calculation_need=='cube':
                        print("Cube of x.")
                        a=float(input("Enter x:"))
                        ans=cubeof(a)
                        history.append(str(a)+"^3 = "+str(ans))
                        print(str(a)+"^3 = "+str(ans))
                    elif user_calculation_need=='x to the power y':
                        a=float(input("Enter x:"))
                        b=float(input("Enter y:"))
                        ans=xtothepowery(a,b)
                        history.append(str(a)+"^"+str(b)+" = "+str(ans))
                        print(str(a)+"^"+str(b)+" = "+str(ans))
                    else:
                        print("Invalid Input")
                elif end_or_continue=='print history' or end_or_continue=='3':
                    for x in history:
                        print(x)
                elif end_or_continue=='end' or end_or_continue=='2':
                    print("Thank you for using calculator")
                    break
                else:
                    print("Invalid Input")
        elif next2== 'from only'or next2=='3':
            while True:
                end_or_continue=input("continue (1) or end (2) or print history (3):")
                if end_or_continue=='continue' or end_or_continue=='1':
                    user_calculation_need=input("Choose operation\nsum,minus,multiply,divide,percentage\nsquare,cube,x to the power y, factorial:")
                    if user_calculation_need=='sum':
                        print("sum of x and y.")
                        a=ans
                        b=float(input("Enter y:"))
                        ans=addition(a,b)
                        history.append(str(a)+" + "+str(b)+" = "+str(ans))
                        print(str(a)+" + "+str(b)+" = "+str(ans))
                    elif user_calculation_need=='minus':
                        print("subtract y from x.")
                        b=float(input("Enter y:"))
                        a=ans
                        ans=subtraction(a,b)
                        history.append(str(a)+" - "+str(b)+" = "+str(ans))
                        print(str(a)+" - "+str(b)+" = "+str(ans))
                    elif user_calculation_need=='multiply':
                        print("multiply x with y.")
                        a=ans
                        b=float(input("Enter y:"))
                        ans=multiplication(a,b)
                        history.append(str(a)+" x "+str(b)+" = "+str(ans))
                        print(str(a)+" x "+str(b)+" = "+str(ans))
                    elif user_calculation_need=='divide':
                        while True:
                            print("Divide x by y.")
                            a=ans
                            b=float(input("Enter y:"))
                            if b==0:
                                print("Invalid operation")
                            else:
                                ans=division(a,b)
                                history.append(str(a)+"/"+str(b)+" results in quotient,remainder and answer as "+str(ans))
                            print(str(a)+"/"+str(b)+" results in quotient,remainder and answer as "+str(ans))
                            break
                    elif user_calculation_need=='factorial':
                        print("Factorial of x.")
                        a=int(ans)
                        ans=factorial(a)
                        history.append(str(int(a))+" + "+str(b)+" = "+str(ans))
                        print(str(a)+" + "+str(b)+" = "+str(ans))
                    elif user_calculation_need=='percentage':
                        print("y percent of x.")
                        b=float(input("Enter y:"))
                        a=ans
                        ans=ypercentofx(a,b)
                        history.append(str(a)+" x "+str(b)+"% = "+str(ans))
                        print(str(a)+" x "+str(b)+"% = "+str(ans))
                    elif user_calculation_need=='square':
                        print("Square of x.")
                        a=ans
                        ans=sqof(a)
                        history.append(str(a)+"^2 = "+str(ans))
                        print(str(a)+"^2 = "+str(ans))
                    elif user_calculation_need=='cube':
                        print("Cube of x.")
                        a=ans
                        ans=cubeof(a)
                        history.append(str(a)+"^3 = "+str(ans))
                        print(str(a)+"^3 = "+str(ans))
                    elif user_calculation_need=='x to the power y':
                        a=ans
                        b=float(input("Enter y:"))
                        ans=xtothepowery(a,b)
                        history.append(str(a)+"^"+str(b)+" = "+str(ans))
                        print(str(a)+"^"+str(b)+" = "+str(ans))
                    else:
                        print("Invalid Input")
                elif end_or_continue=='print history' or end_or_continue=='3':
                    for x in history:
                        print(x)
                elif end_or_continue=='end' or end_or_continue=='2':
                    print("Thank you for using calculator")
                    break
                else:
                    print("Invalid Input")
        else:
            print("Invalid Input")


    #conversion only
    elif next1=='conversion only' or next1=='4':
        next2=input("How would you like your calculations to proceed?\n[ask every time (1), fresh only (2),  from only (3), print history (4):")
        if next2=='ask every time' or next2=='1':
            while True:
                from_or_fresh=input("fresh (1)((continue from last)) or from (2) or end (3) or print history (4):")
                if from_or_fresh=='fresh' or from_or_fresh=='1':
                    conv=input("Choose Data type\n(length,area,volume,time,temprature,weight):")
                    if conv=='length':
                        from_unit=input("please enter your from unit "+str(imperial_length)+str(metric_length)+":")
                        value= float(input("Please enter your value:"))
                        to_unit=input("please enter your to unit "+str(imperial_length)+str(metric_length)+":")
                        if from_unit in imperial_length and to_unit in imperial_length:
                            ans=from_inch(to_inch(value))
                        else:
                            ans=from_meter(to_meter(value))
                    elif conv=='volume':
                        from_unit=input("please enter your from unit "+str(imperial_volume)+str(metric_volume)+":")
                        value= float(input("Please enter your value:"))
                        to_unit=input("please enter your to unit "+str(imperial_volume)+str(metric_volume)+":")
                        if from_unit in imperial_volume and to_unit in imperial_volume:
                            ans=from_cubicinch(to_cubicinch(value,from_unit),to_unit)
                        else:
                            ans=from_cubicmeter(to_cubicmeter(value,from_unit),to_unit)
                    elif conv=='area':
                        from_unit=input("please enter your from unit "+str(imperial_area)+str(metric_area)+":")
                        value= float(input("Please enter your value:"))
                        to_unit=input("please enter your to unit "+str(imperial_area)+str(metric_area)+":")
                        if from_unit in imperial_volume and to_unit in imperial_volume:
                            ans=from_sqinchinch(to_sqinch(value))
                        else:
                            ans=from_sqmeter(to_sqmeter(value))
                    elif conv=='time':
                        from_unit=input("please enter your from unit "+str(time)+":")
                        value= float(input("Please enter your value:"))
                        to_unit=input("please enter your to unit "+str(time)+":")
                        ans=from_sec(to_sec(value))
                    elif conv=='temprature':
                        from_unit=input("please enter your from unit "+str(temprature)+":")
                        value= float(input("Please enter your value:"))
                        to_unit=input("please enter your to unit "+str(temprature)+":")
                        ans=from_celcius(to_celcius(value,from_unit),to_unit)
                    elif conv=='weight':
                        from_unit=input("please enter your from unit "+str(imperial_weight)+str(metric_weight)+":")
                        value= float(input("Please enter your value:"))
                        to_unit=input("please enter your to unit "+str(imperial_weight)+str(metric_weight)+":")
                        if from_unit in imperial_weight and to_unit in imperial_weight:
                            ans=from_oz(to_oz(value,from_unit),to_unit)
                        else:
                            ans=from_kg(to_kg(value,from_unit),to_unit)
                    else:
                        print("Invalid input")
                    history.append(str(value)+" "+str(from_unit)+" = "+str(ans) +" "+str(to_unit))
                    print(str(value)+" "+str(from_unit)+" = "+str(ans) +" "+str(to_unit))
                elif next2=='print history' or next2=='4':
                    for x in history:
                        print(x)
                elif from_or_fresh=='from' or from_or_fresh=='2':
                    conv=input("Choose Data type\n(length,area,volume,time,temprature,weight):")
                    if conv=='length':
                        from_unit=input("please enter your from unit "+str(imperial_length)+str(metric_length)+":")
                        value=ans
                        to_unit=input("please enter your to unit "+str(imperial_length)+str(metric_length)+":")
                        if from_unit in imperial_length and to_unit in imperial_length:
                            ans=from_inch(to_inch(value))
                        else:
                            ans=from_meter(to_meter(value))
                    elif conv=='volume':
                        from_unit=input("please enter your from unit "+str(imperial_volume)+str(metric_volume)+":")
                        value=ans
                        to_unit=input("please enter your to unit "+str(imperial_volume)+str(metric_volume)+":")
                        if from_unit in imperial_volume and to_unit in imperial_volume:
                            ans=from_cubicinch(to_cubicinch(value,from_unit),to_unit)
                        else:
                            ans=from_cubicmeter(to_cubicmeter(value,from_unit),to_unit)
                    elif conv=='area':
                        from_unit=input("please enter your from unit "+str(imperial_area)+str(metric_area)+":")
                        value=ans
                        to_unit=input("please enter your to unit "+str(imperial_area)+str(metric_area)+":")
                        if from_unit in imperial_area and to_unit in imperial_area:
                            ans=from_sqinchinch(to_sqinch(value))
                        else:
                            ans=from_sqmeter(to_sqmeter(value))
                    elif conv=='time':
                        from_unit=input("please enter your from unit "+str(time)+":")
                        value=ans
                        to_unit=input("please enter your to unit "+str(time)+":")
                        ans=from_sec(to_sec(value))
                    elif conv=='temprature':
                        from_unit=input("please enter your from unit "+str(temprature)+":")
                        value=ans
                        to_unit=input("please enter your to unit "+str(temprature)+":")
                        ans=from_celcius(to_celcius(value,from_unit),to_unit)
                    elif conv=='weight':
                        from_unit=input("please enter your from unit "+str(imperial_weight)+str(metric_weight)+":")
                        value=ans
                        to_unit=input("please enter your to unit "+str(imperial_weight)+str(metric_weight)+":")
                        if from_unit in imperial_weight and to_unit in imperial_weight:
                            ans=from_oz(to_oz(value,from_unit),to_unit)
                        else:
                            ans=from_kg(to_kg(value,from_unit),to_unit)
                    else:
                        print("Invalid input")
                    history.append(str(value)+" "+str(from_unit)+" = "+str(ans) +" "+str(to_unit))
                    print(str(value)+" "+str(from_unit)+" = "+str(ans) +" "+str(to_unit))
                elif from_or_fresh=='end' or from_or_fresh=='3':
                    print("Thank you for using calculator")
                    break
                else:
                    print("Invalid Input")
        elif next2=='print history' or next2=='4':
            for x in history:
                print(x)
        elif next2== 'fresh only' or next2=='2':
            while True:
                end_or_continue=input("continue (1) or end (2) or print history (3):")
                if end_or_continue=='continue' or end_or_continue=='1':
                    conv=input("Choose Data type\n(length,area,volume,time,temprature,weight):")
                    if conv=='length':
                        from_unit=input("please enter your from unit "+str(imperial_length)+str(metric_length)+":")
                        value= float(input("Please enter your value:"))
                        to_unit=input("please enter your to unit "+str(imperial_length)+str(metric_length)+":")
                        if from_unit in imperial_length and to_unit in imperial_length:
                            ans=from_inch(to_inch(value))
                        else:
                            ans=from_meter(to_meter(value))
                    elif conv=='volume':
                        from_unit=input("please enter your from unit "+str(imperial_volume)+str(metric_volume)+":")
                        value= float(input("Please enter your value:"))
                        to_unit=input("please enter your to unit "+str(imperial_volume)+str(metric_volume)+":")
                        if from_unit in imperial_volume and to_unit in imperial_volume:
                            ans=from_cubicinch(to_cubicinch(value,from_unit),to_unit)
                        else:
                            ans=from_cubicmeter(to_cubicmeter(value,from_unit),to_unit)
                    elif conv=='area':
                        from_unit=input("please enter your from unit "+str(imperial_area)+str(metric_area)+":")
                        value= float(input("Please enter your value:"))
                        to_unit=input("please enter your to unit "+str(imperial_area)+str(metric_area)+":")
                        if from_unit in imperial_volume and to_unit in imperial_volume:
                            ans=from_sqinchinch(to_sqinch(value))
                        else:
                            ans=from_sqmeter(to_sqmeter(value))
                    elif conv=='time':
                        from_unit=input("please enter your from unit "+str(time)+":")
                        value= float(input("Please enter your value:"))
                        to_unit=input("please enter your to unit "+str(time)+":")
                        ans=from_sec(to_sec(value))
                    elif conv=='temprature':
                        from_unit=input("please enter your from unit "+str(temprature)+":")
                        value= float(input("Please enter your value:"))
                        to_unit=input("please enter your to unit "+str(temprature)+":")
                        ans=from_celcius(to_celcius(value,from_unit),to_unit)
                    elif conv=='weight':
                        from_unit=input("please enter your from unit "+str(imperial_weight)+str(metric_weight)+":")
                        value= float(input("Please enter your value:"))
                        to_unit=input("please enter your to unit "+str(imperial_weight)+str(metric_weight)+":")
                        if from_unit in imperial_weight and to_unit in imperial_weight:
                            ans=from_oz(to_oz(value,from_unit),to_unit)
                        else:
                            ans=from_kg(to_kg(value,from_unit),to_unit)
                    else:
                        print("Invalid input")
                    history.append(str(value)+" "+str(from_unit)+" = "+str(ans) +" "+str(to_unit))
                    print(str(value)+" "+str(from_unit)+" = "+str(ans) +" "+str(to_unit))
                elif end_or_continue=='print history' or end_or_continue=='3':
                    for x in history:
                        print(x)
                elif end_or_continue=='end' or end_or_continue=='2':
                    print("Thank you for using calculator")
                    break
                else:
                    print("Invalid Input")
        elif next2== 'from only'or next2=='3':
            while True:
                end_or_continue=input("continue (1) or end (2) or print history (3):")
                if end_or_continue=='continue' or end_or_continue=='1':
                    conv=input("Choose Data type\n(length,area,volume,time,temprature,weight):")
                    if conv=='length':
                        from_unit=input("please enter your from unit "+str(imperial_length)+str(metric_length)+":")
                        value=ans
                        to_unit=input("please enter your to unit "+str(imperial_length)+str(metric_length)+":")
                        if from_unit in imperial_length and to_unit in imperial_length:
                            ans=from_inch(to_inch(value))
                        else:
                            ans=from_meter(to_meter(value))
                    elif conv=='volume':
                        from_unit=input("please enter your from unit "+str(imperial_volume)+str(metric_volume)+":")
                        value=ans
                        to_unit=input("please enter your to unit "+str(imperial_volume)+str(metric_volume)+":")
                        if from_unit in imperial_volume and to_unit in imperial_volume:
                            ans=from_cubicinch(to_cubicinch(value,from_unit),to_unit)
                        else:
                            ans=from_cubicmeter(to_cubicmeter(value,from_unit),to_unit)
                    elif conv=='area':
                        from_unit=input("please enter your from unit "+str(imperial_area)+str(metric_area)+":")
                        value=ans
                        to_unit=input("please enter your to unit "+str(imperial_area)+str(metric_area)+":")
                        if from_unit in imperial_area and to_unit in imperial_area:
                            ans=from_sqinchinch(to_sqinch(value))
                        else:
                            ans=from_sqmeter(to_sqmeter(value))
                    elif conv=='time':
                        from_unit=input("please enter your from unit "+str(time)+":")
                        value=ans
                        to_unit=input("please enter your to unit "+str(time)+":")
                        ans=from_sec(to_sec(value))
                    elif conv=='temprature':
                        from_unit=input("please enter your from unit "+str(temprature)+":")
                        value=ans
                        to_unit=input("please enter your to unit "+str(temprature)+":")
                        ans=from_celcius(to_celcius(value,from_unit),to_unit)
                    elif conv=='weight':
                        from_unit=input("please enter your from unit "+str(imperial_weight)+str(metric_weight)+":")
                        value=ans
                        to_unit=input("please enter your to unit "+str(imperial_weight)+str(metric_weight)+":")
                        if from_unit in imperial_weight and to_unit in imperial_weight:
                            ans=from_oz(to_oz(value,from_unit),to_unit)
                        else:
                            ans=from_kg(to_kg(value,from_unit),to_unit)
                    else:
                        print("Invalid input")
                    history.append(str(value)+" "+str(from_unit)+" = "+str(ans) +" "+str(to_unit))
                    print(str(value)+" "+str(from_unit)+" = "+str(ans) +" "+str(to_unit))
                elif end_or_continue=='print history' or end_or_continue=='3':
                    for x in history:
                        print(x)
                elif end_or_continue=='end' or end_or_continue=='2':
                    print("Thank you for using calculator")
                    break
                else:
                    print("Invalid Input")
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")

