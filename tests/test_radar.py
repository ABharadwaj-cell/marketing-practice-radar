import json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"src"))
from radar import evaluate,rank
from collect_feeds import read_entries,collect
class TestRadar(unittest.TestCase):
 def setUp(self):self.records=json.loads((ROOT/"fixtures/synthetic_tactics.json").read_text())
 def test_score_range(self):self.assertTrue(all(20<=x["triage_score"]<=100 for x in rank(self.records)))
 def test_ranking(self):self.assertEqual(rank(self.records)[0]["id"],"MPR-002")
 def test_bad_score(self):
  r=dict(self.records[0]);r["evidence_strength"]=6
  with self.assertRaises(ValueError):evaluate(r)
 def test_invalid_source(self):
  r=dict(self.records[0]);r["source_url"]="file:///etc/passwd"
  with self.assertRaises(ValueError):evaluate(r)
 def test_experiment_gate(self):self.assertIn("require approval for public execution",evaluate(self.records[0])["experiment_spec"]["safeguards"])
 def test_rss_parser(self):
  xml=b"<rss><channel><item><title>Sample</title><link>https://example.org/a</link><pubDate>Mon</pubDate></item></channel></rss>"
  self.assertEqual(read_entries(xml,{"id":"s"})[0]["title"],"Sample")
 def test_disabled_sources(self):
  self.assertEqual(collect({"sources":[{"id":"s","rss":"https://example.org/feed","enabled":False}]},lambda u: (_ for _ in ()).throw(Exception("must not fetch"))),[])
 def test_collection_flag(self):
  xml=b"<rss><channel><item><title>Sample</title><link>https://example.org/a</link></item></channel></rss>"
  result=collect({"sources":[{"id":"s","rss":"https://example.org/feed","enabled":True}]},lambda u:xml)
  self.assertEqual(result[0]["review_status"],"unreviewed")
if __name__=="__main__":unittest.main()
