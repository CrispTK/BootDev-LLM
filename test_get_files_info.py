from functions.get_files_info import get_files_info


def print_result(directory: str) -> None:
    # Build the heading from the requested directory.
    title = (
        "Result for current directory:"
        if directory == "."
        else f"Result for '{directory}' directory:"
    )
    print(title)
    result = get_files_info("calculator", directory)
    indent = "    " if result.startswith("Error:") else "  "
    print("\n".join(f"{indent}{line}" for line in result.splitlines()))


print_result(".")
print_result("pkg")
print_result("/bin")
print_result("../")
