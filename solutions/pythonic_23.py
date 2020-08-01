squared = [i**2 for i in items]
greater_three = [i for i in items if i > 3]
print(squared, greater_three)

# but:
list(map(str, items))