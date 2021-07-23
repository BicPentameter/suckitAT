import keyboard
import time

should_run_main_loop = True
dotdashthreshhold = 0.3
endchartime = 1.5
shorttermstring = ""
longtermstring = ""
instant = 0
letter = ""

a = ["a", ".-"]
b = ["b","-..."]
c = ["c","-.-."]
d = ["d","-.."]# = ""
e = ["e","."]# = "."
f = ["f","..-."]# = "..-."
g = ["g","--."]# = "--."
h = ["h","...."]# = "...."
i = ["i",".."]# = ".."
j = ["j",".---"]# = ".---"
k = ["k","-.-"]# = "-.-"
l = ["l",".-.."]# = ".-.."
m = ["m","--"]# = "--"
n = ["n","-."]# = "-."
o = ["o","---"]# = "---"
p = ["p",".--."]# = ".--."
q = ["q","--.-"]# = "--.-"
r = ["r",".-."]# = ".-."
s = ["s","..."]# = "..."
t = ["t","-"]# = "-"
u = ["u","..-"]# = "..-"
v = ["v","...-"]# = "...-"
w = ["w",".--"]# = ".--"
x = ["x","-..-"]# = "-..-"
y = ["y","-.--"]# = "-.--"
z = ["z","--.."]# = "--.."

entirelist = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]


print("Welcome to the morse code translator, courtesy of Henry Swan Corporation! \n")
print("use SPACEBAR to input morse code! \n")
print("at any time you can close the program by hitting 'esc' \n")

print("press 'P' to prepare the program! \n")
keyboard.wait("p")
print("now you're almost ready! press 'b' to load up space detector \n")
keyboard.wait("b")
print("so close! press 'v' to start \n")
keyboard.wait('v')
print("an error has occured, please try again in one second \n")
keyboard.wait('V')
print("press 'd' to reset startup procedure \n")
keyboard.wait('d')
print("press 'P' to prepare the program! \n")
keyboard.wait("p")
print("now you're almost ready! press 'b' to load up space detector \n")
keyboard.wait("b")
print("so close! press 'v' to start \n")
keyboard.wait('v')



print("aedan had the idea to run a calibration before you start, so i decided to rip him off. press spacebar for the length of a . \n")
keyboard.wait('space')
instant = time.time()
while keyboard.is_pressed('space'):
    time.sleep(.000001)
length = time.time() - instant
ultimateunit = length

endchartime = 3 * ultimateunit
dotdashthreshhold = 3 * ultimateunit



print("now you're started, as soon as you press spacebar the morse detection will begin \n")



keyboard.wait("space")
instant = time.time()

while True:  # making a loop
    while keyboard.is_pressed("space"):
        time.sleep(.001)
        #space is released
    
    #counts the amount of time since the last snap
    length = time.time() - instant
    if length < dotdashthreshhold:
        shorttermstring += "."
    else:
        shorttermstring += "-"
    print(shorttermstring)
    instant = time.time()

    keyboard.wait('space')

    if keyboard.is_pressed("space"):
        #counts the amount of time since the last snap
        length = time.time() - instant
        if length > endchartime:
            x = None
            for x in entirelist:
                if x[1] == shorttermstring:
                    letter = x[0]
                    break
            longtermstring += letter + " "
            print(longtermstring)
            shorttermstring = ""
            letter = ""
        instant = time.time()
