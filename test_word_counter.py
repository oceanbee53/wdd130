import pytest
from word_counter import clean_text, count_words, read_file

def test_clean_text():
    text = "Hello, World! This is a test."
    expected = "hello world this is a test"
    assert clean_text(text) == expected

def test_count_words():
    text = "hello world hello"
    expected = {"hello": 2, "world": 1}
    assert count_words(text) == expected

def test_read_file(tmp_path):
    # Create a temporary file
    temp_file = tmp_path / "test.txt"
    temp_file.write_text("Hello World")

    # Test reading the file
    assert read_file(temp_file) == "Hello World"