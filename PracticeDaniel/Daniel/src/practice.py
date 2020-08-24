#
# print('''alsdkjfalsdkjfas;ldkj dsfgsdfgdsdfg"" sdfghi's test''')
# hola = 5
# print (hola)
# print(hola*3)
#
# print(hola/3)
# print(hola//3)
# hola3 = "bullshit"
#
# print("hola","hola2" + hola3 * 4)
#
#
# #print ("The area is ", 3.14159 *float(input("what is your radius?"))**2)

# q = 9//3
# w= 9/3
# print(q,w)
#
# r = 9 % 3
# print(r)

total_secs = int(input("How many seconds, in total?"))
hours = total_secs / 3600
print("hours",hours)
secs_still_remaining = total_secs % 3600
print("secs_still_remaining",secs_still_remaining)
minutes = secs_still_remaining // 60
print("minutes",minutes)
secs_finally_remaining = secs_still_remaining % 60

print("Hrs=", hours, " mins=", minutes,
"secs=", secs_finally_remaining)


