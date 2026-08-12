# List practice Qs

# Qs: Print positive and negative elements of an List?

list = [-40, -15, 45, 20, 78, -2, 6]

positive_ele = []
negative_ele = []
for x in list:
    if x >= 0:
        positive_ele.append(x)
    else:
        negative_ele.append(x)
print(positive_ele)
print(negative_ele)


# Qs: Mean of List elements?

numbers = [40, 15, 45, 20, 78, 2, 6]

sum = 0
for i in range(len(numbers)):
    sum += numbers[i]

mean = sum / len(numbers)
print(mean)

rounded_mean = round(mean, 2)
print(rounded_mean)


# Qs: Find the greatest element and print its index too?

numbers = [40, 15, 45, 20, 78, 2, 6, 78]

greatest_element = numbers[0]
index = 0
for i in range(1, len(numbers)):
    if numbers[i] > greatest_element:
        greatest_element = numbers[i]
        index = i

print(f"Largest element in list: {greatest_element} and its index is {index}")

# Qs: Find the second greatest element?

second_greatest = numbers[0]
for i in range(len(numbers)):
    if numbers[i] > second_greatest and numbers[i] != greatest_element:
        second_greatest = numbers[i]

print(f"Second largest element in list: {second_greatest}")

# Qs: Check if List is sorted or not.

def checkSorted(ls):
    for i in range(1, len(ls)):
        if ls[i] < ls[i-1]:
            return False

    return True

list = [45, 55, 58, 64, 70, 75, 78]
if(checkSorted(list)):
    print("Sorted List!")
else:
    print("Not Sorted List")