import eel

@eel.expose
def sendPosition(pos):
    print(pos)

if __name__ == '__main__':
    eel.init('view')
    eel.start('index.html', port=8005)