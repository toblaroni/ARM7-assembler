import os, sys

class Assembler:
    def __init__(self):
        self._labels = {}

    def assemble(self, source_file):
        # Parse (2 passes)
        self._parse_source_file(source_file)   

        # Translate instructions to binary
        
    def _parse_source_file(self, source_file):
        # First pass collect all the labels and their line num
        try:
            with open(source_file, 'r') as file:
                for line in file:
                    # If label add to label dictionary
                    pass
                    
        except IOError as e:
            print(f"ERROR: Unable to open source file {source_file}'")

        # Second pass translate commands to binary?...

def main():
    if (len(sys.argv) != 2):
        print("ERROR: Usage 'python assembler.py <source_file>'")
        sys.exit(1)

    source_file = sys.argv[1]
    Assembler().assemble(source_file)


if __name__ == "__main__":
    main()

