# Stand with Jensen: public supporters list (scraped 17 Nov 2026)

**Source:** the public supporters list at https://standwithjensen.com/ (robots.txt allows all paths). Collected through the JSON endpoint the page itself uses, `/api/signatures?page=N`, at 100 people per page.

- **Coverage:** 1,265 pages, 126,419 unique signatures. This matches the site's public total at the time of collection.
- **Rate:** 3 workers with a pause after each request.

## Files
- `standwithjensen-signatories-nvidians.csv`: 6,330 self-identified NVIDIA employees (5,206 current, 1,124 former).
- `standwithjensen-signatories-all.csv.gz`: all 126,419 signatures, gzipped.

| Affiliation | Signatures |
|---|---|
| Shareholder | 61,436 |
| Supporter | 53,114 |
| Current employee | 5,206 |
| Partner | 2,718 |
| Former employee | 1,124 |
| Not stated | 2,821 |

## Columns
`id`, `name`, `title_or_organization`, `affiliation`, `affiliation_label`, `is_nvidian`, `message`, `signed_at_utc`, `signed_date`, `source`

## Notes
- **Public fields only.** These are the fields the site publishes for people who chose "show my name". No emails or phone numbers are published or collected. No photos were published.
- **Unverified data.** The site says names, affiliations and titles are self-reported and unverified. Some entries are clearly not genuine, for example "Elon Musk, SpaceX Tesla CEO".
- **Incomplete names.** Some names are first names or initials only.
