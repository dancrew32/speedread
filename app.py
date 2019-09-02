import os
import time
import sys

try:
    filename = sys.argv[1]  # story text file
    speed = int(sys.argv[2])  # words per minute
except IndexError:
    print('Usage: python app.py ./ulysses.txt 200')
    exit(1)

ONE_MINUTE_IN_SECONDS = 60
DELAY_BETWEEN_WORDS = ONE_MINUTE_IN_SECONDS / speed

with open(filename) as f:
    story = f.read()

words = story.replace('\n\n', '\n') \
    .replace('\r\r', '\r') \
    .replace('\n', ' ') \
    .replace('\r', '') \
    .split(' ')
words_len = len(words)
seconds_required = DELAY_BETWEEN_WORDS * words_len
minutes_required = seconds_required / 60
hours_required = minutes_required / 60


print(f"{filename} is {words_len} words long.")
print(f"At {speed} words per minute")
print(f"you'll have {DELAY_BETWEEN_WORDS}s delay between words.")
print(f"It will take {hours_required} hours to complete.")

print('Ready?')
time.sleep(5)

os.system('clear')

print('\n\n\n\n\n')


def run():
    last_word = ''
    for index, word in enumerate(words):
        trimmed_word = word.strip()
        if trimmed_word == '' and last_word == '':
            continue
        rows, columns = os.popen('stty size', 'r').read().split()
        text = trimmed_word.center(int(columns))
        sys.stdout.write(text)
        last_word = trimmed_word
        time.sleep(DELAY_BETWEEN_WORDS)
        sys.stdout.write('\r')
        sys.stdout.flush()


os.system('tput civis')
try:
    run()
except KeyboardInterrupt:
    pass
os.system('tput cnorm')
