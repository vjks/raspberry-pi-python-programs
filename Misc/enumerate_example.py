def skip_elements(elements):
	# code goes here
	mod_elements = []
	enumerated_elements = enumerate(elements)
	for count, ele in enumerated_elements:
		if count % 2 == 0:
			mod_elements.append(ele)
	return mod_elements

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']