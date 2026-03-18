class Course:
    def __init__(self, courseID, teacher, max_students, fees):
        self.courseID = courseID
        self.teacher = teacher
        self.max_students = max_students
        self.fees = fees
        self.studentsenrolled = []

    def enrol(self, studentName):
        if len(self.studentsenrolled) < self.max_students:
            self.studentsenrolled.append(studentName)
            print(f"{studentName} enrolled in {self.courseID}")
        else:
            print(f"Cannot enrol {studentName}: course is full")

    def num_students(self):
        return len(self.studentsenrolled)

    def income(self):
        return self.num_students() * self.fees

    def cost(self):
        raise NotImplementedError("Each course type must define its own cost.")

    def profit(self):
        return self.income() - self.cost()

    def __str__(self):
        return (f"Course ID : {self.courseID}\n"
                f"Teacher   : {self.teacher}\n"
                f"Students  : {self.num_students()}/{self.max_students}\n"
                f"Income    : ${self.income()}\n"
                f"Cost      : ${self.cost()}\n"
                f"Profit    : ${self.profit()}")



class CookingCourse(Course):
    def __init__(self, courseID, teacher, fees):
        super().__init__(courseID, teacher, max_students=10, fees=fees)
        self.fixed_cost = 1000

    def cost(self):
        return self.fixed_cost



class SewingCourse(Course):
    def __init__(self, courseID, teacher, fees=300):
        super().__init__(courseID, teacher, max_students=10, fees=fees)
        self.cost_per_student = 100

    def cost(self):
        return self.num_students() * self.cost_per_student


class WritingCourse(Course):
    def __init__(self, courseID, teacher, fees, flat_cost, max_students=15):
        super().__init__(courseID, teacher, max_students=max_students, fees=fees)
        self.flat_cost = flat_cost

    def cost(self):
        return self.flat_cost



italian_cooking = CookingCourse("001", "Mathew", 500)
seafood_cooking = CookingCourse("002", "Master Cheif", 700)

creative_writing = WritingCourse("003", "GRRM", 200, flat_cost=800)
business_writing = WritingCourse("004", "Thomas Shelby", 200, flat_cost=600)

sewing_course = SewingCourse("005", "John")


italian_cooking.enrol("Dextor")
italian_cooking.enrol("Bob")
seafood_cooking.enrol("Danny Cho")
creative_writing.enrol("Optimus Prime")
business_writing.enrol("Tonny Soprano")
sewing_course.enrol("Edward")
sewing_course.enrol("Mat")


print(italian_cooking)
print(seafood_cooking)
print(sewing_course)
print(creative_writing)
print(business_writing)