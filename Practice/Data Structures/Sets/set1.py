# Sets Concepts - mutable and unordered

st = {10, 15, "hello", 20, 20, 12, 25, 45, 45, 50}
print(st) # only uniques

# sets are unordered, so you cannot access values through index
#print(st[0]) # error

# also, you cannot update values through index
#st[0] = 5 # error
#print(st)

# traverse set - not by index, but directly access value
for x in st:
    print(x)

# sets are mutable, can modify the values but not through index

# sets methods

st.add(100)
print(st)

st.remove(25)
print(st)

st.discard(12)
print(st)

popped = st.pop() # removes a random element, not the last one - as set is unordered
print(popped)

st.clear()
print(st)