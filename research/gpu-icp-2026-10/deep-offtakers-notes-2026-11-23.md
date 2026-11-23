# Smaller GPU offtakers and GPU tenders: deep research, 23 Nov 2026

**The request:** smaller startups that have raised money for GPU capacity, plus public tenders for GPU capacity.
- UK preferred, but anywhere in the world is allowed (sanctioned countries excluded).
- They must need capacity now or within 3–6 months.
- Each one needs contact emails.

## Result

- **Buyers:** 11 verified, 3 of them in the UK.
- **Contacts:** 27 decision makers, 19 with a LinkedIn URL.
- **Emails:**
  - 20 personal work emails: 16 high confidence, 4 medium.
  - 16 published company or tender mailboxes.

| # | Buyer | Where | Type | Tier / when | Why now | Emails |
|---|---|---|---|---|---|---|
| 1 | Anam | London | startup | B / now | Its real-time avatars run on live GPU inference. It signed a CoreWeave GPU deal in Jul 2026 and released new models in Oct–Nov 2026 | caoimhe@anam.ai (CEO), ben@anam.ai (CTO) |
| 2 | Qureight | Cambridge | startup | B / now | Its $20M Series B (29 Jul 2026) pays for an AI imaging lab and a 3D chest foundation model. Staff are set to double to 100 by Dec 2026 | m.thillai@qureight.com (CEO), m.monteiro@qureight.com (ML lead) |
| 3 | SUPC framework ITS4065 SU | Reading | tender | B / 3–6 months | £3bn university framework for servers, storage, HPC and managed infrastructure. The tender is overdue; start 1 Feb 2027. Lot 4 allows hosted capacity | a.rashad@sums.ac.uk (named contact); SUPC@sums.ac.uk |
| 4 | RoboTruck | Tokyo | grant + startup | A / now | A GENIAC government grant (May 2026) to train a trucking world model on "large-scale GPU compute", plus a JPY 5.2bn Series A that lists compute among its uses | info@robotruck.jp (no personal email found) |
| 5 | Motif Technologies | Seoul | startup | A / 3–6 months | Its Series B pays for next-generation infrastructure for 310B VLM and 320B VLA models. It lost its government GPU allocation on 18 Aug 2026, and Motif 4 work has started | contact@motiftech.io |
| 6 | Embo | San Francisco | startup | B / now | $110M seed (23 Nov 2026) to pretrain a robot world model from scratch on internet-scale video | danijar.hafner@embo.com, wilson.yan@embo.com (medium) |
| 7 | Aevius | Boston | startup | B / now | $22M seed (17 Nov 2026) for multimodal medical foundation models | rowland@aevius.ai, ming@aevius.ai (medium) |
| 8 | Leibniz Universität Hannover, Soofi II | Hannover | tender | B / now | Its tender for 1,024 B200/B300-class and 2,048 GB200/GB300 GPUs got zero bids (3 Nov 2026). It may be re-run without a new public notice | nejdl@l3s.de, gottschalk@l3s.de, sandipan.sikdar@l3s.de; vergabe.hannover@luther-lawfirm.com |
| 9 | Network Bio | Palo Alto | startup | B / 3–6 months | $50M (Aug 2026). It is scaling training of its cfRNA foundation model with NVIDIA | asad@network.bio (CEO), mehran.karimzadeh@network.bio (Head of AI) |
| 10 | ValkaAI | Prague | startup | B / 3–6 months | €13M pre-seed to "scale computational infrastructure" for real-time generative video personas | vlastimil.venclik@valka.ai (CEO), milos.lokajicek@valka.ai, michal.kubista@valka.ai |
| 11 | Gnani.ai | Bengaluru | startup | B / 3–6 months | CEO, 5 Sep 2026: "The key constraint has been GPUs". A 70B model is due around Feb 2027 | ganeshg@gnani.ai (CEO), ananth@gnani.ai (CTO), bharath.shankar@gnani.ai |

**Tier:**
- A = there is explicit evidence that money is going to compute, and at least $15M has been raised.
- B = the evidence is strong but implicit, or the company has raised $10–15M.

Read the `fit_caveats` column before pitching. It records the main limits:
- RoboTruck's grant compute was already fixed in its proposal.
- The Hannover lots are short bursts, and their start dates are earlier than Raion's go-live.
- Gnani.ai's core training runs on subsidised Indian GPUs.
- Anam already rents from CoreWeave.
- Network Bio's compute need is still small.

## Files

| File | What it is |
|---|---|
| `deep-offtakers-2026-11-23.csv` | One row per contact (27 rows), best first. It holds:<br>• company facts and why they need GPUs now<br>• compute evidence: a dated quote and its URL<br>• size estimate, data residency and fit caveats<br>• tender details and published company mailboxes<br>• the contact, where the title was confirmed, and LinkedIn<br>• email, confidence, the mail-server check, how it was found, alternates and sources |
| `deep-offtakers-emails-2026-11-23.csv` | Emails only (36 rows), in this order:<br>• 20 personal emails<br>• 1 shared mailbox named for a contact<br>• 15 company or tender mailboxes |
| `deep-offtakers-notes-2026-11-23.md` | This file |

## How the buyers were found and checked

**Searches.** 19 search angles, run in six batches:
- UK startups (twice) and UK public buyers (twice);
- EU tenders and North American tenders;
- the German-language press, the French and Southern European press, and the Nordics, Benelux and Central/Eastern Europe;
- small US startups; US and Canadian science and robotics startups; US and Canadian media, voice and vertical-model startups;
- compute financing deals;
- India; Asia-Pacific; the Middle East, Africa and Latin America; Israel;
- public grants for compute;
- a second look at earlier rejects.

