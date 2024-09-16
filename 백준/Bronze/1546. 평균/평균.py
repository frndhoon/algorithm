N = int(input())  # 과목의 개수
grade_list = list(map(int, input().split()))

max_grade = max(grade_list)

new_grade_list = []
for grade in grade_list:
    new_grade = grade / max_grade * 100
    new_grade_list.append(new_grade)

new_grade_average = sum(new_grade_list) / len(new_grade_list)
print(new_grade_average)