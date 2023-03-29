import os


def add_base_url():
    os.environ['ENV'] = 'test'
    env = os.environ.get('ENV')

    if env.lower() == 'test':
        return 'http://demostore.supersqa.com'
    elif env.lower() == 'prod':
        return 'http://demostore.prod.supersqa.com'
    else:
        raise Exception('Unknown environment is selected!')



