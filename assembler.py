import os, sys

class Assembler:
    def __init__(self):
        self.INSTRUCTION_SIZE= 32
        self._labels = {}

    def assemble(self, source_file):
        # Parse (2 passes)
        self._parse_source_file(source_file)   

        # Translate instructions to binary
        
    def _parse_source_file(self, source_file):
        try:
            with open(source_file, 'r') as file:
                self.source_lines = []
                # Clean the lines
                for line in file:
                    line = line.strip()
                    if line == '' or line.startswith("//"):
                        continue
                    else:
                        self.source_lines.append(line)
        except IOError as e:
            print(f"ERROR: Unable to open source file {source_file}'")
            sys.exit(1)

        self._pass_one()
        self._pass_two()

    def _pass_one(self):
        # First pass collect all the labels and their line num
        PC = 0
        for line in self.source_lines:
            print(line)
            
    def _pass_two(self):
        pass

def main():
    if (len(sys.argv) != 2):
        print("ERROR: Usage 'python assembler.py <source_file>'")
        sys.exit(1)

    source_file = sys.argv[1]
    Assembler().assemble(source_file)


if __name__ == "__main__":
    main()

