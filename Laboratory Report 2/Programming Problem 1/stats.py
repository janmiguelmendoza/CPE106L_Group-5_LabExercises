def mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    if not numbers:
        return 0
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    middle = n // 2

    if n % 2 == 0:
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    else:
        return sorted_numbers[middle]

def mode(numbers):
    if not numbers:
        return 0
    from collections import Counter
    count = Counter(numbers)
    max_count = max(count.values())
    modes = [key for key, value in count.items() if value == max_count]
    return modes[0] if len(modes) == 1 else modes

def main():
    sample_numbers = [1, 2, 3, 4, 4, 5, 6, 7, 7, 7]
    print(f"Mean: {mean(sample_numbers)}")
    print(f"Median: {median(sample_numbers)}")
    print(f"Mode: {mode(sample_numbers)}")

if __name__ == "__main__":
    main()  
