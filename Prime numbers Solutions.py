Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:19:22) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def prime_numbers(count):
	n = 1000000
	i = 2
	result = []

	while i < n:
		flag = True


		for item in range(2, int(i**0.5)+1):
			if i % item == 0 and i != item: 
				flag = False
				break



			if flag:
				result.append(i)

		i += 1

print(result)
