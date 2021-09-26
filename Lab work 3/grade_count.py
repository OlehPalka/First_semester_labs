OP = int(input())
Mat_analiz = int(input())
Disk_mat = int(input()) 
Tvorchij = int(input())
History = int(input())
if OP > 100 or OP < 0 or Mat_analiz > 100 or Mat_analiz < 0 or Disk_mat > 100 or Disk_mat < 0 or Tvorchij > 100 or Tvorchij < 0 or History > 100 or History < 0:
    print("None")
else:

    percent_grade = (OP + Mat_analiz + Disk_mat + Tvorchij + History) / 5
    if percent_grade <= 100 and percent_grade >= 90:
        Grade = "A"
    elif percent_grade < 90 and percent_grade >= 82:
        Grade = "B"
    elif percent_grade < 82 and percent_grade >= 75:
        Grade = "C"
    elif percent_grade < 75 and percent_grade >= 67:
        Grade = "D"
    elif percent_grade < 67 and percent_grade >= 60:
        Grade = "E"
    else:
        Grade = "F"
    if percent_grade == 0.0:
        print("Average grade =", int(percent_grade), "->", Grade)
    else:
        print("Average grade =", percent_grade, "->", Grade)