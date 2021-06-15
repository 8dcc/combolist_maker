#  Made by r4v10l1 (ch0colate)
#  https://github.com/r4v10l1

import os

try:
	string_hash = input(" String:hash file: ")
	hash_pass = input(" Hash:text file: ")
except KeyboardInterrupt:
	print()
	print(" [!] Detected Ctrl+C. Exiting...")
	exit(1)

hash_dict = {}

def make_dict():
	with open(hash_pass, "r") as file4dict:
		while True:
			line1 = file4dict.readline()
			if not line1:
				break
			hash_from_file = line1.split(":")[0]
			text_from_file = line1.split(":")[1].strip()
			hash_dict[hash_from_file] = text_from_file

def main():
	make_dict()
	with open(string_hash, "rt", encoding="utf8") as string_hash_reader:
		while True:
			line2 = string_hash_reader.readline()
			if not line2:
				break
			hash_from_file2 = line2.split(":")[1]
			if hash_from_file2 in hash_dict:
				replaced_line = line2.replace(hash_from_file2, hash_dict[hash_from_file2])
				with open("temp.txt", "at", encoding="utf8") as result_file_new:
					result_file_new.write(replaced_line)
	print(" [+] Done! Removing empty lines...")
	# with open("temp.txt") as infile, open("results.txt", 'w') as outfile:
	# 	for line in infile:
	# 		if not line.strip(): continue
	# 		outfile.write(line)
	print(" [+] All done!")

main()
