longest_sequence = []
sequence = []
a = 2
while a<=1000000:
    b = a
    sequence.append(b) 
    while b>1:
        if b%2==0:
            b /= 2
        else:
            b = 3*b+1
        sequence.append(b) 
    if len(sequence)>len(longest_sequence):
        longest_sequence.clear()
        for i in sequence:
            longest_sequence.append(i)
    sequence.clear()
    a += 1
print(longest_sequence[0])