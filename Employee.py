#! /usr/bin/python3

class Employee(object):
	numEmployee=0
	def __init__(self,name,rate):
		self.name=name
		self.rate=rate
		self.owed=0
		Employee.numEmployee +=1
	def __del__ (self):
		Employee.numEmployee -=1
	def  hours(self,numHours):
		self.owed +=numHours * self.rate
		return("%.2f hours worked" % numHours)
	def pay(self):
		self.owed=0
		return ("payed %s " % self.name)
	def __repr__(self):
		return "Number of Employee %i"%Employee.numEmployee
emp1=Employee("John",15.9)
emp2=Employee("Ruth",10.3)
print(emp1)
