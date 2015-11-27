import re
class sorter:
    # Constructor. 
   def __init__(self, inputFile, outputFile):
        self.inputFile = inputFile
        self.outputFile = outputFile

        if not inputFile or not outputFile:
            raise ValueError('Error the input or output file params are null')

    def readFile(self):
        with open(self.inputFile) as file:
            self.fileContents = file.readlines()

    def sort(self):
        for line in self.fileContents:
            self.dict = {
                'numbers' : [], 
                'strings' : [], 
                'key'     : [], 
                'output'  : []
            }
            # remove non-alphanumeric chars 
            re.sub(r'\W+', '', line)
            # strip line breaks from line.
            line = line.strip('\n')
            # create array of the strings in the line using ' ' as the delimiter
            line = line.split(' ')
            filter(line)

            #Sort
            self.dict['strings'].sort()
            self.dict['numbers'].sort()

            for item in self.dict['key']:
                if item == 'number':
                    self.dict['output'].append(self.dict['numbers'][0])
                    self.dict['numbers'].pop(0)
                else:
                    self.dict['output'].append(self.dict['strings'][0])
                    self.dict['strings'].pop(0)

            new_line = formatLine(self.dict['output'])
            writeLine(new_line)


    def filter(self, line):
        for item in line
            if item.isDigit():
                self.dict['numbers'].append(int(item))
                self.dict['key'].append('number')
            else:
                self.dict['strings'].append(item)
                self.dict['key'].append('string')

    def formatLine(self, line):
        for item in line:
            new_line += (str)item + " "
        new_line += "\n"
        return new_line

    def writeLine(self, line):
        file = open(self.outputFile, 'a')
        file.write(line)
        file.close()


