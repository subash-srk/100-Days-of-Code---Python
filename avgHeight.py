# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
total_height = 0
for height in student_heights:
  total_height += height

print(f"total height = {total_height}")
length = len(student_heights)
print(f"number of students = {length}")
avg_height = round(total_height / length)
print(f"average height = {avg_height}")


