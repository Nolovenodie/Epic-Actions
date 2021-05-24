import os

if __name__ == '__main__':
    Email = os.environ["EPIC_EMAIL"]
    Password = os.environ["EPIC_PASSWORD"]
    QmsgToken = os.environ["QMSG_TOKEN"]
    
    print(Email)
