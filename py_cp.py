import copy
#'''#normal copy without copy module '''
def nornamlcopy():
	a =[[1,2,3],[4,5,6],[7,8,9]]
	print(a)
	a = b
	print(b)
#'''#shallow copy'''
	c = copy.copy(a)
	a.appand([10,11,12])
#'''id of a and id of c is diffrent but id a[0] id c[0] same '''
	print (id(a),id(b))
	print (id(a[0],id(b[0]))
#'''deep copy all  id's are diffrent'''
	d = copy.deepcopy(a)
	print (d)

normalcopy()
