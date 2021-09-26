# import numpy
# import csv

# # with open("lol.txt") as file:
# #     csv_reader = csv.reader(file, delimiter=",")
# #     line_count = 0
# #     for row in csv_reader:
# #         if line_count == 0:
# #             print(f'column names are {", ".join(row)}')
# #             line_count += 1
# #         else:
# #             print(f'\t{row[0]} surname - {row[1]}, was born in {row[2]}.')
# #             line_count += 1
# #     print(f'Processed {line_count} lines.')

# with open("lol.txt", mode='w') as file:
#     lol_writer = csv.writer(file, delimiter=',',
#                             quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     lol_writer.writerow(["Bruh", "Lol"])
#     lol_writer.writerow(["Kek", "Cheburek"])
# with open("lol.txt") as file:
#     for line in file:
#         print(line)

# import pandas
# df = pandas.read_csv("lol.txt")
# print(df)

# data = numpy.array(['a', 'b', 'c', 'd'])
color_list = ["red", "green", "yellow", "blue", "magenta", "cyan"]
color = random.choice(color_list)
print()
print()
print()
print(colored("**********************************************************", color))
print(colored("*", color), end="")
print("Do you want to see possible genres for books of this author?", end="")
print(colored("*", color))
print(colored("*", color), end="")
print("""Enter "yes" or "no".                                        """, end="")
print(colored("*", color))
print(colored("**********************************************************", color))
print()
print()
print()
