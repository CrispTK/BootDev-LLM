import os


def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        # Normalize both paths before validating the working-directory boundary.
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_file_path = (
            os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        )

        if not valid_target_file_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{target_file}" as it is a directory'

        # Make sure that all parent directories of the target_file exist
        os.makedirs(os.path.dirname(target_file), exist_ok=True)

        # Overwrite file contents with own input
        with open(target_file, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{target_file}" ({len(content)} characters written)'

    except Exception as error:
        # Return standard-library failures as text for the agent to handle.
        return f"Error: {error}"

# Function schema
schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Creates a new file or overwrites an existing file with the provided content within a specified working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The path to the file that should be created or updated, relative to the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "The text content that should be written to the file"
                }
            },
        },
    },
}