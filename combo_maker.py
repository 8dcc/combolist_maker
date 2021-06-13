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

def main():
	with open(hash_pass, "r") as r:
		for line_old in r:
			hash_from_file = line_old.split(":")[0]
			text_from_file = line_old.split(":")[1]
			with open(string_hash, "rt") as string_hash_reader:
				for string_hash_reader_line in string_hash_reader:
					if hash_from_file in string_hash_reader_line:
						replaced_line = string_hash_reader_line.replace(hash_from_file, text_from_file)
						with open("temp.txt", "a") as result_file_new:
							result_file_new.write(replaced_line)
	print(" [+] Done! Removing empty lines...")
	with open("temp.txt") as infile, open("results.txt", 'w') as outfile:
		for line in infile:
			if not line.strip(): continue
			outfile.write(line)
	print(" [+] All done!")

main()
