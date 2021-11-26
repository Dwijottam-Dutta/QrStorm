from tqdm import tqdm, trange
import qrcode
import time

print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ WELCOME to QRStorm ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
time.sleep(0.5)
print("A program which can create QR Codes for Free in a Minute")
time.sleep(3.5)
print("Loading...")
for i in trange(100):
    time.sleep(0.05)
print("       ")    
startup = input("Enter your Name for Registration: ")
make = input("Enter your Data (Text, Link or Number): ")
filee = input("Enter your File Name, with image extension (.jpg, .png, .svg): ")
print("     ")

print("Your Request is being Processed...")
with open("SERVER.txt", "a") as f:
    f.write("Request from: ")
    f.write(startup)
    f.write(",")
    f.write(" ")
    f.write("QR Code Data: ")
    f.write(make)
    f.write(",")
    f.write(" ")
    f.write("File Name: ")
    f.write(filee)
    f.write(".\n")
for i in trange(10):
    time.sleep(1.5)

qr=qrcode.QRCode(
	version=1,
	box_size=10,
	border=5
	)
qr.add_data(make)   
qr.make(fit=True)
img=qr.make_image(fill="orange",back_color="white")
img.save(filee)
time.sleep(5.1)
print("Your QR Code is Ready !", end='\n\n')
time.sleep(0.2)
print("Thanks for Choosing QRStorm")


# qr=qrcode.QRCode(
# 	version=1,
# 	box_size=10,
# 	border=5

# 	)

# data="hello i am a qrcode"
# qr.add_data(data)
# qr.make(fit=True)
# img=qr.make_image(fill="black",back_color="white")
# img.save("QR_Code.png")
