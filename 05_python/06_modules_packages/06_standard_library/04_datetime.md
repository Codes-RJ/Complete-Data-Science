# 📘 DATETIME MODULE – COMPLETE GUIDE

## 📌 Table of Contents
1. [What is the Datetime Module?](#what-is-the-datetime-module)
2. [Date Class](#date-class)
3. [Time Class](#time-class)
4. [Datetime Class](#datetime-class)
5. [Timedelta Class](#timedelta-class)
6. [Formatting and Parsing](#formatting-and-parsing)
7. [Timezone Handling](#timezone-handling)
8. [Real-World Examples](#real-world-examples)
9. [Practice Exercises](#practice-exercises)

---

## What is the Datetime Module?

The `datetime` module provides classes for manipulating dates and times. It's essential for handling temporal data in Python.

```python
from datetime import datetime, date, time, timedelta

# Current date and time
now = datetime.now()
print(now)  # 2024-01-15 10:30:45.123456

# Current date only
today = date.today()
print(today)  # 2024-01-15

# Create specific date
birthday = date(1990, 5, 15)
print(birthday)  # 1990-05-15
```

**Key Classes:**
- `date` – Year, month, day
- `time` – Hour, minute, second, microsecond
- `datetime` – Combined date and time
- `timedelta` – Duration between dates/times
- `tzinfo` – Timezone information

---

## Date Class

The `date` class represents a date (year, month, day).

### Creating Date Objects

```python
from datetime import date

# Current date
today = date.today()
print(today)  # 2024-01-15

# Specific date
d = date(2024, 12, 25)
print(d)  # 2024-12-25

# From timestamp
timestamp = 1705315200
d = date.fromtimestamp(timestamp)
print(d)  # 2024-01-15

# From ISO format
d = date.fromisoformat('2024-12-25')
print(d)  # 2024-12-25
```

### Date Attributes and Methods

```python
from datetime import date

d = date(2024, 12, 25)

# Attributes
print(d.year)   # 2024
print(d.month)  # 12
print(d.day)    # 25

# Day of week (Monday=0, Sunday=6)
print(d.weekday())     # 2 (Wednesday)
print(d.isoweekday())  # 3 (Wednesday, Monday=1)

# ISO format
print(d.isoformat())    # 2024-12-25

# Replace parts
d2 = d.replace(year=2025)
print(d2)  # 2025-12-25

# Timetable
print(d.timetuple())    # struct_time
print(d.toordinal())    # days since 0001-01-01
```

### Date Comparisons and Operations

```python
from datetime import date

d1 = date(2024, 1, 1)
d2 = date(2024, 12, 31)

# Comparison
print(d1 < d2)   # True
print(d1 == d2)  # False

# Difference (returns timedelta)
diff = d2 - d1
print(diff.days)  # 365

# Adding days
from datetime import timedelta
d3 = d1 + timedelta(days=30)
print(d3)  # 2024-01-31
```

---

## Time Class

The `time` class represents a time (hour, minute, second, microsecond).

### Creating Time Objects

```python
from datetime import time

# Specific time
t = time(10, 30, 45, 500000)
print(t)  # 10:30:45.500000

# Without microseconds
t = time(14, 30, 0)
print(t)  # 14:30:00

# Only hour and minute
t = time(8, 15)
print(t)  # 08:15:00

# From ISO format
t = time.fromisoformat('10:30:45')
print(t)  # 10:30:45
```

### Time Attributes and Methods

```python
from datetime import time

t = time(10, 30, 45, 500000)

# Attributes
print(t.hour)        # 10
print(t.minute)      # 30
print(t.second)      # 45
print(t.microsecond) # 500000

# ISO format
print(t.isoformat())  # 10:30:45.500000

# Replace parts
t2 = t.replace(hour=14, minute=0)
print(t2)  # 14:00:45.500000
```

---

## Datetime Class

The `datetime` class combines date and time.

### Creating Datetime Objects

```python
from datetime import datetime

# Current date and time
now = datetime.now()
print(now)  # 2024-01-15 10:30:45.123456

# Current UTC time
utc_now = datetime.utcnow()
print(utc_now)  # 2024-01-15 10:30:45.123456

# Specific datetime
dt = datetime(2024, 12, 25, 10, 30, 45)
print(dt)  # 2024-12-25 10:30:45

# From timestamp
timestamp = 1705315200
dt = datetime.fromtimestamp(timestamp)
print(dt)  # 2024-01-15 10:30:00

# From ISO format
dt = datetime.fromisoformat('2024-12-25T10:30:45')
print(dt)  # 2024-12-25 10:30:45

# From string (using strptime)
dt = datetime.strptime('2024-12-25', '%Y-%m-%d')
print(dt)  # 2024-12-25 00:00:00
```

### Datetime Attributes and Methods

```python
from datetime import datetime

dt = datetime(2024, 12, 25, 10, 30, 45, 500000)

# Date and time components
print(dt.year)        # 2024
print(dt.month)       # 12
print(dt.day)         # 25
print(dt.hour)        # 10
print(dt.minute)      # 30
print(dt.second)      # 45
print(dt.microsecond) # 500000

# Date and time parts
print(dt.date())  # 2024-12-25
print(dt.time())  # 10:30:45.500000

# Day of week
print(dt.weekday())     # 2 (Wednesday)
print(dt.isoweekday())  # 3 (Wednesday)

# Timestamp
print(dt.timestamp())  # 1705315200.5

# ISO format
print(dt.isoformat())  # 2024-12-25T10:30:45.500000

# Replace parts
dt2 = dt.replace(year=2025, hour=14)
print(dt2)  # 2025-12-25 14:30:45.500000
```

---

## Timedelta Class

`timedelta` represents a duration, the difference between two dates or times.

### Creating Timedelta Objects

```python
from datetime import timedelta

# Different ways to create timedelta
td1 = timedelta(days=5)
td2 = timedelta(hours=10)
td3 = timedelta(minutes=30)
td4 = timedelta(seconds=45)
td5 = timedelta(weeks=2)

# Combined
td = timedelta(days=5, hours=10, minutes=30, seconds=45)
print(td)  # 5 days, 10:30:45

# From string (not directly, parse manually)
```

### Timedelta Attributes

```python
from datetime import timedelta

td = timedelta(days=5, hours=10, minutes=30, seconds=45)

print(td.days)          # 5
print(td.seconds)       # 37845 (10*3600 + 30*60 + 45)
print(td.microseconds)  # 0
print(td.total_seconds())  # 5*86400 + 37845 = 469845.0
```

### Date Arithmetic with Timedelta

```python
from datetime import datetime, timedelta

now = datetime.now()

# Future dates
tomorrow = now + timedelta(days=1)
next_week = now + timedelta(weeks=1)
next_hour = now + timedelta(hours=1)
next_minute = now + timedelta(minutes=1)

print(f"Tomorrow: {tomorrow.date()}")
print(f"Next week: {next_week.date()}")
print(f"Next hour: {next_hour.time()}")

# Past dates
yesterday = now - timedelta(days=1)
last_week = now - timedelta(weeks=1)
last_hour = now - timedelta(hours=1)

# Difference between dates
date1 = datetime(2024, 1, 1)
date2 = datetime(2024, 12, 31)
diff = date2 - date1
print(f"Days between: {diff.days}")  # 365
```

---

## Formatting and Parsing

### `strftime()` – Formatting (datetime to string)

```python
from datetime import datetime

now = datetime.now()

# Common formats
print(now.strftime("%Y-%m-%d"))           # 2024-01-15
print(now.strftime("%d/%m/%Y"))           # 15/01/2024
print(now.strftime("%B %d, %Y"))          # January 15, 2024
print(now.strftime("%A, %B %d, %Y"))      # Monday, January 15, 2024
print(now.strftime("%I:%M %p"))           # 10:30 AM
print(now.strftime("%H:%M:%S"))           # 10:30:45
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # 2024-01-15 10:30:45

# Full format
print(now.strftime("%c"))  # Mon Jan 15 10:30:45 2024
print(now.strftime("%x"))  # 01/15/24
print(now.strftime("%X"))  # 10:30:45
```

### strftime Format Codes

| Code | Meaning | Example |
|------|---------|---------|
| `%Y` | Year (4 digits) | 2024 |
| `%y` | Year (2 digits) | 24 |
| `%m` | Month (01-12) | 01 |
| `%d` | Day (01-31) | 15 |
| `%H` | Hour (00-23) | 14 |
| `%I` | Hour (01-12) | 02 |
| `%M` | Minute (00-59) | 30 |
| `%S` | Second (00-59) | 45 |
| `%p` | AM/PM | AM |
| `%A` | Full weekday | Monday |
| `%a` | Abbreviated weekday | Mon |
| `%B` | Full month | January |
| `%b` | Abbreviated month | Jan |
| `%j` | Day of year (001-366) | 015 |
| `%U` | Week number (00-53) | 02 |
| `%w` | Weekday (0-6, Sunday=0) | 1 |
| `%c` | Locale date/time | Mon Jan 15 10:30:45 2024 |
| `%x` | Locale date | 01/15/24 |
| `%X` | Locale time | 10:30:45 |

### `strptime()` – Parsing (string to datetime)

```python
from datetime import datetime

# Parse common formats
date_str = "2024-12-25"
dt = datetime.strptime(date_str, "%Y-%m-%d")
print(dt)  # 2024-12-25 00:00:00

date_str = "25/12/2024"
dt = datetime.strptime(date_str, "%d/%m/%Y")
print(dt)  # 2024-12-25 00:00:00

date_str = "January 15, 2024"
dt = datetime.strptime(date_str, "%B %d, %Y")
print(dt)  # 2024-01-15 00:00:00

date_str = "Mon Jan 15 10:30:45 2024"
dt = datetime.strptime(date_str, "%a %b %d %H:%M:%S %Y")
print(dt)  # 2024-01-15 10:30:45

# Parse with time
datetime_str = "2024-12-25 14:30:45"
dt = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
print(dt)  # 2024-12-25 14:30:45
```

---

## Timezone Handling

### Naive vs Aware Datetime

```python
from datetime import datetime, timezone, timedelta

# Naive datetime (no timezone)
naive = datetime.now()
print(naive)  # 2024-01-15 10:30:45.123456
print(naive.tzinfo)  # None

# Aware datetime (with timezone)
aware = datetime.now(timezone.utc)
print(aware)  # 2024-01-15 10:30:45.123456+00:00
print(aware.tzinfo)  # UTC
```

### Working with Timezones

```python
from datetime import datetime, timezone, timedelta

# UTC time
utc_now = datetime.now(timezone.utc)
print(f"UTC: {utc_now}")

# Create timezone offset
tz_eastern = timezone(timedelta(hours=-5))
eastern_now = datetime.now(tz_eastern)
print(f"Eastern: {eastern_now}")

# Convert between timezones
utc_time = datetime(2024, 12, 25, 10, 0, 0, tzinfo=timezone.utc)
eastern_time = utc_time.astimezone(tz_eastern)
print(f"UTC 10:00 = Eastern {eastern_time.strftime('%H:%M')}")  # 05:00
```

### Using `pytz` (Third-party, more comprehensive)

```python
# Note: pytz needs to be installed: pip install pytz
# import pytz
# tz = pytz.timezone('America/New_York')
# local_time = datetime.now(tz)
```

---

## Real-World Examples

### Example 1: Age Calculator

```python
from datetime import date

class AgeCalculator:
    @staticmethod
    def calculate(birth_date):
        """Calculate age from birth date"""
        today = date.today()
        age = today.year - birth_date.year
        
        # Adjust if birthday hasn't occurred yet this year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        
        return age
    
    @staticmethod
    def days_until_birthday(birth_date):
        """Calculate days until next birthday"""
        today = date.today()
        next_birthday = date(today.year, birth_date.month, birth_date.day)
        
        if next_birthday < today:
            next_birthday = date(today.year + 1, birth_date.month, birth_date.day)
        
        return (next_birthday - today).days
    
    @staticmethod
    def birth_details(birth_date):
        """Get detailed birth information"""
        today = date.today()
        age = AgeCalculator.calculate(birth_date)
        days_to_birthday = AgeCalculator.days_until_birthday(birth_date)
        
        # Calculate total days lived
        days_lived = (today - birth_date).days
        
        return {
            'age': age,
            'days_lived': days_lived,
            'days_to_next_birthday': days_to_birthday,
            'birthday_weekday': birth_date.strftime("%A"),
            'born_in_leap_year': (birth_date.year % 4 == 0 and 
                                   birth_date.year % 100 != 0) or 
                                   birth_date.year % 400 == 0
        }

# Usage
birth = date(1990, 5, 15)
details = AgeCalculator.birth_details(birth)

print("AGE CALCULATOR")
print("=" * 40)
print(f"Birth date: {birth.strftime('%B %d, %Y')}")
print(f"Age: {details['age']} years")
print(f"Days lived: {details['days_lived']:,} days")
print(f"Days to next birthday: {details['days_to_next_birthday']}")
print(f"Born on: {details['birthday_weekday']}")
print(f"Born in leap year: {details['born_in_leap_year']}")
```

### Example 2: Event Countdown Timer

```python
from datetime import datetime, timedelta

class CountdownTimer:
    def __init__(self, event_date, event_name):
        self.event_date = event_date
        self.event_name = event_name
    
    def days_remaining(self):
        """Days until event"""
        now = datetime.now()
        remaining = self.event_date - now
        return remaining.days
    
    def full_countdown(self):
        """Complete countdown (days, hours, minutes, seconds)"""
        now = datetime.now()
        remaining = self.event_date - now
        
        days = remaining.days
        hours = remaining.seconds // 3600
        minutes = (remaining.seconds % 3600) // 60
        seconds = remaining.seconds % 60
        
        return {
            'days': days,
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds,
            'total_seconds': remaining.total_seconds()
        }
    
    def display(self):
        """Display countdown"""
        countdown = self.full_countdown()
        
        print(f"Countdown to {self.event_name}")
        print("=" * 40)
        
        if countdown['days'] < 0:
            print("Event has passed!")
        elif countdown['days'] == 0 and countdown['hours'] == 0 and countdown['minutes'] == 0:
            print("Event is happening NOW!")
        else:
            print(f"  {countdown['days']} days")
            print(f"  {countdown['hours']} hours")
            print(f"  {countdown['minutes']} minutes")
            print(f"  {countdown['seconds']} seconds")

# Usage
new_year = datetime(2025, 1, 1, 0, 0, 0)
countdown = CountdownTimer(new_year, "New Year 2025")
countdown.display()

# Countdown to specific datetime
christmas = datetime(2024, 12, 25, 0, 0, 0)
countdown2 = CountdownTimer(christmas, "Christmas")
countdown2.display()
```

### Example 3: Date Range Generator

```python
from datetime import datetime, timedelta

class DateRange:
    @staticmethod
    def date_range(start_date, end_date):
        """Generate dates between start and end (inclusive)"""
        current = start_date
        while current <= end_date:
            yield current
            current += timedelta(days=1)
    
    @staticmethod
    def business_days(start_date, end_date):
        """Generate business days only (Monday-Friday)"""
        for date in DateRange.date_range(start_date, end_date):
            if date.weekday() < 5:  # Monday=0, Friday=4
                yield date
    
    @staticmethod
    def weekends(start_date, end_date):
        """Generate weekends only"""
        for date in DateRange.date_range(start_date, end_date):
            if date.weekday() >= 5:  # Saturday=5, Sunday=6
                yield date
    
    @staticmethod
    def months_between(start_date, end_date):
        """Generate months between dates"""
        current = start_date.replace(day=1)
        end = end_date.replace(day=1)
        
        while current <= end:
            yield current
            # Move to next month
            if current.month == 12:
                current = current.replace(year=current.year + 1, month=1)
            else:
                current = current.replace(month=current.month + 1)

# Usage
start = datetime(2024, 1, 1)
end = datetime(2024, 1, 15)

print("DATE RANGE GENERATOR")
print("=" * 40)

print(f"Dates from {start.date()} to {end.date()}:")
for d in DateRange.date_range(start, end):
    print(f"  {d.strftime('%a, %b %d')}")

print(f"\nBusiness days:")
for d in DateRange.business_days(start, end):
    print(f"  {d.strftime('%a, %b %d')}")

print(f"\nWeekends:")
for d in DateRange.weekends(start, end):
    print(f"  {d.strftime('%a, %b %d')}")

# Months between
start = datetime(2024, 1, 15)
end = datetime(2024, 6, 20)
print(f"\nMonths between {start.date()} and {end.date()}:")
for m in DateRange.months_between(start, end):
    print(f"  {m.strftime('%B %Y')}")
```

### Example 4: Time Tracker

```python
from datetime import datetime, timedelta

class TimeTracker:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.sessions = []
    
    def start(self):
        """Start tracking time"""
        self.start_time = datetime.now()
        print(f"Started at {self.start_time.strftime('%H:%M:%S')}")
    
    def stop(self):
        """Stop tracking time"""
        if self.start_time is None:
            print("No session started")
            return None
        
        self.end_time = datetime.now()
        duration = self.end_time - self.start_time
        
        self.sessions.append({
            'start': self.start_time,
            'end': self.end_time,
            'duration': duration
        })
        
        print(f"Stopped at {self.end_time.strftime('%H:%M:%S')}")
        print(f"Duration: {duration}")
        
        self.start_time = None
        return duration
    
    def total_time(self):
        """Calculate total tracked time"""
        total = timedelta()
        for session in self.sessions:
            total += session['duration']
        return total
    
    def average_session(self):
        """Calculate average session duration"""
        if not self.sessions:
            return timedelta()
        return self.total_time() / len(self.sessions)
    
    def report(self):
        """Generate time tracking report"""
        print("\nTIME TRACKING REPORT")
        print("=" * 40)
        
        for i, session in enumerate(self.sessions, 1):
            print(f"\nSession {i}:")
            print(f"  Start: {session['start'].strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"  End:   {session['end'].strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"  Duration: {session['duration']}")
        
        print(f"\nTotal sessions: {len(self.sessions)}")
        print(f"Total time: {self.total_time()}")
        print(f"Average session: {self.average_session()}")

# Usage
tracker = TimeTracker()

# Simulate work sessions
tracker.start()
# ... do work (simulated with sleep)
import time
time.sleep(2)
tracker.stop()

tracker.start()
time.sleep(3)
tracker.stop()

tracker.start()
time.sleep(1)
tracker.stop()

tracker.report()
```

### Example 5: Birthday Reminder System

```python
from datetime import date, datetime, timedelta

class BirthdayReminder:
    def __init__(self):
        self.birthdays = {}
    
    def add_birthday(self, name, birth_date):
        """Add a birthday to the system"""
        self.birthdays[name] = birth_date
    
    def get_next_birthday(self, name):
        """Get next birthday date for a person"""
        if name not in self.birthdays:
            return None
        
        birth_date = self.birthdays[name]
        today = date.today()
        
        next_birthday = date(today.year, birth_date.month, birth_date.day)
        if next_birthday < today:
            next_birthday = date(today.year + 1, birth_date.month, birth_date.day)
        
        return next_birthday
    
    def days_until_birthday(self, name):
        """Days until next birthday"""
        next_bday = self.get_next_birthday(name)
        if next_bday is None:
            return None
        return (next_bday - date.today()).days
    
    def upcoming_birthdays(self, days=7):
        """Get birthdays in the next N days"""
        today = date.today()
        upcoming = []
        
        for name, birth_date in self.birthdays.items():
            next_bday = self.get_next_birthday(name)
            days_until = (next_bday - today).days
            
            if 0 <= days_until <= days:
                upcoming.append({
                    'name': name,
                    'date': next_bday,
                    'days': days_until,
                    'age': next_bday.year - birth_date.year
                })
        
        return sorted(upcoming, key=lambda x: x['days'])
    
    def display_upcoming(self, days=30):
        """Display upcoming birthdays"""
        upcoming = self.upcoming_birthdays(days)
        
        if not upcoming:
            print(f"No birthdays in the next {days} days")
            return
        
        print(f"\nUPCOMING BIRTHDAYS (next {days} days)")
        print("=" * 40)
        
        for bday in upcoming:
            if bday['days'] == 0:
                when = "TODAY!"
            elif bday['days'] == 1:
                when = "Tomorrow"
            else:
                when = f"In {bday['days']} days"
            
            print(f"  {bday['name']}: {when} (turning {bday['age']})")

# Usage
reminder = BirthdayReminder()

# Add birthdays
reminder.add_birthday("Alice", date(1990, 5, 15))
reminder.add_birthday("Bob", date(1985, 12, 25))
reminder.add_birthday("Charlie", date(1995, 1, 20))
reminder.add_birthday("Diana", date(1988, 3, 10))
reminder.add_birthday("Eve", date(1992, 7, 8))

# Check upcoming birthdays
reminder.display_upcoming(30)

# Specific person
name = "Alice"
days = reminder.days_until_birthday(name)
print(f"\n{name}'s birthday is in {days} days")
```

### Example 6: Log File Parser

```python
from datetime import datetime
import re

class LogParser:
    @staticmethod
    def parse_timestamp(log_line, format="%Y-%m-%d %H:%M:%S"):
        """Extract timestamp from log line"""
        # Try to find datetime pattern
        pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
        match = re.search(pattern, log_line)
        
        if match:
            return datetime.strptime(match.group(), format)
        return None
    
    @staticmethod
    def filter_by_date(logs, start_date, end_date):
        """Filter logs between two dates"""
        filtered = []
        for log in logs:
            timestamp = LogParser.parse_timestamp(log)
            if timestamp and start_date <= timestamp <= end_date:
                filtered.append(log)
        return filtered
    
    @staticmethod
    def group_by_hour(logs):
        """Group logs by hour"""
        groups = {}
        for log in logs:
            timestamp = LogParser.parse_timestamp(log)
            if timestamp:
                hour = timestamp.replace(minute=0, second=0, microsecond=0)
                groups.setdefault(hour, []).append(log)
        return groups
    
    @staticmethod
    def last_n_hours(logs, hours=24):
        """Get logs from last N hours"""
        now = datetime.now()
        cutoff = now - timedelta(hours=hours)
        
        return [log for log in logs if LogParser.parse_timestamp(log) and 
                LogParser.parse_timestamp(log) >= cutoff]

# Sample log data
log_entries = [
    "2024-01-15 08:30:15 [INFO] Server started",
    "2024-01-15 09:15:22 [INFO] User login: alice",
    "2024-01-15 10:00:05 [ERROR] Database connection failed",
    "2024-01-15 10:30:45 [WARNING] High memory usage",
    "2024-01-15 11:20:33 [INFO] User logout: alice",
    "2024-01-15 14:45:12 [INFO] Backup completed",
    "2024-01-15 15:10:08 [ERROR] File not found",
]

print("LOG PARSER")
print("=" * 40)

# Parse timestamps
print("Log entries with timestamps:")
for log in log_entries:
    ts = LogParser.parse_timestamp(log)
    if ts:
        print(f"  {ts.strftime('%H:%M:%S')} - {log[20:]}")

# Filter by date range
start = datetime(2024, 1, 15, 9, 0, 0)
end = datetime(2024, 1, 15, 12, 0, 0)
filtered = LogParser.filter_by_date(log_entries, start, end)

print(f"\nLogs between {start.strftime('%H:%M')} and {end.strftime('%H:%M')}:")
for log in filtered:
    print(f"  {log}")

# Group by hour
grouped = LogParser.group_by_hour(log_entries)
print("\nLogs grouped by hour:")
for hour, logs in sorted(grouped.items()):
    print(f"  {hour.strftime('%Y-%m-%d %H:00')}: {len(logs)} logs")
```

---

## Practice Exercises

### Beginner Level

1. **Current Date and Time**
   ```python
   # Print current date, time, and datetime
   ```

2. **Date Difference**
   ```python
   # Calculate days between two dates
   ```

3. **Birthday Calculator**
   ```python
   # Calculate age from birth date
   ```

### Intermediate Level

4. **Countdown Timer**
   ```python
   # Calculate days until next Christmas
   ```

5. **Date Formatter**
   ```python
   # Convert date string from one format to another
   ```

6. **Business Day Calculator**
   ```python
   # Calculate number of business days between two dates
   ```

### Advanced Level

7. **Recurring Event Scheduler**
   ```python
   # Generate dates for recurring events (weekly, monthly)
   ```

8. **Time Zone Converter**
   ```python
   # Convert datetime between different time zones
   ```

9. **Working Hours Calculator**
   ```python
   # Calculate total working hours excluding weekends
   ```

---

## Quick Reference Card

```python
from datetime import date, time, datetime, timedelta, timezone

# Current
date.today()                    # Current date
datetime.now()                  # Current datetime
datetime.utcnow()               # Current UTC time

# Create
date(year, month, day)          # Date object
time(hour, minute, second)      # Time object
datetime(year, month, day, ...) # Datetime object
timedelta(days=1, hours=2)      # Duration

# Access
.year, .month, .day             # Date components
.hour, .minute, .second         # Time components
.weekday()                      # Monday=0, Sunday=6
.isoweekday()                   # Monday=1, Sunday=7

# Operations
date1 - date2                   # Difference (timedelta)
datetime + timedelta            # Add duration
datetime - timedelta            # Subtract duration

# Format (datetime to string)
.strftime("%Y-%m-%d %H:%M:%S")  # Format

# Parse (string to datetime)
datetime.strptime(str, format)  # Parse string

# Timezone
datetime.now(timezone.utc)      # UTC datetime
.astimezone(tz)                 # Convert timezone
```

---

## Next Step

- Move to [05_os.md](05_os.md) to learn about operating system interface.

---

*Master the datetime module for all your date and time needs! 🐍✨*