import pickle
from stringDatabase import stringDatabase

from game import game



class guess:
    a= stringDatabase()
    word = a.readfile()
    game_list = []
    init_word = '----'
    guess_word = ''
    guess_letter = ''
    word_list = []
    no =0
    countGuess = 0
    countLetter = 0
    score = 0
    totalLetter = 0
    totalGuess = 0
    final_list = []
    finalle = []
    wo_list  = []
    unknownLetter = []

    dict = {'a':8.17,'b':1.49,'c':2.78,'d':4.25,'e':12.70,'f':2.23,'g':2.02,'h':6.09,'i':6.97,'j':0.15,'k':0.77,'l':4.03,'m':2.41,'n':6.75,'o':7.51,'p':1.93,'q':0.10,'r':5.99,'s':6.33,'t':9.06,'u':2.76,'v':0.98,'w':2.36,'x':0.15,'y':1.97,'z':0.07 }

    # def __init__(self):
    #     self.word = self.a.readfile()

    def calling(self):
        """
        This is the main calling function of the guess class wherein the entire logic resides and the game is played over here
        Moreover it is the entry point of the code
        It performs operation of guess word , guess letter , tell me (give up) and quit game where it provides you with the table

        """
        #self.word = self.a.readfile()
        #print(self.word)
        command = input("g = guess, t = tell me, l for a letter, and q to quit : ")
        gequals = "g"
        tequals = "t"
        lequals = "l"
        qequals = "q"
        if command == gequals:
            self.guess_word = input()
            self.final_list.append(self.guessing_word(self.word, self.guess_word))
            #print(self.final_list)
            #self.countLetter = 0
            #self.countGuess = 0
            self.calling()
        elif command == tequals:
            self.final_list.append(self.tell_me(self.word))
            #print(self.final_list)
            self.calling()
        elif command == lequals:
            self.guess_letter = input()
            self.final_list.append(self.guessing_letter(self.word, self.guess_letter))
            #print(self.final_list)
            #self.countLetter = 0
            #self.countGuess = 0
            self.calling()
        elif command == qequals:
            z = 0
            self.finalle = list(filter(None.__ne__, self.final_list))
            #print(self.finalle)
            #return self.finalle
            # print(self.final_list)
            # return self.final_list
            print("game\tword\tstatus\t Bad Guesses\tMissed Letters\tscore")
            print("----\t----\t------\t -----------\t--------------\t-----")


            for p in self.game_list:
                print ("%s       %s    %s  %s              %s               %s " % (p.game, p.word, p.status, p.guess, p.letter, p.score))
        else:
            print("wrong input, enter again")
            self.calling()

    def guessing_word(self, w, gw):
        """
        This function is used to check whether the given word is equal to the random word generated and calculate the scores accordingly
        :param w: the current random word selected by the random library
        :param gw: the word which the user guesses
        """
        if (w == gw):
            i = 0
            wordCheck = list(w)
            while i <len(self.init_word):
                if(w[i]!=self.init_word[i]):
                    self.score = self.score + self.dict.get(w[i])
                i = i + 1

            print("this is true, you are a scholar")
            self.no = self.no + 1
            self.totalGuess = self.totalGuess + 1
            self.score = self.score / self.totalGuess
            i = 0
            while i <= self.countGuess:
                self.score = self.score * 0.9
                i = i + 1
            #print(self.score)
            self.word_list = [self.no, w, 'success', self.countGuess, self.countLetter, self.score]


            self.game_list.append(game(self.no, w, 'success', self.countGuess, self.countLetter, self.score))
            self.init_word = '----'
            self.score = 0
            self.totalGuess = 0
            self.totalLetter = 0
            self.countGuess = 0
            self.countLetter = 0
            self.unknownLetter = []
            self.word = self.a.readfile()
            #self.countGuess = 0
            #self.countLetter = 0
            #return self.word_list

        else:
            print("wrong")
            self.totalGuess = self.totalGuess + 1
            self.countGuess = self.countGuess + 1

    def guessing_letter(self, w, gl):
        """
        This function is used to check whether the given letter is equal is contained in the random word and checks whether the exact word is retreived and calculate the scores accordingly
        :param w: the current random word selected by the random library
        :param gl: the letter which the user guesses
        """
        w_len = len(self.init_word)
        x = 0
        i = 0
        self.wo_list = list(self.init_word)
        if gl in w:
            self.totalLetter = self.totalLetter + 1
            while x < w_len:
                if w[x] == gl:
                    #index = cw.index(gl)
                    #print(index)
                    self.wo_list[x] = gl
                    self.init_word = ''.join(self.wo_list)
                #else:
                    #self.countLetter = self.countLetter + 1
                x = x + 1
            self.init_word = ''.join(self.wo_list)
            print(self.init_word)
            if (self.init_word != w):
                self.calling()
            else:
                print("great you are a scholar")
                self.no = self.no + 1
                while i < w_len:
                    self.score = self.score + self.dict.get(self.wo_list[i])
                    i = i+1
                self.score = self.score / self.totalLetter
                i = 0
                while i <= self.countLetter:
                    self.score = self.score * 0.9
                    i = i+1
                self.word_list = [self.no, w, 'success', self.countGuess, self.countLetter, self.score]


                self.game_list.append(game(self.no, w, 'success', self.countGuess, self.countLetter, self.score))
                self.init_word = '----'
                self.unknownLetter = []
                self.countLetter = 0
                self.countGuess = 0
                self.totalLetter = 0
                self.totalGuess = 0
                self.score = 0
                #self.score = self.score + 1
                self.word = self.a.readfile()
                #return self.word_list

        else:
            print("try again")
            print(self.init_word)
        self.totalLetter = self.totalLetter + 1
        self.countLetter = self.countLetter + 1
        #print("number of wrong letters: ", self.countLetter)
        self.calling()

    def tell_me(self,w):
        """
        This function is used when the user can't guess the word and he wants to give up the chance. Here the word is displayed and the user is scored negative in the end
        :param w: the current random word selected by the random library
        """
        print("the word is : ", w)
        self.no = self.no + 1
        i = 0
        wordCheck = list(w)
        while i < len(self.init_word):
            if (w[i] != self.init_word[i]):
                self.score = self.score - self.dict.get(w[i])
            i = i + 1

        self.word_list = [self.no, w, 'Gave up', self.countGuess, self.countLetter, self.score]
        self.countGuess = 0
        self.countLetter = 0

        self.game_list.append(game(self.no, w, 'success', self.countGuess, self.countLetter, self.score))
        self.word = self.a.readfile()
        #return self.word_list


print("** The great guessing game **")

stringDatabaseObject = stringDatabase()
guessObject =guess()
#gameObject = game()
stringDatabaseObject.readfile()
guessObject.calling()
#gameObject.finalPrint()
#sys.exit()
