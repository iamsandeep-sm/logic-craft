
#?nConvert a number of seconds into hours, minutes and seconds.

seconds = int(input("User please Enter seconds : " ))
hour = seconds // 3600
min = (seconds // 60) % 60
#* total_min = min % 60    --  you can add this if you don't want to write like """min = (seconds // 60) %60""" .....
sec = seconds % 60
print(f"{hour} hour , {min} minute and {sec} second")

