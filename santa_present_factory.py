from collections import deque

materials = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())

toys_points = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}
presents = {}

while materials and magic:
    if materials[-1] == 0 and magic[0] == 0:
        materials.pop()
        magic.popleft()
        continue
    if materials[-1] == 0:
        materials.pop()
        continue
    if magic[0] == 0:
        magic.popleft()
        continue

    total_magic = materials[-1] * magic[0]
    if total_magic in toys_points:
        new_present = toys_points[total_magic]
        if new_present not in presents:
            presents[new_present] = 0
        presents[new_present] += 1
        materials.pop()
        magic.popleft()
    elif total_magic < 0:
        result = materials.pop() + magic.popleft()
        materials.append(result)
    else:
        magic.popleft()
        materials[-1] += 15


success = (
    ("Doll" in presents and "Wooden train" in presents) or
    ("Teddy bear" in presents and "Bicycle" in presents)
)

if success:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(materials))}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

for toy in sorted(presents):
    print(f"{toy}: {presents[toy]}")