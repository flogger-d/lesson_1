#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Задача-1: поработайте с переменными, создайте несколько,
# выведите на экран, запросите от пользователя и сохраните в переменную, выведите на экран

print("Задача #1:")
var_int      = 10
var_bool     = True
var_float    = 3.141592654
var_string   = "Hello there!"

print("Значения переменных: ")
print("var_int  ="   , var_int)
print("var_bool  ="  , var_bool)
print("var_float  =" , var_float)
print("var_string = '" , var_string, "'")

print("Запрашиваем и вводим новые значения")
var_int     = int  (input("Введите var_int: "))
var_bool    = bool (input("Введите var_bool: "))
var_float   = float(input("Введите var_float: "))
var_string  =       input("Введите var_string: ")

print("Новые значения переменных: ")
print("var_int  = ", var_int)
print("var_bool  = ", var_bool)
print("var_float  = ", var_float)
print("var_string = '", var_string, "'")

# Задача-2: Запросите от пользователя число, сохраните в переменную,
# прибавьте к числу 2 и выведите результат на экран.
# Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.

print("Задача #2:")
import math

value = float('nan')
while math.isnan(value) :
  try:
    value = float(input("Введите число: "))
  except Exception:
    print("Ошибка! Требуется ввести число!")
    
print("Число + 2 = ", (value+2))


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

print("Задача #3:")


age = 0
while True:
  age = input("Введите свой возраст (целое число!): ")
  try:
    age = int(age)
    if age < 0:
      print("Вы фсё врёти! Так не бывает!")
      continue
    else: 
      break
  except Exception:
    print("Требуется ввести число")
    continue

message = "Доступ разрешен" if age >= 18 else "Извините, пользование данным ресурсом только с 18 лет"
print(message)


