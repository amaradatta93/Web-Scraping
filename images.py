from utils import get_parser


def get_image_link(url):
    info_soup = get_parser(url)
    for image in info_soup.find_all('a', {'class': 'image'}):
        image_link = 'https://en.wikipedia.org' + image.get('href')
        print(image_link)
