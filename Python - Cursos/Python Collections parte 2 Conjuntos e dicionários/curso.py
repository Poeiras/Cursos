usuarios_data = [15, 23, 43, 56]
usuarios_machine = [13, 23, 56, 42]

assistiram = usuarios_data.copy()
assistiram.extend(usuarios_machine)


print(set(assistiram))
print(type(assistiram))
