from functions.get_files_info import get_files_info


def print_result(title: str, directory: str) -> None:
    print(title)
    result = get_files_info("calculator", directory)
    indent = "    " if result.startswith("Error:") else "  "
    print("\n".join(f"{indent}{line}" for line in result.splitlines()))


print_result("Result for current directory:", ".")
print_result("Result for 'pkg' directory:", "pkg")
print_result("Result for '/bin' directory:", "/bin")
print_result("Result for '../' directory:", "../")
