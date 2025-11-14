#dictionary
a={
    "name":"vinay",
    "age" : 18,
    "department" :"aiml",
     "college"  :"shridevi"


}
print(a)
a["age"]=25
print(a)
del a["department"]
print(a)

a=[1,2,3]
for i in a:
  print(i,a)
{'name': 'vinay', 'age': 18, 'department': 'aiml', 'college': 'shridevi'}
{'name': 'vinay', 'age': 25, 'department': 'aiml', 'college': 'shridevi'}
{'name': 'vinay', 'age': 25, 'college': 'shridevi'}
1 [1, 2, 3]
2 [1, 2, 3]
3 [1, 2, 3]
