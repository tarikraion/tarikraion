# London financial-services GPU buyers (5 Nov 2026)

These lists cover London banks, hedge funds and trading firms that could buy dedicated GPU capacity. They are mirrored in the Google Sheet "Raion FS searches" (tabs UK Banks, Hedge Funds, Trading Firms, Other Leads).

- `uk-banks-gpu.csv` — 9 UK banks, ranked by **priority score**. The score is the GPU fit (1–10) plus a bonus for financing data centres: +2 if the bank leads or regularly arranges data-centre deals, +1 if it only participates.
- `london-hedge-funds.csv` — 2 London hedge funds added to the main hedge fund list: Squarepoint and Fasanara.
- `london-trading-firms.csv` — London-relevant prop trading firms and market makers: Wintermute, DRW, IMC, Flow Traders and Jump. G-Research and Quadrature are on a watchlist because no dated signal was found.
- `../eu-banks-ai-poc-2026-11/eu-banks-ai-poc-top10.csv` — EU banks, now re-ranked with the same data-centre preference.

## How this was verified
- I re-checked these key signals: HSBC–Mistral self-hosting, NatWest–NVIDIA Nemotron, Starling–Civo, Revolut Research, Lloyds ATUM on Blackwell, Barclays' Chief AI Officer, Wintermute's $1bn plan, IMC/Flow Traders–CoreWeave, Fasanara AI Lab and the Squarepoint London HQ.
- I checked these data-centre deals: VIRTUS £2.45bn (Standard Chartered, BNP Paribas, Crédit Agricole CIB, Société Générale), Mistral $830m (HSBC, BNP Paribas, Crédit Agricole CIB, La Banque Postale, MUFG, Natixis, Bpifrance), Nscale $790m (ABN AMRO, DNB, Nordea, SEB, Eksfin) and Vantage £254m (Barclays, SMBC). The other data-centre deals come from the research agent's sources.
- LinkedIn URLs come from search results or Apollo; none were guessed. No emails or phone numbers are stored.

## Update 5 Nov (second pass): GPU-financing preference and deeper London research
- **Bank priority score** = GPU fit + data-centre bonus (+2 lead, +1 participant) + GPU-financing bonus (+2 lead, +1 participant). The UK and EU bank CSVs are re-ranked on this score.
- I checked these GPU-financing deals myself: Nebius $775m GPU-backed loan (MLAs MUFG, ABN AMRO, Bank of America, Deutsche Bank, HSBC; SLAs Citi, Crédit Agricole CIB, ING, Morgan Stanley); Nscale ~$1.4bn GPU-backed loan (Goldman Sachs sole structuring agent; PIMCO, Blue Owl and LuminArx as leads); Nscale $900m revolving facility (J.P. Morgan and Goldman Sachs International as joint lead arrangers).
- `lenders.csv` lists 17 banks and funds that finance GPUs or data centres. They are possible financing partners for Raion's own capacity.
- `london-fs-firms.csv` covers global banks' London AI hubs (JPMorgan, Goldman Sachs, UBS), London insurers and asset managers (WTW, Aviva, Admiral, Schroders, M&G) and UK fintechs that train their own models (Behavox, Aveni, 9fin, Sumsub, Cleo, Quantexa).
- `london-trading-firms.csv` adds Hudson River Trading (renting more than 1,000 Blackwell systems from Lambda; London AI lab) and Jane Street (a $6bn CoreWeave commitment). Maven is on the watchlist.
- Anonymised London recruiter ads for "GPU Systems Engineer – algorithmic fund" (Oxford Knight, Mar–Apr 2026) and "HPC Platform Engineer – $25bn systematic firm" show further unnamed demand. The first is probably HRT, but that is unconfirmed.
- Not done, because the shared search limit ran out: about 20 UK fintechs (Lendable, ClearScore, GoCardless, Moneybox and others) and several London hedge funds (Caxton, Pharo, TCI and others).

## Update 5 Nov (third pass): more London FS firms
- `london-fs-firms.csv` gains Bloomberg (fit 8), BNY, Elliptic, Experian, Lendable, Tide, Checkout.com, Tractable and ComplyAdvantage. Behavox moves to fit 9 after its $8m dedicated-GPU commitment with Civo (7 Oct 2026, verified on civo.com). The list is re-ranked by GPU fit.
- `london-trading-firms.csv` adds XTX Markets (25,000+ GPU cluster; building its own Finnish data centres).
- In the sheet only (Other Leads): BlueCrest, H2O AM and Cosine (UK sovereign model; not financial services).

## Update 5 Nov: people like Shane Moore (Standard Chartered)
- **Seed:** Shane Moore. Apollo lists him as MD & Head of US Commercial Real Estate, Standard Chartered, New York. Standard Chartered's own releases on VIRTUS Data Centres (EUR210m Berlin, Feb 2026; GBP2.45bn, Sep 2026) quote him as **Head of Commercial Real Estate, EMEA**, so his desk lends to data centres and he is probably London-based now.
- `dc-re-finance-people.csv` lists 43 lookalikes plus the seed, in London, New York and Abu Dhabi:
  - Tier A (23): people who run data-centre or digital-infrastructure lending, or who were quoted on a data-centre deal.
  - Tier B (20): general real-estate lenders and Gulf investors.
  - 28 have a LinkedIn profile: 27 from Apollo matching, 1 from a search result.
