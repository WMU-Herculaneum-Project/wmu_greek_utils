import os
import csv
import sys


def find_tagged_files(directory):
    tagged_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if "tagged" in file and file.endswith(".tsv"):
                tagged_files.append(os.path.join(root, file))
    return tagged_files


def print_sixth_column(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter="\t")
        for row in reader:
            if len(row) >= 6:
                if row[5] != "":
                    print(row[5])
                    # parts = row[5].split("|")
                    # for part in parts:
                    #    print(part)


def main(directory):
    tagged_files = find_tagged_files(directory)
    for file_path in tagged_files:
        print_sixth_column(file_path)


if __name__ == "__main__":
    directory = sys.argv[1]
    main(directory)
