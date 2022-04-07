print '\nWhat\'s your name ?', 
name = raw_input('--> ')
print '\nHow old are you, %s?' % name,
age = int(raw_input())
print '\nHow tall are you (in cms), %s?' % name,
height = int(raw_input())
print '\nHow much do you weigh (in kgs), %s?' % name,
weight = int(raw_input())

print '\nSo, %s is %d years old, %d cms tall and weighs %d kgs.\n' %(
name, age, height, weight)
