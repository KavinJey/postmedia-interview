import sys


class WordCounter:
    """
    Word Counter class written for the Post Media interview
    assessment. This classes function is to count words from text
    file specified from the command line as well as spit out top
    10 occurrences
    """

    def countWords(self):
        """
        :return: Returns an integer representing the amount
                 of words within the file
        """
        # Easy count from the initial computation and init function
        # Just using the len() function to count up the array and return it
        return len(self.fileContentWords)

    def getTopOccurrences(self):
        """
        Function goes through text and looks for top 10
        keyword occurrences and returns them as a dictionary
        :return: Dictionary value of top 10 occurrences
        """
        occurrences = {}
        listOfWords = self.fileContentWords

        for wordElement in listOfWords:
            if wordElement in occurrences:
                occurrences[str(wordElement)] += 1
            else:
                occurrences[str(wordElement)] = 1

        # If there are less than 10 words then we don't need to
        # do any further calculation
        if len(occurrences.keys()) <= 10:
            return occurrences

        else:
            # Returns list of sorted Words from value
            greatestOccurredWords = sorted(occurrences, key=occurrences.get, reverse=True)

            # Cleaner dictionary to return
            toReturnDictionary = {}

            # Getting just the top 10
            for index in range(10):
                currentWord = greatestOccurredWords[index]
                toReturnDictionary[currentWord] = occurrences[currentWord]

            # Sorting our dictionary before returning
            # maintains consistency

            return toReturnDictionary

    def getContent(self):
        """
        Getter for file that is parsed by class instance
        :return: returns the content of the file
        """
        return self.fileContent

    def __init__(self, filename):
        """
        :param filename: Filename specifed in command line
        :type filename: String
        """
        self.filename = filename

        try:
            with open(str(filename), "r") as file:
                self.fileContent = file.read()
                file.close()

                # Assumes that all the words in the text file are separated by words
                # it then splits them into an array for easy computation in other methods
                self.fileContentWords = [line.strip().lower() for line in self.fileContent.split(" ") if line != None]

        except IOError:
            print(
                "File not found. Cannot analyse text.\n"
                "Make sure the file is within the directory or the full path is "
                "specified.")


if __name__ == "__main__":
    """ Main Program that handles all the CLI interaction as
        well as output. 
    """

    d = WordCounter(sys.argv[1])
    numberOfWords = d.countWords()
    highestOccurredWords = d.getTopOccurrences()

    # Since dicts are un ordered and we want the
    # top 10 in order we'll need an ordered data type

    # First getting it into a list of tuples
    orderedPlaceHolder = sorted(highestOccurredWords.items(), key=lambda key: key[0])

    # Ordering by value
    orderedPlaceHolder.sort(key=lambda tuple: tuple[1], reverse=True)

    print("Number of Words: %s" % numberOfWords)
    print("Top 10 Words Occurred in %s" % sys.argv[1])

    count = 1
    for word in orderedPlaceHolder:
        print(str(count) + ". '%s' occurred %s times." % (word[0].capitalize(), word[1]))
        count += 1
