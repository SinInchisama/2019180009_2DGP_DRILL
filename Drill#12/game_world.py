# layer 0 : Background Objects

world = [[],[]]

def add_Object(o,depth):
    world[depth].append(o)
    print('add')

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            del o
    return
    raise ValueError('Trying destroy non existing object')      # 들어있지않은 오브젝트 제거오류를 알려주기위해

def all_objects():
    for layer in  world:
        for o in layer:
            yield o         # yield가 들어간 이 함수는 더이상 함수가 아니고 generate라는 발전기로 취급됨
                            # 나오는 순서대로 넘겨주는 오브젝트가 됨.

def clear():
    for o in all_objects():
        del o
    for layer in world:
        layer.clear()
