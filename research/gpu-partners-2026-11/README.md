# GPU-capacity partners like OVHcloud (26 Nov 2026)

These are companies that **already sell GPU capacity**, where Raion could:
- sell them capacity wholesale;
- resell through their channel;
- co-sell; or
- place clients on their capacity (overflow).

**File:** `gpu-capacity-partners-2026-11-26.csv`

The list has **105 target companies**. OVHcloud is included as a reference row only, at rank 106.

| Region | Count |
|---|---|
| Europe | 32 (incl. the OVHcloud reference row) |
| North America | 28 |
| Rest of world | 25 |
| UK & Ireland | 21 |

**Priority:** 55 are A, 35 are B and 15 are C. Rows are ranked by priority; within each priority, rows with a decision-maker email come first.

**Every row has:**
- an evidence URL and a quote showing the GPU offering;
- the company's scale;
- its latest dated signal;
- the partner angle;
- the partner-programme URL, if it has one;
- its published contact route;
- a named leader.

**Not included:**
- sanctioned-country HQs;
- Easy Compute, which was dropped for weak evidence.

## Partnership decision makers with validated emails (15)

Every email below is Apollo "verified" and LeadMagic "validated" (26 Nov 2026). Six are on catch-all domains (marked †), where acceptance is confirmed but a bounce is still possible.

| # | Company | Contact | Title | Email |
|---|---|---|---|---|
| 1 | CloudFerro | Johann Baermann | Head of Partnerships | jbaermann@cloudferro.com † |
| 2 | evroc | Andreas Jonsson | Co-Founder & VP Business Development | ajonsson@evroc.com |
| 3 | Exoscale | Maxime Gerard | Head of Channel Operations & Head of Sales Switzerland | maxime.gerard@exoscale.ch |
| 4 | Nebius | Matthieu Bienvenu | Head of Business Development | mbienvenu@nebius.com |
| 5 | Scaleway | Orlando Bocaly | Head of Business Development | obocaly@scaleway.com † |
| 6 | CoreWeave | Seann G. (Apollo gives only the surname initial) | Head of Partnerships | sgardiner@coreweave.com † |
| 7 | DigitalOcean | Laura Littman | VP Business Development | llittman@digitalocean.com † |
| 8 | Runpod | Colby Henderson | Head of Partnerships | colby.henderson@runpod.io † |
| 9 | WhiteFiber | Richard Huang | "AI Infrastructure" (check title before outreach) | richardhuang@whitefiber.com |
| 10 | Core42 (G42) | Ahmed Labib | VP Partnerships & Ecosystems | ahmed.labib@core42.ai |
| 11 | Megaport / Latitude.sh | Bernice Chioua | EMEA Channel Director | bernice.chiouavanwaes@megaport.com |
| 12 | NxtGen | Rashmi Jaiswal | VP & Country Head, Channel Sales & Partnership | rashmi.jaiswal@nxtgen.com |
| 13 | Sharon AI | Shiv Radhakishun | Head of Partnerships & Alliances | shiv@sharonai.com |
| 14 | CUDO Compute | Pete Hill | Cofounder & VP Business Development | pete.hill@cudocompute.com |
| 15 | Nscale | Brian Dervan | VP Partnerships | brian.dervan@nscale.com † |

The other 90 companies have a named leader and a published contact route, such as a partner-programme page or contact form, but no decision-maker email yet. The Apollo credits ran out: 3 are left. To get one validated partnership email per remaining company, you need about 180 credits: 90 to find the contact and 90 to validate the email. The alternative is an Apify top-up after 22 Dec.

## Best partners to approach first (they have capacity gaps or are already buying capacity)

**They are short of capacity, so pitch wholesale:**
- **Deutsche Telekom / T-Systems:** the first phase of its Munich AI factory sold out (9 Nov).
- **TELUS:** its Rimouski site is sold out.
- **E2E Networks:** its Blackwell capacity is fully used.
- **Exoscale:** offers B300 only on request.
- **Nscale:** its UK campus capacity mostly lands in 2027 or later.
- **CoreWeave:** says it is contracting new capacity at higher prices.

**They are buying or funding capacity now:**
- **Verda:** raised $189M to "multiply compute capacity".
- **Nebul:** has more than 1,000 GB300 GPUs on order.
- **Runpod:** reached $325M ARR, about 3x since January.
- **WhiteFiber:** signed over $700M of new contracts.
- **QumulusAI:** bought 1,632 B300 GPUs.
- **SF Compute:** sold $245M of 36-month B300 deals.
- **HIVE / BUZZ HPC:** is signing offtake deals faster than its hardware arrives.

**They have channel programmes Raion can join:**
- **Core42:** launched its partner programme on 5 Oct.
- **Neysa:** launched its partner programme on 25 Nov.
- **NexGen / Hyperstack, Hydra Host, Hyperbolic and Vast.ai:** run supplier or reseller tracks.
- **Megaport / Latitude.sh:** runs reseller and agent programmes.
- **Civo:** signs dedicated-GPU deals before its own sites are ready.

**Channel tip:** NVIDIA's $250M of UK AI-safety compute will go through UK NVIDIA Cloud Partners (TFN, 15 Oct 2026). UK partners in this list (Nscale, NexGen, Civo, CUDO, Fluidstack) are the route in.

## Extra channel candidates (not in the CSV; found by the buyer research)
- **Morph:** sells GB300, B300 and B200 GPU-hours.
- **Pareto Inference:** rents B300 nodes.
- **Dapple:** builds GB300 sites.

