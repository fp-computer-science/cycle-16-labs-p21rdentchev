# Ryan Dentchev 2/10/2021

my_file = open("alma_mater.txt", "r")
while True:
    line = my_file.readline()
    if len(line) == 0:
        break
    print(line)

my_file.close()
