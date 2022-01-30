#ping /n 1 google.com
try:
    import subprocess
    from win10toast import ToastNotifier
except:
    print("one of the required modules is missing")
    yn = input('would you like us to try to install them (Y/n)? ')
    if yn == ("y"):
        import os 
        os.system('pip install subprocess')
        os.system('pip insatll win10toast')
    elif yn == ('n'):
        print('ok please install those programs yourself, otherwise this program will not work. (win10toast and subprocess) now exiting program')
        exit()
    else:
        if yn == ('Y'):
            import os 
            os.system('pip install subprocess')
            os.system('pip insatll win10toast')
        elif yn == ("N"):
            print('ok please install those programs yourself, otherwise this program will not work. (win10toast and subprocess) now exiting program')
            exit()
var = int(0)
varforuse = int(0)
def notification(top, content, duration):
    toaster = ToastNotifier()
    toaster.show_toast(top, content, threaded=True,
                   icon_path=None, duration=duration)
while True:
    try:
        print(subprocess.check_output(['ping', '/n 1', 'google.com']))
        varforuse = (varforuse + 1)
        if varforuse == (10000):
            varforuse = (0)
            toaster = ToastNotifier()
            toaster.show_toast("YAY", 'You\'ve been connected for 10000 pings! congrats!', threaded=True,
                        icon_path=None, duration=5)
    except subprocess.CalledProcessError as err:
        print(err)
#       notification('You\'re disconnected', 'You\'re disconnected!', '5')
        var = (var + 1)
        if var > 5:
            toaster = ToastNotifier()
            toaster.show_toast("You're disconnected", 'You are disconnected from the web', threaded=True,
                        icon_path=None, duration=5)
        else:
            toaster = ToastNotifier()
            toaster.show_toast("Unstable", 'Your internet might be unstable or you might be disconnected.', threaded=True,
                        icon_path=None, duration=1)
