def generate_pascal(rows):
    res = [[1]]
    for _ in range(1, rows):
        prev_upper_row = [0] + res[-1] + [0]
        current_row = []
        left_p = 0
        right_p = left_p + 1
        while right_p < len(prev_upper_row):
            current_row.append(prev_upper_row[left_p] +  prev_upper_row[right_p])
            left_p += 1
            right_p = left_p + 1
        res.append(current_row)
    return res

if __name__ == '__main__':
    print(generate_pascal(5))