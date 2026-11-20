from functions.get_file_content import get_file_content


def print_result(working_directory: str, file_path: str) -> None:
    result = get_file_content(working_directory, file_path)
    print(f"Result for {file_path}:")
    print(result)


# Check truncation without printing the full lorem ipsum content.
lorem_result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt truncated: {'truncated' in lorem_result}")

print_result("calculator", "main.py")
print_result("calculator", "pkg/calculator.py")
print_result("calculator", "/bin/cat")
print_result("calculator", "pkg/does_not_exist.py")