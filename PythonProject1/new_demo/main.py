from new_demo.student import Student

def main():
    st1 = Student("John", 22)
    st1.display()
    st1.grade_for(10)
    st1.grade_for(20)
    st1.grade_for(30)
    st1.grade_for(40)
    st1.display()

if __name__ == "__main__":
    main()
