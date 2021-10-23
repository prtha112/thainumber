def toThaiNumber(input_number):
    thai_number = ("ศูนย์", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า")
    unit = ("", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน")
    number = input_number
    i = len(number)
    result = ""
    for c in number:
        i -= 1
        print(i)
        if i > 6:
            x = i - 6
        else:
            x = i
        unit_part = unit[x];
        if c == '1' and x == 0:
            thai_part = "เอ็ด";
        elif c == '1' and i == 6:
            thai_part = "เอ็ด";
        elif c == '1' and x == 1:
            thai_part = "";
        elif c == '2' and x == 1:
            thai_part = "ยี่";
        elif c == '0':
            thai_part = "";
            unit_part = "";
        else:
            thai_part = thai_number[int(c)];
            
        strnumber = thai_part + unit_part
        result = result + strnumber    
        # print("Index {}, number {} {} {}".format(x, c, thai_number[int(c)], unit[x]))
        
    return result
    
def coreThai(input_number):
    n = input_number
    arr = n.split('.')
    result = toThaiNumber(arr[0])
    if len(arr) > 1:
        result = result + "จุด" + toThaiNumber(arr[1])
    return result
    
print(coreThai('1244523213041.13'))
