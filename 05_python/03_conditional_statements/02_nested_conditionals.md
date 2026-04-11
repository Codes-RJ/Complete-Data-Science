# 📘 NESTED CONDITIONALS – COMPLETE GUIDE

## 📌 Table of Contents
1. [What are Nested Conditionals?](#what-are-nested-conditionals)
2. [Basic Nested `if`](#basic-nested-if)
3. [Nested `if-else`](#nested-if-else)
4. [Nested `if-elif-else`](#nested-if-elif-else)
5. [Deep Nesting](#deep-nesting)
6. [Refactoring Nested Conditionals](#refactoring-nested-conditionals)
7. [Real-World Examples](#real-world-examples)
8. Common Pitfalls
9. Practice Exercises

---

## What are Nested Conditionals?

**Nested conditionals** are conditionals inside other conditionals. They are used when a decision depends on multiple levels of conditions.

```python
# Basic nested conditional
age = 25
has_license = True

if age >= 18:
    print("Age check passed")
    if has_license:
        print("You can drive")
    else:
        print("Get a license first")
else:
    print("Too young to drive")
```

**When to Use Nested Conditionals:**
- When conditions are dependent on each other
- When you need to check multiple levels of conditions
- When different combinations of conditions lead to different outcomes

---

## Basic Nested `if`

### Syntax

```python
if outer_condition:
    # Outer block
    if inner_condition:
        # Inner block
        statement
```

### Examples

```python
# Simple nesting
x = 10
y = 20

if x > 0:
    print("x is positive")
    if y > 0:
        print("Both x and y are positive")

# Multiple inner conditions
score = 85
attendance = 90

if score >= 60:
    print("Score requirement met")
    if attendance >= 75:
        print("Attendance requirement met")
        print("Course passed")
    else:
        print("Attendance requirement not met")

# Real example: Discount eligibility
is_member = True
purchase_amount = 150
years_member = 3

if is_member:
    print("Member verified")
    if years_member >= 5:
        discount = 0.25
        print("Gold member discount")
    elif years_member >= 2:
        discount = 0.15
        print("Silver member discount")
    else:
        discount = 0.10
        print("Bronze member discount")
    
    if purchase_amount >= 100:
        discount += 0.05
        print("Additional bulk discount")
else:
    discount = 0
    print("No discount for non-members")

print(f"Total discount: {discount * 100}%")
```

---

## Nested `if-else`

### Syntax

```python
if outer_condition:
    if inner_condition:
        # Inner true block
        statement
    else:
        # Inner false block
        statement
else:
    # Outer false block
    statement
```

### Examples

```python
# Complete nested if-else
age = 25
has_license = True
has_insurance = False

if age >= 18:
    print("Age requirement met")
    if has_license:
        print("License verified")
        if has_insurance:
            print("You can drive legally")
        else:
            print("Need insurance to drive")
    else:
        print("Need a driver's license")
else:
    print("Too young to drive")

# Login system with nested checks
username = "admin"
password = "secret123"
captcha = "ABC12"

if username == "admin":
    print("Username correct")
    if password == "secret123":
        print("Password correct")
        if captcha == "ABC12":
            print("Login successful!")
            print("Welcome admin")
        else:
            print("Invalid captcha")
    else:
        print("Invalid password")
else:
    print("Username not found")
```

---

## Nested `if-elif-else`

### Syntax

```python
if outer_condition1:
    if inner_condition1:
        statement
    elif inner_condition2:
        statement
    else:
        statement
elif outer_condition2:
    if inner_condition3:
        statement
    else:
        statement
else:
    statement
```

### Examples

```python
# Complex nested if-elif-else
user_role = "editor"
resource = "document"
action = "edit"

if user_role == "admin":
    print("Admin access")
    # Admin can do anything
    print(f"Admin can {action} {resource}")
    
elif user_role == "editor":
    print("Editor access")
    if resource == "document":
        if action == "edit":
            print("Editor can edit documents")
        elif action == "read":
            print("Editor can read documents")
        else:
            print(f"Editor cannot {action} documents")
    elif resource == "comment":
        print("Editor can manage comments")
    else:
        print(f"Editor cannot access {resource}")
        
elif user_role == "viewer":
    print("Viewer access")
    if action == "read":
        print("Viewer can read")
    else:
        print(f"Viewer cannot {action}")
        
else:
    print("Unknown role")

# Grade with nested conditions
score = 85
has_extra_credit = True
attendance = 90

if score >= 60:
    print("Base requirement met")
    if has_extra_credit:
        print("Extra credit applied")
        if score >= 90:
            grade = "A+"
        elif score >= 80:
            grade = "A"
        elif score >= 70:
            grade = "B+"
        else:
            grade = "B"
    else:
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        else:
            grade = "D"
    
    if attendance >= 80:
        print(f"Final grade: {grade}")
    else:
        print(f"Grade reduced due to low attendance: {grade}")
        
else:
    print("Failed - Score below 60")
```

---

## Deep Nesting

Multiple levels of nested conditionals (3+ levels).

### Example

```python
# Deep nesting (use sparingly)
def process_order(user, product, quantity, payment_method):
    if user:
        print("User exists")
        if user.get("is_active"):
            print("User is active")
            if user.get("has_permission"):
                print("User has permission")
                if product:
                    print("Product exists")
                    if product.get("in_stock"):
                        print("Product in stock")
                        if product.get("stock") >= quantity:
                            print("Sufficient quantity")
                            if payment_method:
                                print("Payment method provided")
                                if payment_method == "credit_card":
                                    print("Processing credit card...")
                                    return "Order successful"
                                elif payment_method == "paypal":
                                    print("Processing PayPal...")
                                    return "Order successful"
                                else:
                                    return "Unsupported payment method"
                            else:
                                return "No payment method"
                        else:
                            return f"Insufficient stock. Available: {product.get('stock')}"
                    else:
                        return "Product out of stock"
                else:
                    return "Product not found"
            else:
                return "User lacks permission"
        else:
            return "User inactive"
    else:
        return "User not found"

# Test
user = {"is_active": True, "has_permission": True}
product = {"in_stock": True, "stock": 10}
result = process_order(user, product, 5, "credit_card")
print(result)
```

### Problem with Deep Nesting

```python
# ❌ Hard to read and maintain
if condition1:
    if condition2:
        if condition3:
            if condition4:
                if condition5:
                    result = "All true"
                else:
                    result = "Condition5 false"
            else:
                result = "Condition4 false"
        else:
            result = "Condition3 false"
    else:
        result = "Condition2 false"
else:
    result = "Condition1 false"

# ✅ Better - Use guard clauses
if not condition1:
    result = "Condition1 false"
elif not condition2:
    result = "Condition2 false"
elif not condition3:
    result = "Condition3 false"
elif not condition4:
    result = "Condition4 false"
elif not condition5:
    result = "Condition5 false"
else:
    result = "All true"
```

---

## Refactoring Nested Conditionals

### Method 1: Guard Clauses (Early Returns)

```python
# ❌ Deep nesting
def calculate_discount(price, is_member, years_member, has_coupon):
    if price > 0:
        if is_member:
            if years_member >= 5:
                discount = 0.25
                if has_coupon:
                    discount += 0.10
                return discount
            elif years_member >= 2:
                discount = 0.15
                if has_coupon:
                    discount += 0.10
                return discount
            else:
                discount = 0.10
                if has_coupon:
                    discount += 0.10
                return discount
        else:
            if has_coupon:
                return 0.10
            return 0
    else:
        return 0

# ✅ Guard clauses (early returns)
def calculate_discount(price, is_member, years_member, has_coupon):
    if price <= 0:
        return 0
    
    if not is_member:
        return 0.10 if has_coupon else 0
    
    # Member logic
    if years_member >= 5:
        discount = 0.25
    elif years_member >= 2:
        discount = 0.15
    else:
        discount = 0.10
    
    if has_coupon:
        discount += 0.10
    
    return min(discount, 0.50)  # Cap at 50%
```

### Method 2: Combine Conditions with `and`/`or`

```python
# ❌ Nested
if user.is_authenticated:
    if user.has_permission:
        if user.is_active:
            grant_access()

# ✅ Combined
if user.is_authenticated and user.has_permission and user.is_active:
    grant_access()
```

### Method 3: Extract to Separate Functions

```python
# ❌ Nested in main code
def process_data(data):
    if data:
        if data.get('valid'):
            if data.get('processed'):
                return data.get('result')
    return None

# ✅ Extracted functions
def is_valid_data(data):
    return data and data.get('valid')

def is_processed(data):
    return data and data.get('processed')

def process_data(data):
    if not is_valid_data(data):
        return None
    if not is_processed(data):
        return None
    return data.get('result')
```

### Method 4: Use Dictionary Mapping

```python
# ❌ Many nested if-elif
def get_discount(user_type, years):
    if user_type == "premium":
        if years >= 5:
            return 0.25
        elif years >= 2:
            return 0.20
        else:
            return 0.15
    elif user_type == "standard":
        if years >= 5:
            return 0.15
        elif years >= 2:
            return 0.10
        else:
            return 0.05
    else:
        return 0

# ✅ Dictionary mapping
discounts = {
    "premium": {5: 0.25, 2: 0.20, 0: 0.15},
    "standard": {5: 0.15, 2: 0.10, 0: 0.05}
}

def get_discount(user_type, years):
    tier = discounts.get(user_type, {0: 0})
    for threshold in sorted(tier.keys(), reverse=True):
        if years >= threshold:
            return tier[threshold]
    return 0
```

---

## Real-World Examples

### Example 1: ATM Withdrawal System

```python
class ATM:
    def __init__(self):
        self.balance = 1000
        self.daily_limit = 500
        self.withdrawn_today = 0
    
    def withdraw(self, amount, pin, account_type):
        """Process withdrawal with multiple validation levels"""
        
        # Level 1: PIN validation
        if pin != "1234":
            return "Invalid PIN"
        
        print("PIN verified")
        
        # Level 2: Account type validation
        if account_type not in ["checking", "savings"]:
            return "Invalid account type"
        
        print(f"Account type: {account_type}")
        
        # Level 3: Amount validation
        if amount <= 0:
            return "Invalid amount"
        
        if amount > self.balance:
            return f"Insufficient funds. Available: ${self.balance}"
        
        print(f"Amount: ${amount}")
        
        # Level 4: Daily limit validation
        if amount > self.daily_limit:
            return f"Exceeds daily limit of ${self.daily_limit}"
        
        if self.withdrawn_today + amount > self.daily_limit:
            remaining = self.daily_limit - self.withdrawn_today
            return f"Daily limit exceeded. You can withdraw ${remaining} more today"
        
        # Level 5: Account-specific rules
        if account_type == "savings":
            if amount > 500:
                return "Savings accounts have $500 withdrawal limit per transaction"
            if self.balance - amount < 100:
                return "Savings accounts must maintain minimum balance of $100"
        
        # All checks passed
        self.balance -= amount
        self.withdrawn_today += amount
        
        return {
            'status': 'success',
            'amount': amount,
            'new_balance': self.balance,
            'remaining_daily': self.daily_limit - self.withdrawn_today
        }

# Test the ATM
atm = ATM()

print("ATM WITHDRAWAL SYSTEM")
print("=" * 50)

test_cases = [
    (100, "1234", "checking"),      # Valid
    (100, "9999", "checking"),      # Wrong PIN
    (600, "1234", "checking"),      # Exceeds daily limit
    (2000, "1234", "checking"),     # Insufficient funds
    (300, "1234", "savings"),       # Valid savings
    (600, "1234", "savings"),       # Savings limit
]

for amount, pin, account_type in test_cases:
    print(f"\nRequest: ${amount} from {account_type}")
    result = atm.withdraw(amount, pin, account_type)
    
    if isinstance(result, dict):
        print(f"✓ Success! Withdrew ${result['amount']}")
        print(f"  New balance: ${result['new_balance']}")
        print(f"  Remaining daily limit: ${result['remaining_daily']}")
    else:
        print(f"✗ Failed: {result}")
```

### Example 2: Loan Approval System

```python
class LoanSystem:
    def __init__(self):
        self.credit_thresholds = {
            "excellent": 750,
            "good": 700,
            "fair": 650
        }
    
    def check_eligibility(self, credit_score, income, employment_years, loan_amount, existing_debt):
        """Multi-level loan approval check"""
        
        print("\n" + "=" * 50)
        print("LOAN ELIGIBILITY CHECK")
        print("=" * 50)
        
        # Level 1: Credit score check
        if credit_score < self.credit_thresholds["fair"]:
            return {
                'approved': False,
                'reason': f"Credit score too low: {credit_score} (minimum 650)"
            }
        
        print(f"✓ Credit score: {credit_score}")
        
        # Level 2: Employment history
        if employment_years < 1:
            return {
                'approved': False,
                'reason': f"Employment too short: {employment_years} years (minimum 1 year)"
            }
        
        print(f"✓ Employment: {employment_years} years")
        
        # Level 3: Income vs loan amount
        max_loan_by_income = income * 5
        if loan_amount > max_loan_by_income:
            return {
                'approved': False,
                'reason': f"Loan amount ${loan_amount} exceeds ${max_loan_by_income} (5x annual income)"
            }
        
        print(f"✓ Loan amount: ${loan_amount} (within 5x income)")
        
        # Level 4: Debt-to-income ratio
        monthly_income = income / 12
        existing_monthly_payment = existing_debt * 0.05  # Assume 5% of debt as monthly payment
        new_monthly_payment = loan_amount * 0.02  # Assume 2% of loan as monthly payment
        total_monthly_debt = existing_monthly_payment + new_monthly_payment
        dti_ratio = (total_monthly_debt / monthly_income) * 100
        
        if dti_ratio > 40:
            return {
                'approved': False,
                'reason': f"Debt-to-income ratio too high: {dti_ratio:.1f}% (maximum 40%)"
            }
        
        print(f"✓ DTI ratio: {dti_ratio:.1f}%")
        
        # Level 5: Determine interest rate and loan terms
        if credit_score >= self.credit_thresholds["excellent"]:
            rate = 3.5
            tier = "Excellent"
        elif credit_score >= self.credit_thresholds["good"]:
            rate = 5.0
            tier = "Good"
        else:
            rate = 7.5
            tier = "Fair"
        
        # Level 6: Additional discounts for long-term customers
        if employment_years >= 5:
            rate -= 0.5
            print("✓ Additional 0.5% discount for long-term employment")
        
        monthly_payment = (loan_amount * (rate / 100 / 12)) / (1 - (1 + rate / 100 / 12) ** -60)
        
        return {
            'approved': True,
            'tier': tier,
            'interest_rate': rate,
            'monthly_payment': round(monthly_payment, 2),
            'total_payment': round(monthly_payment * 60, 2),
            'total_interest': round(monthly_payment * 60 - loan_amount, 2)
        }

# Test the system
loan_system = LoanSystem()

applicants = [
    {"name": "Alice", "credit": 780, "income": 80000, "employment": 5, "loan": 100000, "debt": 10000},
    {"name": "Bob", "credit": 680, "income": 50000, "employment": 2, "loan": 150000, "debt": 20000},
    {"name": "Charlie", "credit": 620, "income": 60000, "employment": 3, "loan": 50000, "debt": 5000},
    {"name": "Diana", "credit": 720, "income": 40000, "employment": 0.5, "loan": 80000, "debt": 15000},
]

for applicant in applicants:
    print(f"\nApplicant: {applicant['name']}")
    print(f"Credit: {applicant['credit']}, Income: ${applicant['income']}, Employment: {applicant['employment']} years")
    
    result = loan_system.check_eligibility(
        applicant['credit'],
        applicant['income'],
        applicant['employment'],
        applicant['loan'],
        applicant['debt']
    )
    
    if result['approved']:
        print(f"\n✅ LOAN APPROVED!")
        print(f"  Tier: {result['tier']}")
        print(f"  Interest Rate: {result['interest_rate']}%")
        print(f"  Monthly Payment: ${result['monthly_payment']}")
        print(f"  Total Payment: ${result['total_payment']}")
        print(f"  Total Interest: ${result['total_interest']}")
    else:
        print(f"\n❌ LOAN DENIED")
        print(f"  Reason: {result['reason']}")
```

### Example 3: Travel Booking System

```python
class TravelBooking:
    def __init__(self):
        self.destinations = {
            "NYC": {"base_price": 500, "season_multiplier": 1.5},
            "LA": {"base_price": 450, "season_multiplier": 1.3},
            "CHI": {"base_price": 350, "season_multiplier": 1.2},
        }
    
    def calculate_price(self, destination, travelers, days, season, hotel_required, flight_required):
        """Multi-level travel price calculator"""
        
        print("\n" + "=" * 50)
        print("TRAVEL BOOKING SYSTEM")
        print("=" * 50)
        
        # Level 1: Destination validation
        if destination not in self.destinations:
            return {"error": f"Destination {destination} not available"}
        
        dest_info = self.destinations[destination]
        print(f"✓ Destination: {destination}")
        
        # Level 2: Travelers validation
        if travelers < 1:
            return {"error": "At least 1 traveler required"}
        if travelers > 10:
            return {"error": "Maximum 10 travelers per booking"}
        
        print(f"✓ Travelers: {travelers}")
        
        # Level 3: Days validation
        if days < 1:
            return {"error": "Minimum 1 day stay required"}
        if days > 30:
            return {"error": "Maximum 30 days stay"}
        
        print(f"✓ Duration: {days} days")
        
        # Level 4: Calculate base price
        base_price = dest_info["base_price"] * travelers * days
        
        # Level 5: Apply season multiplier
        if season == "peak":
            multiplier = dest_info["season_multiplier"]
            base_price *= multiplier
            print(f"✓ Peak season multiplier: {multiplier}x")
        elif season == "off":
            multiplier = 0.8
            base_price *= multiplier
            print(f"✓ Off-season discount: {multiplier}x")
        
        # Level 6: Add hotel cost
        if hotel_required:
            if travelers <= 2:
                hotel_cost = 150 * days
                room_type = "Standard"
            elif travelers <= 4:
                hotel_cost = 250 * days
                room_type = "Family"
            else:
                hotel_cost = 100 * travelers * days
                room_type = "Multiple rooms"
            
            base_price += hotel_cost
            print(f"✓ Hotel: {room_type} room - ${hotel_cost}")
        
        # Level 7: Add flight cost
        if flight_required:
            flight_cost = 300 * travelers
            base_price += flight_cost
            print(f"✓ Flight: ${flight_cost}")
        
        # Level 8: Apply group discount
        if travelers >= 5:
            discount = 0.10
            discount_amount = base_price * discount
            base_price -= discount_amount
            print(f"✓ Group discount: {discount * 100}% (Saved ${discount_amount:.2f})")
        
        # Level 9: Apply early booking discount
        if days >= 7:
            discount = 0.05
            discount_amount = base_price * discount
            base_price -= discount_amount
            print(f"✓ Early booking discount: {discount * 100}% (Saved ${discount_amount:.2f})")
        
        return {
            'destination': destination,
            'travelers': travelers,
            'days': days,
            'total_price': round(base_price, 2),
            'price_per_person': round(base_price / travelers, 2),
            'price_per_day': round(base_price / days, 2)
        }

# Test the system
booking = TravelBooking()

bookings = [
    {"dest": "NYC", "travelers": 2, "days": 5, "season": "peak", "hotel": True, "flight": True},
    {"dest": "LA", "travelers": 6, "days": 3, "season": "off", "hotel": True, "flight": True},
    {"dest": "CHI", "travelers": 1, "days": 2, "season": "normal", "hotel": False, "flight": True},
    {"dest": "NYC", "travelers": 4, "days": 7, "season": "peak", "hotel": True, "flight": True},
]

for b in bookings:
    result = booking.calculate_price(
        b["dest"], b["travelers"], b["days"],
        b["season"], b["hotel"], b["flight"]
    )
    
    if "error" in result:
        print(f"\n❌ Error: {result['error']}")
    else:
        print(f"\n💰 PRICE SUMMARY")
        print(f"  Total: ${result['total_price']}")
        print(f"  Per Person: ${result['price_per_person']}")
        print(f"  Per Day: ${result['price_per_day']}")
```

---

## Common Pitfalls

### Pitfall 1: Too Many Nesting Levels

```python
# ❌ Too deep (hard to read)
if a:
    if b:
        if c:
            if d:
                if e:
                    result = "All true"

# ✅ Refactor using guard clauses
if not a: return
if not b: return
if not c: return
if not d: return
if not e: return
result = "All true"
```

### Pitfall 2: Dangling Else

```python
# ❌ Ambiguous which if the else belongs to
if condition1:
    if condition2:
        print("Both true")
else:
    print("Condition1 false")  # This belongs to outer if

# ✅ Use explicit nesting
if condition1:
    if condition2:
        print("Both true")
    else:
        print("Condition1 true, condition2 false")
else:
    print("Condition1 false")
```

### Pitfall 3: Forgetting to Handle All Cases

```python
# ❌ Missing else case
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
# What about scores below 70?

# ✅ Complete with else
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

---

## Practice Exercises

### Beginner Level

1. **Nested Even/Odd Check**
   ```python
   # Check if number is positive and even
   # Example: 4 → "Positive even", -3 → "Negative odd"
   ```

2. **Multiple Level Discount**
   ```python
   # Apply discount: member? purchase amount? years member?
   ```

3. **Login with Two-Factor**
   ```python
   # Check username, password, and 2FA code
   ```

### Intermediate Level

4. **Eligibility Checker**
   ```python
   # Check age, license, insurance for driving
   ```

5. **Order Processing**
   ```python
   # Validate: user exists? product in stock? payment valid?
   ```

6. **Hotel Booking**
   ```python
   # Check: dates available? room type? number of guests?
   ```

### Advanced Level

7. **Insurance Quote**
   ```python
   # Calculate insurance based on age, driving history, vehicle type
   ```

8. **Flight Booking System**
   ```python
   # Multi-level validation: destination, dates, passengers, seats
   ```

9. **Loan Calculator**
   ```python
   # Nested conditions for credit score, income, employment, debt
   ```

---

## Quick Reference Card

```python
# Nested if
if condition1:
    if condition2:
        # code

# Nested if-else
if condition1:
    if condition2:
        # code
    else:
        # code
else:
    # code

# Nested if-elif-else
if condition1:
    if condition2:
        # code
    elif condition3:
        # code
    else:
        # code
elif condition4:
    # code
else:
    # code

# Guard clause pattern
def func():
    if not condition1:
        return
    if not condition2:
        return
    # main logic

# Combine conditions
if condition1 and condition2 and condition3:
    # code
```

## Next Step

- Go to [03_ternary_operator.md](03_ternary_operator.md) for understanding about ternary operations.

---

*Master nested conditionals to handle complex decision-making logic! 🐍✨*

---