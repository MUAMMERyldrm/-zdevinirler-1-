class TuringMachine:
    def __init__(self, input_string):
    
        self.tape = list(input_string) + [' ']
        self.head_position = 0
        self.current_state = 'q0'
        self.halted = False
        self.result = "RED"

    def print_current_step(self, symbol, direction):
        
        tape_visual = []
        for i, char in enumerate(self.tape):
            display_char = '_' if char == ' ' else char
            if i == self.head_position:
                tape_visual.append(f"[{display_char}]")
            else:
                tape_visual.append(display_char)
        
        print(f"Durum: {self.current_state} | Okunan: '{'boşluk' if symbol == ' ' else symbol}' | Hareket: {direction} | Bant: {' '.join(tape_visual)}")

    def run_simulation(self):
        print(f"\n--- Girdi Analizi Başlıyor: '{''.join(self.tape).strip()}' ---")
        
        while not self.halted:
           
            symbol = self.tape[self.head_position]
            
            
            is_digit = '0' <= symbol <= '9'
            is_upper_letter = 'A' <= symbol <= 'Z'
            is_blank = (symbol == ' ')

            
            next_state = 'RED'
            direction = 'R'

            if self.current_state == 'q0':
                if is_digit: next_state = 'q1'
            
            elif self.current_state == 'q1':
                if is_digit: next_state = 'q2'
            
            elif self.current_state == 'q2':
                if is_upper_letter: next_state = 'q3'
            
            elif self.current_state == 'q3':
                if is_upper_letter: next_state = 'q4'
            
            elif self.current_state == 'q4':
                if is_digit: next_state = 'q5'
            
            elif self.current_state == 'q5':
                if is_digit: next_state = 'q6'
            
            elif self.current_state == 'q6':
                if is_digit: next_state = 'q7'
            
            elif self.current_state == 'q7':
                if is_blank:
                    self.result = "KABUL"
                    self.halted = True
                    direction = 'S (Dur)'
                    self.print_current_step(symbol, direction)
                    break
                else:
                    next_state = 'RED'

            
            if next_state == 'RED':
                self.print_current_step(symbol, 'S (Dur)')
                self.result = "RED"
                self.halted = True
                break

            
            self.print_current_step(symbol, direction)
            self.current_state = next_state
            
            if direction == 'R':
                self.head_position += 1

        print(f"Sonuç: {self.result}")
        return self.result


# --- Test Alanı ve Otomasyon ---
if __name__ == "__main__":
    
    valid_inputs = ["55AB123", "34TR456", "06AA789", "10XY999", "34AB123"]
    invalid_inputs = ["5AB123", "555AB12", "34A1234", "AB34123", "34AB12X", "55ab123"]

    print("=========================================")
    print("      GEÇERLİ GİRDİLERİN TESTLERİ        ")
    print("=========================================")
    for inp in valid_inputs:
        tm = TuringMachine(inp)
        tm.run_simulation()

    print("\n=========================================")
    print("     GEÇERSİZ GİRDİLERİN TESTLERİ        ")
    print("=========================================")
    for inp in invalid_inputs:
        tm = TuringMachine(inp)
        tm.run_simulation()
        
    print("\n=========================================")
    print("     KULLANICI ETKİLEŞİMLİ TEST MODU     ")
    print("=========================================")
    user_input = input("Lütfen kontrol etmek istediğiniz plakayı girin: ")
    tm = TuringMachine(user_input)
    tm.run_simulation()