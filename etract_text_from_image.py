from unstructured.partition.image import partition_image

elements = partition_image(filename="/content/nfl-howtounderstand-nutrients.png")

for element in elements:
    print(element.text)
