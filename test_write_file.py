from functions.write_file import write_file


def print_result(working_directory: str, file_path: str, content) -> None:
    result = write_file(working_directory, file_path, content)
    print(f"Result for {file_path}:")
    print(result)

print_result("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
print_result("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
print_result("calculator", "/tmp/temp.txt", "this should not be allowed")