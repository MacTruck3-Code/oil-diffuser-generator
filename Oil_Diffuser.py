import random
import clipboard
import console
import os


def findOil():
	oils = {
		1: "Sweet Orange",
		2: "Lavender",
		3: "Lemon",
		4: "Tea Tree",
		5: "Eucalyptus",
		6: "Frankincense"
	}
	
	oilNum = random.randint(1, len(oils))
	oil = oils[oilNum]
	return oil
		

def checkOil(x, pendNote={}):
	pendOil = x
	while True:
		if pendOil in pendNote:
			newOil = findOil()
			pendOil = newOil
		else:
			break
	return pendOil


notification = {}

numOils = random.randint(1, 3)
i = 0
numDrops = 9
while i < numOils:
	if numOils == 1:
		numDroplets = 6
		useOil = findOil()
		notification[useOil] = numDroplets
	else:
		if numDrops != 0:
			numDroplets = random.randint(1, numDrops)
			if numDroplets == numDrops or numDroplets > 4:
				numDroplets = 4
				if numDrops < 4:
					numDroplets = numDrops
			useOil = findOil()
			useOil = checkOil(useOil, notification)
			notification[useOil] = numDroplets
			numDrops = numDrops - numDroplets
	i += 1
	
# print(notification)
list = ''
for x in notification:
	drops = notification[x]
	list += str(x) + ": " + str(notification[x]) + "\n"
	
print(list)
clipboard.set(list)
console.alert('Oil Diffuser', list, 'OK', hide_cancel_button=True)
os.abort()
