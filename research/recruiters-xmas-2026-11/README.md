# UK tech-recruitment lookalikes for the Christmas recruiter offer (25 Nov 2026)

**The request:** decision-maker emails at recruitment agencies like the 95 the user listed (La Fosse, Harnham, Burns Sheehan and others) that could become clients within 30 days on the Christmas offer for recruiters. None of the listed agencies may be repeated.

## File

`recruiter-lookalikes-2026-11-25.csv`: 32 decision makers at 32 UK technology recruitment agencies, one per agency.
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
