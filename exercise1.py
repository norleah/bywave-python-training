print "Write a program that accepts an input value (range: 60-100)"
print "and prints a message based on the following range of values:"

print "RANGE                   MESSAGE"
print "60 to 74                Derp!"
print "75 to 84                Good"
print "85 to 94                Very Good"
print "95 to 100               Level Asian!"
print "any other value         Invalid Value"


# your name and email address here
# leah = '<norleah@bywave.com.au>'

 
# if leah == 'leah':
    # your code here

print "Input number from 60 to 100"
x=range(60, 101)
x=input()
if x in range(60, 75):
 	 print 'derp!'
elif x in range(75, 85):
 print 'Good'
elif x in range(85, 95):
	 print 'Very Good'
elif x in range(95, 101):
	 print 'Level Asian'
else:
	 print 'Invalid Value'