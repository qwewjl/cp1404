celsius = float(input("Celsius: "))


def convert_temps(celsius):
    temps_file = open("temps_output.txt", "a")
    fahrenheit = celsius * 9.0 / 5 + 32
    print(fahrenheit, file=temps_file)
    temps_file.close()
    print("Result: {:.15f} F".format(fahrenheit))
convert_temps(celsius)


def temps_file(celsius):
    temps_file = open("temps_input.txt", "a")
    print(celsius, file=temps_file)
    temps_file.close()
temps_file(celsius)
