"""Apply verification fixes (2 Oct 2026 fact-check pass), add accounts, normalise sectors."""
import json
from pathlib import Path

S = Path("/tmp/claude-0/-home-user/022a5bf0-aa1e-54eb-849d-7d632705af27/scratchpad")
files = {k: S / f"accounts_{k}.json" for k in ("us", "uk", "eu", "enterprise")}
for k, p in files.items():
    orig = p.with_suffix(".orig.json")
    if not orig.exists():
        orig.write_text(p.read_text())
data = {k: json.loads(p.with_suffix(".orig.json").read_text()) for k, p in files.items()}


def find(name):
    for k, rows in data.items():
        for r in rows:
            if r["company"].lower().startswith(name.lower()):
                return r
    raise KeyError(name)


def contact(company, name, **kw):
    r = find(company)
    rename = kw.pop("rename", None)
    for c in r["contacts"]:
        if c["name"] == name:
            c.update(kw)
            if rename:
                c["name"] = rename
            return
    c = {"name": name, "title": "", "linkedin_url": None, "source_url": None, "confidence": "medium"}
    c.update(kw)
    r["contacts"].append(c)


def drop(company, name):
    r = find(company)
    r["contacts"] = [c for c in r["contacts"] if c["name"] != name]


def signal(company, text, date, url):
    find(company)["signals"].append({"signal": text, "date": date, "source_url": url})


# ---------- US ----------
contact("Generalist", "Pete Florence", confidence="high", linkedin_url="https://www.linkedin.com/in/peteflorence/",
        source_url="https://siliconangle.com/2026/06/04/generalist-ai-raises-400m-2b-valuation-build-general-intelligence-real-world/")
signal("Generalist", "Raised $400M at a $2B valuation led by Radical Ventures (8VC, USV, NVentures, Bezos Expeditions)", "2026-06-04",
       "https://siliconangle.com/2026/06/04/generalist-ai-raises-400m-2b-valuation-build-general-intelligence-real-world/")
contact("General Intuition", "Pim de Witte", confidence="high", linkedin_url="https://www.linkedin.com/in/pimdw",
        source_url="https://www.crunchbase.com/person/pim-de-witte")
contact("Chai Discovery", "Joshua Meier", confidence="high", linkedin_url="https://www.linkedin.com/in/joshua-meier-27a6861a/",
        source_url="https://siliconvalleyinvestclub.com/companies/chai-discovery/team/joshua-meier/")
contact("Arcee", "Lucas Atkins", confidence="high", linkedin_url="https://www.linkedin.com/in/lucas-atkins-2892482b6/",
        source_url="https://www.crunchbase.com/person/lucas-atkins-e78e")
contact("Physical Intelligence", "Karol Hausman", confidence="high", linkedin_url="https://www.linkedin.com/in/karolhausman/",
        source_url="https://www.linkedin.com/in/karolhausman/")
contact("Higgsfield", "Alex Mashrabov", confidence="high", source_url="https://en.wikipedia.org/wiki/Higgsfield_AI")
contact("Higgsfield", "Yerzat Dulat", title="Co-founder & CTO", confidence="high",
        source_url="https://x.com/alexmashrabov/status/2072003833883168799")
contact("Higgsfield", "Mahi de Silva", title="Co-founder & Chief Strategy Officer", confidence="medium",
        source_url="https://en.wikipedia.org/wiki/Higgsfield_AI")
contact("Lila Sciences", "Geoffrey von Maltzahn", confidence="high",
        linkedin_url="https://www.linkedin.com/in/geoffrey-von-maltzahn-7a6b755a",
        source_url="https://www.lila.ai/team/geoffrey-von-maltzahn")
contact("Wispr Flow", "Tanay Kothari", confidence="high", source_url="https://www.crunchbase.com/person/tanay-kothari")
for s in find("Wispr Flow")["signals"]:
    if "Series B" in s["signal"]:
        s["date"] = "2026-08"
        s["signal"] = "Series B (reported $260-280M) at a $2B valuation led by Menlo Ventures and Notable Capital; most capital to speech research"
        s["source_url"] = "https://wisprflow.ai/post/series-b"
contact("Harmonic", "Tudor Achim", confidence="high", linkedin_url="https://www.linkedin.com/in/tudorachim",
        source_url="https://www.crunchbase.com/person/tudor-achim")
