import requests
import time


class ApiSO:
    def __init__(self):
        self.url = 'https://api.stackexchange.com/2.3/'

    def get_questions(self, page, time_from, pagesize=20):
        try:
            args = f'fromdate={time_from}' \
                   '&order=asc'\
                   '&sort=creation'\
                   '&tagged=Python'\
                   '&site=stackoverflow'\
                  f'&page={page}'\
                  f'&pagesize={pagesize}'
            url = self.url + 'questions?' + args
            req = requests.get(url)
        except Exception as ex:
            return url
        return req


if __name__ == '__main__':
    try:
        from file import time_from
    except Exception:
        time_from = int(time.time()) - 2 * 24 * 60 * 60

    api_stov = ApiSO()
    page_i = page = 1
    questions_json = {'has_more': True}
    try:
        while questions_json['has_more']:
            questions = api_stov.get_questions(page=page, time_from=time_from)
            if questions is not str:  # if not error
                questions_json = questions.json()
                try:
                    print(page_i, '-\\')
                    for item in questions_json['items']:
                        print('->', item['title'])
                        print(item['link'])
                except Exception:
                    print(f'{page} er', questions_json)  # has more
            else:
                print(f'{page_i} er', questions)
            page_i += 1
            page += 1
            if page == 26:
                time_from = questions_json['items'][-1]['creation_date']+1
                page = 1
    except Exception as ex:
        print(api_stov.get_questions(page=page, time_from=time_from))
