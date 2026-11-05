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
