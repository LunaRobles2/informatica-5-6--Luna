def main():
	print('')
	print('Please enter the following information to create your ID Card.')
	input('Press enter to continue.')

	name = input("Your name: ")
	Last_Name = input("Your Last Name: ")
	Email_Address = input("Email Adress: ")
	Phone_Number = input("Phone Number: ")
	Student_ID_Number = input("Student ID Number (This can be a mix of letters and numbers, like 'S12345'): ")
	FPT_Class= input("FPT Class (e.g., nformatica, Accounting): ")
	Expected_Graduation_Year = input("Expected Graduation Year (e.g., 2026): ")
	Favorite_Subject = input("Favorite Subject: ")
	Extracurricular_Activities = input("Extracurricular Activities (Yes or No): ")

	print ("Your ID Card is:")
	line = "-" * 45
	print(line)
	print(Last_Name.upper,name)
	print(Student_ID_Number)
	print(Email_Address)
	print(Phone_Number)
	print(FPT_Class)
	print(Expected_Graduation_Year)
	print(line)
	print(Favorite_Subject)
	print(Extracurricular_Activities)


main()