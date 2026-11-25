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
