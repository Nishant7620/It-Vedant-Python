nested_di = {"a":1,"b":2,"c":3,"d":4,"e":{"peter":"spiderman","tony":"ironman"}}

print(nested_di)

print(nested_di["a"])

print(nested_di["e"])

print(nested_di["e"]["peter"])

nested_di["e"]["peter"] = "Spider-Man"

print(nested_di)

