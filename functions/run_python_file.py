import os
import subprocess


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        # Normalize both paths before validating the working-directory boundary.
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_file_path = (
            os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        )

        if not valid_target_file_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not target_file.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'

        # Build the command to run, in the form of a list of strings
        command = ["python", target_file]
        if args:
            command.extend(args)

        # Run the commands
        result = subprocess.run(
            command, 
            cwd=working_dir_abs, 
            capture_output=True,
            text=True,
            timeout=30
        )

        # Build an output string based on the CompletedProcess object
        output = ""

        if result.returncode != 0:
            output += f"Process exited with code {result.returncode}\n"

        if not result.stdout and not result.stderr:
            output += "No output produced"

        else:
            if result.stdout:
                output += f"STDOUT:\n{result.stdout}"
            if result.stderr:
                output += f"STDERR:\n{result.stderr}"

        return output
        
    except Exception as error:
        # Return standard-library failures as text for the agent to handle.
        return f"Error: executing Python file: {error}"