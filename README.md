# Educational Management System
A console application that acts as a simplified version of BlackBoard. It allows interactions between professors, students, and teacher assistants (ex. creating/joining courses, creating/solving/grading homeworks, etc.).

## Prerequisites
- Python 3.x
  
## How to Run

1. Clone this repository:
```
git clone <repo-link>
```
2. Run the main.py file:
```
python main.py
```

## Some features
Doctors:
* Each course is created by a doctor. The doctor can add teaching assistants (TAs) for the course.
* Doctors can create assignments, view them, set grades for students, and get statistics on the assignments.

Students:
* Register for courses (view available courses and choose to enroll).
* View their registered courses (see course name, code, and assignment status).
* View assignment details within a course (see submitted/not submitted status and any grades).

Session Saving:
* Upon logging out, the system prompts the user to save their session information (e.g., viewed courses, progress within a course).
* If the user chooses to save, only the most recent session data is saved in JSON files.
* This allows the user to resume their work from where they left off upon their next login.
