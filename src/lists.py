'''lists.py
@author Jasper Williams
'''

L = [1, 2, 3, 4]
L += [5, 6, 7, 8]
print("The length of the list is:", len(L))
print("The members of the list are:")
season = ['spring', 'summer', 'winter', 'fall']
for i, season in enumerate(season):
    print (i, season)