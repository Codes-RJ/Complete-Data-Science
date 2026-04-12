# 📘 STATISTICS MODULE – COMPLETE GUIDE

## 📌 Table of Contents
1. [What is the Statistics Module?](#what-is-the-statistics-module)
2. [Measures of Central Tendency](#measures-of-central-tendency)
3. [Measures of Spread](#measures-of-spread)
4. [Measures of Position](#measures-of-position)
5. [Real-World Examples](#real-world-examples)
6. [Practice Exercises](#practice-exercises)

---

## What is the Statistics Module?

The `statistics` module provides functions for mathematical statistics of numeric data. It's part of Python's standard library.

```python
import statistics

data = [10, 20, 30, 40, 50]

# Mean (average)
print(statistics.mean(data))        # 30

# Median (middle value)
print(statistics.median(data))      # 30

# Mode (most frequent)
print(statistics.mode([1, 1, 2, 3]))  # 1

# Standard deviation
print(statistics.stdev(data))       # 15.811388300841896
```

**Key Characteristics:**
- ✅ Works with integers, floats, and Decimals
- ✅ Handles edge cases (empty data, single value)
- ✅ Suitable for real-world data analysis
- ✅ Part of standard library (no installation needed)

---

## Measures of Central Tendency

Central tendency measures describe the center of a data distribution.

### `mean(data)` – Arithmetic Mean (Average)

```python
import statistics

# Basic mean
data = [10, 20, 30, 40, 50]
print(statistics.mean(data))  # 30

# With float data
data = [1.5, 2.5, 3.5, 4.5]
print(statistics.mean(data))  # 3.0

# With mixed numeric types
data = [1, 2.5, 3, 4.5]
print(statistics.mean(data))  # 2.75

# Edge cases
try:
    statistics.mean([])  # StatisticsError
except statistics.StatisticsError as e:
    print(e)  # mean requires at least one data point
```

### `fmean(data)` – Fast Floating Point Mean (Python 3.8+)

```python
import statistics

# Faster than mean() for float data
data = [10, 20, 30, 40, 50]
print(statistics.fmean(data))  # 30.0

# Works with integers too
print(statistics.fmean([1, 2, 3, 4, 5]))  # 3.0
```

### `geometric_mean(data)` – Geometric Mean (Python 3.8+)

```python
import statistics

# Geometric mean = (x₁ × x₂ × ... × xₙ)^(1/n)
data = [2, 8, 4]
print(statistics.geometric_mean(data))  # 4.0 (2×8×4=64, 64^(1/3)=4)

# Growth rates example
growth_rates = [1.1, 1.2, 0.9, 1.15]
avg_growth = statistics.geometric_mean(growth_rates)
print(f"Average growth factor: {avg_growth:.3f}")  # ~1.085
```

### `harmonic_mean(data)` – Harmonic Mean

```python
import statistics

# Harmonic mean = n / (1/x₁ + 1/x₂ + ... + 1/xₙ)
data = [2, 4, 6]
print(statistics.harmonic_mean(data))  # 3.2727...

# Used for rates and ratios
speeds = [60, 40, 50]  # km/h over same distance
avg_speed = statistics.harmonic_mean(speeds)
print(f"Average speed: {avg_speed:.1f} km/h")  # 48.0
```

### `median(data)` – Median (Middle Value)

```python
import statistics

# Odd number of elements
data = [10, 20, 30, 40, 50]
print(statistics.median(data))  # 30

# Even number of elements (average of middle two)
data = [10, 20, 30, 40]
print(statistics.median(data))  # 25.0

# Unsorted data (automatically sorted)
data = [30, 10, 50, 20, 40]
print(statistics.median(data))  # 30
```

### `median_low(data)` – Low Median

```python
import statistics

# For even number of elements, returns the smaller middle value
data = [10, 20, 30, 40]
print(statistics.median_low(data))  # 20

# For odd, same as median
data = [10, 20, 30, 40, 50]
print(statistics.median_low(data))  # 30
```

### `median_high(data)` – High Median

```python
import statistics

# For even number of elements, returns the larger middle value
data = [10, 20, 30, 40]
print(statistics.median_high(data))  # 30

# For odd, same as median
data = [10, 20, 30, 40, 50]
print(statistics.median_high(data))  # 30
```

### `median_grouped(data, interval=1)` – Grouped Median

```python
import statistics

# For grouped/interval data
data = [10, 20, 30, 40, 50, 60]
print(statistics.median_grouped(data))  # 35.0

# With custom interval
data = [52, 52, 53, 54]
print(statistics.median_grouped(data, interval=2))  # 52.5
```

### `mode(data)` – Most Frequent Value

```python
import statistics

# Single mode
data = [1, 1, 2, 2, 2, 3, 3]
print(statistics.mode(data))  # 2

# With strings
colors = ['red', 'blue', 'red', 'green', 'red']
print(statistics.mode(colors))  # red

# Raises StatisticsError if no unique mode
try:
    statistics.mode([1, 1, 2, 2])  # No unique mode
except statistics.StatisticsError as e:
    print(e)  # no unique mode; found 2 equally common values
```

### `multimode(data)` – All Modes (Python 3.8+)

```python
import statistics

# Returns all modes
data = [1, 1, 2, 2, 3, 3, 4]
print(statistics.multimode(data))  # [1, 2, 3]

# Single mode returns list with one element
data = [1, 1, 1, 2, 3]
print(statistics.multimode(data))  # [1]

# Empty list returns empty list
print(statistics.multimode([]))  # []
```

### `quantiles(data, n=4)` – Quantiles (Python 3.8+)

```python
import statistics

# Quartiles (4 equal parts)
data = [10, 20, 30, 40, 50, 60, 70, 80]
print(statistics.quantiles(data, n=4))  # [22.5, 45.0, 67.5]

# Percentiles (100 equal parts)
percentiles = statistics.quantiles(data, n=100)
print(f"90th percentile: {percentiles[89]}")

# Deciles (10 equal parts)
deciles = statistics.quantiles(data, n=10)
print(f"Deciles: {deciles}")
```

---

## Measures of Spread

Spread measures describe how spread out the data is.

### `pstdev(data, mu=None)` – Population Standard Deviation

```python
import statistics

# Full population data
population = [10, 20, 30, 40, 50]
print(statistics.pstdev(population))  # 14.142135623730951

# With known mean (slightly faster)
mean = statistics.mean(population)
print(statistics.pstdev(population, mu=mean))  # 14.142135623730951
```

### `stdev(data, xbar=None)` – Sample Standard Deviation

```python
import statistics

# Sample data (subset of population)
sample = [10, 20, 30, 40, 50]
print(statistics.stdev(sample))  # 15.811388300841896

# Different from population std dev (uses n-1 degrees of freedom)
```

### `pvariance(data, mu=None)` – Population Variance

```python
import statistics

population = [10, 20, 30, 40, 50]
print(statistics.pvariance(population))  # 200.0

# Variance = (standard deviation)²
print(statistics.pstdev(population) ** 2)  # 200.0
```

### `variance(data, xbar=None)` – Sample Variance

```python
import statistics

sample = [10, 20, 30, 40, 50]
print(statistics.variance(sample))  # 250.0

# Sample variance uses n-1 degrees of freedom
print(statistics.pvariance(sample))  # 200.0 (different)
```

---

## Measures of Position

### `quantiles(data, n=4)` – Quantiles

```python
import statistics

data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Quartiles (4 groups)
q1, q2, q3 = statistics.quantiles(data, n=4)
print(f"Q1: {q1}, Q2: {q2}, Q3: {q3}")  # Q1: 27.5, Q2: 55.0, Q3: 82.5

# Percentiles (100 groups)
percentiles = statistics.quantiles(data, n=100)
print(f"90th percentile: {percentiles[89]}")  # 91.0

# Deciles (10 groups)
deciles = statistics.quantiles(data, n=10)
print(f"Deciles: {deciles}")
```

---

## Real-World Examples

### Example 1: Student Grade Analyzer

```python
import statistics
from collections import Counter

class GradeAnalyzer:
    def __init__(self, grades):
        self.grades = grades
    
    def analyze(self):
        """Complete grade analysis"""
        print("GRADE ANALYSIS")
        print("=" * 50)
        
        # Basic statistics
        print(f"Number of students: {len(self.grades)}")
        print(f"Mean (average): {statistics.mean(self.grades):.2f}")
        print(f"Median: {statistics.median(self.grades):.2f}")
        print(f"Mode: {statistics.mode(self.grades)}")
        print(f"Standard deviation: {statistics.stdev(self.grades):.2f}")
        print(f"Variance: {statistics.variance(self.grades):.2f}")
        
        # Range
        print(f"Range: {min(self.grades)} - {max(self.grades)}")
        
        # Quartiles
        q1, q2, q3 = statistics.quantiles(self.grades, n=4)
        print(f"Q1 (25th percentile): {q1:.2f}")
        print(f"Q2 (50th percentile/median): {q2:.2f}")
        print(f"Q3 (75th percentile): {q3:.2f}")
        print(f"IQR (Interquartile Range): {q3 - q1:.2f}")
        
        # Grade distribution
        print("\nGrade Distribution:")
        grade_counts = Counter()
        for grade in self.grades:
            if grade >= 90:
                grade_counts['A'] += 1
            elif grade >= 80:
                grade_counts['B'] += 1
            elif grade >= 70:
                grade_counts['C'] += 1
            elif grade >= 60:
                grade_counts['D'] += 1
            else:
                grade_counts['F'] += 1
        
        for letter, count in sorted(grade_counts.items()):
            percentage = count / len(self.grades) * 100
            bar = '█' * int(percentage / 2)
            print(f"  {letter}: {count} students ({percentage:.1f}%) {bar}")
        
        # Identify outliers using IQR method
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        outliers = [g for g in self.grades if g < lower_bound or g > upper_bound]
        
        if outliers:
            print(f"\nPotential outliers: {outliers}")
        else:
            print("\nNo outliers detected")

# Sample data
grades = [85, 92, 78, 88, 95, 67, 73, 89, 91, 84, 77, 82, 90, 86, 79]
analyzer = GradeAnalyzer(grades)
analyzer.analyze()
```

### Example 2: Sales Data Analysis

```python
import statistics
from datetime import datetime, timedelta

class SalesAnalyzer:
    def __init__(self, sales_data):
        """
        sales_data: list of dicts with 'date' and 'amount'
        """
        self.sales_data = sales_data
        self.amounts = [s['amount'] for s in sales_data]
    
    def daily_stats(self):
        """Daily sales statistics"""
        print("DAILY SALES STATISTICS")
        print("=" * 50)
        print(f"Total sales days: {len(self.amounts)}")
        print(f"Total revenue: ${sum(self.amounts):,.2f}")
        print(f"Average daily sales: ${statistics.mean(self.amounts):,.2f}")
        print(f"Median daily sales: ${statistics.median(self.amounts):,.2f}")
        print(f"Best day: ${max(self.amounts):,.2f}")
        print(f"Worst day: ${min(self.amounts):,.2f}")
        print(f"Standard deviation: ${statistics.stdev(self.amounts):,.2f}")
    
    def weekly_stats(self):
        """Weekly sales statistics"""
        # Group by week
        weekly_totals = {}
        for sale in self.sales_data:
            week = sale['date'].strftime('%Y-W%W')
            weekly_totals[week] = weekly_totals.get(week, 0) + sale['amount']
        
        weekly_amounts = list(weekly_totals.values())
        
        print("\nWEEKLY SALES STATISTICS")
        print("=" * 50)
        print(f"Number of weeks: {len(weekly_amounts)}")
        print(f"Average weekly sales: ${statistics.mean(weekly_amounts):,.2f}")
        print(f"Best week: ${max(weekly_amounts):,.2f}")
        print(f"Worst week: ${min(weekly_amounts):,.2f}")
    
    def monthly_stats(self):
        """Monthly sales statistics"""
        # Group by month
        monthly_totals = {}
        for sale in self.sales_data:
            month = sale['date'].strftime('%Y-%m')
            monthly_totals[month] = monthly_totals.get(month, 0) + sale['amount']
        
        monthly_amounts = list(monthly_totals.values())
        
        print("\nMONTHLY SALES STATISTICS")
        print("=" * 50)
        print(f"Number of months: {len(monthly_amounts)}")
        print(f"Average monthly sales: ${statistics.mean(monthly_amounts):,.2f}")
        print(f"Best month: ${max(monthly_amounts):,.2f}")
        print(f"Worst month: ${min(monthly_amounts):,.2f}")
    
    def trend_analysis(self):
        """Analyze sales trend"""
        amounts = self.amounts
        n = len(amounts)
        
        if n < 2:
            print("Insufficient data for trend analysis")
            return
        
        # Compare first half vs second half
        mid = n // 2
        first_half = amounts[:mid]
        second_half = amounts[mid:]
        
        first_avg = statistics.mean(first_half)
        second_avg = statistics.mean(second_half)
        
        print("\nTREND ANALYSIS")
        print("=" * 50)
        print(f"First half average: ${first_avg:,.2f}")
        print(f"Second half average: ${second_avg:,.2f}")
        
        if second_avg > first_avg:
            percent_increase = ((second_avg - first_avg) / first_avg) * 100
            print(f"📈 Increasing trend: +{percent_increase:.1f}%")
        elif second_avg < first_avg:
            percent_decrease = ((first_avg - second_avg) / first_avg) * 100
            print(f"📉 Decreasing trend: -{percent_decrease:.1f}%")
        else:
            print("📊 Stable trend")
        
        # Check for outliers
        q1, q2, q3 = statistics.quantiles(amounts, n=4)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        outliers = [a for a in amounts if a < lower or a > upper]
        
        if outliers:
            print(f"\nOutlier days detected: {len(outliers)}")
            for outlier in outliers:
                print(f"  ${outlier:,.2f}")

# Generate sample sales data
def generate_sales_data(days=30):
    import random
    data = []
    start_date = datetime(2024, 1, 1)
    
    for i in range(days):
        date = start_date + timedelta(days=i)
        # Weekly pattern: higher on weekends
        if date.weekday() >= 5:  # Weekend
            amount = random.uniform(800, 1200)
        else:  # Weekday
            amount = random.uniform(400, 800)
        
        data.append({'date': date, 'amount': amount})
    
    return data

# Analyze sales
sales_data = generate_sales_data(90)
analyzer = SalesAnalyzer(sales_data)
analyzer.daily_stats()
analyzer.weekly_stats()
analyzer.monthly_stats()
analyzer.trend_analysis()
```

### Example 3: Quality Control Analysis

```python
import statistics

class QualityControl:
    def __init__(self, measurements, spec_limit_lower, spec_limit_upper):
        self.measurements = measurements
        self.usl = spec_limit_upper  # Upper specification limit
        self.lsl = spec_limit_lower  # Lower specification limit
    
    def calculate_cp(self):
        """Calculate Process Capability Index (Cp)"""
        std_dev = statistics.stdev(self.measurements)
        if std_dev == 0:
            return float('inf')
        return (self.usl - self.lsl) / (6 * std_dev)
    
    def calculate_cpk(self):
        """Calculate Process Capability Index (Cpk) - accounts for centering"""
        mean = statistics.mean(self.measurements)
        std_dev = statistics.stdev(self.measurements)
        if std_dev == 0:
            return float('inf')
        
        cpu = (self.usl - mean) / (3 * std_dev)
        cpl = (mean - self.lsl) / (3 * std_dev)
        return min(cpu, cpl)
    
    def calculate_defect_rate(self):
        """Calculate percentage of measurements outside specs"""
        defects = sum(1 for m in self.measurements 
                     if m < self.lsl or m > self.usl)
        return defects / len(self.measurements) * 100
    
    def generate_report(self):
        """Generate quality control report"""
        print("QUALITY CONTROL REPORT")
        print("=" * 50)
        
        # Basic statistics
        mean = statistics.mean(self.measurements)
        median = statistics.median(self.measurements)
        std_dev = statistics.stdev(self.measurements)
        
        print(f"Sample size: {len(self.measurements)}")
        print(f"Mean: {mean:.4f}")
        print(f"Median: {median:.4f}")
        print(f"Standard deviation: {std_dev:.4f}")
        print(f"Range: {min(self.measurements):.4f} - {max(self.measurements):.4f}")
        
        # Specification limits
        print(f"\nSpecification Limits:")
        print(f"  LSL (Lower): {self.lsl:.4f}")
        print(f"  USL (Upper): {self.usl:.4f}")
        
        # Process capability
        cp = self.calculate_cp()
        cpk = self.calculate_cpk()
        
        print(f"\nProcess Capability:")
        print(f"  Cp: {cp:.3f}")
        print(f"  Cpk: {cpk:.3f}")
        
        # Interpretation
        if cpk >= 1.33:
            print("  ✅ Process is capable")
        elif cpk >= 1.0:
            print("  ⚠️ Process is marginally capable")
        else:
            print("  ❌ Process is NOT capable")
        
        # Defect rate
        defect_rate = self.calculate_defect_rate()
        print(f"\nDefect rate: {defect_rate:.2f}%")
        
        # Identify outliers
        q1, q2, q3 = statistics.quantiles(self.measurements, n=4)
        iqr = q3 - q1
        lower_outlier = q1 - 1.5 * iqr
        upper_outlier = q3 + 1.5 * iqr
        outliers = [m for m in self.measurements 
                   if m < lower_outlier or m > upper_outlier]
        
        if outliers:
            print(f"\nOutliers detected: {len(outliers)}")
            for outlier in outliers[:5]:
                print(f"  {outlier:.4f}")
            if len(outliers) > 5:
                print(f"  ... and {len(outliers) - 5} more")
        else:
            print("\nNo outliers detected")
        
        # Normal distribution check (simplified)
        mean = statistics.mean(self.measurements)
        median = statistics.median(self.measurements)
        if abs(mean - median) < 0.1 * std_dev:
            print("\nData appears approximately normally distributed")
        else:
            print("\nData may be skewed (mean ≠ median)")

# Generate sample measurements
import random
import math

def generate_measurements(n=100, target=10.0, sigma=0.5):
    """Generate normally distributed measurements"""
    return [random.gauss(target, sigma) for _ in range(n)]

# Quality control analysis
measurements = generate_measurements(100, target=10.0, sigma=0.3)
qc = QualityControl(measurements, spec_limit_lower=9.0, spec_limit_upper=11.0)
qc.generate_report()
```

### Example 4: Stock Price Analysis

```python
import statistics
import random

class StockAnalyzer:
    def __init__(self, prices):
        self.prices = prices
    
    def calculate_returns(self):
        """Calculate daily returns"""
        returns = []
        for i in range(1, len(self.prices)):
            ret = (self.prices[i] - self.prices[i-1]) / self.prices[i-1]
            returns.append(ret)
        return returns
    
    def analyze(self):
        """Complete stock analysis"""
        returns = self.calculate_returns()
        
        print("STOCK PRICE ANALYSIS")
        print("=" * 60)
        
        # Price statistics
        print(f"Starting price: ${self.prices[0]:.2f}")
        print(f"Ending price: ${self.prices[-1]:.2f}")
        print(f"Highest price: ${max(self.prices):.2f}")
        print(f"Lowest price: ${min(self.prices):.2f}")
        print(f"Average price: ${statistics.mean(self.prices):.2f}")
        print(f"Median price: ${statistics.median(self.prices):.2f}")
        
        # Return statistics
        if returns:
            print(f"\nDaily Returns Statistics:")
            print(f"  Average daily return: {statistics.mean(returns):.4%}")
            print(f"  Median daily return: {statistics.median(returns):.4%}")
            print(f"  Volatility (std dev): {statistics.stdev(returns):.4%}")
            print(f"  Best day: {max(returns):.4%}")
            print(f"  Worst day: {min(returns):.4%}")
            
            # Total return
            total_return = (self.prices[-1] - self.prices[0]) / self.prices[0]
            print(f"\nTotal return: {total_return:.4%}")
            
            # Positive vs negative days
            positive_days = sum(1 for r in returns if r > 0)
            negative_days = sum(1 for r in returns if r < 0)
            print(f"Positive days: {positive_days} ({positive_days/len(returns):.1%})")
            print(f"Negative days: {negative_days} ({negative_days/len(returns):.1%})")
            
            # Risk metrics
            downside_returns = [r for r in returns if r < 0]
            if downside_returns:
                downside_volatility = statistics.stdev(downside_returns) if len(downside_returns) > 1 else 0
                print(f"Downside volatility: {downside_volatility:.4%}")
            
            # Maximum drawdown
            peak = self.prices[0]
            max_drawdown = 0
            for price in self.prices:
                if price > peak:
                    peak = price
                drawdown = (peak - price) / peak
                if drawdown > max_drawdown:
                    max_drawdown = drawdown
            print(f"Maximum drawdown: {max_drawdown:.4%}")
            
            # Volatility clustering (simplified)
            high_vol_days = sum(1 for r in returns if abs(r) > statistics.stdev(returns))
            print(f"High volatility days: {high_vol_days} ({high_vol_days/len(returns):.1%})")
        
        # Price distribution
        q1, q2, q3 = statistics.quantiles(self.prices, n=4)
        print(f"\nPrice Distribution:")
        print(f"  Q1 (25th percentile): ${q1:.2f}")
        print(f"  Median (50th percentile): ${q2:.2f}")
        print(f"  Q3 (75th percentile): ${q3:.2f}")
        print(f"  IQR: ${q3 - q1:.2f}")

# Generate sample stock prices
def generate_prices(start=100, days=252, volatility=0.02, drift=0.0005):
    """Generate random walk stock prices"""
    prices = [start]
    for _ in range(days - 1):
        change = random.gauss(drift, volatility)
        new_price = prices[-1] * (1 + change)
        prices.append(new_price)
    return prices

# Analyze stock
prices = generate_prices(start=100, days=252, volatility=0.02)
analyzer = StockAnalyzer(prices)
analyzer.analyze()
```

### Example 5: Survey Data Analysis

```python
import statistics
from collections import Counter

class SurveyAnalyzer:
    def __init__(self, responses):
        """
        responses: list of dictionaries with survey responses
        """
        self.responses = responses
    
    def analyze_numeric(self, question):
        """Analyze numeric question responses"""
        values = [r[question] for r in self.responses if question in r]
        
        if not values:
            print(f"No data for '{question}'")
            return
        
        print(f"\n{question.upper()}")
        print("-" * 40)
        print(f"Responses: {len(values)}")
        print(f"Mean: {statistics.mean(values):.2f}")
        print(f"Median: {statistics.median(values):.2f}")
        print(f"Mode: {statistics.mode(values)}")
        print(f"Std Dev: {statistics.stdev(values):.2f}")
        print(f"Range: {min(values)} - {max(values)}")
        
        # Distribution
        q1, q2, q3 = statistics.quantiles(values, n=4)
        print(f"Q1: {q1:.2f}, Q2: {q2:.2f}, Q3: {q3:.2f}")
    
    def analyze_categorical(self, question):
        """Analyze categorical question responses"""
        values = [r[question] for r in self.responses if question in r]
        
        if not values:
            print(f"No data for '{question}'")
            return
        
        counts = Counter(values)
        
        print(f"\n{question.upper()}")
        print("-" * 40)
        print(f"Responses: {len(values)}")
        print(f"Unique answers: {len(counts)}")
        print("\nDistribution:")
        
        for answer, count in counts.most_common():
            percentage = count / len(values) * 100
            bar = '█' * int(percentage / 2)
            print(f"  {answer}: {count} ({percentage:.1f}%) {bar}")
        
        if len(counts) > 1:
            most_common = counts.most_common(1)[0]
            print(f"\nMost common: '{most_common[0]}' ({most_common[1]} responses)")
    
    def correlation(self, question1, question2):
        """Calculate correlation between two numeric questions"""
        # Pair responses
        pairs = []
        for r in self.responses:
            if question1 in r and question2 in r:
                pairs.append((r[question1], r[question2]))
        
        if len(pairs) < 2:
            print("Insufficient data for correlation")
            return
        
        x = [p[0] for p in pairs]
        y = [p[1] for p in pairs]
        
        # Pearson correlation
        n = len(x)
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum(x[i] * y[i] for i in range(n))
        sum_x2 = sum(xi ** 2 for xi in x)
        sum_y2 = sum(yi ** 2 for yi in y)
        
        numerator = n * sum_xy - sum_x * sum_y
        denominator = ((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2)) ** 0.5
        
        if denominator == 0:
            correlation = 0
        else:
            correlation = numerator / denominator
        
        print(f"\nCorrelation between '{question1}' and '{question2}'")
        print("-" * 40)
        print(f"Sample size: {n}")
        print(f"Correlation coefficient: {correlation:.3f}")
        
        if abs(correlation) > 0.7:
            print("  Strong correlation")
        elif abs(correlation) > 0.3:
            print("  Moderate correlation")
        else:
            print("  Weak correlation")
        
        if correlation > 0:
            print("  Positive relationship")
        elif correlation < 0:
            print("  Negative relationship")

# Sample survey data
survey_responses = [
    {'age': 25, 'satisfaction': 4, 'income': 50000, 'city': 'NYC'},
    {'age': 30, 'satisfaction': 5, 'income': 75000, 'city': 'LA'},
    {'age': 22, 'satisfaction': 3, 'income': 40000, 'city': 'NYC'},
    {'age': 35, 'satisfaction': 4, 'income': 80000, 'city': 'Chicago'},
    {'age': 28, 'satisfaction': 5, 'income': 65000, 'city': 'LA'},
    {'age': 40, 'satisfaction': 2, 'income': 90000, 'city': 'NYC'},
    {'age': 26, 'satisfaction': 4, 'income': 55000, 'city': 'Chicago'},
    {'age': 32, 'satisfaction': 3, 'income': 70000, 'city': 'LA'},
]

analyzer = SurveyAnalyzer(survey_responses)
analyzer.analyze_numeric('age')
analyzer.analyze_numeric('satisfaction')
analyzer.analyze_categorical('city')
analyzer.correlation('age', 'satisfaction')
analyzer.correlation('income', 'satisfaction')
```

---

## Practice Exercises

### Beginner Level

1. **Average Calculator**
   ```python
   # Calculate mean of list of numbers
   ```

2. **Median Finder**
   ```python
   # Find median of list of numbers
   ```

3. **Mode Finder**
   ```python
   # Find most common number in list
   ```

### Intermediate Level

4. **Grade Statistics**
   ```python
   # Calculate mean, median, mode of test scores
   ```

5. **Sales Analysis**
   ```python
   # Analyze daily sales data
   ```

6. **Temperature Statistics**
   ```python
   # Calculate average, variance, std dev of temperatures
   ```

### Advanced Level

7. **Quality Control**
   ```python
   # Calculate Cp and Cpk for manufacturing process
   ```

8. **Stock Analysis**
   ```python
   # Calculate returns, volatility, drawdown
   ```

9. **Survey Analysis**
   ```python
   # Analyze survey data with multiple question types
   ```

---

## Quick Reference Card

```python
import statistics

# Central tendency
statistics.mean(data)               # Arithmetic mean
statistics.fmean(data)              # Fast float mean (3.8+)
statistics.geometric_mean(data)     # Geometric mean (3.8+)
statistics.harmonic_mean(data)      # Harmonic mean
statistics.median(data)             # Median
statistics.median_low(data)         # Low median
statistics.median_high(data)        # High median
statistics.median_grouped(data)     # Grouped median
statistics.mode(data)               # Single mode
statistics.multimode(data)          # All modes (3.8+)
statistics.quantiles(data, n=4)     # Quantiles (3.8+)

# Spread
statistics.pstdev(data)             # Population standard deviation
statistics.stdev(data)              # Sample standard deviation
statistics.pvariance(data)          # Population variance
statistics.variance(data)           # Sample variance

# Exceptions
statistics.StatisticsError          # Raised for invalid operations
```

---

## Next Step

- Move to [13_hashlib.md](13_hashlib.md) to learn about cryptographic hashing.

---

*Master the statistics module for data analysis in Python! 🐍✨*