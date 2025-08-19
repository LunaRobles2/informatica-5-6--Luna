def main():
    emoji = input("Write a mesage with emoticon: ")
    convert (emoji)

def convert (message):
    message = message.replace (":)" , "😊").replace(":(" , "😟")
    print (message)

main()