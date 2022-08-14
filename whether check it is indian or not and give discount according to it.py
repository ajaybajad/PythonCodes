country = 1
gender = 1
fess = int(input("Enter The Fees:"))
country = int(input("Press 1 for Indian & 0 for Others:"))
if country == 1:
    gender = int(input("Press 1 For Male & 0 for Female:"))
if gender == 2:
    print("Discount = 30")
elif gender ==1:
    print("discount = 20")

print("\033[3;31;44m Program By Ajay Bajad")