
#? Calculate simple interest and compound interest for given principal, rate and time.

# * si = (P * R * T) / 100
#* total_si = P + si 

#! total_ci = P * (1 + R / 100) ** T
#! ci = total_ci - P

p = float(input("Enter principal amount : "))
r = float(input("Enter rate : "))
t = float(input("Enter the time period : "))

SI = (p * r * t) / 100
total_si = p + SI
print(f"The simple interest is {total_si}")

total_ci= p * (1 + r /100) ** r
CI = total_ci -p
print(f"The compound interest is {CI:.2f}")




