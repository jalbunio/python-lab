# Open file and show its content
print("===== First we will open a single line text file...");

file = open("simple-file.txt","r");

content = file.read();
print(content);

file.close();

# Lets show a multiple lines text file
print("\n\n===== Now, lets see a multiple line text file...");
file = open("text-multiple-lines.txt", "r");

content = file.read();
print(content);

file.close();

# Lets print each line separately
print("\n\n===== Great!! Lets try to enumerate lines...");

file = open("text-multiple-lines.txt","r");

lines = file.readlines();
i = 1;
for line in lines:
	print(str(i)+": "+ line);
	i +=1;

file.close();