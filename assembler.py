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
                self.instructions = []
                # Clean the lines
                for line in file:
                    line = line.strip()
                    if line == '' or line.startswith("//"):
                        continue
                    else:
                        if ("//" in line):
                            line = line[:line.index("//")]      # Remove comments
                        instruction = [el for el in line.split(' ') if el != '']
                        self.instructions.append(instruction)
        except IOError as e:
            print(f"ERROR: Unable to open source file '{source_file}'")
            sys.exit(1)

        self._pass_one()
        self._pass_two()

    def _pass_one(self):
        # First pass collect all the labels and their line num
        PC = 0

        for ins in self.instructions:
            first_word = ins[0]

            if first_word.endswith(':'):        # Label
                label_name = first_word[:-1]

                if first_word[0].isalpha() or first_word.startswith('_'):
                    self._labels[label_name] = PC

                else:
                    print(f"ERROR: Invalid label '{first_word}'. Labels may only start with a letter or underscore.")
                    sys.exit(1)

            elif first_word.startswith('.'):    # Directive
                directive = first_word.upper()

                # Incrememt PC depending on directive
                if directive in [".GLOBAL", ".TEXT", ".ALIGN"]:     # 0 Bytes
                    continue

            
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

