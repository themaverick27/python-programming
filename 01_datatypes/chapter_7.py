# String - immutable

subject_name = "science"
customer_name = "Tom"

print(f"Order for {customer_name}: {subject_name} please!")

# indexing in strings
subject_description = "Theories and Discoveries" 

print(f"first word of subject_decription: {subject_description[0:8]}") # last is not inclusive

print(f"first word of subject_decription: {subject_description[:8]}") # from start to 8 (not inclusive)

print(f"first word of subject_decription: {subject_description[0:8:2]}") # [0:8) after every 2 steps

print(f"Last word of subject_decription: {subject_description[13:]}") # from 13 index to end

print(f"Last word of subject_decription: {subject_description[::-1]}") # from 13 index to end


# special characters - encoding and decoding
label_text = "Teà Special"
encoded_label = label_text.encode("utf-8")

print(f"Label text: {label_text}" )
print(f"Encoded label: {label_text}")

decoded_label = encoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")
