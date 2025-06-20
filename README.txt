Баржа с топливными бочками
Анянов Кирилл, Группа ИТ-4

Описание программы
Программа моделирует работу баржи с K отсеками, в которые последовательно погружаются/выгружаются бочки с топливом по принципу LIFO (последним пришел - первым ушел). Цель - определить максимальное количество бочек, одновременно находящихся на барже, либо зафиксировать ошибки операций.

Алгоритм решения
1. Структуры данных
    Каждый отсек баржи реализован как стек (класс Stack)
    Баржа (класс Barge) управляет K отсеками и отслеживает:
      Текущее количество бочек
      Максимальное допустимое количество бочек (P)
      Наблюдаемый максимум бочек

2. Обработка операций
    Погрузка (+ A B)
      Проверка: 1 ≤ A ≤ K
      Добавление бочки типа B в отсек (A-1)
      Обновление счетчика бочек
      Проверка: не превышен ли лимит P
    Выгрузка (- A B)
      Проверка: 1 ≤ A ≤ K
      Проверка: отсек не пуст
      Сверка типа извлеченной бочки с ожидаемым (B)

3. Проверки корректности
    Корректность формата входных данных
    Соответствие диапазонов: 1 ≤ N, K, P ≤ 100000
    Корректность операций (+, -) и параметров
    Совпадение типов топлива при выгрузке
    Отсутствие переполнения баржи
    Пустота баржи после всех операций

4. Обработка ошибок
    Любая ошибка → вывод "Error"
    Успешное выполнение → вывод максимального количества бочек


Использование
1. Создайте файл input.txt в формате:
N K P
операция_1
операция_2
...
операция_N

Где:
- N: количество операций
- K: количество отсеков
- P: максимальное допустимое количество бочек
- Операции: 
  + A B (погрузка) 
  - A B (выгрузка)
  (A - номер отсека, B - вид топлива)

2. Запустите программу:
python project.py

Пример
Файл input.txt:
6 1 2
+ 1 1
+ 1 2
- 1 2
- 1 1
+ 1 3
- 1 3

Вывод программы:
2