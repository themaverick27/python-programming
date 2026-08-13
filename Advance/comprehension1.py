# List Comprehension 

# Qs: create a list of even nubers between 1 and 20

# naive
ls = []
for i in range(1, 21):
    if i%2 == 0:
        ls.append(i)

print(ls)

# single line 
ls = [i for i in range(1, 21) if i%2 == 0] # list comprehension
print(ls)


# Set Comprehension 
# Qs: create a set of even nubers between 1 and 20

# naive
st = set()
for i in range(1, 21):
    if i%2 == 0:
        st.add(i)

print(st)
print(type(st))

# single line 
s = {i for i in range(1, 21) if i%2 == 0} # list comprehension
print(s)

print(type(s))