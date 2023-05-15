num_tests = int(input())

for x in range(num_tests):
    disp_mask_cost, cloth_mask = map(int, input().split())
    disp_total = disp_mask_cost * 100
    cloth_total = cloth_mask * 10
    if disp_total < cloth_total:
        print("Disposable")
    elif cloth_total < disp_total:
        print("Cloth")
    elif cloth_total == disp_total:
        print("Cloth")
    else:
        print("Error")