
# Append
app = []
app.append(1)
app.append(2)
app.append(3)
aLen = len(app)
print('append 1, 2, 3 to list = ', app, 'Length', aLen) 

# Insert
ext = [4,5,6]
ext.insert(4, 12)
ext.insert(2,18)
print('Insert 12 at idx 4, 18 at idx 2 =', ext)

# Remove
ext.remove(18)
print('Remove 18 = ', ext)

# Pop
ext.pop(0)
print('pop at idx 0', ext)

# Clear
ext.clear()
print('Clear ext', ext)

# Index; Returns index of specified value
print('index at 1 =', app.index(1), app)

# Count
print('Count of value 1', app.count(1))

# Sort
srt = [1,3,5,2,8,4]
srt2 = ['a', 'c', 'e', 'b']
srt.sort()
srt2.sort()
print('Sort letters and numbers lists', srt, srt2)

# Reverse
srt.reverse()
srt2.reverse()
print('String and num list reversal', srt, srt2)

# Copy
srtCop = srt.copy()
print('Copy', srtCop)





