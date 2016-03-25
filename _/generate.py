import os
from argparse import ArgumentParser


def generate_header(path):
    with open(os.path.join(path, 'header.template.html'), 'r') as header_start_template:
        return header_start_template.read() + '\n'


def generate_footer(path):
    with open(os.path.join(path, 'footer.template.html'), 'r') as footer_template:
        return footer_template.read() + '\n'


def generate_page(path, page):
    try:
        with open(os.path.join(path, "{}.content.html".format(page)), 'r') as page_template:
            return page_template.read()
    except Exception:
        return ''


def find_pages(path):
    return map(lambda x: x[:x.rfind('.content.html')],
               filter(lambda p: p.endswith('.content.html'), os.listdir(os.path.join(path, 'content'))))


def main(args):
    for page in find_pages(args.path):
        with open(os.path.join(args.build_path, "{}.html".format(page)), 'w') as page_content:
            page_content.write(generate_header(os.path.join(args.path, 'templates')))
            page_content.write(generate_page(os.path.join(args.path, 'content'), page))
            page_content.write(generate_footer(os.path.join(args.path, 'templates')))


if __name__ == '__main__':
    root = os.path.dirname(os.path.realpath(__file__))
    parser = ArgumentParser(description='generates a super awesome boring website')
    parser.add_argument('--path', default=root, help='name of the band')
    parser.add_argument('--build-path', default='..', help='where to put the website')
    main(parser.parse_args())
