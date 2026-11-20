from functions.get_files_info import get_files_info

def print_result(working_directory: str, directory: str) -> None:
    # Build the heading from the requested directory.
    title = (
        "Result for current directory:"
        if directory == "."
        else f"Result for '{directory}' directory:"
    )
    print(title)
    result = get_files_info(working_directory, directory)
    indent = "    " if result.startswith("Error:") else "  "
    print("\n".join(f"{indent}{line}" for line in result.splitlines()))


print_result("calculator", ".")
print_result("calculator", "pkg")
print_result("calculator", "/bin")
print_result("calculator", "../")