"""
Mini Project 2 — Student Manager 🎓

Concepts used:
- list (students)
- dict (each student record)
- set (unique course names / IDs)
- type conversion (marks input)

Run:
    python student_manager.py
"""


def print_menu() -> None:
    print("\n" + "=" * 45)
    print("STUDENT MANAGER")
    print("=" * 45)
    print("1. Add student")
    print("2. List students")
    print("3. Search by roll no")
    print("4. Add marks to student")
    print("5. Show averages")
    print("0. Exit")


def read_int(prompt: str) -> int | None:
    s = input(prompt).strip()
    if s.isdigit():
        return int(s)
    return None


def read_float(prompt: str) -> float | None:
    s = input(prompt).strip()
    try:
        return float(s)
    except ValueError:
        return None


def find_student(students: list[dict[str, object]], roll: int) -> dict[str, object] | None:
    for st in students:
        if int(st["roll"]) == roll:
            return st
    return None


def main() -> None:
    students: list[dict[str, object]] = []

    while True:
        print_menu()
        choice = input("Enter choice: ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        if choice == "1":
            roll = read_int("Enter roll no (int): ")
            if roll is None:
                print("Invalid roll number.")
                continue
            if find_student(students, roll) is not None:
                print("Roll number already exists.")
                continue

            name = input("Enter student name: ").strip()
            course = input("Enter course name: ").strip()
            students.append({"roll": roll, "name": name, "course": course, "marks": []})
            print("Student added.")

        elif choice == "2":
            if not students:
                print("No students yet.")
                continue
            print("\nRoll | Name | Course | Marks count")
            print("-" * 40)
            for st in students:
                marks: list[float] = st["marks"]  # type: ignore[assignment]
                print(f"{st['roll']} | {st['name']} | {st['course']} | {len(marks)}")

        elif choice == "3":
            roll = read_int("Enter roll no to search: ")
            if roll is None:
                print("Invalid roll number.")
                continue
            st = find_student(students, roll)
            if st is None:
                print("Student not found.")
                continue
            print("Found:", st)

        elif choice == "4":
            roll = read_int("Enter roll no: ")
            if roll is None:
                print("Invalid roll number.")
                continue
            st = find_student(students, roll)
            if st is None:
                print("Student not found.")
                continue

            mark = read_float("Enter mark (0-100): ")
            if mark is None or mark < 0 or mark > 100:
                print("Invalid mark.")
                continue
            marks: list[float] = st["marks"]  # type: ignore[assignment]
            marks.append(mark)
            print("Mark added.")

        elif choice == "5":
            if not students:
                print("No students yet.")
                continue
            for st in students:
                marks: list[float] = st["marks"]  # type: ignore[assignment]
                avg = sum(marks) / len(marks) if marks else 0.0
                print(f"Roll {st['roll']} | {st['name']} | avg = {avg:.2f}")

            courses = {str(st["course"]) for st in students}
            print("Unique courses:", courses)

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
