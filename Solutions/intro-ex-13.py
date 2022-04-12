# 
# File: intro-ex-13.py
# Auth: Martin Burolla
# Date: 8/17/2021
# Desc: Add Only Calculator
#

def should_exit(instr):
    return instr == "exit"


def main():
    print("Type exit at anytime to end program...")
    while True:
        operand1 = input("Enter first integer: ")
        if should_exit(operand1):
            break
        operand2 = input("Enter second integer: ")
        if should_exit(operand2):
            break
        total = int(operand1) + int(operand2);
        print(f'Answer: {total}.')


if __name__ == "__main__":  
    main()
