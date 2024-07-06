import multiprocessing
from pathlib import Path
import time


def load_file_paths(directories):
    """Loading paths to files from specified directories."""
    file_paths = []
    for directory in directories:
        file_paths.extend(Path(directory).rglob('*.txt'))
    return [str(path) for path in file_paths]


def split_work(file_paths, num_processes):
    """Splitting work between processes."""
    chunk_size = len(file_paths) // num_processes + (len(file_paths) % num_processes > 0)
    return [file_paths[i:i + chunk_size] for i in range(0, len(file_paths), chunk_size)]


def process_files(file_paths_chunk, keywords, results_dict, lock):
    """Processing files in a chunk."""
    for path in file_paths_chunk:
        try:
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
                for keyword in keywords:
                    if keyword in content:
                        with lock:
                            if keyword not in results_dict:
                                results_dict[keyword] = [path]
                            elif path not in results_dict[keyword]:
                                results_dict[keyword].append(path)
        except Exception as e:
            print(f"Error processing file {path}: {e}")


def initialize_and_load_file_paths(directories):
    """Initialize and load file paths."""
    file_paths = load_file_paths(directories)
    if not file_paths:
        print("No files found in the specified directories.")
        return None
    return file_paths


def processes_search(file_paths, keywords):
    """Setup and run processes."""
    num_processes = multiprocessing.cpu_count()
    file_paths_chunks = split_work(file_paths, num_processes)

    manager = multiprocessing.Manager()
    results_dict = manager.dict()
    lock = manager.Lock()

    processes = [
        multiprocessing.Process(target=process_files, args=(chunk, keywords, results_dict, lock))
        for chunk in file_paths_chunks]

    for process in processes:
        process.start()
    for process in processes:
        process.join()

    return results_dict


def print_results_and_execution_time(file_paths, results_dict, start_time):
    """Print results and execution time."""
    end_time = time.time()
    print(f"Total files processed: {len(file_paths)}")
    print(f"Execution time: {end_time - start_time} seconds")
    for keyword, paths in results_dict.items():
        print(f"Keyword '{keyword}' found in files: {paths}")


def main():
    """Main function."""
    start_time = time.time()
    directories = ['../public']
    keywords = [
        'unchanged', 'and', 'Aldus', 'accident', 'opposed', 'readable',
        'roots', 'Sections', 'College', 'original', 'passage', 'suffered',
        'believable', 'generators',
    ]

    file_paths = initialize_and_load_file_paths(directories)
    if file_paths is None:
        return

    results = processes_search(file_paths, keywords)
    print_results_and_execution_time(file_paths, results, start_time)


if __name__ == "__main__":
    main()
