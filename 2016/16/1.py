def dragon(data):
    mirror = data[::-1]
    mirror = mirror.replace('1', '_')
    mirror = mirror.replace('0', '1')
    mirror = mirror.replace('_', '0')
    return f'{data}0{mirror}'

def check(data):
    result = ''
    for i in range(0, len(data), 2):
        result += '1' if data[i] == data[i + 1] else '0'
    
    if len(result) % 2:
        return result
        
    return check(result)

data = input()
disk_length = 272

while len(data) < disk_length:
    data = dragon(data)
data = data[:disk_length]

checksum = check(data)
print(checksum)