contact("Runway", "Cristobal Valenzuela", rename="Cristóbal Valenzuela", title="Co-founder & Co-CEO", confidence="high",
        linkedin_url="https://www.linkedin.com/in/cvalenzuelab/", source_url="https://www.linkedin.com/in/cvalenzuelab/")
contact("Runway", "Anastasis Germanidis", title="Co-founder & Co-CEO", confidence="high",
        source_url="https://runway.com/news/new-leaders-to-support-next-phase-of-growth")
contact("Cognition", "Scott Wu", confidence="high", linkedin_url="https://www.linkedin.com/in/scott-wu-8b94ab96/",
        source_url="https://www.crunchbase.com/person/scott-wu")
contact("Xaira", "Marc Tessier-Lavigne", title="Co-founder, Chairman & CEO", confidence="high",
        source_url="https://www.xaira.com/team/marc-tessier-lavigne")
contact("Suno", "Georg Kucsko", confidence="high", linkedin_url="https://www.linkedin.com/in/georgkucsko/",
        source_url="https://www.crunchbase.com/person/georg-kucsko-3d27")
contact("Mirendil", "Behnam Neyshabur", title="Co-founder & CEO", confidence="high",
        source_url="https://the-decoder.com/ex-anthropic-researchers-launch-ai-startup-mirendil-to-tackle-scientific-research/")
contact("Mirendil", "Harsh Mehta", title="Co-founder & CTO", confidence="medium",
        source_url="https://the-decoder.com/ex-anthropic-researchers-launch-ai-startup-mirendil-to-tackle-scientific-research/")
signal("Mirendil", "Signed a $100M+ Google Cloud deal to scale training (primary compute now committed)", "2026-08-06",
       "https://techcrunch.com/2026/08/06/exclusive-mirendil-inks-100m-google-cloud-deal-to-scale-self-improving-ai/")
find("Mirendil")["fit_score"] = 5
find("Mirendil")["timing_rationale"] = ("Primary compute is now committed to Google Cloud (Aug 2026), so pitch Raion as a dedicated "
                                         "second source for NVIDIA training runs in 2027 rather than the main supplier.")
contact("Mind Robotics", "RJ Scaringe", title="Co-founder & Chairman (also CEO of Rivian; no separate CEO named)",
        confidence="high", source_url="https://en.wikipedia.org/wiki/Mind_Robotics")
find("Mind Robotics")["fit_score"] = 6
find("Periodic Labs")["fit_score"] = 7

# ---------- UK ----------
contact("CuspAI", "Chad Edwards", title="Co-founder & CEO", confidence="high",
        linkedin_url="https://www.linkedin.com/in/edwardschad/", source_url="https://time.com/collection/time100-ai/2026/chad-edwards/")
contact("Synthesia", "Peter Hill", confidence="high", source_url="https://www.synthesia.io/blog/authors/peter-hill")
drop("Synthesia", "Steffen Tjerrild")
contact("Cosine", "Alistair Pullen", title="Co-founder & CEO", confidence="high",
        source_url="https://tech.eu/2026/06/08/cosine-secures-industry-backing-for-britain-s-first-sovereign-frontier-model/")
signal("Cosine", "Unveiled coalition (Lloyds, NatWest, BT, LSEG, BAE, Vodafone and others) to co-design Lumen Sovereign, a ~1.35T-parameter model trained on UK soil, targeted for end-2026",
       "2026-06-08", "https://tech.eu/2026/06/08/cosine-secures-industry-backing-for-britain-s-first-sovereign-frontier-model/")
contact("Prima Mente", "Ravi Solanki", title="Co-founder & CEO", confidence="high",
        source_url="https://pmwcintl.com/speaker/ravi-solanki-401_prima-mente_2026sv/")
contact("Doubleword", "Meryem Arik", title="Co-founder & CEO", confidence="high", source_url="https://qconlondon.com/speakers/meryemarik")
contact("Doubleword", "Fergus Finn", title="Co-founder & CTO", confidence="medium",
        source_url="https://techfundingnews.com/doublewords-12m-fuels-mission-to-bring-easy-secure-self-hosted-ai-to-enterprises/")
contact("Emulate", "Jack Parker-Holder", source_url="https://www.bloomberg.com/news/articles/2026-09-17/deepmind-offshoot-emulate-closes-in-on-700-million-seed-round")

