import unittest
from generate_qrels import parse_llm_response

EXAMPLE_01 = """The passage discusses the presence and storage of naturalization records within the Madison County Archives, specifically mentioning declarations of intention, petitions, and naturalization certificates from 1853 to 1953. However, it does not directly address whether naturalization records are public information or how one can access them. The passage provides specific details about a collection of naturalization records, but it does not clearly answer the query about whether such records are public information. Therefore, while it is somewhat related to the topic of naturalization records, it does not provide a direct or clear answer to the query.

1"""

EXAMPLE_02 = """Therefore, the passage is not relevant to the query.

0"""

EXAMPLE_03 = """Does not contain a relevance judgment"""

class TestParsingOfQrels(unittest.TestCase):
    def test_example_01(self):
        qrel, valid = parse_llm_response(EXAMPLE_01)

        self.assertEqual(qrel, 1)
        self.assertEqual(valid, 1)

    def test_example_02(self):
        qrel, valid = parse_llm_response(EXAMPLE_02)

        self.assertEqual(qrel, 0)
        self.assertEqual(valid, 1)

    def test_example_03(self):
        qrel, valid = parse_llm_response(EXAMPLE_03)

        self.assertEqual(qrel, 0)
        self.assertEqual(valid, 0)