# 1 Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.

#day_week = int (input("Введите число: "))
# if 0<day_week<6:
#     print("Это рабочий день")   
# elif 6==day_week or day_week==7:
#     print("Этот день выходной")
# else:
#    print("Данное число не является днем недели")

  

# 2* Напишите программу для
# проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.




#3 Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

#num_1 = int(input("Введите координату точки X: "))
#num_2 = int(input("Введите координату точки Y: "))
#if num_1 > 0 and num_2 > 0:
#     print("первая четверь")
#elif num_1 < 0 and num_2 > 0:
#     print("вторая четверть")
#elif num_1 < 0 and num_2 < 0:
#     print("третья четверть")
#elif num_1 > 0 and num_2 < 0:
#     print("четверая четверть")
#else: 
#     num_1==0 or num_2==0
#     print("Коордитнаты не могут ровняться 0! ")





#4 Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

# quarter = int(input("Введите номер четверти: "))
# if quarter == 1:
#      print ("Диапазон х>0 и y>0 ")
# elif quarter == 2:
#      print ("Диапазон х<0 и y>0 ")
# elif quarter == 3:
#      print ("Диапазон х<0 и y<0 ")   
# elif quarter == 4:
#      print ("Диапазон х>0 и y<0 ")   
# else: 
#      5<quarter<0 
#      print ("Номера четверти не существует!")




#5 Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.


# import math
# Ax = float(input("Введите коордитнату точки А на оси Х: "))
# Ay = float(input("Введите коордитнату точки А на оси Y: "))
# Bx = float(input("Введите коордитнату точки B на оси Х: "))
# By = float(input("Введите коордитнату точки B на оси Y: "))
# ab = math.sqrt((Ay-Ax)**2+(By-Bx)**2)
# print('{:.2f}'.format(ab))