data["uk"] += [
    {
        "company": "Basecamp Research", "website": "https://www.basecamp-research.com", "hq_city": "London", "hq_country": "UK",
        "segment": "AI for science - biological foundation models",
        "what_they_do": "Builds the EDEN biological foundation models on its Trillion Gene Atlas dataset, for AI-designed in vivo cell and gene therapies.",
        "signals": [
            {"signal": "Closed a $140M Series C led by S32 (NVIDIA, Sovereign AI, NATO Innovation Fund, Menlo Anthology) to train a new generation of EDEN models",
             "date": "2026-09-23", "source_url": "https://endpoints.news/ai-startup-basecamp-research-raises-140m-series-c-shares-pipeline/"},
        ],
        "est_gpu_need": "200-1,000 GPUs (1-4 blocks) for EDEN pre-training runs; UK-backed, so in-country capacity is a plus.",
        "fit_score": 9,
        "timing_rationale": "Money raised nine days ago is earmarked for training the next EDEN generation, so the cluster decision is being made this quarter for runs in early 2027.",
        "contacts": [{"name": "Glen Gowers", "title": "Co-founder & CEO", "linkedin_url": None,
                      "source_url": "https://endpoints.news/ai-startup-basecamp-research-raises-140m-series-c-shares-pipeline/", "confidence": "high"}],
    },
    {
        "company": "Ineffable Intelligence", "website": None, "hq_city": "London", "hq_country": "UK",
        "segment": "Model lab - reinforcement learning",
        "what_they_do": "David Silver's lab building a reinforcement-learning 'superlearner' that discovers knowledge without human data.",
        "signals": [
            {"signal": "Raised a $1.1B seed at a $5.1B valuation co-led by Sequoia and Lightspeed (NVIDIA, Google, DST, Index, UK Sovereign AI Fund)",
             "date": "2026-04-27", "source_url": "https://www.cnbc.com/2026/04/27/deepmind-ineffable-intelligence-record-seed-funding-nvidia-google.html"},
        ],
        "est_gpu_need": "Several MW: RL at scale is compute-bound, and a $1.1B seed implies multi-thousand-GPU plans.",
        "fit_score": 8,
        "timing_rationale": "Six months after the raise, the team is moving from setup to large training runs. Google is an investor, so position Raion as dedicated UK capacity alongside any Google allocation.",
        "contacts": [{"name": "David Silver", "title": "Founder (leads the company; CEO title not confirmed)", "linkedin_url": None,
                      "source_url": "https://techcrunch.com/2026/04/27/deepminds-david-silver-just-raised-1-1b-to-build-an-ai-that-learns-without-human-data/",
                      "confidence": "medium"}],
    },
    {
        "company": "Humanoid", "website": "https://thehumanoid.ai", "hq_city": "London", "hq_country": "UK",
        "segment": "Robotics / physical AI (humanoids)",
        "what_they_do": "Industrial humanoid robots (HMND-01 wheeled and bipedal) with in-house robot learning models.",
        "signals": [
            {"signal": "Raised a $152M Series A at a $1.35B valuation led by Prime Movers Lab (Schaeffler, Bosch, Fubon)",
             "date": "2026-07-21", "source_url": "https://siliconangle.com/2026/07/21/humanoid-raises-152m-1-35b-valuation-bring-human-like-robots-factories/"},
        ],
        "est_gpu_need": "About one block (200-250 GPUs) for robot foundation-model training and simulation.",
        "fit_score": 7,
        "timing_rationale": "Series A money is going into model training and deployments with industrial partners through 2027.",
        "contacts": [{"name": "Artem Sokolov", "title": "Founder & CEO", "linkedin_url": None,
                      "source_url": "https://siliconangle.com/2026/07/21/humanoid-raises-152m-1-35b-valuation-bring-human-like-robots-factories/",
                      "confidence": "high"}],
    },
]

# ---------- Europe ----------
contact("AMI Labs", "Alexandre LeBrun", title="CEO", confidence="high",
        source_url="https://techcrunch.com/2026/07/16/why-ami-labs-alexandre-lebrun-wont-call-his-ai-agi-or-superintelligence/")
contact("Gradium", "Neil Zeghidour", title="Co-founder & CEO", confidence="high",
        linkedin_url="https://fr.linkedin.com/in/neil-zeghidour-a838aaa7", source_url="https://www.pymnts.com/news/artificial-intelligence/2026/gradium-ceo-says-voice-ai-must-understand-not-just-transcribe-the-words/")
contact("Gradium", "Olivier Teboul", title="Co-founder & CTO", confidence="medium",
        source_url="https://slator.com/voice-ai-startup-gradium-70m-seed-round/")
