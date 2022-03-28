from flask import Flask, url_for, render_template, request
import string
import random

app = Flask(__webapp__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)



@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    length = int(request.args['#ofslots'])
    letters_count = int(request.args['letter-count'])
    digits_count = int(request.args['digit-count'])
    special_characters_count = int(request.args['special-character-count'])


letters = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():


	characters_count = letters_count + digits_count + special_characters_count


	if characters_count > length:
		print("Characters total count is greater than the password length")
		return

	password = []

	for i in range(letters_count):
		password.append(random.choice(letters))

	for i in range(digits_count):
		password.append(random.choice(digits))

	for i in range(special_characters_count):
		password.append(random.choice(special_characters))

	if characters_count < length:
		random.shuffle(characters)
		for i in range(length - characters_count):
			password.append(random.choice(characters))

	random.shuffle(password)

	print("".join(password))

generate_random_password()

return render_template('response.html', Password = password)

if __name__=="__webapp__":
    app.run(debug=False)
