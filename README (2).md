#  Password Strength Checker

A simple Python script that evaluates the strength of a user-provided password based on multiple criteria such as length, character variety, and use of special symbols.

---

##  Features

-  Checks if the password length is at least 8 characters  
- Ensures the presence of:
  - Lowercase letters
  - Uppercase letters
  - Digits (0–9)
  - Special characters (`~!@#$%^&*()_-+={}[]|\;'<>,.?/`)
-  Provides feedback on missing requirements
-  Classifies password strength as:
  - **WEAK** (≤ 2 conditions met)
  - **MEDIUM** (3–4 conditions met)
  - **STRONG** (all 5 conditions met)

---

##  Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/password-strength-checker.git
   cd password-strength-checker
