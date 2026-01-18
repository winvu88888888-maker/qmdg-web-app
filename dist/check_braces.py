def check_braces(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    stack = []
    lines = content.split('\n')
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char in '{[(':
                stack.append((char, i + 1, j + 1))
            elif char in '}])':
                if not stack:
                    print(f"Extra closing {char} at line {i+1}, col {j+1}")
                    return
                opening, oi, oj = stack.pop()
                if (opening == '{' and char != '}') or \
                   (opening == '[' and char != ']') or \
                   (opening == '(' and char != ')'):
                    print(f"Mismatched {char} at line {i+1}, col {j+1} (matches {opening} at line {oi}, col {oj})")
                    return
    
    if stack:
        for char, oi, oj in stack:
            print(f"Unclosed {char} at line {oi}, col {oj}")
    else:
        print("All braces are balanced!")

if __name__ == "__main__":
    check_braces('qmdg_data.py')
