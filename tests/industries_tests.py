from unittest import TestCase
from pprint import pprint


class IndustriesTests(TestCase):

    def test_tree(self):
        from coursefinder.industries import industries_as_tree
        tree = industries_as_tree()
        pprint(tree)
        self.assertEqual(tree[0]['text'], 'Agriculture, Forestry, And Fishing')
        fish_hunt = tree[0]['nodes'][-1]
        self.assertEqual(fish_hunt['text'], 'Fishing, hunting, and trapping')
        shellfish = fish_hunt['nodes'][0]['nodes'][1]
        self.assertEqual(shellfish['text'], 'Shellfish')
