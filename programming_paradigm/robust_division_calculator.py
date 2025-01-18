def safe_divide(numerator, denominator):
    try:
        numerator / denominator
    except ZeroDivisionError:
        print("You cannot divide by 0")
    except ValueError:
        print("You can only use numerals")
