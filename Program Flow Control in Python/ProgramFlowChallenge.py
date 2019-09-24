ipAddress = input("Please enter your ip address (including '.'): ")
if ipAddress[-1] != '.':
    ipAddress += '.'

segment = 1
segment_length = 0
# character = ''

for character in ipAddress:
    if character == '.':
        print("segment {} contains {} characters".format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1

# unless final character in string was a . then we haven't printed the last statement
# if character != '.':
#     print("segment {} contains {} characters".format(segment, segment_length))
