# This version we are trying file functions using "with" structure to make sure our files are being opened and closed

# Open file and show its content
print("===== First we will open a single line text file...");

with open("simple-file.txt","r") as file:
	content = file.read();
print(content);

# Using "with" structure we don't need file.close(); command after all file operations


# Lets show a multiple lines text file
print("\n\n===== Now, lets see a multiple line text file...");
with open("text-multiple-lines.txt", "r") as file:
	content = file.read();
print(content);


# Lets print each line separately
print("\n\n===== Great!! Lets try to enumerate lines...");

with open("text-multiple-lines.txt", "r") as file:
	lines = file.readlines();
	
i = 1;
for line in lines:
	print(str(i)+": "+ line);
	i +=1;


# Now we are going to create a new text file with a text prompted to user

print("");
print("");
print("Now we are going to create a new text file with a text prompted to user\n");
filename = input("Set a name for create a text file: ");

newtext = input("What you want to save in this file?");

print("Creating file...");

with open(filename,"w") as newfile:
	print("Writing...");
	newfile.write(newtext);


# Lets add some information
print("Signing file...");
with open(filename, "a") as file:
	file.write("\n==========================\nTHIS FILE WAS VALIDATED BY PYTHON\n")
	file.write("SUCCESS")


# Print file on screen
print("Result file...\n");
with open(filename,"r") as file:
	print(file.read());
# Succeed