import csv

def read(csv_file):
    toReturn = []
    with open(csv_file, 'r') as file:
        file = csv.reader(file, delimiter=',')
        for row in file:
            toReturn.append(row)
    return toReturn


def filter_data(user_input, data):
    emptyList = []
    for rowList in data:
        if user_input in rowList:
            emptyList.append(rowList)
        else:
            pass
    return emptyList


def calc_averages(filtered_data):
    lmidaclopridConcentration = []
    beeLongevityInBioassay = []
    daysParalyzed = []
    for rowList in filtered_data:
        lmidaclopridConcentration.append(float(rowList[7]))
        beeLongevityInBioassay.append(int(rowList[8]))
        daysParalyzed.append(int(rowList[9]))
    return [sum(lmidaclopridConcentration) / len(lmidaclopridConcentration),
            sum(beeLongevityInBioassay) / len(beeLongevityInBioassay), sum(daysParalyzed) / len(daysParalyzed)]


def calc_minimums(filtered_data):
    lmidaclopridConcentration = []
    beeLongevityInBioassay = []
    daysParalyzed = []
    for rowList in filtered_data:
        lmidaclopridConcentration.append(float(rowList[7]))
        beeLongevityInBioassay.append(int(rowList[8]))
        daysParalyzed.append(int(rowList[9]))
    return [min(lmidaclopridConcentration), min(beeLongevityInBioassay), min(daysParalyzed)]


def calc_maximums(filtered_data):
    lmidaclopridConcentration = []
    beeLongevityInBioassay = []
    daysParalyzed = []
    for rowList in filtered_data:
        lmidaclopridConcentration.append(float(rowList[7]))
        beeLongevityInBioassay.append(int(rowList[8]))
        daysParalyzed.append(int(rowList[9]))
    return [max(lmidaclopridConcentration), max(beeLongevityInBioassay), max(daysParalyzed)]


def print_stats(input, stat_type, stats):
    print(f"{stat_type}s for {input} bees:")
    print(f"{stat_type} Imidacloprid Concentration: {stats[0]:.2f}")
    print(f"{stat_type} Longevity: {stats[1]:.2f}")
    print(f"{stat_type} Days Paralyzed: {stats[2]:.2f}")
    print()


def run(data):
    user_input = input("Enter the species/genus or the sociality of bee you would like information about: ")
    for rowList in data:
        if user_input.upper() in rowList:
            filteredData = filter_data(user_input.upper(), data)
            averages = calc_averages(filteredData)
            minimums = calc_minimums(filteredData)
            maximums = calc_maximums(filteredData)
            print_stats(user_input, "Average", averages)
            print_stats(user_input, "Minimum", minimums)
            print_stats(user_input, "Maximum", maximums)
            again = input("Would you like to see more data? (Y/N) ")
            if again[0].lower() == 'y':
                return True
            else:
                return False
    print("Test not found. Please enter valid Sociality or Species/Genus")
    return False


def main():
    data = read(r"C:\Users\Fresh\Desktop\Python CS150B Sanjar Projects\INSECTICIDES ON BEES Data\BEETOX.csv")
    while run(data):
        continue


if __name__ == '__main__':
    main()
