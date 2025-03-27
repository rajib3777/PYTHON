Things = 'Ronit','Rajib','Monoichcha','Jahid','Nijam'

print(Things[0])
print(Things[1])
print(Things[2])
print(Things[3])
print(Things[4])

if 'Nijam' in Things :
    print('Exists')

if 'Dihan' in Things :
    print('Exists')
else:
    print('Not Exists')

try:
    'Dihan' in Things
except:
    print('Naika')
finally :
    print('Dawat Dey nai')



ifter = ['Ronit','Rajib','Monoichcha','Jahid','Nijam']
x = len(ifter)
print(x)
cost = lambda x : x*300
print(cost)