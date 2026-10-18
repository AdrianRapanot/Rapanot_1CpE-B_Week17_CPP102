readings = [28, 31, 35, 37, 29]


def classify_reading(temperature):
    if temperature < 30:
        return "NORMAL"
    elif temperature <= 35:
        return "WARNING"
    else:
        return "CRITICAL"


def view_readings():
    print("\nCURRENT READINGS")
    print("-----------------")

    for i in range(len(readings)):
        print(f"Reading {i + 1}: {readings[i]} °C")


def add_reading():
    new_reading = input("\nEnter new reading: ").strip()

    if new_reading == "":
        print("\nInvalid input. The reading cannot be empty.")
        return

    if new_reading.startswith("-"):
        if not new_reading[1:].isdigit():
            print("\nInvalid input. Enter a whole number only.")
            return
    elif not new_reading.isdigit():
        print("\nInvalid input. Enter a whole number only.")
        return

    temperature = int(new_reading)

    if temperature < 0 or temperature > 100:
        print("\nInvalid reading. Enter a value from 0 to 100.")
    else:
        readings.append(temperature)
        print("\nReading added successfully.")


def classify_readings():
    print("\nREADING CLASSIFICATION")
    print("----------------------")

    for temperature in readings:
        status = classify_reading(temperature)
        print(f"{temperature} °C -> {status}")


def generate_summary():
    total = 0
    minimum = readings[0]
    maximum = readings[0]

    normal_count = 0
    warning_count = 0
    critical_count = 0

    for temperature in readings:
        total += temperature

        if temperature < minimum:
            minimum = temperature

        if temperature > maximum:
            maximum = temperature

        status = classify_reading(temperature)

        if status == "NORMAL":
            normal_count += 1
        elif status == "WARNING":
            warning_count += 1
        else:
            critical_count += 1

    number_of_readings = len(readings)
    average = total / number_of_readings

    normal_percentage = normal_count / number_of_readings * 100
    warning_percentage = warning_count / number_of_readings * 100
    critical_percentage = critical_count / number_of_readings * 100

    if critical_count >= 1:
        overall_status = "ATTENTION REQUIRED"
    elif warning_count >= 1:
        overall_status = "MONITOR"
    else:
        overall_status = "NORMAL"

    print("\nMONITORING SUMMARY")
    print("------------------")
    print(f"\nNumber of readings : {number_of_readings}")
    print(f"Total of readings  : {total}")
    print(f"Average temperature: {average:.2f} °C")
    print(f"Minimum temperature: {minimum} °C")
    print(f"Maximum temperature: {maximum} °C")

    print(f"\nNORMAL  : {normal_count} ({normal_percentage:.2f}%)")
    print(f"WARNING : {warning_count} ({warning_percentage:.2f}%)")
    print(f"CRITICAL: {critical_count} ({critical_percentage:.2f}%)")

    print(f"\nOverall Status: {overall_status}")


while True:
    print("\nSIMULATED DEVICE MONITORING SYSTEM")
    print("---------------------------------")
    print("[1] View Readings")
    print("[2] Add Reading")
    print("[3] Classify Readings")
    print("[4] Generate Summary")
    print("[5] Exit")

    choice = input("\nEnter choice: ").strip()

    if choice == "1":
        view_readings()
    elif choice == "2":
        add_reading()
    elif choice == "3":
        classify_readings()
    elif choice == "4":
        generate_summary()
    elif choice == "5":
        print("\nExiting program. Goodbye!")
        break
    else:
        print("\nInvalid choice. Please select 1 to 5.")