import os
import sys
import random
import string


def main():
    files = [f"file_{''.join(random.choices(string.ascii_lowercase, k=6))}.pdf" for _ in range(100)]
    # files that have been completely processed
    processed = dict(
        zip(
            random.choices(files, k=10),
            random.choices(range(1, 100), k=10)
        )
    )
    # files currently processing
    processing = random.choices(list(set(files).difference(processed.keys())), k=15)
    # files yet to be processed
    # unprocessed = None

    unprocessed = []

    for file in files:
        if file not in processing and file not in processed:
            unprocessed.append(file)

    # print(f"Files: {len(files)}\n"
    #       f"Processed: {len(processed)}\n"
    #       f"Processing: {len(processing)}\n"
    #       f"Unprocessed: {len(unprocessed)}")

    print(f"filename\t\t\tscore\n"
          f"{'=' * 50}")
    for file, value in processed.items():
        if value > 50:
            print(f"{file}\t\t{value}")

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
