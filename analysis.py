def main():
    # Replace with the path to your file
    # Caveat: Current implementation assumes that data in file is separated by newlines
    with open('survey.txt', 'r') as file:
        data = file.readlines()
    data = [int(line.strip()) for line in data]
    file.close()

    print_statistics(data)

def sample_mean(data):
    return sum(data) / len(data)

def sample_variance(data):
    mean = sample_mean(data)
    return sum((x - mean) ** 2 for x in data) / (len(data) - 1)

def sample_standard_deviation(data):
    return sample_variance(data) ** 0.5

def print_statistics(data):
    print(f'Sample Mean: {sample_mean(data)}')
    print(f'Sample Variance: {sample_variance(data)}')
    print(f'Sample Standard Deviation: {sample_standard_deviation(data)}')

if __name__ == '__main__':
    main()