contact("H Company", "Gautier Cloix", title="President & CEO", confidence="high",
        source_url="https://www.bloomberg.com/news/audio/2026-08-25/tech-disruptors-h-company-ceo-on-automating-enterprise-work")
contact("Harmattan", "Mouad M'Ghari", title="Co-founder & CEO", confidence="high",
        source_url="https://siliconangle.com/2026/01/12/french-fighter-company-dassault-invests-200m-autonomous-drone-startup-harmattan-ai/")
for n in ("Torsten Reil", "Gundbert Scherf"):
    contact("Helsing", n, confidence="high",
            source_url="https://www.forbes.com/sites/madhulika-pathak/2026/07/14/helsing-cofounders-fortunes-get-big-boost-from-new-18-billion-valuation/")
contact("NEURA", "David Reger", confidence="high", source_url="https://www.crunchbase.com/person/david-reger")
signal("NEURA", "Announced a Series C of up to $1.4B at a $7B valuation, led by industrial and tech investors with Tether", "2026-06",
       "https://neura-robotics.com/record-series-c/")
drop("Cohere", "Jonas Andrulis")
contact("DeepL", "Sebastian Enderlein", title="CTO", confidence="high", linkedin_url="https://www.linkedin.com/in/sebastianenderlein/",
        source_url="https://www.deepl.com/en/blog/accelerate-language-ai-innovation-from-the-big-apple")
data["eu"] = [r for r in data["eu"] if r["company"] != "Roche"]  # merged into the enterprise record

# ---------- Enterprise ----------
contact("XTX", "Alex Gerko", title="Founder & Co-CEO", confidence="high", source_url="https://en.wikipedia.org/wiki/XTX_Markets")
contact("XTX", "Hans Buehler", title="Co-CEO", confidence="medium", source_url="https://en.wikipedia.org/wiki/XTX_Markets")
signal("XTX", "Sued Dell in Ireland over a $62-70M price increase on 1,680 servers for its Finnish data centres: a sign of hardware cost pain",
       "2026-06-19", "https://www.caproasia.com/2026/06/19/ex-deutsche-bank-trader-billionaire-founder-alex-gerko-age-46-with-17-billion-fortune-quant-trading-firm-xtx-markets-xtx-finland-oy-files-ireland-lawsuit-against-265-billion-computer-giant-del/")
contact("Roche", "Wafaa Mamilli", title="Chief Digital & Technology Officer", confidence="high",
        source_url="https://pharmafile.com/news/roche-adds-2176-nvidia-blackwell-gpus-to-its-hybrid-cloud-ai-factory/")
contact("EDF", "Bernard Fontana", title="Chairman & CEO", confidence="high", linkedin_url="https://fr.linkedin.com/in/bernard-fontana/en",
        source_url="https://www.datacenterdynamics.com/en/news/opcore-plans-4bn-data-center-at-former-edf-coal-power-plant-outside-paris-france/")
signal("EDF", "Picked SoftBank (400 MW, Bouchain) and Eclairion (330 MW, Loire-sur-Rhône) for AI data centres on former power-station sites; more sites still offered",
       "2026-06-02", "https://www.datacenterdynamics.com/en/news/edf-selects-softbank-and-eclairion-to-deliver-ai-data-center-projects-at-former-power-stations-in-france/")
find("EDF")["fit_score"] = 6
contact("Deutsche Telekom", "Ferri Abolhassan", title="CEO, T-Systems", confidence="high",
        source_url="https://www.t-systems.com/de/en/insights/newsroom/management-unplugged/t-systems-ceo-forges-a-sovereign-germany-stack-for-manufacturing-1133930")
signal("Deutsche Telekom", "Munich Industrial AI Cloud reported as largely booked out; preparing an EU AI Gigafactory bid", "2026",
       "https://www.t-systems.com/de/en/insights/newsroom/management-unplugged/from-the-ai-factory-to-the-ai-gigafactory-1211580")
contact("Telenor", "Kaaren Hilsen", title="CEO, Telenor AI Factory", confidence="high",
        source_url="https://www.telecomtv.com/content/spotlight-on-5g/telenor-s-sovereign-ai-factory-puts-norway-in-control-the-country-s-critical-data-55081/")
