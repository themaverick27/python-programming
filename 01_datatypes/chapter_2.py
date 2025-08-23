#  mutable 

spice_mix = set()
print(f"Initial spice mix: {spice_mix}")
print(f"Initial spice mix id: {id(spice_mix)}") 

spice_mix.add("Cardamom")
spice_mix.add("Ginger")

print(f"Updated spice mix: {spice_mix}")
print(f"Updated spice mix id: {id(spice_mix)}") 

# identity same, values got overwritten in the same memory reference - mutable
# mutable because the old values remained in the memory, and the values got overwritten or new values added to the same reference, not in the new memory reference, that's why mutable.

