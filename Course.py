from dataclasses import dataclass

# Makes it as a struct in C++
@dataclass
class Course:
    name: str  = " "
    code: int  = 0
    registeredStudents: list[str] = []
