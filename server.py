from flask import Flask, render_template, request

app = Flask(__name__)



@app.route("/")
def homepage():
    word = 'march'
    guessed_word = request.args.get('guess')

    if guessed_word:
        counts = {}
        for letter in word:
            counts[letter] = counts.get(letter, 0) + 1

        #  counts = {'m':1, 'a': 1, 'r': 1, 'c': 1, 'h': 1}
        overlap = 0
        for letter in guessed_word:
            if letter in counts and counts[letter] != 0:
                counts[letter] -= 1
                overlap += 1 
    else:
        overlap = None
    return render_template('gamepage.html', guessed_word=guessed_word, overlap=overlap)


if __name__ == "__main__":
    app.debug = True
    app.run()