**Sources.**
- Tender portals:
  - Find a Tender and Contracts Finder (APIs);
  - TED (v3 API);
  - SAM.gov;
  - CanadaBuys open data.
- News: Google News and Bing News feeds.
- Company sites and press releases.
- Government grant pages: NEDO/GENIAC, IndiaAI and the UK Sovereign AI Unit.
- National tech press, such as CTech, Unicorn Factory and BusinessCloud.

**Checks.**
- Every candidate was checked against all earlier Raion lists and reject files, so nothing here repeats an earlier list.
- A second, independent agent then reopened every source and rejected anything it could not confirm.
- 14 candidates were proposed and 11 kept. The checkers rejected 3:
  - Dream: no dated GPU need.
  - AegisAI: a compact security model with no capacity signal.
  - The UK National Nuclear Laboratory partnership: its timing could not be confirmed.
- More than 280 other names were screened out during the search, for one of these reasons:
  - already in Raion lists;
  - too small;
  - app layer only;
  - acquired;
  - a neocloud or chipmaker;
  - no dated GPU need.

**The UK is nearly exhausted.** Almost every UK startup with a 2026 compute signal is already in earlier Raion lists. This round adds Anam, Qureight and the SUPC framework.

## How the contacts and emails were found

**Names and titles** come from company sites, 2026 press releases and LinkedIn result titles. A LinkedIn URL was used only when it appeared in a search result tied to the company. None was guessed.

**Where the emails come from:**
1. Addresses published on company, university or tender pages, copied verbatim: the L3S Soofi page, Find a Tender, TED and press-release contact blocks.
2. Email databases:
   - harvestapi covered 10 priority profiles;
   - vulnv covered 6 more;
   - Dievio returned no emails;
   - b2bsearch has used up its free allowance until 1 Dec;
   - snipercoder failed to run.

**Checks.**
- Every address was run through bounceverify.
- Twice, bounceverify said a domain did not exist when DNS shows working mail servers (zuv.uni-hannover.de and bwh.harvard.edu). Those two addresses are marked "not confirmed", not "invalid".

**Confidence levels:**
- **High:** either the mail server confirmed the mailbox at the current employer's domain, or the employer published the address itself.
- **Medium:** one database, on a server that accepts any address (Embo and Aevius).

**Addresses not used as the main email:**
- Personal or academic addresses are kept only as alternates, with a warning:
  - mail@danijar.com
  - wilson1.yan@berkeley.edu
  - hani@arcinstitute.org
  - FaisalMahmood@bwh.harvard.edu
- PR-agency, legal and security mailboxes are left out.

No address was guessed or built from a pattern.

**Contacts without a personal email (7):**
- Qureight's CTO Darren Gallagher.
- Mark Lewis at SUPC, who has only a shared mailbox.
- Motif's CEO.
- RoboTruck's CEO and founder.
- Network Bio's Hani Goodarzi.
- Aevius's Faisal Mahmood.

## Watch leads (not qualified today)

**UK**
- **Sovereign AI Unit startup call** (Oct 2026): up to 1M Isambard-AI GPU hours per startup. It closed 6 Nov, and recipients are not named yet. The Sovereign AI Fund was topped up to £560M on 24 Oct 2026.
- **Agon** (London) is already in Raion lists. On 23 Nov 2026 it raised a further $70M, with the Sovereign AI Unit and NSSIF investing, for defence AI models. Refresh its existing record.
- **University of Exeter, Digital Research Infrastructure** (FTS 081584-2025):
  - £8.3M ex VAT, with the contract estimated at 1 Aug 2026 to 2031;
  - the tender notice has not been published;
  - published contact: Simon Denton, s.denton@exeter.ac.uk.
- **UK National Nuclear Laboratory, NACIP** (FTS 062236-2026): access to HPC and AI/ML compute, worth about £500k over 2 years. The tender is about 4 months overdue.
- **Mantic** ($25M seed, Sep 2026) adapts other labs' models. **Hiverge**'s Series A is pending, and its compute sits with its customers. Recheck both if they start their own training runs.

**EU**
- **SWR, for the ARD broadcasters** (TED 776095-2026):
  - a €44.15M sovereign-cloud framework;
  - participation deadline 7 Dec 2026, with service from 16 Jun 2027;
  - no GPUs are named in its scope;
  - contact: vergabe-it@swr.de.

**US and Canada**
- **DARPA NODES:** a Phase II GPU re-buy around Mar 2027 is plausible. Phase I rented 50 dedicated H100-class GPUs plus 100 in reserve. Published contact: nodes@darpa.mil.
- **Shared Services Canada, Sovereign Cloud Invitation to Qualify:** the second intake closes 31 Jan 2027. It requires Canadian ownership and control.
- **Vivodyne and Transfyr:** recheck if they raise a new round or make a compute statement.

**Rest of the world**
- **Turing Inc.** (Tokyo) passes the rules, but it already gets compute through strategic investors (AMD, GMO).
- **WideLabs** (São Paulo) is closing a $50M Series A for "models and GPUs". Recheck when it closes.
- Also worth watching:
  - CNTXT AI (Abu Dhabi);
  - Scala Biodesign (Israel);
  - an unnamed Israeli "neolab" founded by an ex-Meta researcher (Haaretz, 17 Sep 2026).

## Limits this round

- **Apify:** about $0.10 is left until the monthly cycle resets on 22 Dec.
- **Other resources:**
  - Crunchbase is out until 1 Dec.
  - Apollo credits reset 25 Nov. From then, Apollo could try the 7 contacts without a personal email.
  - Explorium has no credits.
- **Blocked sources:** Business Wire returned 403. Bing web search through curl was unusable. A few EU press sites refused connections.
