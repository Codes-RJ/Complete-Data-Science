# 📘 RANDOM MODULE – COMPLETE GUIDE

## 📌 Table of Contents
1. [What is the Random Module?](#what-is-the-random-module)
2. [Basic Random Functions](#basic-random-functions)
3. [Integer Random Functions](#integer-random-functions)
4. [Sequence Random Functions](#sequence-random-functions)
5. [Distribution Functions](#distribution-functions)
6. [Random Seed](#random-seed)
7. [Real-World Examples](#real-world-examples)
8. [Practice Exercises](#practice-exercises)

---

## What is the Random Module?

The `random` module provides functions for generating random numbers and making random selections. It's essential for simulations, games, sampling, and cryptography (though not for security-critical applications).

```python
import random

# Basic random number
print(random.random())      # 0.0 to 1.0
print(random.randint(1, 10))  # 1 to 10
print(random.choice(['a', 'b', 'c']))  # Random choice
```

**Key Characteristics:**
- ✅ Pseudo-random (deterministic based on seed)
- ✅ Not suitable for cryptography (use `secrets` module)
- ✅ Can be seeded for reproducible results
- ✅ Uses Mersenne Twister algorithm

---

## Basic Random Functions

### `random.random()` – Float in [0.0, 1.0)

```python
import random

# Generate random float between 0.0 and 1.0
print(random.random())   # 0.37444887175646646
print(random.random())   # 0.9507143064099162

# Generate multiple random numbers
for _ in range(5):
    print(f"{random.random():.4f}", end=" ")
print()
```

### `random.uniform(a, b)` – Float in [a, b]

```python
import random

# Random float between 1.0 and 10.0
print(random.uniform(1, 10))    # 5.487654321
print(random.uniform(1, 10))    # 8.123456789

# Negative range
print(random.uniform(-10, -5))  # -7.123456789

# With different types
print(random.uniform(1.5, 5.5))  # 3.1415926535
```

### `random.randrange(start, stop[, step])` – Integer in Range

```python
import random

# Single argument (0 to stop-1)
print(random.randrange(10))     # 0-9

# Two arguments (start to stop-1)
print(random.randrange(5, 10))  # 5-9

# Three arguments (with step)
print(random.randrange(0, 20, 2))  # Even numbers: 0,2,4,...,18

# Equivalent to random.randint(a, b-1)
```

### `random.randint(a, b)` – Integer in [a, b] (Inclusive)

```python
import random

# Inclusive range
print(random.randint(1, 10))    # 1-10 (including 10)
print(random.randint(100, 200)) # 100-200

# Negative range
print(random.randint(-10, -1))  # -10 to -1

# Same as random.randrange(a, b+1)
```

### `random.getrandbits(k)` – Integer with k random bits

```python
import random

# Generate random integer with k bits
print(random.getrandbits(8))    # 0-255
print(random.getrandbits(16))   # 0-65535
print(random.getrandbits(32))   # 0-4294967295

# Generate random byte
byte = random.getrandbits(8).to_bytes(1, 'big')
print(byte)  # b'\x8f'
```

---

## Integer Random Functions

### `random.randint(a, b)` – Random Integer

```python
import random

# Dice roll
dice = random.randint(1, 6)
print(f"Dice roll: {dice}")

# Multiple dice rolls
rolls = [random.randint(1, 6) for _ in range(10)]
print(f"10 rolls: {rolls}")
```

### `random.randrange()` – More Flexible Integer Range

```python
import random

# Generate even numbers only
even = random.randrange(0, 100, 2)
print(f"Even number: {even}")

# Generate odd numbers only
odd = random.randrange(1, 100, 2)
print(f"Odd number: {odd}")

# Generate multiples of 5
multiple = random.randrange(0, 100, 5)
print(f"Multiple of 5: {multiple}")
```

---

## Sequence Random Functions

### `random.choice(seq)` – Random Element from Sequence

```python
import random

# From list
colors = ['red', 'green', 'blue', 'yellow']
print(random.choice(colors))

# From string
print(random.choice('abcdefg'))

# From tuple
numbers = (1, 2, 3, 4, 5)
print(random.choice(numbers))

# From range
print(random.choice(range(10)))
```

### `random.choices(population, weights=None, k=1)` – Multiple Random Choices

```python
import random

# Pick 5 items with replacement
colors = ['red', 'green', 'blue']
picks = random.choices(colors, k=5)
print(picks)  # ['blue', 'red', 'blue', 'green', 'red']

# Weighted choices
colors = ['red', 'green', 'blue']
weights = [0.5, 0.3, 0.2]  # 50% red, 30% green, 20% blue
picks = random.choices(colors, weights=weights, k=10)
print(picks)

# Count frequencies
from collections import Counter
counts = Counter(picks)
print(counts)
```

### `random.sample(population, k)` – Unique Random Sample

```python
import random

# Pick 3 unique items from list
colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']
sample = random.sample(colors, 3)
print(sample)  # ['blue', 'yellow', 'red']

# Sample from range (lottery numbers)
lottery = random.sample(range(1, 50), 6)
print(f"Lottery numbers: {sorted(lottery)}")

# Sample from string
letters = random.sample('abcdefghijklmnopqrstuvwxyz', 5)
print(f"Random letters: {''.join(letters)}")

# Cannot sample more than population
# random.sample(colors, 10)  # ValueError!
```

### `random.shuffle(x)` – Shuffle List In-Place

```python
import random

# Shuffle a list
cards = list(range(1, 11))  # Cards 1-10
print(f"Original: {cards}")

random.shuffle(cards)
print(f"Shuffled: {cards}")

# Shuffle again
random.shuffle(cards)
print(f"Reshuffled: {cards}")

# Shuffle a list of strings
words = ['apple', 'banana', 'cherry', 'date']
random.shuffle(words)
print(words)
```

### `random.shuffle()` with Custom Random Function

```python
import random

# Shuffle with custom random function
def my_random():
    return 0.5  # Always returns same value (not random)

items = [1, 2, 3, 4, 5]
random.shuffle(items, random=my_random)
print(items)  # Still shuffled but deterministically
```

---

## Distribution Functions

### `random.triangular(low, high, mode)` – Triangular Distribution

```python
import random

# Triangular distribution (low, high, mode)
# Mode is the most likely value
values = [random.triangular(0, 10, 5) for _ in range(1000)]

# Most values cluster around mode (5)
print(f"Average: {sum(values)/len(values):.2f}")
```

### `random.betavariate(alpha, beta)` – Beta Distribution

```python
import random

# Beta distribution (0 to 1)
values = [random.betavariate(2, 5) for _ in range(1000)]

# Used in Bayesian statistics
print(f"Sample: {values[:5]}")
```

### `random.expovariate(lambd)` – Exponential Distribution

```python
import random

# Exponential distribution (lambd = 1/mean)
# Used for modeling time between events
wait_times = [random.expovariate(0.5) for _ in range(10)]
print(f"Wait times: {[f'{t:.2f}' for t in wait_times]}")
```

### `random.gammavariate(alpha, beta)` – Gamma Distribution

```python
import random

# Gamma distribution
values = [random.gammavariate(2, 1) for _ in range(1000)]
print(f"Sample: {values[:5]}")
```

### `random.gauss(mu, sigma)` – Gaussian (Normal) Distribution

```python
import random

# Normal distribution with mean (mu) and standard deviation (sigma)
scores = [random.gauss(70, 10) for _ in range(1000)]

# Most scores cluster around 70
average = sum(scores) / len(scores)
print(f"Average: {average:.2f}")

# Count scores in ranges
below_60 = sum(1 for s in scores if s < 60)
between_60_80 = sum(1 for s in scores if 60 <= s < 80)
above_80 = sum(1 for s in scores if s >= 80)

print(f"Below 60: {below_60}")
print(f"60-80: {between_60_80}")
print(f"Above 80: {above_80}")
```

### `random.normalvariate(mu, sigma)` – Normal Distribution (Thread-safe)

```python
import random

# Thread-safe version of normal distribution
values = [random.normalvariate(100, 15) for _ in range(1000)]
print(f"Average: {sum(values)/len(values):.2f}")
```

### `random.lognormvariate(mu, sigma)` – Log Normal Distribution

```python
import random

# Log normal distribution
values = [random.lognormvariate(0, 1) for _ in range(1000)]
print(f"Sample: {values[:5]}")
```

### `random.vonmisesvariate(mu, kappa)` – Von Mises Distribution

```python
import random

# Von Mises distribution (circular)
angles = [random.vonmisesvariate(0, 2) for _ in range(100)]
print(f"Angles: {[f'{a:.2f}' for a in angles[:5]]}")
```

### `random.paretovariate(alpha)` – Pareto Distribution

```python
import random

# Pareto distribution (80-20 rule)
values = [random.paretovariate(2) for _ in range(1000)]
print(f"Sample: {values[:5]}")
```

### `random.weibullvariate(alpha, beta)` – Weibull Distribution

```python
import random

# Weibull distribution (failure rates)
values = [random.weibullvariate(1, 1.5) for _ in range(1000)]
print(f"Sample: {values[:5]}")
```

---

## Random Seed

The seed initializes the random number generator, making results reproducible.

### `random.seed(a=None)` – Set Random Seed

```python
import random

# Without seed (different each run)
print(random.random())  # Different each time

# With seed (reproducible)
random.seed(42)
print(random.random())  # 0.6394267984578837
print(random.random())  # 0.025010755222666936

random.seed(42)  # Reset to same seed
print(random.random())  # 0.6394267984578837 (same as before)
print(random.random())  # 0.025010755222666936 (same as before)

# Use current time as seed (default)
random.seed()  # Uses system time
```

### Reproducible Examples

```python
import random

# Reproducible random sequence
def reproducible_random(seed=42):
    random.seed(seed)
    return [random.randint(1, 10) for _ in range(5)]

# Same seed produces same results
print(reproducible_random(42))  # [10, 1, 5, 1, 5]
print(reproducible_random(42))  # [10, 1, 5, 1, 5]

# Different seed produces different results
print(reproducible_random(100))  # [8, 6, 9, 7, 2]
```

### Use Cases for Seeding

```python
import random

# 1. Testing - reproducible test cases
random.seed(123)
test_data = [random.randint(1, 100) for _ in range(10)]
print(f"Test data: {test_data}")

# 2. Debugging - reproduce bugs
random.seed(456)
bug_repro = random.sample(range(100), 10)
print(f"Bug repro: {bug_repro}")

# 3. Machine Learning - reproducible results
random.seed(42)
train_indices = random.sample(range(1000), 800)
print(f"Training set size: {len(train_indices)}")
```

---

## Real-World Examples

### Example 1: Dice Roll Simulator

```python
import random
from collections import Counter

class Dice:
    @staticmethod
    def roll(sides=6):
        return random.randint(1, sides)
    
    @staticmethod
    def roll_multiple(count, sides=6):
        return [random.randint(1, sides) for _ in range(count)]
    
    @staticmethod
    def roll_with_advantage(sides=6):
        """Roll two dice, take the higher"""
        roll1 = random.randint(1, sides)
        roll2 = random.randint(1, sides)
        return max(roll1, roll2)
    
    @staticmethod
    def roll_with_disadvantage(sides=6):
        """Roll two dice, take the lower"""
        roll1 = random.randint(1, sides)
        roll2 = random.randint(1, sides)
        return min(roll1, roll2)

# Simulate dice rolls
print("DICE SIMULATOR")
print("=" * 40)

# Single roll
print(f"Single d6: {Dice.roll()}")
print(f"Single d20: {Dice.roll(20)}")

# Multiple rolls
rolls = Dice.roll_multiple(10, 6)
print(f"10 d6 rolls: {rolls}")
print(f"Average: {sum(rolls)/len(rolls):.2f}")

# Advantage vs disadvantage
normal = [Dice.roll(20) for _ in range(1000)]
advantage = [Dice.roll_with_advantage(20) for _ in range(1000)]
disadvantage = [Dice.roll_with_disadvantage(20) for _ in range(1000)]

print(f"\nAverage d20: {sum(normal)/len(normal):.2f}")
print(f"Average with advantage: {sum(advantage)/len(advantage):.2f}")
print(f"Average with disadvantage: {sum(disadvantage)/len(disadvantage):.2f}")

# Distribution analysis
rolls = Dice.roll_multiple(10000, 6)
counter = Counter(rolls)
print(f"\nDistribution of 10,000 d6 rolls:")
for face in range(1, 7):
    print(f"  {face}: {counter[face]} ({counter[face]/100:.1f}%)")
```

### Example 2: Password Generator

```python
import random
import string

class PasswordGenerator:
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    def generate(self, length=12, use_upper=True, use_digits=True, use_symbols=True):
        """Generate random password"""
        pool = self.lowercase
        if use_upper:
            pool += self.uppercase
        if use_digits:
            pool += self.digits
        if use_symbols:
            pool += self.symbols
        
        if not pool:
            return "Error: No character types selected"
        
        # Generate password
        password = []
        for _ in range(length):
            password.append(random.choice(pool))
        
        # Ensure at least one of each selected type
        if use_upper and not any(c in self.uppercase for c in password):
            password[0] = random.choice(self.uppercase)
        if use_digits and not any(c in self.digits for c in password):
            password[1] = random.choice(self.digits)
        if use_symbols and not any(c in self.symbols for c in password):
            password[2] = random.choice(self.symbols)
        
        random.shuffle(password)
        return ''.join(password)
    
    def generate_multiple(self, count=5, **kwargs):
        """Generate multiple passwords"""
        return [self.generate(**kwargs) for _ in range(count)]
    
    def generate_memorable(self, words=3, separator='-', digits=2):
        """Generate memorable password using words"""
        word_list = ['apple', 'banana', 'cherry', 'dragon', 'eagle', 
                     'forest', 'garden', 'harmony', 'island', 'jungle']
        
        selected = random.sample(word_list, words)
        num = random.randint(10**(digits-1), 10**digits - 1)
        
        password = separator.join(selected) + str(num)
        return password

# Usage
pwd_gen = PasswordGenerator()

print("PASSWORD GENERATOR")
print("=" * 40)

# Standard password
print(f"Standard: {pwd_gen.generate(12)}")

# Strong password
print(f"Strong: {pwd_gen.generate(16, use_upper=True, use_digits=True, use_symbols=True)}")

# Multiple passwords
print("\nMultiple passwords:")
for i, pwd in enumerate(pwd_gen.generate_multiple(5, length=10), 1):
    print(f"  {i}. {pwd}")

# Memorable password
print(f"\nMemorable: {pwd_gen.generate_memorable(3, '-', 2)}")
```

### Example 3: Card Deck Simulator

```python
import random

class CardDeck:
    suits = ['♠', '♥', '♣', '♦']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    def __init__(self):
        self.cards = []
        self.reset()
    
    def reset(self):
        """Create a new deck in order"""
        self.cards = [f"{rank}{suit}" for suit in self.suits for rank in self.ranks]
    
    def shuffle(self):
        """Shuffle the deck"""
        random.shuffle(self.cards)
    
    def draw(self, count=1):
        """Draw cards from the top"""
        drawn = []
        for _ in range(count):
            if self.cards:
                drawn.append(self.cards.pop())
        return drawn if count > 1 else drawn[0] if drawn else None
    
    def deal(self, num_players, cards_per_player):
        """Deal cards to players"""
        hands = [[] for _ in range(num_players)]
        for _ in range(cards_per_player):
            for i in range(num_players):
                if self.cards:
                    hands[i].append(self.cards.pop())
        return hands
    
    def remaining(self):
        """Number of cards remaining"""
        return len(self.cards)
    
    def __str__(self):
        return f"Deck({self.remaining()} cards)"

# Usage
print("CARD DECK SIMULATOR")
print("=" * 40)

deck = CardDeck()
print(f"New deck: {deck}")
print(f"First few cards: {deck.cards[:5]}")

# Shuffle
deck.shuffle()
print(f"\nAfter shuffle: {deck}")
print(f"First few cards: {deck.cards[:5]}")

# Draw cards
print(f"\nDraw 5 cards: {deck.draw(5)}")
print(f"Remaining: {deck.remaining()}")

# Deal to players
deck.reset()
deck.shuffle()
hands = deck.deal(4, 5)
print(f"\nDealt 5 cards to 4 players:")
for i, hand in enumerate(hands, 1):
    print(f"  Player {i}: {hand}")
print(f"Remaining in deck: {deck.remaining()}")
```

### Example 4: Random Name Generator

```python
import random

class NameGenerator:
    def __init__(self):
        self.first_names = [
            'Alice', 'Bob', 'Charlie', 'Diana', 'Edward', 'Fiona', 'George', 'Hannah',
            'Ian', 'Julia', 'Kevin', 'Laura', 'Michael', 'Nina', 'Oliver', 'Patricia'
        ]
        
        self.last_names = [
            'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis',
            'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson'
        ]
        
        self.adjectives = [
            'Swift', 'Brave', 'Wise', 'Bold', 'Calm', 'Fierce', 'Gentle', 'Mighty',
            'Noble', 'Quick', 'Silent', 'Strong', 'Valiant', 'Wild', 'Young'
        ]
        
        self.nouns = [
            'Wolf', 'Eagle', 'Hawk', 'Lion', 'Tiger', 'Bear', 'Falcon', 'Raven',
            'Phoenix', 'Dragon', 'Griffin', 'Panther', 'Viper', 'Cobra', 'Shark'
        ]
    
    def random_name(self):
        """Generate random full name"""
        first = random.choice(self.first_names)
        last = random.choice(self.last_names)
        return f"{first} {last}"
    
    def random_username(self, length=8):
        """Generate random username"""
        letters = 'abcdefghijklmnopqrstuvwxyz0123456789'
        return ''.join(random.choice(letters) for _ in range(length))
    
    def random_nickname(self):
        """Generate random nickname (Adjective + Noun)"""
        adj = random.choice(self.adjectives)
        noun = random.choice(self.nouns)
        return f"{adj}{noun}"
    
    def random_email(self, domain='example.com'):
        """Generate random email address"""
        username = self.random_username(random.randint(6, 10))
        return f"{username}@{domain}"
    
    def generate_multiple(self, count=10):
        """Generate multiple names"""
        return [self.random_name() for _ in range(count)]

# Usage
name_gen = NameGenerator()

print("NAME GENERATOR")
print("=" * 40)

print(f"Random name: {name_gen.random_name()}")
print(f"Random username: {name_gen.random_username()}")
print(f"Random nickname: {name_gen.random_nickname()}")
print(f"Random email: {name_gen.random_email()}")

print("\n10 Random names:")
for i, name in enumerate(name_gen.generate_multiple(10), 1):
    print(f"  {i:2}. {name}")
```

### Example 5: Lottery Number Generator

```python
import random

class LotteryGenerator:
    @staticmethod
    def powerball():
        """Generate Powerball numbers (5 white + 1 red)"""
        white = sorted(random.sample(range(1, 70), 5))
        red = random.randint(1, 26)
        return {'white': white, 'red': red}
    
    @staticmethod
    def mega_millions():
        """Generate Mega Millions numbers (5 white + 1 gold)"""
        white = sorted(random.sample(range(1, 71), 5))
        gold = random.randint(1, 25)
        return {'white': white, 'gold': gold}
    
    @staticmethod
    def lotto(max_num=49, picks=6):
        """Generate standard lotto numbers"""
        return sorted(random.sample(range(1, max_num + 1), picks))
    
    @staticmethod
    def generate_tickets(count=5, lottery_type='lotto'):
        """Generate multiple tickets"""
        tickets = []
        for _ in range(count):
            if lottery_type == 'powerball':
                tickets.append(LotteryGenerator.powerball())
            elif lottery_type == 'megamillions':
                tickets.append(LotteryGenerator.mega_millions())
            else:
                tickets.append(LotteryGenerator.lotto())
        return tickets
    
    @staticmethod
    def quick_pick(count=6):
        """Generate quick pick numbers"""
        return sorted(random.sample(range(1, 50), count))

# Usage
print("LOTTERY NUMBER GENERATOR")
print("=" * 40)

# Powerball
pb = LotteryGenerator.powerball()
print(f"Powerball: White: {pb['white']}, Red: {pb['red']}")

# Mega Millions
mm = LotteryGenerator.mega_millions()
print(f"Mega Millions: White: {mm['white']}, Gold: {mm['gold']}")

# Standard Lotto
print(f"Standard Lotto: {LotteryGenerator.lotto()}")

# Multiple tickets
print("\n5 Quick Pick tickets:")
for i, ticket in enumerate(LotteryGenerator.generate_tickets(5), 1):
    print(f"  Ticket {i}: {ticket}")

# Statistics of random distribution
tickets = [LotteryGenerator.lotto() for _ in range(10000)]
all_numbers = [num for ticket in tickets for num in ticket]
from collections import Counter
freq = Counter(all_numbers)
most_common = freq.most_common(6)
print(f"\nMost common numbers in 10,000 tickets: {[num for num, _ in most_common]}")
```

### Example 6: Random Walk Simulation

```python
import random
import math

class RandomWalk:
    def __init__(self, steps=1000):
        self.steps = steps
        self.x = 0
        self.y = 0
        self.history = [(0, 0)]
    
    def step_2d(self):
        """Random step in 2D (up, down, left, right)"""
        direction = random.choice(['N', 'S', 'E', 'W'])
        if direction == 'N':
            self.y += 1
        elif direction == 'S':
            self.y -= 1
        elif direction == 'E':
            self.x += 1
        else:
            self.x -= 1
        self.history.append((self.x, self.y))
    
    def step_2d_diagonal(self):
        """Random step including diagonals"""
        dx = random.randint(-1, 1)
        dy = random.randint(-1, 1)
        self.x += dx
        self.y += dy
        self.history.append((self.x, self.y))
    
    def step_1d(self):
        """Random step in 1D (left or right)"""
        self.x += random.choice([-1, 1])
        self.history.append((self.x, 0))
    
    def simulate(self, dimension='2d'):
        """Run simulation"""
        self.reset()
        for _ in range(self.steps):
            if dimension == '1d':
                self.step_1d()
            elif dimension == '2d_diagonal':
                self.step_2d_diagonal()
            else:
                self.step_2d()
    
    def reset(self):
        """Reset walker to origin"""
        self.x = 0
        self.y = 0
        self.history = [(0, 0)]
    
    def final_distance(self):
        """Distance from origin"""
        return math.sqrt(self.x**2 + self.y**2)
    
    def max_distance(self):
        """Maximum distance from origin"""
        distances = [math.sqrt(x**2 + y**2) for x, y in self.history]
        return max(distances)

# Simulation
print("RANDOM WALK SIMULATION")
print("=" * 40)

# 1D Random Walk
walk1d = RandomWalk(1000)
walk1d.simulate('1d')
print(f"1D Walk - Final position: {walk1d.x}, Distance: {walk1d.final_distance():.2f}")

# 2D Random Walk
walk2d = RandomWalk(1000)
walk2d.simulate('2d')
print(f"2D Walk - Final position: ({walk2d.x}, {walk2d.y})")
print(f"  Distance: {walk2d.final_distance():.2f}")
print(f"  Max distance: {walk2d.max_distance():.2f}")

# 2D with diagonals
walk2d_diag = RandomWalk(1000)
walk2d_diag.simulate('2d_diagonal')
print(f"2D Diagonal Walk - Final position: ({walk2d_diag.x}, {walk2d_diag.y})")
print(f"  Distance: {walk2d_diag.final_distance():.2f}")

# Multiple runs average
runs = 100
avg_distance_2d = 0
for _ in range(runs):
    walk = RandomWalk(1000)
    walk.simulate('2d')
    avg_distance_2d += walk.final_distance()
avg_distance_2d /= runs

print(f"\nAverage distance after 1000 steps ({runs} runs): {avg_distance_2d:.2f}")
print(f"Theoretical expected distance: ~{math.sqrt(1000):.2f}")
```

---

## Practice Exercises

### Beginner Level

1. **Dice Roller**
   ```python
   # Simulate rolling a six-sided die 100 times
   # Print the frequency of each number
   ```

2. **Random Name Picker**
   ```python
   # Randomly select a name from a list of students
   ```

3. **Coin Toss**
   ```python
   # Simulate 100 coin tosses
   # Print number of heads and tails
   ```

### Intermediate Level

4. **Password Generator**
   ```python
   # Generate random password with specified length
   # Include uppercase, lowercase, digits, symbols
   ```

5. **Lottery Number Generator**
   ```python
   # Generate 6 unique random numbers between 1-49
   ```

6. **Card Shuffler**
   ```python
   # Create a deck of 52 cards and shuffle
   # Deal 5 cards to 4 players
   ```

### Advanced Level

7. **Random Walk Simulation**
   ```python
   # Simulate 2D random walk
   # Calculate average distance after N steps
   ```

8. **Weighted Random Selection**
   ```python
   # Select items with different probabilities
   # Example: 50% red, 30% green, 20% blue
   ```

9. **Monte Carlo Simulation**
   ```python
   # Estimate π using random points in a circle
   ```

---

## Quick Reference Card

```python
import random

# Basic floats
random.random()              # 0.0 to 1.0
random.uniform(a, b)         # a to b
random.triangular(a, b, m)   # Triangular distribution

# Integers
random.randint(a, b)         # a to b (inclusive)
random.randrange(stop)       # 0 to stop-1
random.randrange(start, stop)# start to stop-1
random.randrange(s, t, step) # With step
random.getrandbits(k)        # k random bits

# Sequences
random.choice(seq)           # Single element
random.choices(seq, k=n)     # Multiple (with replacement)
random.sample(seq, k)        # Unique sample
random.shuffle(seq)          # Shuffle in-place

# Distributions
random.gauss(mu, sigma)      # Normal
random.normalvariate(mu, s)  # Normal (thread-safe)
random.expovariate(lambd)    # Exponential
random.gammavariate(a, b)    # Gamma
random.betavariate(a, b)     # Beta
random.paretovariate(a)      # Pareto
random.weibullvariate(a, b)  # Weibull
random.vonmisesvariate(m, k) # Von Mises

# Seed (for reproducibility)
random.seed(n)               # Set seed
random.seed()                # Use system time
```

---

## Next Step

- Move to [04_datetime.md](04_datetime.md) to learn about date and time handling.

---

*Master the random module for simulations, games, and sampling! 🐍✨*