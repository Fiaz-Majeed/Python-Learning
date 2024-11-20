class Student: 
    def __init__(self, name: str, scores: list[int]):
        self.name = name
        self.scores = scores

    def calculate_average(self):
        return sum(self.scores) / len(self.scores)
    
    def is_passing(self, passing_score = 40):
         for score in self.scores:
            if score < passing_score:
                return False
            return True

class PerformanceTracker:
    def __init__(self):
        self.students = {}

    
    def add_student(self, name: str, scores: list[int]):
        if name in self.students:
            print(f"Student {name} is already in the system.")
        else:
            self.students[name] = Student(name, scores)
            print(f"Added {name} with scores: {scores}")
    
    def calculate_Class_Average(self):
        if not self.students:
            return 0
        total_average = sum(student.calculate_average() for student in self.students.values())
        return total_average / len(self.students)
    
    def display_student_performance(self):
        if not self.students:
            print("No students in the tracker.")
            return

        print("\nStudent Performance:")
        for name, student in self.students.items():
            avg_score = student.calculate_average()
            status = "Passing" if student.is_passing() else "Failing"
            print(f"Student: {name}, Average Score: {avg_score:.2f}, Status: {status}")

        try:
            class_avg = self.calculate_Class_Average()
            #print(f"\nClass Average Score: {class_avg:.2f}")
        except ZeroDivisionError:
            print("\nClass Average Score: N/A (No students in tracker)")

def main():
       
    tracker = PerformanceTracker()

    while True:
        name = input("Enter name of the student or quit to stop: ") 
        if name.lower() == 'quit':
            break
        try:
            scores = [
                int(input(f"Enter score for subject {i+1}: "))
                for i in range(3)
            ]
            tracker.add_student(name, scores)
        except ValueError:
            print("Invalid input. Please enter numeric values for scores.")
        print("\nStudent Performance:")
        
    tracker.display_student_performance()
    class_avg = tracker.calculate_Class_Average()
    print(f"\nClass Average Score: {class_avg:.2f}")


# Sample usage
if __name__ == "__main__":
    main()