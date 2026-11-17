# NVIDIA engineers with 5+ years (17 Nov 2026)

`nvidia-5yr-engineers-2026-11-17.csv`: 26 current and 3 former NVIDIA engineers in roles relevant to a GPU-capacity provider (GPU cloud, DGX, data-centre power, networking, HPC, solutions architecture).

How it was built:
- **Candidates:** Apollo people search (no credits used), filtered to people at NVIDIA who have held their current title for 5+ years: about 117 records across UK/EU, Israel and US/Canada. Apollo masks surnames.
- **Name and LinkedIn:** resolved through LinkedIn-restricted web searches. A URL is listed only if it appeared in a search result.
- **Cross-check:** each resolved full name was searched in Apollo again with the 5+ year filter, to confirm it is the same long-tenure record.

Confidence:
- **High:** tenure is shown by a dated public source (LinkedIn dates, a conference talk, an NVIDIA blog or docs bio).
- **Medium-high:** the name and LinkedIn are resolved, and Apollo shows 5+ years in the current title for that exact name.
- **Medium:** a single source, or conflicting details.

Mellanox staff (Israel) count from the April 2020 acquisition; earlier Mellanox years are noted.

No emails, phone numbers or addresses were collected. About 30 Apollo candidates could not be resolved to a full name, because Apollo masks surnames and the search tool strips names from many queries.

## Round 2 (17 Nov 2026): `nvidia-5yr-people-round2-2026-11-17.csv`

This round adds 46 more people, all currently at NVIDIA, with none repeated from round 1. Unlike round 1, it includes business-side people (alliances, cloud-provider business development, partner/channel, data-centre acquisitions) alongside engineers.

| Group | People |
|---|---|
| EU technical | 14 |
| Israel networking/cloud (mostly ex-Mellanox) | 12 |
| US data centre / GPU cloud | 8 |
| EU partners/sales | 8 |
| US cloud partners/leaders | 4 |

**Confidence:** 14 high, 27 medium-high, 5 medium.

How it was built:
- **Candidates:** a new Apollo pull (no credits used) of NVIDIA staff with 5+ years in their current title, about 2,000 records across UK/EU, US/Canada and Israel. From these, 88 people were shortlisted, excluding everyone in round 1 and its unresolved list.
- **Names and LinkedIn:** resolved with LinkedIn-restricted web searches. A URL is listed only if it appeared in a result.
- **Extra check:** all 41 LinkedIn URLs were fed back into Apollo's free LinkedIn-URL filter, together with the NVIDIA and 5+ year filters. Every one returned the same long-tenure record, so the profile, the name and the tenure belong to one person.

Ratings adjusted conservatively:
- **Downgraded to medium-high:** Ariel Kit, Arik Kol and Eyal Babish, because their dated evidence came only from search summaries.
- **Needs a manual check:** Christi DeCuir. Her LinkedIn headline now reads "Sr. Director, Robotics Strategic Alliances", so Apollo's title may be stale.

**Unresolved:** 42 shortlisted people could not be matched to a full name. The search tool strips first names from people queries, and Apollo masks surnames. Revealing them would need Apollo enrichment credits, which reset on 25 Nov.

## Rounds 3 and 4 (17 Nov 2026)

New method in these rounds:
1. **Harvest:** LinkedIn-restricted searches collected NVIDIA profile URLs by role and place.
2. **Bulk check:** the URLs went through Apollo's free LinkedIn-URL filter, combined with the nvidia.com and 5+ years-in-current-title filters. Only profiles Apollo returned were kept, and each record's first name and surname mask had to match the profile name.
3. **Re-check:** every URL was checked again before saving. All passed.

The method is strict. Someone who has been at NVIDIA a long time but changed title less than 5 years ago does not pass, so the list leans towards stable roles.

**Round 3:** `nvidia-5yr-people-round3-2026-11-17.csv`
- 47 people: US/Canada 16, UK 8, continental Europe 18, other 4, and 1 former (Gary Hicok, 25 years at NVIDIA).
- Name + LinkedIn: `nvidia-5yr-people-round3-names-linkedin.csv`.

**Round 4:** `nvidia-5yr-people-round4-2026-11-17.csv`
- 166 people: Israel 35, India/APAC 33, leadership 29, US DGX/sales/SA 29, US networking 25, EMEA 15.
- The `raion_relevant` column marks 143 as yes; the other 23 are in HR, finance, audit, chip design and similar roles.
- Name + LinkedIn: `nvidia-5yr-people-round4-names-linkedin.csv`.

**Flagged for a manual check:**
- David Hogan (round 3): his profile headline doesn't mention NVIDIA.
- Keiko Wakabayashi (round 4): sources disagree on whether she is still at NVIDIA.
- Fredrik Liljegren (round 4): his Apollo title is informal ("Chief Happiness Manager").

**Known limitation:** in one case (Jean Baptiste Riaux, dropped), Apollo's 5+ year tenure conflicted with a recent "joined from Groq" post. Rows rated medium-high rest on Apollo's tenure data.

**Cumulative total:** 29 + 46 + 47 + 166 = 288 people.
