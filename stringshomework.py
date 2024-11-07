#2. Write a program that collects two strings from a user, inserts them into 
#the string "Yesterday I wrote a [response_one]. I sent it to [response_
#two]!" and prints a new string

print("Please enter two words to complete the sentence 'Yesterday I wrote a [response_one]. I sent it to [response_#two]!'")
response2a= input("enter response one: ")
response2b= input("enter response two: ")
phrase2= ("Yesterday I wrote a {}. I sent it to {}!".format(response2a,response2b))
print(phrase2)

#7. Use a method to find the first index of the character 
#"m" in the string "Hemingway"

string7 = "Hemingway"
string7b = string7.index("m")
print (string7b)

#10. Slice the string 
#"It was a bright cold day in April, and the clocks were striking thirteen." 
#to only include the characters before the comma
string10= "It was a bright cold day in April, and the clocks were striking thirteen."
string10= [string10[0:string10.index(",")]]
print(string10)

#22. Pig Latin is a nonsense language.  To transform a word from English to Pig Latin, you move the first 
#letter to the end and add ‘ay’ after that.  For example, monkey becomes onkeymay in Pig Latin, and 
#word becomes Ordway.  Write a program that takes a single word as input and translates it to Pig Latin.

input22 = input("q22) enter a word to convert to pig latin: ")
input22= input22[1:]+input22[0]+"ay"
print(input22)

#23. The NAME GAME lets you make a song out of any person’s name. For an example of the song see 
#the hyperlink HERE.  Your program should take a person’s name as input, for example “pearl”, and print 
#out the song

input23 = input("q23) enter a name to play the name game!: ")
print (input23+",", input23+", bo-b"+input23[1:])
print("banana-fana fo-f"+ input23[1:])
print("fee-fi-mo-m"+input23[1:])
print(input23+"!")