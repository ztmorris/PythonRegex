import re


def regextest(value):
    typeofdata = 'string'

    datatyperegex = [
        # This works for 23, 233454, 1, -17
        {'int': re.compile(r'^-*[0-9]*$')},
        # This works for '06/12/2004'
        {'date': re.compile(r'^\d{1,2}[/]\d{1,2}[/]\d{2,4}$')},
        # This works for '07/34/2011 12:32:34'
        {'datetime': re.compile(r'^\d{1,2}[/]\d{1,2}[/]\d{2,4} \d{1,2}[:]\d{2}[:]\d{2}$')},
        # This works for '07/34/2011 12:32:34 pm', '07/34/2011 12:32:34 Am', '07/34/2011 12:32:34 AM', '07/34/2011 12:32:34 PM'
        {'datetime_ampm': re.compile(r'^\d{1,2}[/]\d{1,2}[/]\d{2,4} \d{1,2}[:]\d{2}[:]\d{2} [ap][m]$', flags=re.I)},
        # This works for: 'true','faLSe','NO','T','N'
        {'bool': re.compile(r'^t$|^f$|^true$|^false$|^y$|^n$|^yes$|^no$', flags=re.I)},
        # This works for 45.23, 65465.7564, 654., .876776
        {'float': re.compile(r'^[0-9]*[.][0-9]*$')},
        # This works for 2021-07-28T00:00:00.000+00:00
        {'datetime_mongo': re.compile(
            r'^[0-9]{4}[-][0-9]{2}[-][0-9]{2}[T][0-9]{2}[:][0-9]{2}[:][0-9]{2}[.][0]{3}[+][0]{2}[:][0]{2}$')}
    ]

    for datatype in datatyperegex:
        for d in datatype:
            if datatype[d].search(value):
                if d.split('_')[0] == 'datetime':
                    typeofdata = 'datetime'
                else:
                    typeofdata = d

    return typeofdata


if __name__ == '__main__':

    teststuff = ['uyu',
                 '23',
                 '232454',
                 'fdvfbg',
                 'dfgdfg43534',
                 '45.23',
                 'o08uhg',
                 '1',
                 'faLSe',
                 '-17',
                 '06/12/2004',
                 '07/34/2011 12:32:34 PM',
                 'true',
                 'NO',
                 'T',
                 'N',
                 '65465.7564',
                 '654.',
                 '.876776',
                 '2021-07-28T00:00:00.000+00:00'
                 ]

    for tc in teststuff:
        result = regextest(tc)
        if result:
            print(tc + ' - ' + result)
