student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
for a in student_scores:
    if 91<= student_scores[a] <=100:
        student_scores[a] = "Outstanding"
    elif 81 <= student_scores[a] <= 90:
        student_scores[a] = "Exceeds Expectations"
    elif 71 <= student_scores[a] <= 80:
        student_scores[a] = "Acceptable"
    else:
        student_scores[a] = "fail"
print(student_scores)