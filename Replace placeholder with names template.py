import pyperclip

def get_names():
    print("Paste the list of names (one per line), then press Enter twice:")
    lines = []
    while True:
        line = input()
        if line.strip() == '':
            break
        # Title-case the name to fix capitalization
        lines.append(line.strip().title())
    return lines

def get_multiline_input(prompt):
    print(prompt)
    lines = []
    blank_lines = 0  # Counter for consecutive blank lines
    
    while True:
        line = input()
        if line == "":  # Empty line
            blank_lines += 1
            if blank_lines == 3:  # Three blank lines signals the end of input
                break
        else:
            blank_lines = 0  # Reset blank line counter if input is given
        lines.append(line)

    return "\n".join(lines)  # Join the lines into a single string with newlines

def main():
    names = get_names()
    
    # Prompt for custom placeholder
    placeholder = input("\nEnter the placeholder you want to use (e.g., XX):\n").strip()

    # Now using the custom function to get a multi-line message template
    template = get_multiline_input(f"\nEnter your message template using {placeholder} as placeholder (press Enter three times to finish):\n")
    
    print("\nReady! Press Enter to generate and copy the next message, or type 'b' to go back.\n")

    index = 0

    while 0 <= index < len(names):
        name = names[index]
        message = template.replace(placeholder, name)
        pyperclip.copy(message)
        print(f"[{index+1}/{len(names)}] Copied message for {name} to clipboard.")

        user_input = input("Press Enter for next, or type 'b' to go back: ").strip().lower()

        if user_input == 'b':
            if index == 0:
                print("You're already at the first name. Can't go back further.")
            else:
                index -= 1
                continue
        else:
            index += 1

    print("\nAll messages copied. Done!")

if __name__ == "__main__":
    main()