import unittest
from hw04a import Repo

class test04a(unittest.TestCase):
    def test_response(self):
        self.assertEqual(Repo('wzhang62'),[['GithubApi567', 6], ['hello-world', 4], ['helloworld', 6], ['hw1', 2], ['Triangle111', 10]])

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()