## Reserves (not in the CSV)
Aruba, Elastx, ResetData, Akamai/Linode, Liquid Web, Prime Intellect, TensorDock and Salad.

## Rules followed
- No email or LinkedIn URL was guessed or built from a pattern. Masked surnames were not completed.
- Titles are as Apollo gives them, except where a column says otherwise.
- Web text was treated as data, not instructions.

---

# UK-based GPU providers to resell (added 26 Nov 2026)

**File:** `uk-gpu-providers-2026-11-26.csv`

These are **new** companies, none already in the 105-partner list above. The UK pool is small. The 21 UK and Ireland providers already listed (Nscale, NexGen/Hyperstack, Radiant/Ori, Civo, CUDO, Fluidstack, Fuse, DataPacket, Scan, iomart, Northflank, Deep Green and others) cover most of the real UK GPU fleets. I didn't pad the list.

**How each company was checked:**
- the GPU offer is quoted from the company's own site, and I re-fetched each page to confirm the quote;
- Companies House shows it as Active;
- the LinkedIn company URL was seen in the company's own website HTML and rechecked, unless the `linkedin_source` column says otherwise.

LinkedIn itself blocks automated checks, so no URL was opened on LinkedIn. No URL was guessed.

## UK HQ, verified (8)

| # | Company | Priority | GPU capacity | LinkedIn |
|---|---|---|---|---|
| 1 | Era4 (formerly Carbon3.ai), London | A | HGX B300. The 5 MW Chesterfield site is fully contracted to Fireworks. There is a pipeline of 40+ sites; Canterbury is approved and Newport is planned at up to 1 GW. | No company page found; posts appear under the handle "helloera4" |
| 2 | Hyve Managed Hosting, Brighton | B | H100, H200 and L40S GPU servers and GPU-as-a-service. Has a referral and reseller partner programme. | linkedin.com/company/hyve-managed-hosting |
| 3 | Exponential-e, London | B | "Private GPU Platforms as a Service" (sovereign). | linkedin.com/company/exponential-e (seen in a search result) |
| 4 | Fast2host (Fast4networks Ltd), St Ives, Cambridgeshire | B | Dedicated L4 to H100 and H200 servers in its own Cambridge data centre. | linkedin.com/company/fast2host-ltd |
| 5 | Nublue, Manchester | C | Managed NVIDIA GPU hosting; models are not named. | linkedin.com/company/nublue |
| 6 | Binary Racks, London | C | Dedicated T4, A2, A10, A30, A40, L4 and L40S servers. Has a reseller programme. | linkedin.com/company/binaryracks |
| 7 | Eco Web Hosting (Enix Ltd), Fareham | C | Ampere GPU dedicated servers from £500 a month. | linkedin.com/company/eco-web-hosting-ltd (from a directory only, so confirm it) |
| 8 | heata (Bit Warmer Ltd), Godalming | C | RTX 4090 at £0.89 per GPU-hour, on servers it runs in people's homes. | linkedin.com/company/heatacompute |

## UK-registered but run or controlled from abroad (3)

Confirm which entity actually signs contracts before treating these as UK.

| # | Company | Priority | GPU capacity | Abroad | LinkedIn |
|---|---|---|---|---|---|
| 9 | Runware Ltd, Harrow | A | HGX B300, GB300 NVL72 and Vera Rubin bare-metal clusters on its own modular data centres; serverless RTX PRO 6000. | 75%+ owned by Runware Inc (Delaware) | linkedin.com/company/runware |
| 10 | M247 Global Ltd, London | C | RTX A5000 dedicated servers. Has a commission-based partner programme. | Operations are in Bucharest; owned by Ares Management | linkedin.com/company/m247-global |
| 11 | Xesktop (GarageFarm.NET Ltd) | C | RTX PRO 6000 Blackwell at $0.99–1.99 per hour. | Team appears largely Poland-based | linkedin.com/company/garagefarm |

## Watchlist: UK HQ, but no live capacity yet (2 in the CSV)

| Company | Status | LinkedIn |
|---|---|---|
| Volta, London | NVIDIA Cloud Partner. Its first site is 133 MW of Vera Rubin capacity in Norway, with a $10B AI-lab contract. No go-live date. | linkedin.com/company/voltacompute |
| Greenweaver AI | Modular pods with heat reuse, about 75 MW from Q1 2027, all in continental Europe. | linkedin.com/company/11223836 |

These are on the watchlist but not in the CSV:
- **Chainergy:** first GPUs targeted for Q2 2027.
- **Nexus Core Systems:** sites still "in planning".
- **GigaGPU:** rents UK-hosted RTX GPUs, but no legal entity is named, so it couldn't be checked at Companies House.

## Checked and rejected: 90+ names

Each one is in the agent outputs with a reason. They fall into these groups:
- **Colocation only:** Kao Data, DataVita, Verne, Polar, GreenScale.
- **Hardware integrators:** Boston, OCF, Vespertec, XMA, BIOS IT, Server Factory.
- **MSPs with no GPU offer:** Redcentric, Node4, Six Degrees, ANS, Claranet (AI platform only).
- **Telcos:** BT (its capacity is built by Nscale), Vodafone, VMO2, Colt.
- **Brokers or aggregators with no fleet of their own:** GPU Rental Group, Canopy, Koi Compute, Yobitel.
- **Token-only networks:** NetMind, Flux (in administration).
- **Not credible:** ATAI Systems, Media Stream AI.
- **Not UK HQ:** UKDedicated (team.blue), Leaseweb, HOSTKEY, Define Tech, SeiMaxim, LeaderGPU, Oblivus (UK company dissolved).
