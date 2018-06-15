month=input("Put in the month:")
if month==("January"):
    x=6
if month==("February"):
    x=2
if month==("March"):
    x=2
if month==("April"):
    x=5
if month==("May"):
    x=0
if month==("June"):
    x=3
if month==("July"):
    x=5
if month==("August"):
    x=1
if month==("September"):
    x=4
if month==("October"):
    x=6
if month==("November"):
    x=2
if month==("December"):
    x=4
x=int(x)
day=input("Put in the day:")
day=int(day)
x=x+day
year=input("Put in the year(2000-2018):")
if year==("2000"):
    x=x+0
if year==("2001"):
    x=x+1
if year==("2002"):
    x=x+2
if year==("2003"):
    x=x+3
if year==("2004"):
    x=x+5
if year==("2005"):
    x=x+6
if year==("2006"):
    x=x+0
if year==("2007"):
    x=x+1
if year==("2008"):
    x=x+3
if year==("2009"):
    x=x+4
if year==("2010"):
    x=x+5
if year==("2011"):
    x=x+3
if year==("2012"):
    x=x+1
if year==("2013"):
    x=x+2
if year==("2014"):
    x=x+3
if year==("2015"):
    x=x+4
if year==("2016"):
    x=x+6
if year==("2017"):
    x=x+0
if year==("2018"):
    x=x+1
mod=(x%7)
if mod==(0):
    print("Sunday")
if mod==(1):
    print("Monday")
if mod==(2):
    print("Tuesday")
if mod==(3):
    print("Wednesday")
if mod==(4):
    print("Thursday")
if mod==(5):
    print("Friday")
if mod==(6):
    print("Saturday")
