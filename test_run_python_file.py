from functions.run_python_file import run_python_file


def print_result(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> None:
    result = run_python_file(working_directory, file_path, args)
    print(f"Result for {file_path}:")
    print(result)

print_result("calculator", "main.py")
print_result("calculator", "main.py", ["3 + 5"])
print_result("calculator", "tests.py")
print_result("calculator", "../main.py")
print_result("calculator", "nonexistent.py")
print_result("calculator", "lorem.txt")