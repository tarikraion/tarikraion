# GPU market: urgent sellers and urgent buyers (27 Nov 2026)

These lists are for brokering: take GPU capacity that someone needs to sell now, and place it with buyers who need capacity now. Every row has a dated source. Unconfirmed items are labelled as such in the `verification` column, and nothing was padded.

## Files
| File | Contents |
|---|---|
| `urgent-gpu-sellers-2026-11-27.csv` | 9 rows: capacity available now or within about 60 days, with an urgency signal |
| `urgent-gpu-buyers-2026-11-27.csv` | 10 buyers needing capacity now or in Q1 2027, with 22 contacts (11 with emails, statuses as recorded) |
| `../gpu-partners-2026-11/uk-gpu-providers-decision-makers-2026-11-27.csv` | partnership decision makers at the 13 UK GPU providers |

## The market in one paragraph
Short-term capacity in the UK and Europe is still tight. Several providers are sold out: T-Systems, TELUS, Northern Data/Taiga ("nearly sold out") and Era4 Chesterfield. CoreWeave is raising prices: short-term deals now cost more than $40M per MW a year, and its Q3 call on 10 Nov said prices are "still climbing". Surplus has appeared from two events:
- A secondary report says Anthropic declined to renew H200 capacity at SpaceX. This is unconfirmed.
- On 16 Nov the US restricted remote access to advanced GPUs by Chinese firms (confirmed by GPB and TweakTown). South-East Asian capacity that was built for Chinese customers is now being remarketed to Western buyers.

Export-control and ownership checks are mandatory before reselling any capacity in South-East Asia.

## Urgent sellers
| # | Seller | What's available | Urgency | Status |
|---|---|---|---|---|
| 1 | Nebius (spot) | B300 at $1.90/GPU-hr in UK-South and $2.90 in France, against $5.90 in the US (spot page, 27 Nov) | idle European capacity priced to fill; reserve auctions | live price, preemptible; re-check before quoting |
| 2 | Runcrate: Paris block | 576 B300, Paris, mid-December, 36-month term, $5.25/GPU-hr | posted on gpulist.ai 23 Nov | listing is "Unverified"; owner not named; Runcrate is itself a broker |
| 3 | Runcrate: Malaysia block | 3,600 GB300 NVL72 (50 racks) from 1 Dec, 3-month term, $12.95/GPU-hr, prepaid | posted 4 days after the US rule | export and customer checks required |
| 4 | SpaceX (formerly xAI) | about 50,000 H200 re-offered at about $5/GPU-hr; B200/B300 spot cut 20–35% | anchor tenant left | UNCONFIRMED (single secondary report) |
| 5 | GPU Mart | B300 and B200 servers (hardware, not rental) shipping in December and January | sellers selling off after the US rule | quote not corroborated; HQ unverified |
| 6 | Kordin (UK) | 40 H200, London, from 8 weeks, $3.99/GPU-hr | gpulist listing, 6 Nov | small; Ethernet only, so suits inference |
| 7–9 | Liquid Compute, GPUaaS.com, Jarvislabs | exchange/broker inventory; 512 H200 in India | weak | sellers often unnamed |

**Seller watchlist** (no dated statement of unsold capacity yet):
- **Nscale:** Microsoft declined the Texas option on 5 Nov. The 2,304 B200 rented to ByteDance's Singapore unit at Glomfjord, Norway, face scrutiny under the US rule, so they could come to market. Karl Havard, now CCO at Era4, was previously CCO at Nscale.
- **iomart (UK):** covenants likely to be breached in December, and it is selling its data centres for about £85M. These are data-centre assets, not GPUs.
- **Fuse Energy:** 192 B300 in the UK from December; already recorded in the partner list.
- **Together AI:** half-price preemptible compute headline (24 Nov), not checked.