find("Jane Street")["fit_score"] = 7
find("Jane Street")["timing_rationale"] = (find("Jane Street").get("timing_rationale", "") +
                                            " Large deals are already signed with CoreWeave and Crusoe, so 0.5 MW blocks are a small, owned second source; the firm does not publish its C-suite, so reach it through a warm introduction.")
find("UK Department")["fit_score"] = 6
find("UK Department")["timing_rationale"] = (find("UK Department").get("timing_rationale", "") +
                                              " This is a public tender, so the route is a bid or a partnership with a bidding managed-service provider, not C-level outreach.")
# Long-standing executives whose titles are well documented before 2026 but not re-checked this session
for comp, name in [("Bristol Myers", "Christopher Boerner"), ("Eli Lilly", "David A. Ricks"), ("Eli Lilly", "Diogo Rau"),
                   ("Citadel", "Peng Zhao"), ("Man Group", "Robyn Grew"), ("BT Group", "Allison Kirkby"), ("HSBC", "Georges Elhedery"),
                   ("Lloyds", "Charlie Nunn"), ("Telefónica", "Marc Murtra"), ("ACS", "Florentino Pérez"), ("Orange", "Christel Heydemann"),
                   ("Nokia", "Justin Hotard"), ("Telenor", "Benedicte Schilbred Fasmer"), ("University of Edinburgh", "Mark Parsons"),
                   ("Roche", "Thomas Schinecker")]:
    contact(comp, name, confidence="medium")


# ---------- LinkedIn URLs seen in search results (2 Oct 2026) ----------
LI = [
    ("Arcee", "Mark McQuade", "https://www.linkedin.com/in/mark-mcquade/"),
    ("Higgsfield", "Alex Mashrabov", "https://www.linkedin.com/in/amashrabov/"),
    ("Periodic Labs", "Liam Fedus", "https://www.linkedin.com/in/liam-fedus-26547811/"),
    ("Synthesia", "Victor Riparbelli", "https://www.linkedin.com/in/victorriparbelli/"),
    ("PhysicsX", "Jacomo Corbo", "https://uk.linkedin.com/in/jacomo-corbo"),
    ("Basecamp Research", "Glen Gowers", "https://www.linkedin.com/in/glen-gowers-bba1a284/"),
    ("Cosine", "Alistair Pullen", "https://www.linkedin.com/in/alistair-pullen-616129226/"),
    ("Cosine", "Yang Li", "https://www.linkedin.com/in/yangli92/"),
    ("Wayve", "Alex Kendall", "https://www.linkedin.com/in/alexgkendall/"),
    ("Humanoid", "Artem Sokolov", "https://uk.linkedin.com/in/artem-sokolov-s"),
    ("Helsing", "Torsten Reil", "https://uk.linkedin.com/in/torstenreil"),
    ("Helsing", "Gundbert Scherf", "https://de.linkedin.com/in/gscherf"),
    ("NEURA", "David Reger", "https://de.linkedin.com/in/dregerofficial"),
    ("H Company", "Gautier Cloix", "https://fr.linkedin.com/in/gcloix"),
    ("Stability AI", "Prem Akkaraju", "https://www.linkedin.com/in/prem-akkaraju-7b10a265/"),
    ("Bristol Myers", "Greg Meyers", "https://www.linkedin.com/in/greg-meyers-cio"),
    ("Emulate", "Jack Parker-Holder", "https://www.linkedin.com/in/jack-parker-holder-0bb66a29/"),
]
for comp, name, url in LI:
    contact(comp, name, linkedin_url=url)
contact("Arcee", "Mark McQuade", confidence="high")
contact("PhysicsX", "Jacomo Corbo", title="Co-founder & Co-CEO")
find("Arcee")["hq_city"] = "Miami, FL"

