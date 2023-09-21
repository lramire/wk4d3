#Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
    if number % 2 != 0:
        return "Odd"
    else:
        return "Even"
print(even_or_odd(5))
print(even_or_odd(18))
print(even_or_odd(80))

#I believe the time complexity with this solution is linear. We've got an if statement doing a simple single math operation. Space complexity: we are only holding one value at a time, being the return "Even" or "Odd" and can only ever hold one per argument passed..I say constant space.
#...now that I say that, I could argue time complexity is also constant regarding this particular if statement. The if statement is only ever checking one value (being a number) and doing a simple modulo operation on it. 
#Time complexity: constant
#Space complexity: constant
 
# original solution ..couldn't think of how to make this faster/more efficient so I tried making it less efficient....I made this note first, then the time/space complexity....after figuring out the time/space complexity I realized I would have never made that more efficient. ROFL


#revisit 1

#Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
    even_odd = ""
    for i in range(number +1):
        # print(range(number))
        if i == number:
            if i % 2 != 0:
                even_odd = "Odd"
                # print(even_odd)
            else:
                even_odd = "Even"
                print(i)
    return even_odd
    
print(even_or_odd(5))
print(even_or_odd(18))
print(even_or_odd(80))

# for loop traversing through all the numbers from 0 to number ...which is extra considering just the modulo if statement can be sufficient. This is a linear operation depending on size of 'number'
# For loop going through a potentially large range - I don't believe it's over linear time though.
#I'm torn on the nested if statement. Linear for the first if statement hit. Nested loops typically imply quadratic time ...but this is if statements, with simple conditions at that...linear I venture to say. L x L(n) = 2L(n) not enough to get it to O(n log n)
#Time complexity: linear
#Space complexity: constant




# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

# It should remove all values from list a, which are present in list b keeping their order.
def array_diff(a, b):
    for i in b:
        if i in a:
            for num in range(a.count(i)):
                a.remove(i)
    return a
    if len(b) == 0:
        return a

#nested for loop, quadratic. If statement linear, .remove linear, range function is linear
#space: arguments are lists of unknown length and comparing, then potentially removing from one list. worst case, nothing gets removed.
#Time complexity: quadratic
#Space complexity: linear

#revisit 2
def array_diff(a, b):
    for i in range(len(b)):
        while b[i] in a:
            a.remove(b[i])
    return a

#for loop traversing length of b, linear. while loop, linear. .remove function is linear
#Time complexity: linear
#Space complexity: linear



# Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

# If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

def order(string):
    if string == '':
        return ''
    string=string.split()
    print(string)
    map={}
    for word in string:
        for ch in word:
            if ch.isdigit():
                map[int(ch)]= word
                break
    print(map)
    key = []
    for i in range(1, len(string)+1):
        key.append(map[i])
    return ' '.join(key) 
#time with nested for loop, quadratic, if statements & builtins are linear. append is only ever appending one value ..constant function.
#Holding values that could grow. linear space
#Time complexity: quadratic
#Space complexity: linear

#revist 3

def order(string):
    s = []

    for i in range(1,10):
        for j in list(string.split()):
            if str(i) in j:
               s.append(j)
    return " ".join(s)

#Well, still quadratic with the nested for loops, range is linear, append constant, join seems linear based off the size of list
# ...looking at this now it is still quadratic time and linear space..just with less code. Not enough to get it under quadratic. POOP.
#Time complexity: quadratic
#Space complexity: linear