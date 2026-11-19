# Sponsors of AI, GPU and tech-business events in the UK and Europe (Nov 2024 – Nov 2026)

Built 19 Nov 2026 for Raion: which companies that sponsor relevant events are the best buyers (or partners) for dedicated NVIDIA Blackwell capacity?

## Files
- `events-sponsors-all.csv`: 945 sponsor rows across 50+ event editions. Columns: event, edition, city, tier as published, Raion classification, source URL, confidence.
- `ideal-sponsors-for-raion.csv`: 93 sponsors classified as Raion-relevant, ranked by group and fit.
  - Group 1 = AI-native GPU buyers.
  - Group 2 = regulated or enterprise AI buyers.
  - Group 3 = channel and partners.
  - Each row lists the events they sponsored, with tier, and whether the name appears in earlier Raion research.
- `events-ranked-for-raion.csv`: events ranked by how many group 1 and group 2 buyers sponsor them. Use it to decide where Raion should attend or sponsor.

## Coverage
- **UK:** London Tech Week, AI Summit London, SXSW London, AI & Big Data Expo, Tech Show London (Big Data & AI World, Cloud & AI Infrastructure, Data Centre World), Founders Forum, Tech.eu Summit, AI Engineer Europe, DCD>Connect, Capacity Europe.
- **Europe:** VivaTech, RAISE Summit, Web Summit, Slush, GITEX Europe, World Summit AI, TNW, NVIDIA GTC Paris, ISC Hamburg, Datacloud Global Congress, Datacenter Forum, Sifted Summit, AI Engineer Paris, Data Innovation Summit, Big Data & AI Paris, Bits & Pretzels, Dublin Tech Summit, TechBBQ, HumanX Amsterdam, GenAI Zurich, Mistral and Hugging Face hackathons, STATION F events, Nordic AI events, DES Málaga, AI Summit Barcelona.
- **Academic:** ACL 2025, Interspeech 2025, ICASSP 2026, ICRA 2026, ECCV 2026, EurIPS 2025, RecSys 2025, ECAI 2025, ECML PKDD 2025, AMLD, EuroPython 2025/2026, PyData London.

## Method and caveats
- **How sponsors were found:** event websites and the web archive are blocked in this environment, and the request to allow them was rejected. So sponsors come from web-search results that quote official sponsor pages, press releases and companies' own announcements. The exceptions are ACL 2025 and EuroPython, whose public GitHub site repositories were read directly, and the official VivaTech 2025 closing release.
- **Confidence:** "high" = official page, press release or the company's own announcement. "medium" = a credible secondary source or a search summary of the official page. Anything weaker was dropped.
- **Gaps:** tier lists are incomplete for some events. The missing tiers are:
  - ISC Gold/Silver;
  - GTC Paris Diamond;
  - VivaTech 2026 Gold;
  - the EurIPS logo wall;
  - ICASSP Diamond/Gold.

  No usable list was found for:
  - WAICF;
  - AI & Big Data Expo Europe;
  - the Paris AI Action Summit;
  - CogX and ODSC 2025/26;
  - DCD London 2025.
- **Edition dates:** a few rows (Web Summit 2024, World Summit AI 2024) fall just before 19 Nov 2024 and are kept because they were explicitly in scope. Rows dated 2027 are upcoming editions whose sponsors are already announced.
- **Classification** is analyst judgement against the Raion ICP:
  - **Included:** companies that train or serve their own models, inference platforms that rent GPUs, and regulated enterprises with real AI compute.
  - **Excluded from buyer groups:** hyperscalers, frontier labs, acquired companies (e.g. Hugging Face → Nvidia, Cursor → xAI), China-HQ companies, chip/hardware/power vendors and neoclouds (competitors).
- "name_in_earlier_raion_research" is a text match against earlier Raion research files and dedup lists. It can produce false positives, so check before relying on it.
- No emails or phone numbers were collected.
