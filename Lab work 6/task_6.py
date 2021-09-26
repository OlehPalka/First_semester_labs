import urllib.request

def read_input_file(url, number):
    webpage_decoder = ""
    with urllib.request.urlopen(url) as webpage:
        for line in webpage:
            line = line.strip()
            line = line.decode("utf-8")
            webpage_decoder += line
        students_list = webpage_decoder.split("+")
        for student in students_list:
            print(student)
url ='https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt'
read_input_file(url, 3)