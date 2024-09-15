# Belajar Keyword Argument List
# keyword argument list menggunakan 2 bintang (**)
# jika kita ingin nambah atau custom parameter kita bisa memanfaatkan keyword argument
def create_html(tag, text, **atribut):
    html = f'<{tag}> '

    for key, value in atribut.items():
        html = html + f"{key}='{value}'"

    html = html + f'{text}</{tag}>'
    return html


html = create_html('p', 'Hallo python', style='paragraf')
print(html)
html = create_html('a', 'ini Link', href='www.google.com', style='link')
print(html)
html = create_html('div', 'ini Div', style='contoh')
print(html)
