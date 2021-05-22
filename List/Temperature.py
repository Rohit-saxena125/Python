# check five temperature on different values
S = 'convert celsius to farhenite '
print(S.center(50,'-'))
celsius = list(map(float,input('Enter the temperature in degree celsius :').split()))
print(celsius)
farhenite = [((float(9)/5) * x + 32) for x in celsius]
print(farhenite)
S = 'convert farhenite to celsius'
print(S.center(50,'-'))
farhenite= list(map(float,input('Enter the temperature in degree farhenite :').split()))
print(farhenite)
celsius = [(float(5)/9)*(x-32) for x in farhenite]
print(celsius)

