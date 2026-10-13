"""Collect public RSS/Atom metadata from explicitly enabled sources. No automatic validation."""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import urlparse
import xml.etree.ElementTree as ET

def read_entries(xml_bytes,source):
    root=ET.fromstring(xml_bytes)
    entries=[]
    if root.tag.rsplit("}",1)[-1]=="rss":
        for item in root.findall("./channel/item"):
            entries.append({"title":item.findtext("title") or "","url":item.findtext("link") or "",
              "published_at":item.findtext("pubDate"),"source_id":source["id"]})
    else:
        ns={"a":"http://www.w3.org/2005/Atom"}
        for item in root.findall("a:entry",ns):
            link=item.find("a:link",ns)
            entries.append({"title":item.findtext("a:title",default="",namespaces=ns),
              "url":link.get("href","") if link is not None else "",
              "published_at":item.findtext("a:updated",namespaces=ns),"source_id":source["id"]})
    return entries

def collect(registry,fetcher=None):
    fetcher=fetcher or (lambda url: urlopen(Request(url,headers={"User-Agent":"MarketingPracticeRadar/0.1 (public research)"}),timeout=12).read())
    output=[]
    for source in registry.get("sources",[]):
        if not source.get("enabled",False):continue
        url=source["rss"];parsed=urlparse(url)
        if parsed.scheme!="https" or not parsed.netloc:raise ValueError("Only HTTPS public feeds allowed")
        try:
            items=read_entries(fetcher(url),source)
            for item in items:
                if not item["url"].startswith(("https://","http://")):continue
                item.update({"observed_at":datetime.now(timezone.utc).isoformat(),
                  "review_status":"unreviewed","origin_status":"first_observed_not_original_proven"})
                output.append(item)
        except Exception as e:
            output.append({"source_id":source["id"],"review_status":"collection_error","error":str(e)})
    return output

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--registry",default="config/sources.json")
    parser.add_argument("--output",default="unreviewed_signals.json")
    args=parser.parse_args()
    results=collect(json.loads(Path(args.registry).read_text()))
    Path(args.output).write_text(json.dumps(results,indent=2))
    print(f"Collected {len(results)} unreviewed signals/errors into {args.output}")
if __name__=="__main__":main()
