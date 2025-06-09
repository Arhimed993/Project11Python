class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Error")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Error")

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
            raise ValueError("Error")
        
        self.compartments[compartment_idx].push(fuel_type)
        self.current_barrels += 1
        
        if self.current_barrels > self.max_barrels_observed:
            self.max_barrels_observed = self.current_barrels
        
        if self.current_barrels > self.max_barrels:
            raise ValueError("Error")

    def unload_barrel(self, compartment_idx, expected_fuel):
        if compartment_idx < 0 or compartment_idx >= len(self.compartments):
            raise ValueError("Error")
        
        if self.compartments[compartment_idx].is_empty():
            raise ValueError("Error")
        
        actual_fuel = self.compartments[compartment_idx].pop()
        if actual_fuel != expected_fuel:
            raise ValueError("Error")
        
        self.current_barrels -= 1

    def is_empty(self):
        return self.current_barrels == 0


def main():
    try:
        with open("input.txt", "r") as f:
            first_line = f.readline().strip().split()
            if len(first_line) != 3:
                print("Error")
                return
            
            try:
                N = int(first_line[0])
                K = int(first_line[1])
                P = int(first_line[2])
            except ValueError:
                print("Error")
                return
            
            if not (1 <= N <= 100000) or not (1 <= K <= 100000) or not (1 <= P <= 100000):
                print("Error")
                return
            
            barge = Barge(K, P)
            
            for i in range(N):
                line = f.readline().strip()
                if not line:
                    print("Error")
                    return
                
                parts = line.split()
                if len(parts) != 3:
                    print("Error")
                    return
                
                op, A_str, B_str = parts
                
                try:
                    A = int(A_str)
                    B = int(B_str)
                except ValueError:
                    print("Error")
                    return
                
                if A < 1 or A > K:
                    print("Error")
                    return
                
                compartment_idx = A - 1
                
                try:
                    if op == '+':
                        barge.load_barrel(compartment_idx, B)
                    elif op == '-':
                        barge.unload_barrel(compartment_idx, B)
                    else:
                        print("Error")
                        return
                except ValueError:
                    print("Error")
                    return
            
            if not barge.is_empty():
                print("Error")
            else:
                print(barge.max_barrels_observed)
    
    except FileNotFoundError:
        print("Error")
    except Exception:
        print("Error")


if __name__ == "__main__":
    main()