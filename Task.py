# # Task-1
# numbers = []
# # Range(5) 0-dan 5-ə qədər (lakin 5-i daxil etmədən) ardıcıllıq törədən ədədləri ifadə edir.
# for i in range(5):
#     num1 = int(input("Rəqəm daxil edin: "))
#     numbers.append(num1)

# # sort metodu ile siralayiriq
# numbers.sort()

# # Nəticəni çap edirik
# print("Sıralanmış list:", numbers)



#########################################################################################################################


# # Task-2
# cumle = input("Cümlə daxil edin: ")
# # Split metoduyla cümlədəki hər bir sözü ayırırıq
# kəlimələr = cumle.split()
# # Hər bir sözün hərflərini alfabetik sıraya 
# siralanmis_kəlimələr = [''.join(sorted(word)) for word in kəlimələr]
# # Yeni cümlə
# yeni_cumle = ' '.join(siralanmis_kəlimələr)

# print("Nəticə:", yeni_cumle)


###########################################################################################################################


# Task-3
n = 13
cehd = 0

while True:
    daxil = int(input("Bir ədəd daxil edin: "))
    cehd += 1
    if daxil == n:
        print(f"Təbriklər! {cehd} cəhdə tapdınız.")
        break



########################################################################################################################
 
# Task-4
# for x in range(1, 101):
#     müraciət = 0
#     for bölünən in range(2, x):
#         if x % bölünən == 0:
#             müraciət = 1
#             break
#     if müraciət == 0:
#         print(x)

