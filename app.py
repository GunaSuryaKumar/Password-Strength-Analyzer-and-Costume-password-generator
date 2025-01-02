from flask import Flask, render_template, request

import re
import math
import random
import string
import enchant
import secrets
import hashlib
import requests
import nltk

nltk.download('words')
capitals_length=0
smalls_length=0
special_chars_length=0
numbers_length=0

app = Flask(__name__)

@app.route('/')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    user_name = request.form.get('username')
    password = request.form.get('password')
    check_username(user_name)
    check_password(user_name, password)
    entropy_strength = Entropy_calculation(password)
    leaked = leaked_db_check(password)
    diction = Dictionary_vulnerability(password)
    overall = check_strength(password)
    return render_template('password_report.html', user_name=user_name, password=password, entropy_strength=entropy_strength, leaked=leaked, diction=diction, overall=overall)

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    fcolor = request.form.get('color')
    factor = request.form.get('actor')
    fsch_name = request.form.get('school')
    if fcolor is None or factor is None or fsch_name is None:
        output = ""
        return render_template('last.html', output=output)
    else:
        output = generate_password(fcolor, factor, fsch_name)
        return render_template('last.html', output=output)

def check_username(user_name):
    if user_name is None or len(user_name)<5:
        return "username must contain at least 5 characters"

def check_similarity(username, password):
    if password is None:
        return "password is required"
    for i in range(len(password)-3):
        for j in range(len(password)-3):
            if username[i:i+4]==password[j:j+4]:
                return "There should be no username in password"

def check_length(password):
    if len(password)<12 or len(password)>25:
        return "Password length should be between 12 and 25"

def numbers_check(password):
    number_pattern=re.compile('[0-9]')
    numbers=number_pattern.findall(password)
    number_count=len(numbers)
    if number_count<1:
        return "The password must contain at least one numerical character"

def special_chararcter_check(password):
    special_pattern=re.compile(r'[^A-Za-z0-9]')
    special_chars=special_pattern.findall(password)
    special_chars_count=len(special_chars)
    if special_chars_count<1:
        return "The password must contain at least one special character"

def small_check(password):
    lower_count=sum(1 for i in list(password) if i.islower())
    if lower_count<1:
        return "The password must contain at least one lowercase letter"

def capital_check(password):
    upper_count=sum(1 for i in list(password) if i.isupper())
    if upper_count<1:
        return "The password must contain at least one capital case letter"

def check_password(username, password):
    checkers = [check_similarity, check_length, numbers_check, special_chararcter_check, small_check, capital_check]
    for checker in checkers:
        error = checker(username, password) if checker == check_similarity else checker(password)
        if error:
            return error

def Entropy_calculation(password):
# Define the character sets
    capitals = string.ascii_uppercase
    smalls = string.ascii_lowercase
    special_chars = string.punctuation
    numbers = string.digits
# Determine the size of the character set used in the password
    character_set_size = 0
    if any(c in capitals for c in password):
        character_set_size += len(capitals)
    if any(c in smalls for c in password):
        character_set_size += len(smalls)
    if any(c in special_chars for c in password):
        character_set_size += len(special_chars)
    if any(c in numbers for c in password):
        character_set_size += len(numbers)
# Calculate entropy
    if character_set_size == 0:
        return 0  
# To handle the case where password is empty or has no valid characters
    password_length = len(password)
    entropy_per_bit = math.log2(character_set_size)
    total_entropy = password_length * entropy_per_bit
# Define the maximum entropy for a typical 32-character password using all printable ASCII characters
    max_entropy = 32 * math.log2(len(string.printable))
# Calculate entropy percentage
    entropy_percentage = (total_entropy / max_entropy) * 100
    return entropy_percentage

def leaked_db_check(password):
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    if response.status_code == 200:
        hashes = (line.split(":") for line in response.text.splitlines())
        for h, _ in hashes:
            if h == suffix:
                return True
        return False
    else:
        return False
    
def Dictionary_vulnerability(password):
    dictionary_vulnerability_meter = 0
# Load NLTK words corpus
    words = set(nltk.corpus.words.words())
# Check if each word in the password is in the dictionary
    for word in re.split(r"[^a-zA-Z0-9]+", password):
        if len(word) >= 3 and word.lower() in words:
            dictionary_vulnerability_meter += 1
# Define patterns for common keyboard patterns
    patterns = [
        r"(?:[a-z]{3,})",
        r"(?:[A-Z]{3,})",
        r"(?:[0-9]{3,})",
        r"(?:[^a-zA-Z0-9]{3,})",
        r"(?:qwertyuiop)",
        r"(?:asdfghjkl;)",
        r"(?:zxcvbnm,.<>/?)+"
    ]
# Check if any patterns are found in the password
    for pattern in patterns:
        if re.search(pattern, password):
            dictionary_vulnerability_meter += 0.5
# Calculate vulnerability percentage
    dictionary_vulnerability_percentage = (dictionary_vulnerability_meter * 100) / (len(password) + len(patterns)) 
    return dictionary_vulnerability_percentage

def check_strength(password):
    return 0.5*(100-Dictionary_vulnerability(password)+Entropy_calculation(password))

def generate_password(fcolor, factor, fsch_name):
    special_characters = string.punctuation
    password_list = list(fcolor + factor + fsch_name + secrets.token_hex(4))
    length = len(password_list)
    random_positions = random.sample(range(5, length), min(3, length - 5))
    for i in random_positions:
        password_list.insert(i, random.choice(special_characters))
    new_password = ''.join(remove_duplicates(password_list))
    strength = check_strength(new_password)
    return new_password

def remove_duplicates(lst):
    seen = set()
    seen_add = seen.add
    return [x for x in lst if not (x in seen or seen_add(x))]

if __name__ == '__main__':
    app.run(debug=True, port=5000)