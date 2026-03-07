def main():
    # Ask for student's name
    name = input("Enter student name: ")
    
    # Ask for 3 subject marks
    try:
        mark1 = float(input("Enter marks for Subject 1: "))
        mark2 = float(input("Enter marks for Subject 2: "))
        mark3 = float(input("Enter marks for Subject 3: "))
        
        # Calculate the average
        average = (mark1 + mark2 + mark3) / 3
        
        # Determine the grade and status
        if average >= 75:
            grade = "A"
            status = "Pass"
        elif average >= 60:
            grade = "B"
            status = "Pass"
        elif average >= 40:
            grade = "C"
            status = "Pass"
        else:
            grade = "Fail"
            status = "Fail"
            
        # Display the result
        print(f"\nStudent Name: {name}")
        print(f"Average Marks: {average:.2f}")
        print(f"Grade: {grade}")
        print(f"Status: {status}")
            
    except ValueError:
        print("Error: Please enter valid numeric marks.")

if __name__ == "__main__":
    main()