# ---------- Explorium enrichment (2 Oct 2026): profiles matched by name + company ----------
EXP = "Explorium profile match, 2 Oct 2026"
exli = json.loads((S / "icp" / "explorium_li.json").read_text())
name_map = {  # Explorium full_name -> (company prefix, our contact name)
    "Max Welling": ("CuspAI", "Max Welling"), "Martin Camacho": ("Suno", "Martin Camacho"),
    "Rissa Cao": ("Fish Audio", "Rissa Cao"), "Olivier Teboul": ("Gradium", "Olivier Teboul"),
    "Mahi De Silva": ("Higgsfield", "Mahi de Silva"), "Carina Hong": ("Axiom", "Carina Hong"),
    "Jarek Kutylowski": ("DeepL", "Jarek Kutylowski"), "Jeff Hawke": ("Odyssey", "Jeff Hawke"),
    "Florian Seibel": ("Quantum Systems", "Florian Seibel"),
    "Benedicte Schilbred Fasmer": ("Telenor", "Benedicte Schilbred Fasmer"), "Kaaren Hilsen": ("Telenor", "Kaaren Hilsen"),
    "Erez Dagan": ("Wayve", "Erez Dagan"), "Tanay Kothari": ("Wispr", "Tanay Kothari"), "Aidan Gomez": ("Cohere", "Aidan Gomez"),
    "Dr. Ferri Abolhassan": ("Deutsche Telekom", "Ferri Abolhassan"), "Fergus Finn": ("Doubleword", "Fergus Finn"),
    "Ravi Solanki": ("Prima Mente", "Ravi Solanki"), "Stijn Bijnens": ("Proximus", "Stijn Bijnens"),
    "Thomas Schinecker": ("Roche", "Thomas Schinecker"), "Wafaa Mamilli": ("Roche", "Wafaa Mamilli"),
    "Carla Gómez Cano": ("THEKER", "Carla Gómez Cano"), "Peng Zhao": ("Citadel", "Peng Zhao"),
    "Stef Van Grieken": ("Cradle", "Stef van Grieken"), "Diogo Rau": ("Eli Lilly", "Diogo Rau"),
    "Behnam Neyshabur": ("Mirendil", "Behnam Neyshabur"), "Justin Hotard": ("Nokia", "Justin Hotard"),
    "Nikola Mrkšić": ("PolyAI", "Nikola Mrkšić"), "Charlie Nunn": ("Lloyds", "Charlie Nunn"),
    "Arthur Mensch": ("Mistral", "Arthur Mensch"), "Artem Sokolov": ("Humanoid", None),
}
for ex_name, (comp, ours) in name_map.items():
    if ours is None:
        continue
    r = find(comp)
    c = next(c for c in r["contacts"] if c["name"] == ours)
    if not c.get("linkedin_url"):
        c["linkedin_url"] = exli[ex_name]["linkedin"]
    c["confidence"] = "high"
    if not c.get("source_url"):
        c["source_url"] = None
    c["verified_by"] = EXP
contact("CuspAI", "Max Welling", title="Co-founder & CTO")
contact("Suno", "Martin Camacho", title="Co-founder & President")
contact("THEKER", "Carla Gómez Cano", title="Co-founder (title per LinkedIn)", confidence="medium")
contact("Telenor", "Kaaren Hilsen", title="CEO, Telenor AI Factory (Mar 2026 press); LinkedIn lists Chief Innovation & Sustainability Officer, Telenor Infrastructure",
        confidence="medium")
contact("Proximus", "Stijn Bijnens", title="CEO, Proximus Group (since Sep 2025)")
# New C-level contacts from Explorium fetch-prospects (business match + c-suite filter)
for comp, name, title, li, conf in [
    ("Hudson River", "Brad Olson", "Chief Financial Officer", "https://linkedin.com/in/brad-olson-8385511", "medium"),
    ("mimic", "Stefan Weirich", "Co-founder & CEO", "https://linkedin.com/in/stefan-weirich", "medium"),
    ("mimic", "Elvis Nava", "Co-founder & CTO", "https://linkedin.com/in/elvisnava", "medium"),
    ("STARK", "Martin Rost", "Chief Operating Officer", "https://linkedin.com/in/martin-rost-29b51870", "medium"),
    ("STARK", "Johannes Schaback", "Co-founder (formerly CTO)", "https://linkedin.com/in/johannes-schaback", "medium"),
    ("Pleias", "Anastasia Stasenko", "CEO & Co-founder", "https://linkedin.com/in/anastasia-stasenko", "medium"),
    ("Ineffable", "Lasse Espeholt", "Chief Technology Officer", "https://linkedin.com/in/lasseespeholt", "medium"),
    ("Ineffable", "Wojciech Czarnecki", "Chief Scientific Officer", "https://linkedin.com/in/wojciechczarnecki", "medium"),
]:
    contact(comp, name, title=title, linkedin_url=li, confidence=conf, source_url=None, verified_by=EXP)
for n in ("Pierre-Carl Langlais", "Ivan Yamshchikov"):
    drop("Pleias", n)

for k, p in files.items():
    p.write_text(json.dumps(data[k], indent=1, ensure_ascii=False))
print({k: len(v) for k, v in data.items()})
