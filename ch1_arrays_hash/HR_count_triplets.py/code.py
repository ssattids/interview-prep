# %%
from collections import defaultdict

# Complete the countTriplets function below.
def countTriplets(arr, r):
    v2 = {}
    v3 = {}
    count = 0

    for value in arr:
        print("=====================================")
        print("=====================================")
        print(f"Looping...")
        print(f"value: {value}")
        print(f"v3_before_count: {v3}")
        if value not in v3:
            v3[value] = 0
        count += v3[value]
        print(f"v3_after_count: {v3}")
        print(f"count: {count}")
        print("=====================================")
        print(f"v2_before: {v2}")
        print(f"v3_before: {v3}")
        if value not in v2:
            v2[value] = 0
        if value*r not in v3:
            v3[value*r] = 0
        v3[value*r] += v2[value]
        print(f"v2_after: {v2}")
        print(f"v3_after: {v3}")
        print("=====================================")
        print(f"v2_before: {v2}")
        if value*r not in v2:
            v2[value*r] = 0
        v2[value*r] += 1
        print(f"v2_after: {v2}")
        print(f"v2[value*r]: {v2[value*r]}")
    return count

countTriplets([1,3,9,9,27,81],3)
# %%
