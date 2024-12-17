Programming Problem 1


def mean(numbers):
    if not numbers:
        raise ValueError("The list is empty.")
    return sum(numbers) / len(numbers)

def median(numbers):
    if not numbers:
        raise ValueError("The list is empty.")
    sortednumbers = sorted(numbers)
    n = len(sortednumbers)
    mid = n // 2
    if n % 2 == 0:
        return (sortednumbers[mid - 1] + sortednumbers[mid]) / 2
    else:
        return sorted_numbers[mid]
