"""CISC 121 Assignment 1 

I chose the 5 beginner problems which included: (CyclicRotation, OddOcurrencesinArray, FrogJmp, PermMissingElem, and Perm Check) 
"""


# This is number 1: CyclicRotation
def cyclic_rotation(A, K):
    numbers = A
    rotations = K

    # Return an empty list if there are no numbers
    if len(numbers) == 0:
        return []

    rotated_numbers = [0] * len(numbers)

    # Move each number to its new position
    for position in range(len(numbers)):
        new_position = (position + rotations) % len(numbers)
        rotated_numbers[new_position] = numbers[position]

    return rotated_numbers


# This is number 2: OddOccurrencesInArray
def odd_occurrences_in_array(A):
    sorted_numbers = sorted(A)
    position = 0

    # Look at two numbers at a time to find one without a pair
    while position < len(sorted_numbers) - 1:
        if sorted_numbers[position] != sorted_numbers[position + 1]:
            return sorted_numbers[position]
        position += 2

    return sorted_numbers[-1]


# This is number 3: FrogJmp
def frog_jmp(X, Y, D):
    start_position = X
    target_position = Y
    jump_length = D

    # Find how many jumps are needed
    distance_to_go = target_position - start_position
    jumps_needed = distance_to_go // jump_length

    # Add one more jump if the distance does not divide evenly
    if distance_to_go % jump_length != 0:
        jumps_needed += 1

    return jumps_needed


# This is number 4: PermMissingElem
def perm_missing_elem(A):
    numbers = A
    expected_total = 0

    # Add up all the numbers that should be in the list.
    for number in range(1, len(numbers) + 2):
        expected_total += number

    # Add up the numbers that are actually in the list.
    actual_total = 0
    for number in numbers:
        actual_total += number

    return expected_total - actual_total


# This is number 5: PermCheck
def perm_check(A):
    sorted_numbers = sorted(A)

    # Check whether the list contains 1, 2, 3, etc
    for position in range(len(sorted_numbers)):
        expected_number = position + 1
        if sorted_numbers[position] != expected_number:
            return 0
return 1
