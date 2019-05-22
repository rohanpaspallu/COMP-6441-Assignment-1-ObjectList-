import random
class stringDatabase:
    w_lis = []
    def readfile(self):
        """
        Used to read a file from the f
        :return:
        """
        file = open("four_letters.txt", "r")
        if file.mode == 'r':
            for x in file:
                self.w_lis.extend(x.split())
        self.current_word = random.choice(self.w_lis)
        # #print(self.current_word)
        return self.current_word
