# Reflection on TDD Lab (Part A)

### 1. How many tests did you write in Part A, and how many lines of production code? What is the ratio?
In Part A, we ended up with **9 tests** (around 56 lines in `test_kitchen.py`) and **53 lines of code** in `kitchen.py`. That means we have about **1 test for every 6 lines of code** (roughly 0.17).

### 2. When was your bar red for the longest time, and what made it last so long?
The test bar was red the longest in **Step A5** and **Step A7**:
- In **A5**, right after we added `unit` to `Quantity.__init__`, all the earlier tests broke because they didn't pass the new unit argument. We had to stop and clean up the old tests with `grams()` and `ounces()` helpers before they could pass again.
- In **A7**, changing `reduce` to work with the converter was confusing at first. We got errors because `Converter.reduce` called `source.reduce(unit)` instead of passing `self` along, so fixing the arguments took a while.

### 3. Find one place where you used Fake It, one where you triangulated, and one where you used Obvious Implementation. Looking back, was each choice right?
- **Fake It:** In Step A1, we just returned a hardcoded 600 in `times(3)`. It felt kind of funny to do, but it was nice because we got the basic class setup working first.
- **Triangulation:** In Step A2, we added a second test for `times(2)`. The hardcoded 600 didn't work anymore, so we had to write the real formula (`amount * multiplier`). This felt very natural and safe.
- **Obvious Implementation:** Writing `__repr__` and simple helpers like `grams()` and `ounces()`. They were so simple that faking them would have just wasted time.

### 4. Which items are still on your test list? Which would you implement next, and which should you delete because they were speculation?
We actually finished all the core items on our list up to Step A8.
- **What to do next:** We could add subtraction (`minus`) or make `Converter` throw a clean error if an exchange rate is missing.
- **What to delete:** Things like negative numbers, fractional kitchen units (teaspoons/tablespoons), or automatic reverse conversion rates. We don't need them right now and shouldn't add them until someone actually asks for them.

### 5. Look at Quantity.reduce. If you had designed the whole system on paper first, would you have written this method?
Honestly, **no**. If I planned this on paper from the start, I would have treated `Quantity` as just dumb data and put all the math and conversion inside `Converter` with `if/else` checks. Doing TDD pushed us into a much cleaner design where both `Quantity` and `Sum` can just handle `reduce` on their own.

### 6. In Part 0 you wrote the tests after the code, and in Part A before it. How did the two feel different, and which tests shaped your design?
Writing tests after the code in Part 0 felt like an inspection—we were just looking for bugs in code that was already finished. In Part A, writing tests first actually forced how we built the code. It made `Quantity` immutable and led us to create the `Sum` class. Tests for mixed-unit addition in A6 and A7 definitely had the biggest impact on our design.