t = int(input())

while(t != 0):
    total_apples, boxes = input().split()
    total_apples, boxes = int(total_apples), int(boxes)
    apples = boxes

    candidate1_apples_in_boxes = total_apples//apples
    candidate1_boxes = boxes
    flag = False

    if((total_apples//apples) <= boxes):
        candidate2_apples_in_boxes = apples
        candidate2_boxes = total_apples//apples
        flag = True

    else:
        squared = boxes * boxes
        left_over = total_apples%squared


    if(flag):
        if((candidate2_apples_in_boxes == candidate1_apples_in_boxes) and (candidate2_boxes == candidate1_boxes)):
            print("NO")

        else:
            print("YES")
    else:
        if(left_over != 0):
            print("YES")
        else:
            filler = total_apples//squared
            candidate2_apples_in_boxes = filler*apples
            candidate2_boxes = boxes
            if((candidate2_apples_in_boxes == candidate1_apples_in_boxes) and (candidate2_boxes == candidate1_boxes)):
                print("NO")

            else:
                print("YES")

    t -= 1
