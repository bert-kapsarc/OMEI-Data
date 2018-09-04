import requests
import numpy
f = open('OMEI_mlinks.txt', 'r')
links = f.readlines()
f.close()
prices = {}
month_prev = 0
year_prev = 0
for link in links:

	file_number = link.split("_")[1]
	year = file_number[0:4]	
	if int(year)>2014:
		r= requests.get(link.strip())
		if r.status_code==200:
	#		print(r.text)

			month = file_number[4:6]
			session = file_number[8:10]

			if int(year) != int(year_prev) and int(year_prev)>0:
				print(year_prev)
				numpy.save('prices_'+year_prev+'.npy', prices)
				prices = {}

			year_prev = year


			lines = r.text.split("\n")
			iterlines = iter(lines)
			next(iterlines)
			for line in iterlines:
				#year,month,day,hour,low/high
				text = line.split(";")
				if len(text)>=7:
					# year, month, day, hour, session, hig/low
					key = (int(text[0]),int(text[1]),int(text[2]),int(text[3]),int(session))
					prices[key+("high",)] = float(text[4])
					prices[key+("low",)] = float(text[5])
					#print prices
					#print row 
					#if len(prices)==0:
					#	prices = row
					#else:		
					#	prices=numpy.vstack([prices,row])
					#print(prices)
				
			
		else:
			print(link)
			print(r.status_code)

	#numpy.save('prices.npy', prices)
print(year_prev)
numpy.save('prices_'+year_prev+'.npy', prices)