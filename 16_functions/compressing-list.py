def rle(chars):
    result = []
    prev = chars[0]
    count = 1

    for ch in chars[1:]:
        if(ch == prev):
            count += 1
        else:
            result.append((prev, count))
            prev = ch
            count = 1
            

