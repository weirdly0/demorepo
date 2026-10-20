
def average_marks(marks):
    return sum(marks) / len(marks)


if __name__ == "__main__":
    print("Average:", average_marks([70, 80, 90]))
    print("Empty:", average_marks([]))
