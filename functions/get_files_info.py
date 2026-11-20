import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        # Normalize the requested path before checking its lexical boundary.
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        valid_target_dir = (
            os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        )

        # Resolve symlinks too, so an in-bound path cannot redirect outside.
        working_dir_real = os.path.realpath(working_dir_abs)
        target_dir_real = os.path.realpath(target_dir)
        target_resolves_within_working_directory = (
            os.path.commonpath([working_dir_real, target_dir_real])
            == working_dir_real
        )

        if not valid_target_dir or not target_resolves_within_working_directory:
            return (
                f'Error: Cannot list "{directory}" as it is outside the '
                "permitted working directory"
            )
        if not os.path.isdir(target_dir_real):
            return f'Error: "{directory}" is not a directory'

        # Collect the requested metadata for each item in the directory.
        entries = []
        for name in os.listdir(target_dir_real):
            item_path = os.path.join(target_dir_real, name)
            file_size = os.path.getsize(item_path)
            is_directory = os.path.isdir(item_path)
            entries.append(
                f"- {name}: file_size={file_size} bytes, "
                f"is_dir={is_directory}"
            )

        return "\n".join(entries)
    except Exception as error:
        # Report standard-library errors instead of letting them escape.
        return f"Error: {error}"