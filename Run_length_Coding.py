# Nén ảnh Run-length Coding
def run_length_encoding(input_string):
    encoded_string = ""
    count = 1

    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            encoded_string += input_string[i - 1] + str(count)
            count = 1

    encoded_string += input_string[-1] + str(count)
    return encoded_string


# Đọc đầu vào
input()
input_data = input()


# Thực hiện phép nén dữ liệu Run-Length encoding
output_data = run_length_encoding(input_data)

# In kết quả
print(output_data)
# Input
# AAAABBBCCDAA
# Output
# A4B3C2D1A2