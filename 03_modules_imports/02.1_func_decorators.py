def mi_decorador(func):
    def abrazador(*args, **kwargs):
        print("Antes de la llamada a la funcion original")
        result = func(*args, **kwargs)  # llama a la funcion original
        print("Despues")
        return result

    return abrazador


@mi_decorador
def hola_fulano(name):
    print(f"Hola, {name}!")


# Mejor usar decoradores en lugar de:
# def hola_fulano(name):
#    print(f"Hola, {name}!")

# hola_fulano = mi_decorador(say_hello)

if __name__ == "main":
    hola_fulano("Alice")
