# -*- coding: utf-8 -*-
import argparse
import csv
import os

class QualisSearch():
    def __init__(self):
        script_path = os.path.dirname(os.path.realpath(__file__))
        with open(script_path + "/data.csv") as f:
            self.data = list(csv.reader(f, delimiter = ";"))
        self.data.sort(key = lambda x: x[3])

    def search(self, string, row_id):
        for row in self.data:
            if string.lower() in row[row_id].lower():
                print("\033[1;36m{}\033[0m\t\033[0;32m{}\033[0m\t\033[1;34m{}\033[0m ({})".format(row[0], row[3], row[1], row[2].strip()))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Script para consulta de Qualis em periódicos")
    parser.add_argument("-p", dest = "periodico", type = str, help = "Nome do periódico")
    parser.add_argument("-i", dest = "issn", type = str, help = "ISSN")
    args = parser.parse_args()
    qs = QualisSearch()

    if args.periodico is not None:
        print("\033[;1mISSN\t\tQualis\tJournal name\033")
        qs.search(args.periodico, 1)
    elif args.issn is not None:
        print("\033[;1mISSN\t\tQualis\tJournal name\033")
        qs.search(args.issn, 0)
    else:
        print("[-h] para ajuda.")
