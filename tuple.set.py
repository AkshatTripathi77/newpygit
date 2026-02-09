s = {22,24,252,6}
print(s)
s= {12,34,56,78,90}
print(s)
# Dictionary
data = {1:'Navin',2:'Kiran',4:'Harsh'}
print(data[1])
print(data.get(2))
keys = ['Navin','kiran','Harsh']
values = ['Python' ,'java' ,'JS']
data = dict(zip(keys,values))

print(data)
data['Monika'] = 'cs'
print(data)
del data['Harsh']
print(data)
prog = {'js':'Atom','Cs':'vs','Python':['Pycharm','Sublime'],'java':{'Jse':'Netbeans','JEE':'Eclipse'}}
print(prog['java']['Jse'])
