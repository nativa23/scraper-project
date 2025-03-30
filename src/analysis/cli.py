"""
взять шаблон КЛИ из прошлого задания
хотим cli.py <file_path>
внутри КЛИ.ПАЙ буду вызывать:
    df = load_data(file_path)
    visualization(*analyze_data(df))
"""
import argparse
import datetime
import os
import sys
from analyze import load_data, analyze_data, save_results

def main():
    """
    Main function to handle the command-line interface (CLI) commands.
    This function uses argparse to parse user input, determine the desired action,a
    and call the corresponding function from the 'commands' module.

    Available commands:
    - copy: Copy a file from source to destination.
    - delete: Delete a file or directory.
    - count: Count the number of files in a directory.
    - find: Find files based on a pattern in a directory.
    - add_date: Add the creation date to the filenames in a directory.
    - analyse: Analyse the size of a directory.
    - move_ebooks: Move ebooks to a "MyBooks" folder.
    """
    parser = argparse.ArgumentParser(description="Analysis CLI")

    # Define the commands and their arguments
    parser.add_argument(dest='file_path')

    # Parse the arguments and call the appropriate function
    args = parser.parse_args()

    if args.file_path:
        df = load_data(args.file_path)
        region_gross, film_gross, weekly_gross, top_releases = analyze_data(df)
        data_dir = os.path.dirname(os.path.realpath(args.file_path))
        data_dir = os.path.join(data_dir, datetime.date.today().strftime("%d_%m_%Y"))
        os.makedirs(data_dir, exist_ok=True)
        save_results(data_dir, region_gross, film_gross, weekly_gross, top_releases)
    else:
        parser.print_help(sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()


