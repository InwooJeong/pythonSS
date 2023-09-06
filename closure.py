def counter(init_count=0):
    count = init_count
    def increase(c=1):
        nonlocal count
        count += c
        return count
    return increase

counter = counter(0)
print(counter())
print(counter())
print(counter())
new_counter = counter(100)
print(new_counter)