import sys, urllib
from pymd5 import md5, padding

# Command: python sol_3.2.1.2.py 3.2.1.2_query.txt 3.2.1.2_command3.txt sol_3.2.1.2.txt

if len(sys.argv) < 4:
    print("Missing arguments: python your_script.py query_file command3_file output_file")

with open(sys.argv[1]) as query, open(sys.argv[2]) as command, open(sys.argv[3], 'w') as out:
	query_content = query.read().strip()
	command_content = command.read().strip()
	token_str = (query_content.split("&")[0]).split("=")[1]
	user_str = "user=" + query_content.split("user=")[1]

	new_token = md5(state=token_str.decode("hex"), count=512)
	new_token.update(command_content)
	out.write("token=" + new_token.hexdigest() + '&' + user_str + urllib.quote(padding(len(user_str*8) + 8*8)) + command_content)

	# test = "password" + "user=admin&command1=ListFiles&command2=NoOp"
	# h = md5()
	# h.update(test)
	# print("Test: " + h.hexdigest())
	#
	# h1 = md5()
	# h1.update(test + padding(len(user_str*8) + 8*8) + command_content)
	# print("Test: " + h1.hexdigest())
	#
	# h2 = md5(state=h.hexdigest().decode("hex"), count=512)
	# h2.update(command_content)
	# print("Test: " + h2.hexdigest())
