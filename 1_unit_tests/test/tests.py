import pytest

def test_is_palindrome():
    # Test normal palindromes
    assert is_palindrome("madam") == True
    assert is_palindrome("racecar") == True
    
    # Test non-palindromes
    assert is_palindrome("hello") == False
    assert is_palindrome("world") == False
    
    # Edge cases
    assert is_palindrome("") == True  # An empty string is considered a palindrome
    assert is_palindrome("a") == True  # Single character strings are palindromes
    assert is_palindrome("Aba") == False  # Case-sensitive check

def test_fibonacci():
    # Test known Fibonacci numbers
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    
    # Test larger Fibonacci number
    assert fibonacci(10) == 55
    
    # Test invalid input
    with pytest.raises(ValueError):
        fibonacci(-1)

def test_count_vowels():
    # Test strings with different vowels
    assert count_vowels("hello") == 2  # 'e' and 'o'
    assert count_vowels("world") == 1  # 'o'
    
    # Test strings with no vowels
    assert count_vowels("rhythm") == 0
    
    # Test empty string
    assert count_vowels("") == 0
    
    # Test case sensitivity
    assert count_vowels("aAeEiIoOuU") == 10

def test_calculate_discount():
    # Test with normal values
    assert calculate_discount(100, 20) == 80.0  # 100 - 20% = 80
    assert calculate_discount(50, 10) == 45.0   # 50 - 10% = 45
    
    # Edge cases
    assert calculate_discount(200, 0) == 200.0   # No discount
    assert calculate_discount(0, 10) == 0.0      # Zero price
    
    # Invalid input handling (e.g., discount > 100)
    assert calculate_discount(100, 110) == -10.0  # Discounts over 100%

def test_flatten_list():
    # Test nested lists
    assert flatten_list([1, 2, [3, 4], [5, [6]]]) == [1, 2, 3, 4, 5, 6]
    
    # Test with a list of numbers
    assert flatten_list([1, 2, 3]) == [1, 2, 3]
    
    # Test empty list
    assert flatten_list([]) == []
    
    # Test deeply nested list
    assert flatten_list([[[1, 2], 3], 4]) == [1, 2, 3, 4]

def test_word_frequencies():
    # Test basic input
    assert word_frequencies("hello hello world") == {"hello": 2, "world": 1}
    
    # Test case insensitivity
    assert word_frequencies("Hello hello World") == {"hello": 2, "world": 1}
    
    # Test single word input
    assert word_frequencies("test") == {"test": 1}
    
    # Test empty string
    assert word_frequencies("") == {}
    
    # Test with punctuation
    assert word_frequencies("hello, world!") == {"hello": 1, "world": 1}

def test_is_prime():
    # Test prime numbers
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True
    assert is_prime(11) == True
    
    # Test non-prime numbers
    assert is_prime(4) == False
    assert is_prime(6) == False
    assert is_prime(9) == False
    assert is_prime(10) == False
    
    # Edge cases
    assert is_prime(1) == False  # 1 is not prime
    assert is_prime(0) == False  # 0 is not prime


