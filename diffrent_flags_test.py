a,b,c,=0,1,2
if a==1 or b==1 or c==1:
    print('with values passed or method')

if 1 in (a,b,c):
    print('with values passed in of method')

if a or b or c:
   print('or with out values passed')

if any ((a,b,c)):
    print('in and any ,with out values passed')
