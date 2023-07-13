from dataclasses import dataclass

# Makes it as a struct in C++
@dataclass
class HW:
    courseName: str = " " # Which course does it belong to
    solution: str  = " " # The solution of the HW
