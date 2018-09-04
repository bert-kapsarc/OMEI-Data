import numpy
#prices = numpy.load('prices_200106.npy')

#print prices

prices = numpy.load('prices_200106.npy').item()
#print prices.keys()
print prices.get((2001,6,29,22,,"high"))
#print prices