import sys

def calculate_average(values):
    if len(values) == 0:
        return 0
    return sum(values) / len(values)
def passenger_category(avg_age):
    if avg_age < 12:
        return "Children"
    elif 12 <= avg_age < 60:
        return "Adults"
    else:
        return "Senior Citizens"
if __name__ == "__main__":
    script_name = sys.argv[0]
    if len(sys.argv) > 4:
        train_name = sys.argv[1]
        source = sys.argv[2]
        destination = sys.argv[3]
        ages = list(map(int, sys.argv[4:]))
        print("User provided train and passenger details:")
    else:
        train_name = "Express"
        source = "CityA"
        destination = "CityB"
        ages = [10, 25, 30, 45, 65]
        print("No input given - using default values:")
    total_passengers = len(ages)
    average_age = calculate_average(ages)
    category = passenger_category(average_age)
    print("\n========== Train Passenger Details ==========")
    print("Script Name:", script_name)
    print("Train Name:", train_name)
    print("Source:", source)
    print("Destination:", destination)
    print("Passenger Ages:", ages)
    print("Total Passengers:", total_passengers)
    print("Average Age:", average_age)
    print("Youngest Passenger Age:", min(ages))
    print("Oldest Passenger Age:", max(ages))
    print("Passenger Category:", category)
    
