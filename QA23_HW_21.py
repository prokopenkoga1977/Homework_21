# Задание 1
# Пользователь вводит с клавиатуры число в диапазоне от 1 до 100. Если число кратно 3 (делится на 3 без
# остатка) нужно вывести слово Fizz. Если число кратно 5
# нужно вывести слово Buzz. Если число кратно 3 и 5 нужно
# вывести Fizz Buzz. Если число не кратно не 3 и 5 нужно
# вывести само число.
# Если пользователь ввел значение не в диапазоне от 1
# до 100 требуется вывести сообщение об ошибке.

number=int(input("Enter number: "))
if 1<=number<=100:
    if not number%3 and not number%5:
        print("Fizz Buzz")
    elif not number%3:
        print("Fizz")
    elif not number%5:
        print("Buzz")
    else:
        print(number)
else:
    print("Error! Enter a number between 1 and 100")
print("----------------------------------------------------------------")

# Задание 2
# Написать программу, которая по выбору пользователя возводит введенное им число в степень от нулевой
# до седьмой включительно.

number=int(input("Enter a number: "))
for i in range(8):
    print("Exponentiate", i,"=", number**i)
print("----------------------------------------------------------------")
# Задание 3
# Написать программу подсчета стоимости разговора
# для разных мобильных операторов. Пользователь вводит
# стоимость разговора и выбирает с какого на какой оператор он звонит. Вывести стоимость на экран.

cost_call=[
    0.10, # $/min Kyivstar -> Kyivstar
    0.09, # $/min Vodafone -> Vodafone
    0.15, # $/min Kyivstar -> Vodafone
    0.20, # $/min Vodafone -> Kyivstar
 ]
operator_choise=[
    1, "Kyivstar -> Kyivstar",
    2, "Vodafone -> Vodafone", 
    3, "Kyivstar -> Vodafone",
    4, "Vodafone -> Kyivstar",
]
call_duration=int(input("Enter your call duration, min: "))
print (operator_choise)
operator_choise=int(input("Enter operator choise (1-4): "))
if 1<=operator_choise<=4:
        print("Cost, $: ", round(cost_call[operator_choise-1]*call_duration,2))
else:
    print("Error! Enter a valid operator choise from 1 to 4")
print("----------------------------------------------------------------")
# Задание 4
# Зарплата менеджера составляет 200$ + процент от продаж, продажи до 500$ — 3%, от 500 до 1000 — 5%, свыше
# 1000 — 8%. Пользователь вводит с клавиатуры уровень
# продаж для трех менеджеров. Определить их зарплату,
# определить лучшего менеджера, начислить ему премию
# 200$, вывести итоги на экран.

sales_percentage=[
    0.03, # 3% - sales up to 500$
    0.05, # 5% - sales from 500$ to 1000$
    0.08, # 8% - sales over 1000$
]

salary=200
sales_1=int(input("Enter Mike's sales, $: "))
sales_2=int(input("Enter Tom's sales, $: "))
sales_3=int(input("Enter Bob's sales, $: "))

if sales_1 >1000:
    salary_1=salary+sales_1*sales_percentage[2] 
else:
    if sales_1<500:
       salary_1=salary+sales_1*sales_percentage[0]
    else:
       salary_1=salary+sales_1*sales_percentage[1]  
if sales_2 >1000:
    salary_2=salary+sales_2*sales_percentage[2] 
else:
    if sales_2<500:
       salary_2=salary+sales_2*sales_percentage[0]
    else:
       salary_2=salary+sales_2*sales_percentage[1] 
if sales_3 >1000:
    salary_3=salary+sales_2*sales_percentage[2] 
else:
    if sales_3<500:
       salary_3=salary+sales_3*sales_percentage[0]
    else:
       salary_3=200+sales_3*sales_percentage[1] 
if salary_1>salary_2 and salary_1>salary_3:
       print("The best manager - Mike")
       salary_1+=200  
if salary_2>salary_1 and salary_2>salary_3:
       print("The best manager - Tom") 
       salary_2+=200
if salary_3>salary_1 and salary_3>salary_2:
       print("The best manager - Bob") 
       salary_3+=200
print("Mike's salary, $: ", salary_1)  
print("Tom's salary, $: ", salary_2)  
print("Bob's salary, $: ", salary_3)      
       
       
 