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

def mode(numbers):
    if not numbers:
        raise ValueError("The list is empty.")
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    max_freq = max(freq.values())
    modes = [key for key, val in freq.items() if val == max_freq]
    return modes[0] if len(modes) == 1 else modes

if __name == "__main":
    numbers = [1, 2, 2, 3, 4, 4, 4, 5, 5]
    print("Mean:", mean(numbers))
    print("Median:", median(numbers))
    print("Mode:", mode(numbers))
