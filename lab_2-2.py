# Ryan Dentchev 2/10/2021

my_file = open("alma_mater.txt", "r")
contents = my_file.readlines()
my_file.close

contents.reverse()

for line in contents:
    print(line)
