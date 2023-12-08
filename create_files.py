for i in range(24):
    for j in range(2):
        with open(f"data{i}-{j*30}.txt", 'w') as file:
            file.write("empty")
