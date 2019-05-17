class WordGenerator:
    # def __init__():

    all_english_words = set()
    # letters = "lnoeym"
    # word_len = 4
    def isValid(self, word_to_find, word_len):
        #with particular length
        if len(word_to_find) != word_len:
            return False
        return True
        # return dict_entry[-2] == "e"

    def isMaskValid(self, word, word_mask):
        for i in range(len(word)):
            if word_mask[i] != "_":
                if word_mask[i] != word[i]:
                    return False
        return True
        
    def getCombinations(self, head, tail):
        #print("head ", head, "  tail ", tail)
        results = []
        if len(tail) == 1:
            results.append(head+tail)
            results.append(tail+head)
        else:
            sequencies = self.getCombinations(tail[0], tail[1:])
            #print("head is ", head, " received seqs ", sequencies)
            for seq in sequencies:
                for i in range(len(seq) + 1):
                    #print(i, " - ", seq[:i] + head + seq[i:])
                    results.append(seq[:i] + head + seq[i:])
        return results

    def getPlacements(self, head, tail, group_count):
        print("placements head ", head, "  tail ", tail)

        if group_count > (len(tail) + 1):
            return []

        results = []
        for i in (range(len(tail) + 2 - group_count)):
            results = results + self.getCombinations(head, tail[i:group_count-1 + i])
        return results

    def getGroupsOfPlacements(self, head, tail, group_count):
        results = []
        if len(tail) == 1:
            results.append(head+tail)
        elif len(tail) >= group_count:
            groups = self.getGroupsOfPlacements(tail[0], tail[1:], group_count)
            for group in groups:
                for i in range(len(group)):
                    results.append(group[:i] + head + group[i+1:])
            results = results + groups
        else:
            groups = self.getGroupsOfPlacements(tail[0], tail[1:], group_count)
            for group in groups:
                results.append(head + group)

        list_set = set(results) 
        results = (list(list_set)) 

        print("head ", head, " tail ", tail, "results ", results)
        return results

    def getAllPlacements(self, letters, group_count, word_mask):
        print("word mask is ", word_mask)
        results = []
        if len(letters) > group_count:
            groups = self.getGroupsOfPlacements(letters[0], letters[1:], group_count)
            for group in groups:
                results = results + self.getCombinations(group[0], group[1:])
        elif len(letters) == group_count:
            results = results + self.getCombinations(letters[0], letters[1:])

        print("unfiltered legnth ", len(results))

        #return only unique values
        list_set = set(results) 
        unique_list = (list(list_set)) 

        if len(word_mask) > 0:
            print("word mask is ", word_mask)
            unique_list = [word for word in unique_list if self.isMaskValid(word, word_mask)]

        return unique_list

    def initDictionary(self, file_name):
        print("init dictionary ", len(self.all_english_words))
        if len(self.all_english_words) == 0:
            print("init dictionary read from file")
            file = open(file_name, "r")
            dictionary = file.readlines()
            self.all_english_words = set([word.strip().upper() for word in dictionary])
        print("end init dictionary ", len(self.all_english_words))


    def checkDictionary(self, word_results, file_name, word_len):
        self.initDictionary(file_name)
        return [word for word in word_results if word.upper() in self.all_english_words and self.isValid(word, word_len)]
        #and self.isValid(word, word_len)

    def process(self, letters, word_len):
        all_placements = self.getAllPlacements(letters, word_len, "")
        print("________________________________________________________________________________")
        return self.checkDictionary(all_placements, "words.txt", word_len)

def main():
    print("Start")
    word_generator = WordGenerator()
    words = word_generator.getGroupsOfPlacements("1", "2345", 3)

    print("result len ", len(words))
    for w in words:
        print(w)

if __name__ == '__main__':
    main()    

# getCombinations("1", "2345")
# getPlacements("1", "2345", 3)
# getAllPlacements("12345", 3)
# checkDictionary(["melon", "home", "lemon"], "words.txt")
