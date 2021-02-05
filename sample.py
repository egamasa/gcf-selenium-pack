from lib.driver import Driver


def handler(event={}, context={}):
    Driver.setup(event)

    d1 = Driver.new()
    d2 = Driver.new()

    d1.get('https://en.wikipedia.org/wiki/Special:Random')
    d2.get('https://ja.wikipedia.org/wiki/Special:Random')
    titleEn = d1.find_element_by_class_name('firstHeading').text
    titleJa = d2.find_element_by_class_name('firstHeading').text
    print(titleEn)
    print(titleJa)
    d1.quit()
    d2.quit()
    return titleEn, titleJa


if __name__ == '__main__':
    handler()
