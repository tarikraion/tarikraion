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

## Contacts at the 93 sponsors (added 23 Nov 2026)
- `sponsor-clevel-contacts-2026-11-23.csv`:
  - 206 current C-level contacts at 92 of the 93 sponsors.
  - 130 have LinkedIn and 85 have emails (38 high and 47 medium confidence).
  - QuantumBlack has no C-level of its own: it is led by McKinsey senior partners.
  - Copied, without emails, into the "Event Sponsors – C-level" tab of the Raion FS searches sheet.
- `sponsor-partnership-contacts-2026-11-23.csv`:
  - 115 directors, heads and VPs of partnerships, alliances, ecosystem, business development and corporate development at 72 sponsors.
  - None of them are C-level or already on the C-level list.
  - 96 have LinkedIn. Verification: 89 verified, 26 partly verified.
  - Each row gives the role's function, location, how and when the role was confirmed, and a note on fit.
  - Copied, without emails, into the "Event Sponsors – Partnerships" tab. That tab's "Email found" column shows High, Medium or None.
  - Email columns added on 23 Nov: email, email_confidence, smtp_check, alternate_emails, email_how_found and email_note. There is also research_note_2026_11_23, which covers role checks such as people who have left.
- `sponsor-partnership-emails-2026-11-23.csv`:
  - Only the partnership contacts with a usable work email: 54 people at 42 companies, best first.
  - 28 are high confidence and 26 medium.
- How the partnership emails were found (23 Nov):
  - Two email databases (b2bsearch and Dievio) were run on all 96 LinkedIn profiles, and harvestapi on 10 priority profiles.
  - A 162-query Google sweep and 9 research agents looked for addresses published anywhere on the web.
  - Every address was checked against the person's current employer and with a mail-server check (bounceverify).
  - **High** means one of:
    - the mail server confirmed the mailbox;
    - two independent sources agree;
    - the company published the address itself.

    **Medium** means one database, on a server that accepts any address.
  - Addresses that bounced, belong to old employers, are personal, or don't fit the person (for example initials-only) are not used as the primary email. A few are listed under alternate_emails with a warning.
  - No address was guessed or built from a pattern.
- `sponsor-partnership-company-notes-2026-11-23.csv`:
  - One row per sponsor (93), giving how many partnership contacts were found and the research notes.
  - The notes include leads that could not be confirmed (masked surnames, unconfirmed titles).
  - They also explain why 21 sponsors have no partnership contact.
- Contact rules for both lists:
  - Names and titles come from Apollo or a source dated 2025–26.
  - LinkedIn URLs were used only when seen in results; none were guessed.
  - Masked or abbreviated surnames were left as shown (for example "Ash K."), unless a database record or the company's own pages gave the full name. "Jack G." is now Jack Grey (database record), and "Mae W." is now Mae Wang (TD SYNNEX pages).
  - The 23 Nov email round added 12 LinkedIn URLs and corrected 1, so 108 of the 115 partnership contacts now have one. Two of the new URLs (Mauro Xavier, Patrick Pugh) are linked from PwC's own contact pages.

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
- The sponsor lists hold no emails or phone numbers. Emails exist only in `sponsor-clevel-contacts-2026-11-23.csv`, `sponsor-partnership-contacts-2026-11-23.csv` and `sponsor-partnership-emails-2026-11-23.csv`. No phone numbers were collected.
