import urllib.request

def read_input_file(url, number):
    webpage_decoder = ""
    with urllib.request.urlopen(url) as webpage:
        
        for i,line in enumerate(webpage):
            line = line.strip()
            line = line.decode('utf-8')
            if i > 2:
                webpage_decoder += line
            if i== number+2:
                break
        #     line = line.strip()
        #     line = line.decode('utf-8')
        #     webpage_decoder += line
        student_list = webpage_decoder.split('+')
        for student in student_list:
            print(student)

url ='https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt'
read_input_file(url, 80)
