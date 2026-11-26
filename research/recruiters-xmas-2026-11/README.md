# UK tech-recruitment lookalikes for the Christmas recruiter offer (25 Nov 2026)

**The request:** decision-maker emails at recruitment agencies like the 95 the user listed (La Fosse, Harnham, Burns Sheehan and others) that could become clients within 30 days on the Christmas offer for recruiters. None of the listed agencies may be repeated.

## Files

`recruiter-lookalikes-2026-11-25.csv` (round 1): 32 decision makers at 32 UK technology recruitment agencies, one per agency.
- 26 high confidence: the mail server confirmed the mailbox.
- 6 medium confidence: the address could not be confirmed (server temporarily unavailable, timed out, or accepts any address), or there is a role caveat.
- Ranked with mail-server-confirmed emails first, then by headcount growth over the last 6 months.

## How they were chosen

- **Lookalike:** UK-headquartered staffing and recruiting firms (11–250 staff) that specialise in tech, IT, data, AI, SAP/CRM, fintech, payments, quant or digital roles, like the reference list.
- **Ready to buy in the next 30 days:** every agency grew its headcount over the last 6 months. That signals hiring budget and growth now, which is the best available proxy because the Christmas offer details sit in Salesforce, and that connector is not authorised in this session.
- **Excluded:** every agency on the user's list (Signify Technology, iO Associates, Venturi, Noir, Hexwired, TRG, Wave Talent and Lawrence Harvey also appeared in search results and were removed).
- **Enriched but dropped as not close lookalikes:**
  - Copello Global (procurement recruiting);
  - CLM Search (automotive and executive search, shrinking);
  - Owen Daniels (STEM engineering);
  - Tech Professionals (engineering technicians).

## How the emails were found

- Apollo people match by exact person ID; every email is marked verified by Apollo.
- Each person's current title and employer come from the Apollo record.
- Every address then went through a bounceverify mail-server check.
- No address was guessed.

Caveats are in the `note` column:
- Linksap's Alistair Coker also has a "Retired" entry in Apollo.
- Coders Connect's co-founder also lists a stealth-startup role.
- Searchability's CEO is based in Austin.
- Durlston's founder is based in Dubai.

## Round 2: `recruiter-lookalikes-round2-2026-11-25.csv`

25 more decision makers at 25 UK recruitment agencies, one per agency.

**Nothing repeats.** The build script checks every agency against two lists and stops if it finds a match:
- the 95 agencies on the user's list;
- the 32 agencies delivered in round 1.

**Confidence:**
- 23 high: the mail server confirmed the mailbox.
- 2 medium:
  - TalentCo is on a catch-all server;
  - Quanta's server would not confirm.

**Ranking:**
1. High confidence first.
2. Then core tech recruiters before adjacent ones.
3. Then by headcount growth over the last 6 months.

**Core tech recruiters (16):**
- Beynd, Venatrix, HOK Consulting, Plan A Digital, Autonomai, Clear. (data centres), Link Chase (cyber), RemoteStar, Addition+.
- Global Technology Solutions, Insight Recruitment, bloom, Hamilton Barnes (networking), Hera, Gravitas, Maxwell Bond.
- The two medium-confidence agencies, TalentCo and Quanta, are also core tech recruiters.

**Adjacent fit (7, marked in `note`):**
- CodeVerse: trains and deploys developer teams.
- Bond Global and Chapter 2: embedded or RPO model.
- Strativ: tech plus engineering.
- Experts Group International: infrastructure, energy and technology.
- Techifide: AEC-industry IT.
- Vallum Associates: multi-sector.

**Enriched but dropped as not close lookalikes:**
- Millar Cameron, Wilton & Bain and NEO International Partners: executive search.
- X4 Group: flat headcount.
- Damia Group: catch-all domain, flat headcount.
- meritt.: sales hiring only.
- Resourcehive: outsourced resourcing.
- Solutions Driven: STEM executive search.
- OXBO: agri-tech.
- Hernshead: automation and motorsport.
- Proactive Global: industrial staffing.

**Also screened out from the websites before enrichment:**
- Kenton Black, Galago and 2i Recruit: multi-sector or general recruiters.
- Oyster Partnership: property.
- Danos Group: governance.
- TEC Group: energy and chemicals.
- Ascendo, Strive and CD Recruitment: sales/GTM hiring.
- Alecto: building automation.
- Green Recruitment Company: renewables.
- Jumpstart: hiring platform.
- Talisman, SourceWhale, Paiger and other recruitment-software firms.

**Method:** the same as round 1:
- Apollo people match by person ID, with emails marked verified by Apollo;
- a bounceverify check on the mail server;
- no guessed addresses.

The Clear. contact's title had a phone number in Apollo; it was removed.

## Round 3: `recruiter-lookalikes-round3-2026-11-26.csv`

39 more decision makers at 39 UK recruitment agencies, one per agency.

**Nothing repeats.** The build script checks every agency against three lists and stops if it finds a match:
- the 95 agencies on the user's list;
- the agencies delivered in rounds 1 and 2;
- the agencies dropped in rounds 1 and 2.

