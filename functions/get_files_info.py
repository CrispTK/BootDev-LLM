import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        # Normalize both paths before validating the working-directory boundary.
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir = (
            os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        )

        if not valid_target_dir:
            return (
                f'Error: Cannot list "{directory}" as it is outside the '
                "permitted working directory"
            )
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        # Collect the requested metadata for each item in the directory
        entries = []
        for name in os.listdir(target_dir):
            item_path = os.path.join(target_dir, name)
            file_size = os.path.getsize(item_path)
            is_directory = os.path.isdir(item_path)
            entries.append(
                f"- {name}: file_size={file_size} bytes, "
                f"is_dir={is_directory}"
            )

        return "\n".join(entries)

    except Exception as error:
        # Return standard-library failures as text for the agent to handle.
        return f"Error: {error}"
