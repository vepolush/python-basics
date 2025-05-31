class Human:
    """
    Class for Human description
    """
    def __init__(self, gender: str, age: int, first_name: str, last_name: str):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.age} years old"

    __repr__ = __str__


class Student(Human):
    """
    Class for Student description
    """
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.record_book = record_book

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} has book record №{self.record_book}"

    __repr__ = __str__


class Group:
    """
    Class for Group description
    """
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student) -> None:
        """
        Adds student to the group
        """
        self.group.add(student)

    def delete_student(self, last_name) -> None:
        """
        Deletes student from the group
        """
        student_found = self.find_student(last_name)
        if student_found:
            self.group.remove(student_found)


    def find_student(self, last_name) -> Student | None:
        """
        Returns the student by last name or 'None' if student was not found
        """
        student_found = set(filter(lambda elem: elem.last_name == last_name, self.group))
        if student_found:
            for student in student_found:
                return student
        return None

    def __str__(self) -> str:
        all_students = f"{self.group}"
        return f'Number:{self.number}\n{all_students} '


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)

print(gr)

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!
print(gr)

print("Ok")