**How they were found.**
1. Two Apollo company searches for UK agencies tagged IT, tech, data, cyber, software or digital recruitment, or with a niche platform tag (SAP, Salesforce, ServiceNow, quant, AI, cloud). Each agency has 5–500 staff and grew headcount by at least 3% over 6 months. This returned about 390 firms.
2. Every remaining homepage was read to confirm the agency recruits for tech.
3. Decision makers were found with Apollo people search and then enriched, so every email is marked verified by Apollo.

**Confidence.**
- 21 high: the mail server confirmed the mailbox.
- 18 medium. They split three ways:
  - 8 sit on catch-all mail servers;
  - Recruit 121's mail-server check timed out;
  - 9 are Apollo-verified, not catch-all and have live mail (MX) records, but were not checked by bounceverify because the Apify budget ran out after 22 checks.

**Core and adjacent.**
- 27 are core tech recruiters.
- 12 are adjacent fits and are marked in `note`. These are:
  - finance and quant: AAA Global, Venture Search, Mondrian Alpha;
  - executive search: Candela, Scene;
  - RPO or embedded hiring: Join Talent, Talent Works;
  - multi-sector: QCS, Rise Technical, AEJ Consulting, Cogs, Forsyth Barnes.

**Dropped after enrichment.** Apollo matched the wrong organisation or a non-work address for these:
- Arrows: the contact works at a US sales-software company called Arrows.
- Scout: the contact's email is at a ski-travel company.
- npv: the contact's email is on another domain and they are based in the US.
- Henderson Scott: Apollo returned a US production company owner.
- Thor: Apollo returned a bookkeeping mailbox.
- Darwin Recruitment: the CEO's address is a personal domain.
- Move: the founder's address is at a PR company.

**Dropped as not close lookalikes:**
- Flowtec: engineering.
- Source: creative and design.
- Trust In SODA: it belongs to Trinnovo Group, the same group as DeepRec.ai, which was delivered in round 1.

**Screened out from the websites.** About 100 more were screened out before any enrichment:
- non-tech desks: sales/GTM, property, energy, life sciences, legal, finance-only, healthcare and education;
- recruitment software and job platforms;
- offshore IT outsourcing.

One find is directly relevant to Raion: **TTC Group** recruits for AI-infrastructure, data-centre and GPU-cluster roles.

## Round 4: `recruiter-lookalikes-round4-2026-11-26.csv`

47 more decision makers at 47 UK tech and IT recruitment agencies, one per agency.

**Nothing repeats.** The build script checks every agency and stops if it finds a match:
- the user's list;
- rounds 1–3 and every firm dropped in them;
- sister brands of already-covered groups:
  - Huxley and SThree (Computer Futures);
  - Nigel Frank and Frank/FRG (Mason Frank);
  - Opus Talent (Opus RS);
  - Trinnovo (DeepRec.ai);
  - X4 Technology (X4 Group);
  - Sartre Group (Satre Group).

**How they were found.**
1. Apollo's free company lookup returned UK agencies tagged IT, tech, data, cyber, SAP, Salesforce or AI recruitment. It returned:
   - firms with 3%+ headcount growth, including staffing firms tagged with tech domains;
   - for the first time, firms with stable headcount (0–2% over 6 months), because the growing pool was almost used up.
2. Every homepage was read to confirm a tech, IT or data recruitment focus.
3. Decision makers with Apollo-verified emails were then enriched: 50 credits for 50 people.

**Readiness signal.** 40 of the 47 have stable rather than growing headcount, and the `note` column says so. The growing ones rank first within each confidence level.

**Confidence: all 47 high.**
- 8 were confirmed by bounceverify's mail-server check.
- The other 39 were confirmed with Apollo's email check, run by LeadMagic on 26 Nov at the user's request, using 39 credits. Each came back "validated".
- 6 of the 39 sit on domains Apollo flags as catch-all, where any validator is less certain: HCR Digital, Client Server, Unify Talent, Found Talent, Madison Bridge and Paradigm Tech. `smtp_check` marks them.
- Primus Connect had earlier got a false "domain does not exist" from bounceverify. Apollo's check validated it.

**Adjacent fit (6, marked in `note`):** Sanderson, Oliver James, Sentinel Staffing, Akkar, Certus and TEC Partners.

**Dropped after enrichment (3):**
- TXP Talent: its CEO's current employer is Concept Resourcing.
- Moriati: media sales and advertising, not tech.
- A duplicate second contact at Digital Waffle.

**Caveats in `note`:**
- **Shrinking headcount:**
  - Focus Cloud Group: -15% over 6 months.
  - European Tech Recruit and Oakwell Hampton: -50% over 12 months.
  - Masento: -33% over 12 months.
- **Email on another domain the company uses:**
  - Focus Cloud: focuscloud.org.
  - Sentinel: sentinelit.com.
  - Explore Group: exploreltd.com.
  - Dynamic Search: its German entity, dynamicsearch.de.
- **Contact based outside the UK:** Impax, Saragossa, primehire, Akkar, ON3 Works and SO Digital.

Apollo returned shortened surnames for "Rory G", "Charles S" and "Callum D". They were not completed.
