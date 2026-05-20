
# ==========================================
# Password Generator for Customer Support
# ==========================================

# ✅ Step 1: Get a valid phone number
while True:
    phone = input("Enter the phone number (11 digits, must start with 0): ")

    if len(phone) == 11 and phone.isdigit() and phone.startswith("0"):
        break
    else:
        print("❌ Invalid phone number. Please try again.\n")


# ✅ Step 2: Get a valid project name (at least 4 characters)
while True:
    project = input(
        "Enter at least 4 characters (e.g., website/company/email/provider): "
    )

    if len(project) >= 4:
        break
    else:
        print("❌ Must be at least 4 characters. Please try again.\n")


# ==========================================
# 🔐 MAIN PASSWORD FORMULA
# ==========================================

# ✅ Step A: Sum of the first 5 digits
sum_first5 = sum(int(digit) for digit in phone[:5])

# ✅ Step B: 3rd character from project
char = project[2]
char_upper = char.upper()
char_lower = char.lower()

# ✅ Step C: last 2 digits → digit % digit
last_two = phone[-2:]
a = int(last_two[0])
b = int(last_two[1])

verify_code = a % b if b != 0 else a

# ✅ Build main password
password_main = f"{sum_first5} * {char_upper}!{char_lower}! {verify_code}"


# ==========================================
# 🔁 ALTERNATIVE PASSWORDS (BASED ON MAIN)
# ==========================================

# Option 1: replace " " → ?, "*" → /, "!" → \
alt1 = password_main.replace(" ", "?").replace("*", "/").replace("!", "\\")

# Option 2: replace " " → @, "*" → &, "!" → *
alt2 = password_main.replace(" ", "@").replace("*", "&").replace("!", "*")

# Option 3: replace " " → %, "*" → £, "!" → _
alt3 = password_main.replace(" ", "%").replace("*", "£").replace("!", "_")


# ==========================================
# ✅ OUTPUT
# ==========================================

print("\n✅ Generated Passwords:\n")

print("🔹 Main Password:")
print(password_main)

print("\n🔹 Alternative Options:")
print("Option 1:", alt1)
print("Option 2:", alt2)
print("Option 3:", alt3)
