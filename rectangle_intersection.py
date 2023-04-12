import collections
Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))

def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    no_intersection_conditions = [
        r1.x >= r2.x + r2.width,
        r2.x >= r1.x + r1.width,
        r1.y >= r2.y + r2.height,
        r2.y >= r1.y + r1.height
    ]
    assert not any(no_intersection_conditions), "Intersection rectangle does not exist"
    r1_x1 = r1.x + r1.width
    r1_y1 = r1.y + r1.height
    r2_x1 = r2.x + r2.width
    r2_y1 = r2.y + r2.height

    # find coordinates of intersection rectangle r3
    r3_x = max(r1.x, r2.x)
    r3_y = max(r1.y, r2.y)
    r3_x1 = min(r1_x1, r2_x1)
    r3_y1 = min(r1_y1, r2_y1)
    r3_width = abs(r3_x-r3_x1)
    r3_height = abs(r3_y - r3_y1)

    return Rect(x=r3_x, y=r3_y, width=r3_width, height=r3_height)





if __name__ == '__main__':
    # r1 = Rect(x=2, y=2, width=2, height=2)
    # r2 = Rect(x=6, y=6, width=2, height=2)

    r1 = Rect(x=1, y=2, width=3, height=2)
    r2 = Rect(x=3, y=2, width=1, height=2)
    print(intersect_rectangle(r1, r2))