numbers = [1, 2, 3, 4, 5, 6, 7, 8]
output = []

def even(unfiltered_numbers):
    even_output = []
    for i in unfiltered_numbers:
        if i % 2 == 0:
            even_output.append(i)
    return even_output

output = even(unfiltered_numbers)
print(output)



"""i = 0
    while i < len(numbers):
        if numbers[i] % 2 == 0:
            output.append(numbers[i])
        i += 1

print(output)"""
