def tag_bloco(texto, classe='success', inline = False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'

def tag_listagem(*itens):
    listagem = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul>{listagem}</ul>'


if __name__ == '__main__':
    print(tag_bloco(tag_listagem('joana','carla','pedro'),'info'))

