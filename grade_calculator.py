# Building a program that takes student marks and returns grade (A, B, C, D and F) with encouraging messages

student_name = input("Enter student name: ")

def calculate_grade(marks):
     if marks < 0 or marks > 100:
          return None, "Invalid marks entered by. Please enter a number between 0 and 100."
     if marks >= 90:
          return "A", "Excellent! Keep up the great work! 🌟"
     elif marks >= 80:
          return "B", "Very Good! Keep it up! 👍"
     elif marks >= 70:
          return "C", "Good effort! You can do even better! 💪"
     elif marks >= 60:
          return "D", "Fair, but there's room for improvement. Keep trying! 🚀"
     else:
          return "F", "Don't be discouraged. Learn from this and come back stronger! 🌈"

while True:
     try:
          marks = int(input("Enter marks (0-100): "))
          if 0 <= marks <= 100:
               grade, message = calculate_grade(marks)
               print(f"\n📊 RESULT FOR {student_name.upper()}:")
               print(f"Marks: {marks}/100")
               print(f"Grade: {grade}")
               print(f"Message: {message}")
               break
          else:
               print("Invalid marks entered. Please enter a number between 0 and 100.")
     except ValueError:
          print("Invalid input. Please enter a valid integer for marks.")
          

     
