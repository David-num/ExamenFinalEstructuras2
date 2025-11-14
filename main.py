import json

def custom_hash(data):
    serialized = json.dumps(data, sort_keys=True)
    hash_value = 2166136261
    fnv_prime = 16777619

    for char in serialized.encode('utf-8'):
        hash_value = (hash_value * fnv_prime) ^ char
        hash_value = hash_value & 0xFFFFFFFF

    result = (hash_value % 100) + 1
    return result

def rle_compress(data):
    compressed = []
    for line in data.splitlines():
        if not line:
            continue
        count = 1
        result = []
        for i in range(1, len(line)):
            if line[i] == line[i - 1]:
                count += 1
            else:
                result.append((line[i - 1], count))
                count = 1
        result.append((line[-1], count))
        compressed.append(result)
    return compressed

mensaje = ""
comprecion = ""
while True:
    option = input("Bienbenido al probrama\n" \
    "1. Ingresar mensaje\n" \
    "2. Comprimir mensaje\n" \
    "3. Firmar hash con la clave privada\n" \
    "4. Simular envio\n" \
    "5. Descomprimir y verificar firma\n" \
    "6. Mostrar si el mensaje es autentico o alterado\n" \
    "7. Salir\n" \
    "Seleccione una opción: ")
    if option == "1":
        mensaje = input("Ingrese el mensaje: ")
        hash = custom_hash(mensaje)
        print("La hash del mensaje es el siguiente: ",hash,"\n")
    elif option == "2":
        print("Antes: ",mensaje)
        comprecion = rle_compress(mensaje)
        print("Despues: ",comprecion,"\n")
    elif option == "3":
        pass
    elif option == "4":
        pass
    elif option == "5":
        pass
    elif option == "6":
        pass
    elif option == "7":
        print("Gracias por utilizar el programa")
        break
    else:
        print("Opcion invalida, intente de nuevo\n")