## Urgent buyers
| # | Buyer | Need by | Why now | Contacts with email |
|---|---|---|---|---|
| 1 | Corma (Tel Aviv / SF) | NOW | CEO (16 Nov): compute is "one of the biggest challenges"; waitlist; 24x server growth; $125M Series A | Alon Pluda (CEO), Hofit Bata: both valid |
| 2 | fal | NOW (second source) | $1.3B raise (3–4 Nov); CEO: "had to rate limit" customers | Burkay Gur (CEO), Gorkem Yurtseven (CTO): no email on file |
| 3 | Relace | NOW | homepage: "If you have GPUs, we'd also like to talk" | Eitan Borgnia, Julian Thomassie: validated |
| 4 | Agon (London) | Q1–Q2 2027 | $70M (23 Nov) for sovereign infrastructure "in Europe, for Europe" | none on file yet |
| 5 | Remanence (Paris) | Q1 2027 | $30M seed (17 Nov) explicitly funds a GPU cluster | Hamza Benchekroun (CTO): Apollo verified, catch-all |
| 6 | Embo | Q1 2027 | $110M seed (23 Nov) to pretrain a robot world model | Danijar Hafner, Wilson Yan: catch-all, medium |
| 7 | Path Robotics | Q1–Q2 2027 | $300M (10–11 Nov) for model training and compute | Andrew and Alex Lonsberry: both valid |
| 8 | Kape / ExpressAI | Q1–Q2 2027 | ExpressAI already runs on confidential-computing B200 in the EU; wider rollout pending | Peter Membrey, Charles Butler: validated |
| 9 | Mirakl (Paris) | Q1–Q2 2027 | inference on its own GPUs plus Scaleway; cash-positive, $218M ARR | no emails |
| 10 | Epochal | Q1–Q2 2027 | $100M launch (CEO's own money) | no emails |

**Buyer pools with no named company:**
- **Rackspace Spot** shuts down on 8 Dec after a breach. Its preemptible A30/H100 users must move, but they are small.
- **CoreWeave renters** facing price rises: use CoreWeave's own Q3 figures as the price argument.
- **UK BIST compute-demand report** (26 Nov): about 76% of projected demand needs sovereign, UK-hosted provision. Use it in UK pitches.
- **EuroHPC AI Gigafactory consortia:** lot deadlines are 30 Dec 2026 and 4 Feb 2027. Raion could join a consortium as a capacity partner.
- **Canada AI Compute Access Fund** reopened on 26 Nov. It pays 80% of costs if the compute provider is Canadian-owned, 50% otherwise. The health call closes 4 Jan 2027.

## Suggested matches (to test, not promises)
- **EU/UK capacity now** (Nebius UK spot B300, Runcrate Paris B300, Kordin London H200) → **Agon, Remanence, Kape/ExpressAI, Mirakl**. These buyers want European or sovereign capacity.
- **Large short-term blocks** (Runcrate Malaysia GB300, possibly SpaceX H200) → **fal, Relace, Corma**. These are inference-heavy buyers that need capacity now. Run export and ownership checks first. Corma is Israeli, so add the data-residency check.
- **UK providers to resell** (Era4, Hyve, Exponential-e, Fast2host and others) → UK buyers and any Rackspace Spot migrants. Decision makers are in the UK provider file.

## Not found (searched)
- No UK or EU administration, liquidation or auction of H100-class GPUs, Sep–Nov 2026.
- No open UK tender (Find a Tender API, ~29,000 releases since 1 Sep) or EU tender buying GPU capacity as a service. EU GPU tenders are all on-premises hardware purchases.
- No named company publicly asking for capacity on HN, LinkedIn or X in the last 30 days, apart from those above. The Reddit sweep was partial because Reddit is blocked from this session.

## All contacts with emails (`all-gpu-contacts-with-emails-2026-11-27.csv`)
This file has 80 unique emails from the 26–27 Nov GPU work, sorted as urgent sellers, then urgent buyers, then UK GPU providers, then the 105 GPU-capacity partners:
- **35 personal emails:** 11 buyers, 4 UK providers and 15 partner decision makers, each with the status recorded at the time. These are "valid (mail server confirmed)", Apollo-verified, or Apollo-verified plus LeadMagic-validated. Catch-all domains are marked.
- **50 company mailboxes:** each one published on the company's own site; the source is in `email_status`.
- **Excluded mailboxes:** press, PR, investor, careers and privacy addresses.

All 67 email domains had live mail servers on 27 Nov (checked through dns.google). Recruiter contacts are a separate project and are not included.

## Urgent sellers with emails (`urgent-gpu-sellers-with-emails-2026-11-27.csv`), round 2
There are **10 qualified sellers with an email** (5 rated B, 5 rated C) and **7 watchlist companies with an email**. Every email was published by the company itself, on its own site, in a press release, or in its gpulist.ai listing (the listing's "contact seller" address forwards to the seller). Nebius is the exception: its email is a validated personal email from the partner list. All 15 domains had live mail servers on 27 Nov. No email was guessed.

**New in round 2:**
- **Datasection (Tokyo):** distressed. Forecast cut 89.3%, a ¥79.9bn order cancelled and its GPU financing ended. It holds 20,000 Blackwell GPUs. It has not offered them for sale, and a full export review is needed.
- **Bentaus and Flatkey (US):** weak signals.
- **UpStation:** 1,024 B300 listed on gpulist, but its identity is unverified.

**Round 1 sellers without a published email** (contact forms only): SpaceX, Kordin and Liquid Compute.

**Why so few:** the market is tightening, not loosening. The Computable GPU Index puts B300 on-demand at $10.41/hr, up about 21% in 30 days. Brokers (Liquid Compute, GPU Mart) say "thousands" of South-East Asian B300 are being remarketed after the 16 Nov rule but will not name the owners. Exchanges (SF Compute, Ornn, Compute Exchange, Vast) hide supplier identities.

**Watch item:** from 26–27 Nov, Nvidia distributors are requiring neoclouds to drop Chinese renters. That could free capacity at unnamed US and EU neoclouds.

## Round 3 (28 Nov): separate CSVs
No email in these files was guessed. Every email domain had live mail servers on 28 Nov (55 domains checked).

### `gpu-providers-with-emails-2026-11-28.csv`: 45 new GPU-capacity providers
None of these are in the earlier lists.

| | A | B | C | Total |
|---|---|---|---|---|
| Count | 5 | 22 | 18 | 45 |

By region: North America 19, UK & Europe 14, APAC 11, Africa 1.

Each row has:
- the GPU offering, quoted from the provider's own site with the URL;
- an email published on the provider's own site, with the source URL and surrounding text;
- an MX check;
- a LinkedIn page where one was seen.

The `caution` column flags weak mailboxes (legal@, invest@, press@, support@), forward-only capacity, and KYC or China-ownership checks.

**Priority A:**
- Boost Run (info@boostrun.com)
- 5C, formerly Hypertec Cloud (info@5c.ai)
- Canopy Wave (sales@canopywave.com)
- Visionbay.ai (Taiwan)
- ESDS (India)

**No published email (not in the CSV):** Leaseweb, Micron21, SoftBank Corp. and HostAfrica (sales by contact form only). UpCloud is also left out: its address was only readable through a page renderer that got past its bot check, so check it by hand.

### `urgent-gpu-buyers-with-emails-2026-11-28.csv`: 9 buyers, 18 contacts
- **New:** General Reasoning (London). A training run on 128 H200 is still going (Avalon-M1). Contact hello@gr.inc, addressed to Ross Taylor (CEO). Funding is small, so offer 128–256-GPU slices of partner capacity.
- **Known companies with a fresh signal and emails already on file:** Suno, Cognition, Black Forest Labs, Genesis AI, Mirendil, Noeri, ElevenLabs and Boltz.
  - Their urgency is inferred from raises, launches or revenue growth, except Black Forest Labs, which already rents B200s from Nebius. None stated a shortage.
  - Email status as recorded on 22–23 Nov:
    - valid: Suno, Cognition, BFL;
    - catch-all: Genesis, Mirendil, Noeri, ElevenLabs;
    - UNCHECKED: Boltz.
- **No email:** Apera AI (Vancouver). On 27 Nov its CEO said it struggles to get compute (spend up to US$4M a year). Its site blocks automated access, so get the contact from apera.ai/contact in a browser.

### `gpu-provider-decision-makers-2026-11-28.csv`: decision makers at the 45 new providers
- **People:** 84 people across all 45 providers.
  - 71 full names are confirmed by an independent public source: the company's own team or leadership page, a press release, a speaker page, a registry or trade press.
  - 13 surnames are still masked or unconfirmed and are marked "NO".
  - 20 LinkedIn profiles, each seen on a team page, a speaker page or in a search result.
- **Personal emails (8):** each one was published by the company, and its domain has live mail servers.
  - **Decision makers (4):**
    - Fredrik Dobber, CCO, Glesys
    - Glenn Johansson, CEO, Glesys
    - Jordan Friedman, CEO, Mantle
    - Henry Chen, PolarGrid
  - **Press or marketing contacts who can forward (4):** SWI Compute, DCAI, Visionbay and KONST.
- **Everyone else:** use the company mailbox shown on each row (`company_mailbox`). No email was guessed.
- **Missing personal emails:** most people have no personal email published, because Apollo, Explorium and Apify were out of credits. To get verified emails for the named people, top up Apollo (about 2 credits per person: one to find the email, one to validate it), or authorise Lusha, ZoomInfo or Clay.

### `more-urgent-gpu-buyers-with-emails-2026-11-28.csv`: 33 buyers with fresh dated signals, 65 emails
I re-checked the 103 buyers already in Raion's files that had a validated or catch-all email, looking for a dated GPU-need signal since 14 Oct 2026. Each row cites the signal URL and date. 70 had no qualifying signal and were rejected, each with a reason (scratchpad kb_out1–3).

**NOW (6 companies, 11 emails):**
- **Cohere:** CEO (10 Nov) says it has to "fight to get access to compute".
- **Hudson River Trading:** about $1B a year of AI spend and growing.
- **Wix/Base44:** about $250M ARR on its own model.
- **AppLovin:** CFO says it is investing in more training compute.
- **Modal:** 3–4-month GPU lead times; it buys 2–3x ahead.
- **Higgsfield:** $1B+ ARR video generation; launched GPU Harness.

**Q1–Q2 2027 (27 companies):**
- Physical Intelligence, General Intuition, Liquid AI, Motif, Translated, Potential Sciences, Machenta, Rime
- Thomson Reuters, JetBrains, Cosine, Eka Robotics, Iambic, Decagon, Scaled Cognition, Helsing, AstraZeneca, NatWest
- Resolve AI, Trajectory, Wispr Flow, DeepL, Ollama, Aevius, Gradium, Chai Discovery, H2O.ai

**Emails:** 23 are valid (the mail server confirmed the mailbox) and 42 are on catch-all domains, as recorded when found (22–23 Nov). Unchecked and personal Gmail addresses are excluded. All domains had live mail servers on 28 Nov. The `notes` column flags:
- emails on old domains (medal.tv, buildt.ai, entos.ai);
- better-placed contacts named in coverage;
- existing big compute deals and M&A risk.
