# Wordsly - Wordle Clone

## Pseudocode
* [x] generate random, common, 5-letter word for answer
* get 5-letter word for user
* display typing in real time
* check if user's word matches generated word
    * if so, tell them they're a winner, make all letters green, and maybe we can try confetti animation later lol
* check if user's word is a real word 
* if (userWord != generatedWord && isRealWord == True), then
    * check if any letters of user's word are in the generated word,
        * for all letter(s) that are in the word:
            * check that they are in the correct location(s),
                * if not in the correct locations -> make letter background yellow
                * if letter(s) in the correct location -> make letter background green
        * for all letter(s) not in the generated word, make them grey
    * repeat this five time(s), awaiting user entry before starting the block
* if user doesn't get it in five turns
    * that's too bad, make the final letters red, tell them the words, maybe a flames animation later lol
* List of Common 5 Letter Words: [Credit: charlesreidi on Github](https://github.com/charlesreid1/five-letter-words/blob/master/sgb-words.txt)


## Stack 
* Flask - backend, API
* HTML, CSS, & Vanilla JavaScript - frontend, animations (in the future)

## Fancy Features to Try
* try switching to React?
* show letters already chosen
* confetti animation for winners
* fire animation for losers
* tell the user the definition of the generated word at the end of the game
    * set up API requests to dictionary API for this