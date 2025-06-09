class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Попытка извлечь элемент из пустого стека")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Попытка просмотреть элемент пустого стека")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class Barge:
    def __init__(self, num_compartments, max_barrels):
        self.compartments = [Stack() for _ in range(num_compartments)]
        self.current_barrels = 0
        self.max_barrels = max_barrels
        self.max_barrels_observed = 0

    def load_barrel(self, compartment_idx, fuel_type):
        if compartment_idx < 0 or compartment_idx >= len(self.compartments):
            raise ValueError(f"Ошибка: неверный номер отсека {compartment_idx + 1}. Допустимые значения: от 1 до {len(self.compartments)}")
        
        self.compartments[compartment_idx].push(fuel_type)
        self.current_barrels += 1
        
        if self.current_barrels > self.max_barrels_observed:
            self.max_barrels_observed = self.current_barrels
        
        if self.current_barrels > self.max_barrels:
            raise ValueError(f"Ошибка: превышено максимальное количество бочек. Текущее количество: {self.current_barrels}, максимум: {self.max_barrels}")

    def unload_barrel(self, compartment_idx, expected_fuel):
        if compartment_idx < 0 or compartment_idx >= len(self.compartments):
            raise ValueError(f"Ошибка: неверный номер отсека {compartment_idx + 1}. Допустимые значения: от 1 до {len(self.compartments)}")
        
        if self.compartments[compartment_idx].is_empty():
            raise ValueError(f"Ошибка: отсек {compartment_idx + 1} пуст, нельзя извлечь бочку")
        
        actual_fuel = self.compartments[compartment_idx].pop()
        if actual_fuel != expected_fuel:
            raise ValueError(f"Ошибка: несоответствие типа топлива в отсеке {compartment_idx + 1}. Ожидалось: {expected_fuel}, получено: {actual_fuel}")
        
        self.current_barrels -= 1

    def is_empty(self):
        return self.current_barrels == 0


def main():
    try:
        with open("input.txt", "r") as f:
            # Чтение и проверка первой строки
            first_line = f.readline().strip().split()
            if len(first_line) != 3:
                print("Ошибка: неверный формат первой строки. Ожидается три числа: N K P")
                return
            
            try:
                N = int(first_line[0])
                K = int(first_line[1])
                P = int(first_line[2])
            except ValueError:
                print("Ошибка: в первой строке должны быть целые числа N, K, P")
                return
            
            if not (1 <= N <= 100000) or not (1 <= K <= 100000) or not (1 <= P <= 100000):
                print("Ошибка: числа N, K, P должны быть в диапазоне от 1 до 100000")
                return
            
            barge = Barge(K, P)
            
            for i in range(N):
                line = f.readline().strip()
                if not line:
                    print(f"Ошибка: строка {i + 2} пуста")
                    return
                
                parts = line.split()
                if len(parts) != 3:
                    print(f"Ошибка: неверный формат строки {i + 2}. Ожидается операция '+ A B' или '- A B'")
                    return
                
                op, A_str, B_str = parts
                
                try:
                    A = int(A_str)
                    B = int(B_str)
                except ValueError:
                    print(f"Ошибка: в строке {i + 2} номера отсека и топлива должны быть целыми числами")
                    return
                
                if A < 1 or A > K:
                    print(f"Ошибка: в строке {i + 2} номер отсека {A} вне допустимого диапазона (1-{K})")
                    return
                
                compartment_idx = A - 1
                
                try:
                    if op == '+':
                        barge.load_barrel(compartment_idx, B)
                    elif op == '-':
                        barge.unload_barrel(compartment_idx, B)
                    else:
                        print(f"Ошибка: в строке {i + 2} неверная операция '{op}'. Допустимые операции: '+' или '-'")
                        return
                except ValueError as e:
                    print(f"Ошибка в строке {i + 2}: {str(e)}")
                    return
            
            if not barge.is_empty():
                print("Ошибка: после обработки всех операций баржа не пуста")
            else:
                print(barge.max_barrels_observed)
    
    except FileNotFoundError:
        print("Ошибка: файл input.txt не найден")
    except Exception as e:
        print(f"Неизвестная ошибка: {str(e)}")


if __name__ == "__main__":
    main()