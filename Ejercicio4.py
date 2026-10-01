def organizar_eventos(eventos, descendente=False):
    if descendente:
        return sorted(eventos, key=str.lower, reverse=True)
    else:
        return sorted(eventos, key=str.lower)