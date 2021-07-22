import os

# fetch words from text file
def get_words(file_path):
    with open(file_path, 'r') as f:
        text = f.readlines()[0]
        words = text.split()
    return words

def get_lines(file_path):
    with open(file_path, 'r') as f:
        text = f.readlines()
    return text

def send_message(phone_number, message):
    os.system('osascript send.scpt {} "{}"'.format(phone_number, message))

if __name__ == '__main__':
    target_phone_number = ''
    words = get_words('toSend.txt')
    
    # for word in words:
    #         send_message(target_phone_number, word) #{phone number, text message}

    message = ""
    for i in range(5):
        send_message(target_phone_number, message) #{phone number, text message}