- `lenders.csv` adds 16 banks and investors "like Standard Chartered", plus a contact for each lender where one is known.
- **Method:**
  - Apollo lookalike agent, plus free Apollo people search, plus Apollo matching (28 credits).
  - Three research agents, one each for London, New York and Abu Dhabi, at about 45 searches each.
- **Spot checks:** Shane Moore's VIRTUS quotes, HSBC–Core42 $550m (Shaikha Almarri), Khazna $2.62bn (ADCB/FAB, Ludovic Nobili) and John Wilson's SMBC data-centre role.
- **Gaps:**
  - No LinkedIn found for Jess Tomlinson (Lloyds) or MGX's CEO.
  - Several titles come from Apollo only (marked "Partly verified").
  - Nick Donias has moved from SMBC to Goldman Sachs.
  - No 2026 data-centre deal was found for CIBC, NAB or OCBC in the US.

## Update 5 Nov: Abu Dhabi capital, more lenders like Standard Chartered, and missing contact LinkedIn profiles
- **`abu-dhabi-capital.csv`:** 42 Abu Dhabi and UAE banks, sovereign funds, holding companies and global credit or infrastructure funds with Abu Dhabi offices that finance data centres, GPU clouds or AI infrastructure.
  - Tier A (13) is active in Raion's markets in 2025–26. Top picks:
    - Blue Owl: lender on Nscale's GPU-backed loan; ADGM office since Jun 2026.
    - ADIC: backed Nscale's $3.36bn pre-IPO notes.
    - Mubadala Capital: co-led Crusoe's Series E.
    - HSBC UAE: Core42's $550m.
    - Stonepeak, Partners Group, Harrison Street and EQT.
  - Spot-checked: ADIC–Nscale (Sep 2026) and Blue Owl's ADGM office.
- **`lenders.csv`:** 24 more lenders "like Standard Chartered" (real-estate or infrastructure desks that financed data centres in 2025–26):
  - Aareal Bank: its first data-centre loan, from a new dedicated unit.
  - US banks: Wells Fargo (its CRE Specialty Capital group), Citizens, First Citizens, Truist, PNC, U.S. Bank and regional banks.
  - Canadian banks: TD, Scotiabank and National Bank of Canada.
  - European banks: UniCredit, Intesa, NORD/LB and LBBW.
  - Debt funds: ICG (a £750m London data centre), AllianzGI, Infranity, Brookfield Infrastructure Debt, Rivage, AXA IM Alts, F2i, Apollo and Starwood.
  - Asian banks: DBS, UOB and Maybank.
  - Israel: Mizrahi-Tefahot.
  - Spot-checked: Aareal–Goodman, DataBank's $800m syndicate and First Citizens–T5.
- **Missing contact LinkedIn:** Apollo filled most gaps across all tabs, using 63 credits in total. The monthly Apollo allowance is now used up and resets on 25 Nov 2026.
- **Contact moves found:**
  - Kristin Khanna: Barclays to QTS.
  - Pri McNair: left Emirates NBD.
  - François Regnier: left BNP Paribas.
  - Nick Donias: SMBC to Goldman Sachs.

## Update 5 Nov: top 10 new UK/London data-centre financiers
`uk-top10-dc-financiers.csv` (also Lenders rows 59–68) ranks the 10 best new UK financiers for Raion:
1. OakNorth: £25m DataVita AI data-centre loan
2. National Wealth Fund
3. Legal & General
4. Siemens Financial Services
5. Investec
6. Barclays
7. InfraRed
8. 3i Infrastructure
9. USS
10. Scottish National Investment Bank

Contact LinkedIn URLs were taken from LinkedIn-restricted web search results, because Apollo, Explorium and Apify had no credits left. A URL was found for 9 of the 10; there is none for USS's Ben Levenstein. No London private-credit fund lending against GPUs was found: the GPU-backed loans traced went to lenders already listed.

## Update 10 Nov: next 10 data-centre / GPU financiers (banks that fund data centres first)
`next10-dc-financiers-banks-first.csv` (also Lenders rows 84–93). Following the preference for banks that fund data centres, 7 of the 10 are banks:
1. BBVA: AtlasEdge €1.2bn lender; structuring bank on Switch's $2.6bn facility; London project-finance head
2. Nordic Investment Bank: €22m GPU loan to Verda (Jul 2026)
3. La Banque Postale: one of seven banks on Mistral's $830m GPU debt
4. KfW IPEX-Bank: AtlasEdge lender; London branch infrastructure team
5. EBRD: London HQ; $14–70m data-centre loans in its countries
6. CIBC: joint lead arranger on Switch's $2.6bn facility
7. EIB: €1bn Mistral GPU project financing under appraisal (not signed)
8. Silver Point Capital: co-lender on NexGen Cloud's $106m GPU loan
9. Future Growth Capital: £20m nLighten UK edge data-centre loan
10. GLIL Infrastructure: buying a majority stake in Yondr's Slough campus (equity)

Lenders column O ("Preference") flags every bank with a data-centre deal. Contact LinkedIn was found for 8 of 10 (none for KfW's Linda Zahri or for GLIL). Left out: NIBC (an ABN AMRO subsidiary since 3 Aug 2026), Bank of Ireland (its €1.85bn deal could not be confirmed), and Alpha Bank and NatWest (each named as an AtlasEdge lender in one source only). Silver Point is a London private-credit lender against GPUs, which the 5 Nov search had not found.
