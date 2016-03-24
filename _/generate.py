import os
from argparse import ArgumentParser

def generate_header(path, pages, links):
    content = ''
    with open(os.path.join(path, 'header.start.template.html'), 'r') as header_start_template:
        content += header_start_template.read()
        content += '\n'
    for page in pages:
        with open(os.path.join(path, 'header.page.template.html'), 'r') as page_template:
            content += page_template.read().replace('~~NAME~~', page)
            content += '\n'
    for link in links:
        with open(os.path.join(path, 'header.link.template.html'), 'r') as link_template:
            content += link_template.read().replace('~~NAME~~', link[0]).replace('~~LINK~~', link[1])
        content += '\n'
    with open(os.path.join(path, 'header.end.template.html'), 'r') as header_end_template:
        content += header_end_template.read()
        content += '\n'
    return content


def generate_footer(path):
    with open(os.path.join(path, 'footer.template.html'), 'r') as footer_template:
        return footer_template.read() + '\n'


def generate_page(path, page):
    try:
        with open(os.path.join(path, "{}.content.html".format(page)), 'r') as page_template:
            return page_template.read()
    except Exception:
        return ''


def main(args, pages, links):
    for page in pages:
        with open(os.path.join(args.build_path, "{}.html".format(page)), 'w') as page_content:
            page_content.write(generate_header(os.path.join(args.path, 'templates'), pages, links))
            page_content.write(generate_page(os.path.join(args.path, 'content'), page))
            page_content.write(generate_footer(os.path.join(args.path, 'templates')))


if __name__ == '__main__':
    root = os.path.dirname(os.path.realpath(__file__))
    parser = ArgumentParser(description='generates a super awesome boring website')
    parser.add_argument('--path', default=root, help='name of the band')
    parser.add_argument('--build-path', default='..', help='where to put the website')
    pages = ('index', 'about', 'weather')
    links = zip(('hiking', 'music', 'linkedin', 'github', 'stackoverflow'),
                ('http://hiking.tonygaetani.com',
                 'http://music.tonygaetani.com',
                 'https://de.linkedin.com/pub/tony-gaetani/93/b6b/970',
                 'https://github.com/tonygaetani',
                 'https://stackoverflow.com/users/664594/tonyg',))
    main(parser.parse_args(), pages, links)
