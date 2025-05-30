# String is a sequence of Characters enclosed in quotes
name="Harish"       #Double quoted string
surname='raj'       #Single quoted string
initial='''SEM'''   #triple quoted string
username=input("Enter your name ")
print(f"good afternoon {username}")

#String Slicing
Name="Edwin"
sl=len(Name)
short=Name[0:3]
print(sl)
print(short)

#Negative slicing
Name2="hello"
print(Name2[-4:-1])

#Slicing using skip value
word="amazon"
len=word[1:6:2]
print(len)