#!/usr/bin/env python
var1 = 0
var2 = []
input_number = None
while input_number != "":
    input_number = raw_input()
    if input_number.isdigit():
        var2.append(float(var3))
for var in var2:
    var1+=var
print var1/len(var2)
