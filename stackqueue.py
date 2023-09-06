# stack -> LIFO
stack = []

for i in range(1,11):
    stack.append(i)
    
def stack_pop():
    global stack
    if len(stack) > 0:
        return stack.pop()
    else:
        return None
    
print(f"{len(stack)}개의 데이터가 저장되어 있습니다.")

#queue -> FIFO
#      -> 양방향
queue = []

for i in range(1,11):
    queue.insert(0,i)
    
print(f"{len(queue)}개의 데이터가 저장되어 있습니다.")

for i in range(1,11):
    print(queue.pop())