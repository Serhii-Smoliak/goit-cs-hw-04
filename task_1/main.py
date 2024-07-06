import threading
from pathlib import Path
import queue
import time


def load_file_paths(directories):
    """Loading paths to files from specified directories."""
    file_paths = []
    for directory in directories:
        file_paths.extend(Path(directory).rglob('*.txt'))
    return [str(path) for path in file_paths]


def search_in_file(file_path, keywords, results_queue):
    """Searching for keywords in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            for keyword in keywords:
                if keyword in content:
                    results_queue.put((keyword, file_path))
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")


def threaded_search(file_paths, keywords):
    """Searching for keywords in files using threads."""
    results_queue = queue.Queue()
    threads = []

    for file_path in file_paths:
        thread = threading.Thread(target=search_in_file, args=(file_path, keywords, results_queue))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    results = {}
    while not results_queue.empty():
        keyword, file_path = results_queue.get()
        if keyword in results:
            results[keyword].append(file_path)
        else:
            results[keyword] = [file_path]

    return results


def print_results_and_execution_time(file_paths, results, start_time):
    """Print results and execution time."""
    end_time = time.time()
    print(f"Total files processed: {len(file_paths)}")
    print(f"Execution time: {end_time - start_time} seconds")
    for keyword, paths in results.items():
        print(f"Keyword '{keyword}' found in files: {paths}")


def main():
    """Main function."""
    start_time = time.time()
    directories = ['../public']
    file_paths = load_file_paths(directories)

    if not file_paths:
        print("No files found in the specified directories.")
        return

    keywords = [
        'unchanged', 'and', 'Aldus', 'accident', 'opposed', 'readable',
        'roots', 'Sections', 'College', 'original', 'passage', 'suffered',
        'believable', 'generators',
    ]

    results = threaded_search(file_paths, keywords)
    print_results_and_execution_time(file_paths, results, start_time)


if __name__ == "__main__":
    main()
